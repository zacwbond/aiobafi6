from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProperyQuery(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ALL: _ClassVar[ProperyQuery]
    FAN: _ClassVar[ProperyQuery]
    LIGHT: _ClassVar[ProperyQuery]
    FIRMWARE_MORE_DATETIME_API: _ClassVar[ProperyQuery]
    NETWORK: _ClassVar[ProperyQuery]
    SCHEDULES: _ClassVar[ProperyQuery]
    SENSORS: _ClassVar[ProperyQuery]

class OffOnAuto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    OFF: _ClassVar[OffOnAuto]
    ON: _ClassVar[OffOnAuto]
    AUTO: _ClassVar[OffOnAuto]

class MultiLightMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ALL_LIGHTS: _ClassVar[MultiLightMode]
    DOWNLIGHT: _ClassVar[MultiLightMode]
    UPLIGHT: _ClassVar[MultiLightMode]
ALL: ProperyQuery
FAN: ProperyQuery
LIGHT: ProperyQuery
FIRMWARE_MORE_DATETIME_API: ProperyQuery
NETWORK: ProperyQuery
SCHEDULES: ProperyQuery
SENSORS: ProperyQuery
OFF: OffOnAuto
ON: OffOnAuto
AUTO: OffOnAuto
ALL_LIGHTS: MultiLightMode
DOWNLIGHT: MultiLightMode
UPLIGHT: MultiLightMode

class Root(_message.Message):
    __slots__ = ["root2"]
    ROOT2_FIELD_NUMBER: _ClassVar[int]
    root2: Root2
    def __init__(self, root2: _Optional[_Union[Root2, _Mapping]] = ...) -> None: ...

class Root2(_message.Message):
    __slots__ = ["commit", "query", "query_result"]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    commit: Commit
    query: Query
    query_result: QueryResult
    def __init__(self, commit: _Optional[_Union[Commit, _Mapping]] = ..., query: _Optional[_Union[Query, _Mapping]] = ..., query_result: _Optional[_Union[QueryResult, _Mapping]] = ...) -> None: ...

class Commit(_message.Message):
    __slots__ = ["properties"]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: Properties
    def __init__(self, properties: _Optional[_Union[Properties, _Mapping]] = ...) -> None: ...

class Query(_message.Message):
    __slots__ = ["property_query"]
    PROPERTY_QUERY_FIELD_NUMBER: _ClassVar[int]
    property_query: ProperyQuery
    def __init__(self, property_query: _Optional[_Union[ProperyQuery, str]] = ...) -> None: ...

class QueryResult(_message.Message):
    __slots__ = ["properties", "schedules"]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.RepeatedCompositeFieldContainer[Properties]
    schedules: _containers.RepeatedCompositeFieldContainer[Schedule]
    def __init__(self, properties: _Optional[_Iterable[_Union[Properties, _Mapping]]] = ..., schedules: _Optional[_Iterable[_Union[Schedule, _Mapping]]] = ...) -> None: ...

class RgbLed(_message.Message):
    __slots__ = ["preset", "enabled", "brightness_percent", "red", "green", "blue"]
    class Preset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        CUSTO: _ClassVar[RgbLed.Preset]
        RED: _ClassVar[RgbLed.Preset]
        GREEN: _ClassVar[RgbLed.Preset]
        BLUE: _ClassVar[RgbLed.Preset]
        TEAL: _ClassVar[RgbLed.Preset]
        YELLOW: _ClassVar[RgbLed.Preset]
        VIOLET: _ClassVar[RgbLed.Preset]
        WHITE: _ClassVar[RgbLed.Preset]
        ORANGE: _ClassVar[RgbLed.Preset]
        PINK: _ClassVar[RgbLed.Preset]
    CUSTO: RgbLed.Preset
    RED: RgbLed.Preset
    GREEN: RgbLed.Preset
    BLUE: RgbLed.Preset
    TEAL: RgbLed.Preset
    YELLOW: RgbLed.Preset
    VIOLET: RgbLed.Preset
    WHITE: RgbLed.Preset
    ORANGE: RgbLed.Preset
    PINK: RgbLed.Preset
    PRESET_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    BRIGHTNESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    preset: RgbLed.Preset
    enabled: bool
    brightness_percent: int
    red: int
    green: int
    blue: int
    def __init__(self, preset: _Optional[_Union[RgbLed.Preset, str]] = ..., enabled: bool = ..., brightness_percent: _Optional[int] = ..., red: _Optional[int] = ..., green: _Optional[int] = ..., blue: _Optional[int] = ...) -> None: ...

class Properties(_message.Message):
    __slots__ = ["name", "model", "local_datetime", "utc_datetime", "firmware_version", "mac_address", "uuid9", "dns_sd_uuid", "api_endpoint", "api_version", "firmware", "capabilities", "fan_mode", "reverse_enable", "speed_percent", "speed", "whoosh_enable", "eco_enable", "auto_comfort_enable", "comfort_ideal_temperature", "comfort_heat_assist_enable", "comfort_heat_assist_speed", "comfort_heat_assist_reverse_enable", "comfort_min_speed", "comfort_max_speed", "motion_sense_enable", "motion_sense_timeout", "return_to_auto_enable", "return_to_auto_timeout", "target_rpm", "current_rpm", "fan_occupancy_detected", "light_mode", "light_brightness_percent", "light_brightness_level", "light_color_temperature", "light_dim_to_warm_enable", "light_auto_motion_timeout", "light_return_to_auto_enable", "light_return_to_auto_timeout", "light_warmest_color_temperature", "light_coolest_color_temperature", "light_multilight_mode", "light_rgb_led", "light_occupancy_detected", "temperature", "humidity", "ip_address", "wifi", "led_indicators_enable", "fan_beep_enable", "legacy_ir_remote_enable", "remote_firmware", "stats", "uvcOn"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DATETIME_FIELD_NUMBER: _ClassVar[int]
    UTC_DATETIME_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UUID9_FIELD_NUMBER: _ClassVar[int]
    DNS_SD_UUID_FIELD_NUMBER: _ClassVar[int]
    API_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FAN_MODE_FIELD_NUMBER: _ClassVar[int]
    REVERSE_ENABLE_FIELD_NUMBER: _ClassVar[int]
    SPEED_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    WHOOSH_ENABLE_FIELD_NUMBER: _ClassVar[int]
    ECO_ENABLE_FIELD_NUMBER: _ClassVar[int]
    AUTO_COMFORT_ENABLE_FIELD_NUMBER: _ClassVar[int]
    COMFORT_IDEAL_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    COMFORT_HEAT_ASSIST_ENABLE_FIELD_NUMBER: _ClassVar[int]
    COMFORT_HEAT_ASSIST_SPEED_FIELD_NUMBER: _ClassVar[int]
    COMFORT_HEAT_ASSIST_REVERSE_ENABLE_FIELD_NUMBER: _ClassVar[int]
    COMFORT_MIN_SPEED_FIELD_NUMBER: _ClassVar[int]
    COMFORT_MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSE_ENABLE_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RETURN_TO_AUTO_ENABLE_FIELD_NUMBER: _ClassVar[int]
    RETURN_TO_AUTO_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TARGET_RPM_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RPM_FIELD_NUMBER: _ClassVar[int]
    FAN_OCCUPANCY_DETECTED_FIELD_NUMBER: _ClassVar[int]
    LIGHT_MODE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_BRIGHTNESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    LIGHT_BRIGHTNESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LIGHT_COLOR_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_DIM_TO_WARM_ENABLE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_AUTO_MOTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    LIGHT_RETURN_TO_AUTO_ENABLE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_RETURN_TO_AUTO_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    LIGHT_WARMEST_COLOR_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_COOLEST_COLOR_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_MULTILIGHT_MODE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_RGB_LED_FIELD_NUMBER: _ClassVar[int]
    LIGHT_OCCUPANCY_DETECTED_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    LED_INDICATORS_ENABLE_FIELD_NUMBER: _ClassVar[int]
    FAN_BEEP_ENABLE_FIELD_NUMBER: _ClassVar[int]
    LEGACY_IR_REMOTE_ENABLE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    UVCON_FIELD_NUMBER: _ClassVar[int]
    name: str
    model: str
    local_datetime: str
    utc_datetime: str
    firmware_version: str
    mac_address: str
    uuid9: str
    dns_sd_uuid: str
    api_endpoint: str
    api_version: str
    firmware: FirmwareProperties
    capabilities: Capabilities
    fan_mode: OffOnAuto
    reverse_enable: bool
    speed_percent: int
    speed: int
    whoosh_enable: bool
    eco_enable: bool
    auto_comfort_enable: bool
    comfort_ideal_temperature: int
    comfort_heat_assist_enable: bool
    comfort_heat_assist_speed: int
    comfort_heat_assist_reverse_enable: bool
    comfort_min_speed: int
    comfort_max_speed: int
    motion_sense_enable: bool
    motion_sense_timeout: int
    return_to_auto_enable: bool
    return_to_auto_timeout: int
    target_rpm: int
    current_rpm: int
    fan_occupancy_detected: bool
    light_mode: OffOnAuto
    light_brightness_percent: int
    light_brightness_level: int
    light_color_temperature: int
    light_dim_to_warm_enable: bool
    light_auto_motion_timeout: int
    light_return_to_auto_enable: bool
    light_return_to_auto_timeout: int
    light_warmest_color_temperature: int
    light_coolest_color_temperature: int
    light_multilight_mode: MultiLightMode
    light_rgb_led: RgbLed
    light_occupancy_detected: bool
    temperature: int
    humidity: int
    ip_address: str
    wifi: WifiProperties
    led_indicators_enable: bool
    fan_beep_enable: bool
    legacy_ir_remote_enable: bool
    remote_firmware: FirmwareProperties
    stats: Stats
    uvcOn: bool
    def __init__(self, name: _Optional[str] = ..., model: _Optional[str] = ..., local_datetime: _Optional[str] = ..., utc_datetime: _Optional[str] = ..., firmware_version: _Optional[str] = ..., mac_address: _Optional[str] = ..., uuid9: _Optional[str] = ..., dns_sd_uuid: _Optional[str] = ..., api_endpoint: _Optional[str] = ..., api_version: _Optional[str] = ..., firmware: _Optional[_Union[FirmwareProperties, _Mapping]] = ..., capabilities: _Optional[_Union[Capabilities, _Mapping]] = ..., fan_mode: _Optional[_Union[OffOnAuto, str]] = ..., reverse_enable: bool = ..., speed_percent: _Optional[int] = ..., speed: _Optional[int] = ..., whoosh_enable: bool = ..., eco_enable: bool = ..., auto_comfort_enable: bool = ..., comfort_ideal_temperature: _Optional[int] = ..., comfort_heat_assist_enable: bool = ..., comfort_heat_assist_speed: _Optional[int] = ..., comfort_heat_assist_reverse_enable: bool = ..., comfort_min_speed: _Optional[int] = ..., comfort_max_speed: _Optional[int] = ..., motion_sense_enable: bool = ..., motion_sense_timeout: _Optional[int] = ..., return_to_auto_enable: bool = ..., return_to_auto_timeout: _Optional[int] = ..., target_rpm: _Optional[int] = ..., current_rpm: _Optional[int] = ..., fan_occupancy_detected: bool = ..., light_mode: _Optional[_Union[OffOnAuto, str]] = ..., light_brightness_percent: _Optional[int] = ..., light_brightness_level: _Optional[int] = ..., light_color_temperature: _Optional[int] = ..., light_dim_to_warm_enable: bool = ..., light_auto_motion_timeout: _Optional[int] = ..., light_return_to_auto_enable: bool = ..., light_return_to_auto_timeout: _Optional[int] = ..., light_warmest_color_temperature: _Optional[int] = ..., light_coolest_color_temperature: _Optional[int] = ..., light_multilight_mode: _Optional[_Union[MultiLightMode, str]] = ..., light_rgb_led: _Optional[_Union[RgbLed, _Mapping]] = ..., light_occupancy_detected: bool = ..., temperature: _Optional[int] = ..., humidity: _Optional[int] = ..., ip_address: _Optional[str] = ..., wifi: _Optional[_Union[WifiProperties, _Mapping]] = ..., led_indicators_enable: bool = ..., fan_beep_enable: bool = ..., legacy_ir_remote_enable: bool = ..., remote_firmware: _Optional[_Union[FirmwareProperties, _Mapping]] = ..., stats: _Optional[_Union[Stats, _Mapping]] = ..., uvcOn: bool = ...) -> None: ...

class FirmwareProperties(_message.Message):
    __slots__ = ["firmware_version", "bootloader_version", "mac_address"]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    BOOTLOADER_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    firmware_version: str
    bootloader_version: str
    mac_address: str
    def __init__(self, firmware_version: _Optional[str] = ..., bootloader_version: _Optional[str] = ..., mac_address: _Optional[str] = ...) -> None: ...

class Capabilities(_message.Message):
    __slots__ = ["has_temp", "has_humidity", "has_occupancy", "has_light", "has_light_temp", "has_fan", "has_uplight", "has_uvc", "has_rgb"]
    HAS_TEMP_FIELD_NUMBER: _ClassVar[int]
    HAS_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    HAS_OCCUPANCY_FIELD_NUMBER: _ClassVar[int]
    HAS_LIGHT_FIELD_NUMBER: _ClassVar[int]
    HAS_LIGHT_TEMP_FIELD_NUMBER: _ClassVar[int]
    HAS_FAN_FIELD_NUMBER: _ClassVar[int]
    HAS_UPLIGHT_FIELD_NUMBER: _ClassVar[int]
    HAS_UVC_FIELD_NUMBER: _ClassVar[int]
    HAS_RGB_FIELD_NUMBER: _ClassVar[int]
    has_temp: bool
    has_humidity: bool
    has_occupancy: bool
    has_light: bool
    has_light_temp: bool
    has_fan: bool
    has_uplight: bool
    has_uvc: bool
    has_rgb: bool
    def __init__(self, has_temp: bool = ..., has_humidity: bool = ..., has_occupancy: bool = ..., has_light: bool = ..., has_light_temp: bool = ..., has_fan: bool = ..., has_uplight: bool = ..., has_uvc: bool = ..., has_rgb: bool = ...) -> None: ...

class WifiProperties(_message.Message):
    __slots__ = ["ssid"]
    SSID_FIELD_NUMBER: _ClassVar[int]
    ssid: str
    def __init__(self, ssid: _Optional[str] = ...) -> None: ...

class Schedule(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Stats(_message.Message):
    __slots__ = ["uptime_minutes"]
    UPTIME_MINUTES_FIELD_NUMBER: _ClassVar[int]
    uptime_minutes: int
    def __init__(self, uptime_minutes: _Optional[int] = ...) -> None: ...
