"""Command line tool for aiobaf6."""
from __future__ import annotations

import argparse
import asyncio
import difflib
import ipaddress

from aiobafi6.generated import aiobafi6_pb2
from aiobafi6 import wireutils
from google.protobuf import text_format

ARGS = argparse.ArgumentParser(description="Command line tool for aiobaf6.")
ARGS.add_argument(
    "-i",
    "--ip",
    action="store",
    dest="ip_addr",
    help="device address",
)
ARGS.add_argument(
    "-d",
    "--dump",
    action="store_true",
    dest="dump",
    help="enable proto dumping",
)
ARGS.add_argument(
    "property",
    nargs="?",
    help="property name",
)
ARGS.add_argument(
    "value",
    nargs="?",
    help="property value",
)

PORT = 31415


async def query_loop(writer: asyncio.StreamWriter):
    print("sending initial query")
    root = aiobafi6_pb2.Root()
    root.root2.query.property_query = aiobafi6_pb2.ALL
    writer.write(wireutils.serialize(root))
    while True:
        await asyncio.sleep(15)
        print("sending refresh query")
        root = aiobafi6_pb2.Root()
        root.root2.query.property_query = aiobafi6_pb2.ALL
        writer.write(wireutils.serialize(root))


async def query_state(ip_addr: str, dump: bool):
    print(f"Querying all state from {ip_addr}")
    reader, writer = await asyncio.open_connection(ip_addr, PORT)
    _ = asyncio.create_task(query_loop(writer))
    i = 0
    previous = aiobafi6_pb2.Properties()
    latest = aiobafi6_pb2.Properties()
    unknown = {}
    previous_sorted_unknown = []
    while True:
        # The wire format frames protobuf messages with 0xc0, so the first `readuntil`
        # will return just that byte and the next will return the message with the
        # terminating byte.
        raw_buf = await reader.readuntil(b"\xc0")
        if len(raw_buf) == 1:
            continue
        buf = wireutils.remove_emulation_prevention(raw_buf[:-1])
        if dump:
            with open(f"dump-query-{i}.bin", "wb") as f:
                f.write(buf)
            i += 1
        root = aiobafi6_pb2.Root()
        root.ParseFromString(buf)
        for p in root.root2.query_result.properties:
            for f in p.UnknownFields():
                unknown[f.field_number] = f.data
        root.DiscardUnknownFields()
        for p in root.root2.query_result.properties:
            try:
                p.ClearField("local_datetime")
            except ValueError():
                pass
            try:
                p.ClearField("utc_datetime")
            except ValueError():
                pass
            try:
                p.stats.ClearField("uptime_minutes")
            except ValueError():
                pass
            latest.MergeFrom(p)
        d = "".join(
            difflib.unified_diff(
                text_format.MessageToString(previous).splitlines(keepends=True),
                text_format.MessageToString(latest).splitlines(keepends=True),
            )
        )
        if len(d) > 0:
            print(d)
        previous.CopyFrom(latest)
        sorted_unknown = [f"{k}: {str(unknown[k])}\n" for k in sorted(unknown.keys())]
        d = "".join(difflib.unified_diff(previous_sorted_unknown, sorted_unknown))
        if len(d) > 0:
            print(d)
        previous_sorted_unknown = sorted_unknown


async def set_property(ip_addr: str, property: str, value: int, dump: bool):
    print(f"Setting {property} of fan at {ip_addr} to {value}")
    root = aiobafi6_pb2.Root()
    try:
        setattr(root.root2.commit.properties, property, value)
    except TypeError:
        setattr(root.root2.commit.properties, property, int(value))
    buf = wireutils.serialize(root)
    if dump:
        with open(f"dump-set-{property}-{value}.bin", "wb") as f:
            f.write(buf)
    reader, writer = await asyncio.open_connection(ip_addr, PORT)
    writer.write(buf)
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def async_main():
    args = ARGS.parse_args()
    try:
        ip_addr = ipaddress.ip_address(args.ip_addr)
    except ValueError:
        print("invalid address ", args.ip_addr)
        return
    if args.property is not None:
        if args.value is None:
            raise RuntimeError("must specify property value")
        await set_property(str(ip_addr), args.property, args.value, dump=args.dump)
    else:
        await query_state(str(ip_addr), dump=args.dump)


def main():
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
