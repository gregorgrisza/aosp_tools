# Copyright (C) 2025 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# DO NOT EDIT MANUALLY
# This file was autogenerated by vhal_const_generate.py

# VehiclePropertyType
VEHICLEPROPERTYTYPE_STRING = 0x100000
VEHICLEPROPERTYTYPE_BOOLEAN = 0x200000
VEHICLEPROPERTYTYPE_INT32 = 0x400000
VEHICLEPROPERTYTYPE_INT32_VEC = 0x410000
VEHICLEPROPERTYTYPE_INT64 = 0x500000
VEHICLEPROPERTYTYPE_INT64_VEC = 0x510000
VEHICLEPROPERTYTYPE_FLOAT = 0x600000
VEHICLEPROPERTYTYPE_FLOAT_VEC = 0x610000
VEHICLEPROPERTYTYPE_BYTES = 0x700000
VEHICLEPROPERTYTYPE_MIXED = 0xe00000
VEHICLEPROPERTYTYPE_MASK = 0xff0000

# VehicleArea
VEHICLEAREA_GLOBAL = 0x1000000
VEHICLEAREA_WINDOW = 0x3000000
VEHICLEAREA_MIRROR = 0x4000000
VEHICLEAREA_SEAT = 0x5000000
VEHICLEAREA_DOOR = 0x6000000
VEHICLEAREA_WHEEL = 0x7000000
VEHICLEAREA_MASK = 0xf000000

# VehiclePropertyGroup
VEHICLEPROPERTYGROUP_SYSTEM = 0x10000000
VEHICLEPROPERTYGROUP_VENDOR = 0x20000000
VEHICLEPROPERTYGROUP_MASK = 0xf0000000

# VehicleProperty
VEHICLEPROPERTY_INVALID = 0x0
VEHICLEPROPERTY_INFO_VIN = 0x11100100
VEHICLEPROPERTY_INFO_MAKE = 0x11100101
VEHICLEPROPERTY_INFO_MODEL = 0x11100102
VEHICLEPROPERTY_INFO_MODEL_YEAR = 0x11400103
VEHICLEPROPERTY_INFO_FUEL_CAPACITY = 0x11600104
VEHICLEPROPERTY_INFO_FUEL_TYPE = 0x11410105
VEHICLEPROPERTY_INFO_EV_BATTERY_CAPACITY = 0x11600106
VEHICLEPROPERTY_INFO_EV_CONNECTOR_TYPE = 0x11410107
VEHICLEPROPERTY_INFO_FUEL_DOOR_LOCATION = 0x11400108
VEHICLEPROPERTY_INFO_EV_PORT_LOCATION = 0x11400109
VEHICLEPROPERTY_INFO_DRIVER_SEAT = 0x1540010a
VEHICLEPROPERTY_INFO_EXTERIOR_DIMENSIONS = 0x1141010b
VEHICLEPROPERTY_INFO_MULTI_EV_PORT_LOCATIONS = 0x1141010c
VEHICLEPROPERTY_PERF_ODOMETER = 0x11600204
VEHICLEPROPERTY_PERF_VEHICLE_SPEED = 0x11600207
VEHICLEPROPERTY_PERF_VEHICLE_SPEED_DISPLAY = 0x11600208
VEHICLEPROPERTY_PERF_STEERING_ANGLE = 0x11600209
VEHICLEPROPERTY_PERF_REAR_STEERING_ANGLE = 0x11600210
VEHICLEPROPERTY_ENGINE_COOLANT_TEMP = 0x11600301
VEHICLEPROPERTY_ENGINE_OIL_LEVEL = 0x11400303
VEHICLEPROPERTY_ENGINE_OIL_TEMP = 0x11600304
VEHICLEPROPERTY_ENGINE_RPM = 0x11600305
VEHICLEPROPERTY_WHEEL_TICK = 0x11510306
VEHICLEPROPERTY_FUEL_LEVEL = 0x11600307
VEHICLEPROPERTY_FUEL_DOOR_OPEN = 0x11200308
VEHICLEPROPERTY_EV_BATTERY_LEVEL = 0x11600309
VEHICLEPROPERTY_EV_CHARGE_PORT_OPEN = 0x1120030a
VEHICLEPROPERTY_EV_CHARGE_PORT_CONNECTED = 0x1120030b
VEHICLEPROPERTY_EV_BATTERY_INSTANTANEOUS_CHARGE_RATE = 0x1160030c
VEHICLEPROPERTY_RANGE_REMAINING = 0x11600308
VEHICLEPROPERTY_TIRE_PRESSURE = 0x17600309
VEHICLEPROPERTY_CRITICALLY_LOW_TIRE_PRESSURE = 0x1760030a
VEHICLEPROPERTY_GEAR_SELECTION = 0x11400400
VEHICLEPROPERTY_CURRENT_GEAR = 0x11400401
VEHICLEPROPERTY_PARKING_BRAKE_ON = 0x11200402
VEHICLEPROPERTY_PARKING_BRAKE_AUTO_APPLY = 0x11200403
VEHICLEPROPERTY_FUEL_LEVEL_LOW = 0x11200405
VEHICLEPROPERTY_NIGHT_MODE = 0x11200407
VEHICLEPROPERTY_TURN_SIGNAL_STATE = 0x11400408
VEHICLEPROPERTY_IGNITION_STATE = 0x11400409
VEHICLEPROPERTY_ABS_ACTIVE = 0x1120040a
VEHICLEPROPERTY_TRACTION_CONTROL_ACTIVE = 0x1120040b
VEHICLEPROPERTY_HVAC_FAN_SPEED = 0x15400500
VEHICLEPROPERTY_HVAC_FAN_DIRECTION = 0x15400501
VEHICLEPROPERTY_HVAC_TEMPERATURE_CURRENT = 0x15600502
VEHICLEPROPERTY_HVAC_TEMPERATURE_SET = 0x15600503
VEHICLEPROPERTY_HVAC_DEFROSTER = 0x13200504
VEHICLEPROPERTY_HVAC_AC_ON = 0x15200505
VEHICLEPROPERTY_HVAC_MAX_AC_ON = 0x15200506
VEHICLEPROPERTY_HVAC_MAX_DEFROST_ON = 0x15200507
VEHICLEPROPERTY_HVAC_RECIRC_ON = 0x15200508
VEHICLEPROPERTY_HVAC_DUAL_ON = 0x15200509
VEHICLEPROPERTY_HVAC_AUTO_ON = 0x1520050a
VEHICLEPROPERTY_HVAC_SEAT_TEMPERATURE = 0x1540050b
VEHICLEPROPERTY_HVAC_SIDE_MIRROR_HEAT = 0x1440050c
VEHICLEPROPERTY_HVAC_STEERING_WHEEL_HEAT = 0x1140050d
VEHICLEPROPERTY_HVAC_TEMPERATURE_DISPLAY_UNITS = 0x1140050e
VEHICLEPROPERTY_HVAC_ACTUAL_FAN_SPEED_RPM = 0x1540050f
VEHICLEPROPERTY_HVAC_POWER_ON = 0x15200510
VEHICLEPROPERTY_HVAC_FAN_DIRECTION_AVAILABLE = 0x15410511
VEHICLEPROPERTY_HVAC_AUTO_RECIRC_ON = 0x15200512
VEHICLEPROPERTY_HVAC_SEAT_VENTILATION = 0x15400513
VEHICLEPROPERTY_HVAC_ELECTRIC_DEFROSTER_ON = 0x13200514
VEHICLEPROPERTY_HVAC_TEMPERATURE_VALUE_SUGGESTION = 0x11610515
VEHICLEPROPERTY_DISTANCE_DISPLAY_UNITS = 0x11400600
VEHICLEPROPERTY_FUEL_VOLUME_DISPLAY_UNITS = 0x11400601
VEHICLEPROPERTY_TIRE_PRESSURE_DISPLAY_UNITS = 0x11400602
VEHICLEPROPERTY_EV_BATTERY_DISPLAY_UNITS = 0x11400603
VEHICLEPROPERTY_FUEL_CONSUMPTION_UNITS_DISTANCE_OVER_VOLUME = 0x11200604
VEHICLEPROPERTY_VEHICLE_SPEED_DISPLAY_UNITS = 0x11400605
VEHICLEPROPERTY_EPOCH_TIME = 0x11500606
VEHICLEPROPERTY_STORAGE_ENCRYPTION_BINDING_SEED = 0x11700607
VEHICLEPROPERTY_ENV_OUTSIDE_TEMPERATURE = 0x11600703
VEHICLEPROPERTY_AP_POWER_STATE_REQ = 0x11410a00
VEHICLEPROPERTY_AP_POWER_STATE_REPORT = 0x11410a01
VEHICLEPROPERTY_AP_POWER_BOOTUP_REASON = 0x11400a02
VEHICLEPROPERTY_DISPLAY_BRIGHTNESS = 0x11400a03
VEHICLEPROPERTY_HW_KEY_INPUT = 0x11410a10
VEHICLEPROPERTY_HW_ROTARY_INPUT = 0x11410a20
VEHICLEPROPERTY_HW_CUSTOM_INPUT = 0x11410a30
VEHICLEPROPERTY_DOOR_POS = 0x16400b00
VEHICLEPROPERTY_DOOR_MOVE = 0x16400b01
VEHICLEPROPERTY_DOOR_LOCK = 0x16200b02
VEHICLEPROPERTY_MIRROR_Z_POS = 0x14400b40
VEHICLEPROPERTY_MIRROR_Z_MOVE = 0x14400b41
VEHICLEPROPERTY_MIRROR_Y_POS = 0x14400b42
VEHICLEPROPERTY_MIRROR_Y_MOVE = 0x14400b43
VEHICLEPROPERTY_MIRROR_LOCK = 0x11200b44
VEHICLEPROPERTY_MIRROR_FOLD = 0x11200b45
VEHICLEPROPERTY_SEAT_MEMORY_SELECT = 0x15400b80
VEHICLEPROPERTY_SEAT_MEMORY_SET = 0x15400b81
VEHICLEPROPERTY_SEAT_BELT_BUCKLED = 0x15200b82
VEHICLEPROPERTY_SEAT_BELT_HEIGHT_POS = 0x15400b83
VEHICLEPROPERTY_SEAT_BELT_HEIGHT_MOVE = 0x15400b84
VEHICLEPROPERTY_SEAT_FORE_AFT_POS = 0x15400b85
VEHICLEPROPERTY_SEAT_FORE_AFT_MOVE = 0x15400b86
VEHICLEPROPERTY_SEAT_BACKREST_ANGLE_1_POS = 0x15400b87
VEHICLEPROPERTY_SEAT_BACKREST_ANGLE_1_MOVE = 0x15400b88
VEHICLEPROPERTY_SEAT_BACKREST_ANGLE_2_POS = 0x15400b89
VEHICLEPROPERTY_SEAT_BACKREST_ANGLE_2_MOVE = 0x15400b8a
VEHICLEPROPERTY_SEAT_HEIGHT_POS = 0x15400b8b
VEHICLEPROPERTY_SEAT_HEIGHT_MOVE = 0x15400b8c
VEHICLEPROPERTY_SEAT_DEPTH_POS = 0x15400b8d
VEHICLEPROPERTY_SEAT_DEPTH_MOVE = 0x15400b8e
VEHICLEPROPERTY_SEAT_TILT_POS = 0x15400b8f
VEHICLEPROPERTY_SEAT_TILT_MOVE = 0x15400b90
VEHICLEPROPERTY_SEAT_LUMBAR_FORE_AFT_POS = 0x15400b91
VEHICLEPROPERTY_SEAT_LUMBAR_FORE_AFT_MOVE = 0x15400b92
VEHICLEPROPERTY_SEAT_LUMBAR_SIDE_SUPPORT_POS = 0x15400b93
VEHICLEPROPERTY_SEAT_LUMBAR_SIDE_SUPPORT_MOVE = 0x15400b94
VEHICLEPROPERTY_SEAT_HEADREST_HEIGHT_POS = 0x11400b95
VEHICLEPROPERTY_SEAT_HEADREST_HEIGHT_MOVE = 0x15400b96
VEHICLEPROPERTY_SEAT_HEADREST_ANGLE_POS = 0x15400b97
VEHICLEPROPERTY_SEAT_HEADREST_ANGLE_MOVE = 0x15400b98
VEHICLEPROPERTY_SEAT_HEADREST_FORE_AFT_POS = 0x15400b99
VEHICLEPROPERTY_SEAT_HEADREST_FORE_AFT_MOVE = 0x15400b9a
VEHICLEPROPERTY_SEAT_OCCUPANCY = 0x15400bb0
VEHICLEPROPERTY_WINDOW_POS = 0x13400bc0
VEHICLEPROPERTY_WINDOW_MOVE = 0x13400bc1
VEHICLEPROPERTY_WINDOW_LOCK = 0x13200bc4
VEHICLEPROPERTY_VEHICLE_MAP_SERVICE = 0x11e00c00
VEHICLEPROPERTY_OBD2_LIVE_FRAME = 0x11e00d00
VEHICLEPROPERTY_OBD2_FREEZE_FRAME = 0x11e00d01
VEHICLEPROPERTY_OBD2_FREEZE_FRAME_INFO = 0x11e00d02
VEHICLEPROPERTY_OBD2_FREEZE_FRAME_CLEAR = 0x11e00d03
VEHICLEPROPERTY_HEADLIGHTS_STATE = 0x11400e00
VEHICLEPROPERTY_HIGH_BEAM_LIGHTS_STATE = 0x11400e01
VEHICLEPROPERTY_FOG_LIGHTS_STATE = 0x11400e02
VEHICLEPROPERTY_HAZARD_LIGHTS_STATE = 0x11400e03
VEHICLEPROPERTY_HEADLIGHTS_SWITCH = 0x11400e10
VEHICLEPROPERTY_HIGH_BEAM_LIGHTS_SWITCH = 0x11400e11
VEHICLEPROPERTY_FOG_LIGHTS_SWITCH = 0x11400e12
VEHICLEPROPERTY_HAZARD_LIGHTS_SWITCH = 0x11400e13
VEHICLEPROPERTY_CABIN_LIGHTS_STATE = 0x11400f01
VEHICLEPROPERTY_CABIN_LIGHTS_SWITCH = 0x11400f02
VEHICLEPROPERTY_READING_LIGHTS_STATE = 0x15400f03
VEHICLEPROPERTY_READING_LIGHTS_SWITCH = 0x15400f04
VEHICLEPROPERTY_SUPPORT_CUSTOMIZE_VENDOR_PERMISSION = 0x11200f05
VEHICLEPROPERTY_DISABLED_OPTIONAL_FEATURES = 0x11100f06
VEHICLEPROPERTY_INITIAL_USER_INFO = 0x11e00f07
VEHICLEPROPERTY_SWITCH_USER = 0x11e00f08
VEHICLEPROPERTY_CREATE_USER = 0x11e00f09
VEHICLEPROPERTY_REMOVE_USER = 0x11e00f0a
VEHICLEPROPERTY_USER_IDENTIFICATION_ASSOCIATION = 0x11e00f0b
VEHICLEPROPERTY_EVS_SERVICE_REQUEST = 0x11410f10
VEHICLEPROPERTY_POWER_POLICY_REQ = 0x11100f21
VEHICLEPROPERTY_POWER_POLICY_GROUP_REQ = 0x11100f22
VEHICLEPROPERTY_CURRENT_POWER_POLICY = 0x11100f23
VEHICLEPROPERTY_WATCHDOG_ALIVE = 0x11500f31
VEHICLEPROPERTY_WATCHDOG_TERMINATED_PROCESS = 0x11e00f32
VEHICLEPROPERTY_VHAL_HEARTBEAT = 0x11500f33
VEHICLEPROPERTY_CLUSTER_SWITCH_UI = 0x11400f34
VEHICLEPROPERTY_CLUSTER_DISPLAY_STATE = 0x11410f35
VEHICLEPROPERTY_CLUSTER_REPORT_STATE = 0x11e00f36
VEHICLEPROPERTY_CLUSTER_REQUEST_DISPLAY = 0x11400f37
VEHICLEPROPERTY_CLUSTER_NAVIGATION_STATE = 0x11700f38
VEHICLEPROPERTY_ELECTRONIC_TOLL_COLLECTION_CARD_TYPE = 0x11400f39
VEHICLEPROPERTY_ELECTRONIC_TOLL_COLLECTION_CARD_STATUS = 0x11400f3a
VEHICLEPROPERTY_VENDOR_INTERIOR_LIGHTNING = 0x2140deaf

# ElectronicTollCollectionCardType
ELECTRONICTOLLCOLLECTIONCARDTYPE_UNKNOWN = 0x0
ELECTRONICTOLLCOLLECTIONCARDTYPE_JP_ELECTRONIC_TOLL_COLLECTION_CARD = 0x1
ELECTRONICTOLLCOLLECTIONCARDTYPE_JP_ELECTRONIC_TOLL_COLLECTION_CARD_V2 = 0x2

# ElectronicTollCollectionCardStatus
ELECTRONICTOLLCOLLECTIONCARDSTATUS_UNKNOWN = 0x0
ELECTRONICTOLLCOLLECTIONCARDSTATUS_ELECTRONIC_TOLL_COLLECTION_CARD_VALID = 0x1
ELECTRONICTOLLCOLLECTIONCARDSTATUS_ELECTRONIC_TOLL_COLLECTION_CARD_INVALID = 0x2
ELECTRONICTOLLCOLLECTIONCARDSTATUS_ELECTRONIC_TOLL_COLLECTION_CARD_NOT_INSERTED = 0x3

# VehicleVendorPermission
VEHICLEVENDORPERMISSION_PERMISSION_DEFAULT = 0x0
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_WINDOW = 0x1
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_WINDOW = 0x2
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_DOOR = 0x3
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_DOOR = 0x4
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_SEAT = 0x5
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_SEAT = 0x6
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_MIRROR = 0x7
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_MIRROR = 0x8
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_INFO = 0x9
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_INFO = 0xa
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_ENGINE = 0xb
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_ENGINE = 0xc
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_HVAC = 0xd
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_HVAC = 0xe
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_LIGHT = 0xf
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_LIGHT = 0x10
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_1 = 0x10000
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_1 = 0x11000
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_2 = 0x20000
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_2 = 0x21000
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_3 = 0x30000
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_3 = 0x31000
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_4 = 0x40000
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_4 = 0x41000
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_5 = 0x50000
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_5 = 0x51000
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_6 = 0x60000
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_6 = 0x61000
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_7 = 0x70000
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_7 = 0x71000
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_8 = 0x80000
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_8 = 0x81000
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_9 = 0x90000
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_9 = 0x91000
VEHICLEVENDORPERMISSION_PERMISSION_SET_VENDOR_CATEGORY_10 = 0xa0000
VEHICLEVENDORPERMISSION_PERMISSION_GET_VENDOR_CATEGORY_10 = 0xa1000
VEHICLEVENDORPERMISSION_PERMISSION_NOT_ACCESSIBLE = 0xf0000000

# VehicleSeatOccupancyState
VEHICLESEATOCCUPANCYSTATE_UNKNOWN = 0x0
VEHICLESEATOCCUPANCYSTATE_VACANT = 0x1
VEHICLESEATOCCUPANCYSTATE_OCCUPIED = 0x2

# EvsServiceType
EVSSERVICETYPE_REARVIEW = 0x0
EVSSERVICETYPE_SURROUNDVIEW = 0x1

# EvsServiceState
EVSSERVICESTATE_OFF = 0x0
EVSSERVICESTATE_ON = 0x1

# EvsServiceRequestIndex
EVSSERVICEREQUESTINDEX_TYPE = 0x0
EVSSERVICEREQUESTINDEX_STATE = 0x1

# VehicleLightState
VEHICLELIGHTSTATE_OFF = 0x0
VEHICLELIGHTSTATE_ON = 0x1
VEHICLELIGHTSTATE_DAYTIME_RUNNING = 0x2

# VehicleLightSwitch
VEHICLELIGHTSWITCH_OFF = 0x0
VEHICLELIGHTSWITCH_ON = 0x1
VEHICLELIGHTSWITCH_DAYTIME_RUNNING = 0x2
VEHICLELIGHTSWITCH_AUTOMATIC = 0x100

# EvConnectorType
EVCONNECTORTYPE_UNKNOWN = 0x0
EVCONNECTORTYPE_IEC_TYPE_1_AC = 0x1
EVCONNECTORTYPE_IEC_TYPE_2_AC = 0x2
EVCONNECTORTYPE_IEC_TYPE_3_AC = 0x3
EVCONNECTORTYPE_IEC_TYPE_4_DC = 0x4
EVCONNECTORTYPE_IEC_TYPE_1_CCS_DC = 0x5
EVCONNECTORTYPE_IEC_TYPE_2_CCS_DC = 0x6
EVCONNECTORTYPE_TESLA_ROADSTER = 0x7
EVCONNECTORTYPE_TESLA_HPWC = 0x8
EVCONNECTORTYPE_TESLA_SUPERCHARGER = 0x9
EVCONNECTORTYPE_GBT_AC = 0xa
EVCONNECTORTYPE_GBT_DC = 0xb
EVCONNECTORTYPE_OTHER = 0x65

# PortLocationType
PORTLOCATIONTYPE_UNKNOWN = 0x0
PORTLOCATIONTYPE_FRONT_LEFT = 0x1
PORTLOCATIONTYPE_FRONT_RIGHT = 0x2
PORTLOCATIONTYPE_REAR_RIGHT = 0x3
PORTLOCATIONTYPE_REAR_LEFT = 0x4
PORTLOCATIONTYPE_FRONT = 0x5
PORTLOCATIONTYPE_REAR = 0x6

# FuelType
FUELTYPE_FUEL_TYPE_UNKNOWN = 0x0
FUELTYPE_FUEL_TYPE_UNLEADED = 0x1
FUELTYPE_FUEL_TYPE_LEADED = 0x2
FUELTYPE_FUEL_TYPE_DIESEL_1 = 0x3
FUELTYPE_FUEL_TYPE_DIESEL_2 = 0x4
FUELTYPE_FUEL_TYPE_BIODIESEL = 0x5
FUELTYPE_FUEL_TYPE_E85 = 0x6
FUELTYPE_FUEL_TYPE_LPG = 0x7
FUELTYPE_FUEL_TYPE_CNG = 0x8
FUELTYPE_FUEL_TYPE_LNG = 0x9
FUELTYPE_FUEL_TYPE_ELECTRIC = 0xa
FUELTYPE_FUEL_TYPE_HYDROGEN = 0xb
FUELTYPE_FUEL_TYPE_OTHER = 0xc

# VehicleHvacFanDirection
VEHICLEHVACFANDIRECTION_UNKNOWN = 0x0
VEHICLEHVACFANDIRECTION_FACE = 0x1
VEHICLEHVACFANDIRECTION_FLOOR = 0x2
VEHICLEHVACFANDIRECTION_FACE_AND_FLOOR = 0x3
VEHICLEHVACFANDIRECTION_DEFROST = 0x4
VEHICLEHVACFANDIRECTION_DEFROST_AND_FLOOR = 0x6

# VehicleOilLevel
VEHICLEOILLEVEL_CRITICALLY_LOW = 0x0
VEHICLEOILLEVEL_LOW = 0x1
VEHICLEOILLEVEL_NORMAL = 0x2
VEHICLEOILLEVEL_HIGH = 0x3
VEHICLEOILLEVEL_ERROR = 0x4

# VehicleApPowerStateConfigFlag
VEHICLEAPPOWERSTATECONFIGFLAG_ENABLE_DEEP_SLEEP_FLAG = 0x1
VEHICLEAPPOWERSTATECONFIGFLAG_CONFIG_SUPPORT_TIMER_POWER_ON_FLAG = 0x2

# VehicleApPowerStateReq
VEHICLEAPPOWERSTATEREQ_ON = 0x0
VEHICLEAPPOWERSTATEREQ_SHUTDOWN_PREPARE = 0x1
VEHICLEAPPOWERSTATEREQ_CANCEL_SHUTDOWN = 0x2
VEHICLEAPPOWERSTATEREQ_FINISHED = 0x3

# VehicleApPowerStateReqIndex
VEHICLEAPPOWERSTATEREQINDEX_STATE = 0x0
VEHICLEAPPOWERSTATEREQINDEX_ADDITIONAL = 0x1

# VehicleApPowerStateShutdownParam
VEHICLEAPPOWERSTATESHUTDOWNPARAM_SHUTDOWN_IMMEDIATELY = 0x1
VEHICLEAPPOWERSTATESHUTDOWNPARAM_CAN_SLEEP = 0x2
VEHICLEAPPOWERSTATESHUTDOWNPARAM_SHUTDOWN_ONLY = 0x3
VEHICLEAPPOWERSTATESHUTDOWNPARAM_SLEEP_IMMEDIATELY = 0x4

# VehicleApPowerStateReport
VEHICLEAPPOWERSTATEREPORT_WAIT_FOR_VHAL = 0x1
VEHICLEAPPOWERSTATEREPORT_DEEP_SLEEP_ENTRY = 0x2
VEHICLEAPPOWERSTATEREPORT_DEEP_SLEEP_EXIT = 0x3
VEHICLEAPPOWERSTATEREPORT_SHUTDOWN_POSTPONE = 0x4
VEHICLEAPPOWERSTATEREPORT_SHUTDOWN_START = 0x5
VEHICLEAPPOWERSTATEREPORT_ON = 0x6
VEHICLEAPPOWERSTATEREPORT_SHUTDOWN_PREPARE = 0x7
VEHICLEAPPOWERSTATEREPORT_SHUTDOWN_CANCELLED = 0x8

# VehicleHwKeyInputAction
VEHICLEHWKEYINPUTACTION_ACTION_DOWN = 0x0
VEHICLEHWKEYINPUTACTION_ACTION_UP = 0x1

# VehicleDisplay
VEHICLEDISPLAY_MAIN = 0x0
VEHICLEDISPLAY_INSTRUMENT_CLUSTER = 0x1

# VehicleUnit
VEHICLEUNIT_SHOULD_NOT_USE = 0x0
VEHICLEUNIT_METER_PER_SEC = 0x1
VEHICLEUNIT_RPM = 0x2
VEHICLEUNIT_HERTZ = 0x3
VEHICLEUNIT_PERCENTILE = 0x10
VEHICLEUNIT_MILLIMETER = 0x20
VEHICLEUNIT_METER = 0x21
VEHICLEUNIT_KILOMETER = 0x23
VEHICLEUNIT_MILE = 0x24
VEHICLEUNIT_CELSIUS = 0x30
VEHICLEUNIT_FAHRENHEIT = 0x31
VEHICLEUNIT_KELVIN = 0x32
VEHICLEUNIT_MILLILITER = 0x40
VEHICLEUNIT_LITER = 0x41
VEHICLEUNIT_GALLON = 0x42
VEHICLEUNIT_US_GALLON = 0x42
VEHICLEUNIT_IMPERIAL_GALLON = 0x43
VEHICLEUNIT_NANO_SECS = 0x50
VEHICLEUNIT_MILLI_SECS = 0x51
VEHICLEUNIT_SECS = 0x53
VEHICLEUNIT_YEAR = 0x59
VEHICLEUNIT_WATT_HOUR = 0x60
VEHICLEUNIT_MILLIAMPERE = 0x61
VEHICLEUNIT_MILLIVOLT = 0x62
VEHICLEUNIT_MILLIWATTS = 0x63
VEHICLEUNIT_AMPERE_HOURS = 0x64
VEHICLEUNIT_KILOWATT_HOUR = 0x65
VEHICLEUNIT_KILOPASCAL = 0x70
VEHICLEUNIT_PSI = 0x71
VEHICLEUNIT_BAR = 0x72
VEHICLEUNIT_DEGREES = 0x80
VEHICLEUNIT_MILES_PER_HOUR = 0x90
VEHICLEUNIT_KILOMETERS_PER_HOUR = 0x91

# VehiclePropertyChangeMode
VEHICLEPROPERTYCHANGEMODE_STATIC = 0x0
VEHICLEPROPERTYCHANGEMODE_ON_CHANGE = 0x1
VEHICLEPROPERTYCHANGEMODE_CONTINUOUS = 0x2

# VehiclePropertyAccess
VEHICLEPROPERTYACCESS_NONE = 0x0
VEHICLEPROPERTYACCESS_READ = 0x1
VEHICLEPROPERTYACCESS_WRITE = 0x2
VEHICLEPROPERTYACCESS_READ_WRITE = 0x3

# VehiclePropertyStatus
VEHICLEPROPERTYSTATUS_AVAILABLE = 0x0
VEHICLEPROPERTYSTATUS_UNAVAILABLE = 0x1
VEHICLEPROPERTYSTATUS_ERROR = 0x2

# VehicleGear
VEHICLEGEAR_GEAR_UNKNOWN = 0x0
VEHICLEGEAR_GEAR_NEUTRAL = 0x1
VEHICLEGEAR_GEAR_REVERSE = 0x2
VEHICLEGEAR_GEAR_PARK = 0x4
VEHICLEGEAR_GEAR_DRIVE = 0x8
VEHICLEGEAR_GEAR_1 = 0x10
VEHICLEGEAR_GEAR_2 = 0x20
VEHICLEGEAR_GEAR_3 = 0x40
VEHICLEGEAR_GEAR_4 = 0x80
VEHICLEGEAR_GEAR_5 = 0x100
VEHICLEGEAR_GEAR_6 = 0x200
VEHICLEGEAR_GEAR_7 = 0x400
VEHICLEGEAR_GEAR_8 = 0x800
VEHICLEGEAR_GEAR_9 = 0x1000

# VehicleAreaSeat
VEHICLEAREASEAT_ROW_1_LEFT = 0x1
VEHICLEAREASEAT_ROW_1_CENTER = 0x2
VEHICLEAREASEAT_ROW_1_RIGHT = 0x4
VEHICLEAREASEAT_ROW_2_LEFT = 0x10
VEHICLEAREASEAT_ROW_2_CENTER = 0x20
VEHICLEAREASEAT_ROW_2_RIGHT = 0x40
VEHICLEAREASEAT_ROW_3_LEFT = 0x100
VEHICLEAREASEAT_ROW_3_CENTER = 0x200
VEHICLEAREASEAT_ROW_3_RIGHT = 0x400

# VehicleAreaWindow
VEHICLEAREAWINDOW_FRONT_WINDSHIELD = 0x1
VEHICLEAREAWINDOW_REAR_WINDSHIELD = 0x2
VEHICLEAREAWINDOW_ROW_1_LEFT = 0x10
VEHICLEAREAWINDOW_ROW_1_RIGHT = 0x40
VEHICLEAREAWINDOW_ROW_2_LEFT = 0x100
VEHICLEAREAWINDOW_ROW_2_RIGHT = 0x400
VEHICLEAREAWINDOW_ROW_3_LEFT = 0x1000
VEHICLEAREAWINDOW_ROW_3_RIGHT = 0x4000
VEHICLEAREAWINDOW_ROOF_TOP_1 = 0x10000
VEHICLEAREAWINDOW_ROOF_TOP_2 = 0x20000

# VehicleAreaDoor
VEHICLEAREADOOR_ROW_1_LEFT = 0x1
VEHICLEAREADOOR_ROW_1_RIGHT = 0x4
VEHICLEAREADOOR_ROW_2_LEFT = 0x10
VEHICLEAREADOOR_ROW_2_RIGHT = 0x40
VEHICLEAREADOOR_ROW_3_LEFT = 0x100
VEHICLEAREADOOR_ROW_3_RIGHT = 0x400
VEHICLEAREADOOR_HOOD = 0x10000000
VEHICLEAREADOOR_REAR = 0x20000000

# VehicleAreaMirror
VEHICLEAREAMIRROR_DRIVER_LEFT = 0x1
VEHICLEAREAMIRROR_DRIVER_RIGHT = 0x2
VEHICLEAREAMIRROR_DRIVER_CENTER = 0x4

# VehicleTurnSignal
VEHICLETURNSIGNAL_NONE = 0x0
VEHICLETURNSIGNAL_RIGHT = 0x1
VEHICLETURNSIGNAL_LEFT = 0x2

# VehicleIgnitionState
VEHICLEIGNITIONSTATE_UNDEFINED = 0x0
VEHICLEIGNITIONSTATE_LOCK = 0x1
VEHICLEIGNITIONSTATE_OFF = 0x2
VEHICLEIGNITIONSTATE_ACC = 0x3
VEHICLEIGNITIONSTATE_ON = 0x4
VEHICLEIGNITIONSTATE_START = 0x5

# SubscribeFlags
SUBSCRIBEFLAGS_UNDEFINED = 0x0
SUBSCRIBEFLAGS_EVENTS_FROM_CAR = 0x1
SUBSCRIBEFLAGS_EVENTS_FROM_ANDROID = 0x2

# StatusCode
STATUSCODE_OK = 0x0
STATUSCODE_TRY_AGAIN = 0x1
STATUSCODE_INVALID_ARG = 0x2
STATUSCODE_NOT_AVAILABLE = 0x3
STATUSCODE_ACCESS_DENIED = 0x4
STATUSCODE_INTERNAL_ERROR = 0x5

# VehicleAreaWheel
VEHICLEAREAWHEEL_UNKNOWN = 0x0
VEHICLEAREAWHEEL_LEFT_FRONT = 0x1
VEHICLEAREAWHEEL_RIGHT_FRONT = 0x2
VEHICLEAREAWHEEL_LEFT_REAR = 0x4
VEHICLEAREAWHEEL_RIGHT_REAR = 0x8

# Obd2FuelSystemStatus
OBD2FUELSYSTEMSTATUS_OPEN_INSUFFICIENT_ENGINE_TEMPERATURE = 0x1
OBD2FUELSYSTEMSTATUS_CLOSED_LOOP = 0x2
OBD2FUELSYSTEMSTATUS_OPEN_ENGINE_LOAD_OR_DECELERATION = 0x4
OBD2FUELSYSTEMSTATUS_OPEN_SYSTEM_FAILURE = 0x8
OBD2FUELSYSTEMSTATUS_CLOSED_LOOP_BUT_FEEDBACK_FAULT = 0x10

# Obd2IgnitionMonitorKind
OBD2IGNITIONMONITORKIND_SPARK = 0x0
OBD2IGNITIONMONITORKIND_COMPRESSION = 0x1

# Obd2CommonIgnitionMonitors
OBD2COMMONIGNITIONMONITORS_COMPONENTS_AVAILABLE = 0x1
OBD2COMMONIGNITIONMONITORS_COMPONENTS_INCOMPLETE = 0x2
OBD2COMMONIGNITIONMONITORS_FUEL_SYSTEM_AVAILABLE = 0x4
OBD2COMMONIGNITIONMONITORS_FUEL_SYSTEM_INCOMPLETE = 0x8
OBD2COMMONIGNITIONMONITORS_MISFIRE_AVAILABLE = 0x10
OBD2COMMONIGNITIONMONITORS_MISFIRE_INCOMPLETE = 0x20

# Obd2SparkIgnitionMonitors
OBD2SPARKIGNITIONMONITORS_EGR_AVAILABLE = 0x40
OBD2SPARKIGNITIONMONITORS_EGR_INCOMPLETE = 0x80
OBD2SPARKIGNITIONMONITORS_OXYGEN_SENSOR_HEATER_AVAILABLE = 0x100
OBD2SPARKIGNITIONMONITORS_OXYGEN_SENSOR_HEATER_INCOMPLETE = 0x200
OBD2SPARKIGNITIONMONITORS_OXYGEN_SENSOR_AVAILABLE = 0x400
OBD2SPARKIGNITIONMONITORS_OXYGEN_SENSOR_INCOMPLETE = 0x800
OBD2SPARKIGNITIONMONITORS_AC_REFRIGERANT_AVAILABLE = 0x1000
OBD2SPARKIGNITIONMONITORS_AC_REFRIGERANT_INCOMPLETE = 0x2000
OBD2SPARKIGNITIONMONITORS_SECONDARY_AIR_SYSTEM_AVAILABLE = 0x4000
OBD2SPARKIGNITIONMONITORS_SECONDARY_AIR_SYSTEM_INCOMPLETE = 0x8000
OBD2SPARKIGNITIONMONITORS_EVAPORATIVE_SYSTEM_AVAILABLE = 0x10000
OBD2SPARKIGNITIONMONITORS_EVAPORATIVE_SYSTEM_INCOMPLETE = 0x20000
OBD2SPARKIGNITIONMONITORS_HEATED_CATALYST_AVAILABLE = 0x40000
OBD2SPARKIGNITIONMONITORS_HEATED_CATALYST_INCOMPLETE = 0x80000
OBD2SPARKIGNITIONMONITORS_CATALYST_AVAILABLE = 0x100000
OBD2SPARKIGNITIONMONITORS_CATALYST_INCOMPLETE = 0x200000

# Obd2CompressionIgnitionMonitors
OBD2COMPRESSIONIGNITIONMONITORS_EGR_OR_VVT_AVAILABLE = 0x40
OBD2COMPRESSIONIGNITIONMONITORS_EGR_OR_VVT_INCOMPLETE = 0x80
OBD2COMPRESSIONIGNITIONMONITORS_PM_FILTER_AVAILABLE = 0x100
OBD2COMPRESSIONIGNITIONMONITORS_PM_FILTER_INCOMPLETE = 0x200
OBD2COMPRESSIONIGNITIONMONITORS_EXHAUST_GAS_SENSOR_AVAILABLE = 0x400
OBD2COMPRESSIONIGNITIONMONITORS_EXHAUST_GAS_SENSOR_INCOMPLETE = 0x800
OBD2COMPRESSIONIGNITIONMONITORS_BOOST_PRESSURE_AVAILABLE = 0x1000
OBD2COMPRESSIONIGNITIONMONITORS_BOOST_PRESSURE_INCOMPLETE = 0x2000
OBD2COMPRESSIONIGNITIONMONITORS_NOx_SCR_AVAILABLE = 0x4000
OBD2COMPRESSIONIGNITIONMONITORS_NOx_SCR_INCOMPLETE = 0x8000
OBD2COMPRESSIONIGNITIONMONITORS_NMHC_CATALYST_AVAILABLE = 0x10000
OBD2COMPRESSIONIGNITIONMONITORS_NMHC_CATALYST_INCOMPLETE = 0x20000

# Obd2SecondaryAirStatus
OBD2SECONDARYAIRSTATUS_UPSTREAM = 0x1
OBD2SECONDARYAIRSTATUS_DOWNSTREAM_OF_CATALYCIC_CONVERTER = 0x2
OBD2SECONDARYAIRSTATUS_FROM_OUTSIDE_OR_OFF = 0x4
OBD2SECONDARYAIRSTATUS_PUMP_ON_FOR_DIAGNOSTICS = 0x8

# Obd2FuelType
OBD2FUELTYPE_NOT_AVAILABLE = 0x0
OBD2FUELTYPE_GASOLINE = 0x1
OBD2FUELTYPE_METHANOL = 0x2
OBD2FUELTYPE_ETHANOL = 0x3
OBD2FUELTYPE_DIESEL = 0x4
OBD2FUELTYPE_LPG = 0x5
OBD2FUELTYPE_CNG = 0x6
OBD2FUELTYPE_PROPANE = 0x7
OBD2FUELTYPE_ELECTRIC = 0x8
OBD2FUELTYPE_BIFUEL_RUNNING_GASOLINE = 0x9
OBD2FUELTYPE_BIFUEL_RUNNING_METHANOL = 0xa
OBD2FUELTYPE_BIFUEL_RUNNING_ETHANOL = 0xb
OBD2FUELTYPE_BIFUEL_RUNNING_LPG = 0xc
OBD2FUELTYPE_BIFUEL_RUNNING_CNG = 0xd
OBD2FUELTYPE_BIFUEL_RUNNING_PROPANE = 0xe
OBD2FUELTYPE_BIFUEL_RUNNING_ELECTRIC = 0xf
OBD2FUELTYPE_BIFUEL_RUNNING_ELECTRIC_AND_COMBUSTION = 0x10
OBD2FUELTYPE_HYBRID_GASOLINE = 0x11
OBD2FUELTYPE_HYBRID_ETHANOL = 0x12
OBD2FUELTYPE_HYBRID_DIESEL = 0x13
OBD2FUELTYPE_HYBRID_ELECTRIC = 0x14
OBD2FUELTYPE_HYBRID_RUNNING_ELECTRIC_AND_COMBUSTION = 0x15
OBD2FUELTYPE_HYBRID_REGENERATIVE = 0x16
OBD2FUELTYPE_BIFUEL_RUNNING_DIESEL = 0x17

# DiagnosticIntegerSensorIndex
DIAGNOSTICINTEGERSENSORINDEX_FUEL_SYSTEM_STATUS = 0x0
DIAGNOSTICINTEGERSENSORINDEX_MALFUNCTION_INDICATOR_LIGHT_ON = 0x1
DIAGNOSTICINTEGERSENSORINDEX_IGNITION_MONITORS_SUPPORTED = 0x2
DIAGNOSTICINTEGERSENSORINDEX_IGNITION_SPECIFIC_MONITORS = 0x3
DIAGNOSTICINTEGERSENSORINDEX_INTAKE_AIR_TEMPERATURE = 0x4
DIAGNOSTICINTEGERSENSORINDEX_COMMANDED_SECONDARY_AIR_STATUS = 0x5
DIAGNOSTICINTEGERSENSORINDEX_NUM_OXYGEN_SENSORS_PRESENT = 0x6
DIAGNOSTICINTEGERSENSORINDEX_RUNTIME_SINCE_ENGINE_START = 0x7
DIAGNOSTICINTEGERSENSORINDEX_DISTANCE_TRAVELED_WITH_MALFUNCTION_INDICATOR_LIGHT_ON = 0x8
DIAGNOSTICINTEGERSENSORINDEX_WARMUPS_SINCE_CODES_CLEARED = 0x9
DIAGNOSTICINTEGERSENSORINDEX_DISTANCE_TRAVELED_SINCE_CODES_CLEARED = 0xa
DIAGNOSTICINTEGERSENSORINDEX_ABSOLUTE_BAROMETRIC_PRESSURE = 0xb
DIAGNOSTICINTEGERSENSORINDEX_CONTROL_MODULE_VOLTAGE = 0xc
DIAGNOSTICINTEGERSENSORINDEX_AMBIENT_AIR_TEMPERATURE = 0xd
DIAGNOSTICINTEGERSENSORINDEX_TIME_WITH_MALFUNCTION_LIGHT_ON = 0xe
DIAGNOSTICINTEGERSENSORINDEX_TIME_SINCE_TROUBLE_CODES_CLEARED = 0xf
DIAGNOSTICINTEGERSENSORINDEX_MAX_FUEL_AIR_EQUIVALENCE_RATIO = 0x10
DIAGNOSTICINTEGERSENSORINDEX_MAX_OXYGEN_SENSOR_VOLTAGE = 0x11
DIAGNOSTICINTEGERSENSORINDEX_MAX_OXYGEN_SENSOR_CURRENT = 0x12
DIAGNOSTICINTEGERSENSORINDEX_MAX_INTAKE_MANIFOLD_ABSOLUTE_PRESSURE = 0x13
DIAGNOSTICINTEGERSENSORINDEX_MAX_AIR_FLOW_RATE_FROM_MASS_AIR_FLOW_SENSOR = 0x14
DIAGNOSTICINTEGERSENSORINDEX_FUEL_TYPE = 0x15
DIAGNOSTICINTEGERSENSORINDEX_FUEL_RAIL_ABSOLUTE_PRESSURE = 0x16
DIAGNOSTICINTEGERSENSORINDEX_ENGINE_OIL_TEMPERATURE = 0x17
DIAGNOSTICINTEGERSENSORINDEX_DRIVER_DEMAND_PERCENT_TORQUE = 0x18
DIAGNOSTICINTEGERSENSORINDEX_ENGINE_ACTUAL_PERCENT_TORQUE = 0x19
DIAGNOSTICINTEGERSENSORINDEX_ENGINE_REFERENCE_PERCENT_TORQUE = 0x1a
DIAGNOSTICINTEGERSENSORINDEX_ENGINE_PERCENT_TORQUE_DATA_IDLE = 0x1b
DIAGNOSTICINTEGERSENSORINDEX_ENGINE_PERCENT_TORQUE_DATA_POINT1 = 0x1c
DIAGNOSTICINTEGERSENSORINDEX_ENGINE_PERCENT_TORQUE_DATA_POINT2 = 0x1d
DIAGNOSTICINTEGERSENSORINDEX_ENGINE_PERCENT_TORQUE_DATA_POINT3 = 0x1e
DIAGNOSTICINTEGERSENSORINDEX_ENGINE_PERCENT_TORQUE_DATA_POINT4 = 0x1f
DIAGNOSTICINTEGERSENSORINDEX_LAST_SYSTEM_INDEX = 0x1f

# DiagnosticFloatSensorIndex
DIAGNOSTICFLOATSENSORINDEX_CALCULATED_ENGINE_LOAD = 0x0
DIAGNOSTICFLOATSENSORINDEX_ENGINE_COOLANT_TEMPERATURE = 0x1
DIAGNOSTICFLOATSENSORINDEX_SHORT_TERM_FUEL_TRIM_BANK1 = 0x2
DIAGNOSTICFLOATSENSORINDEX_LONG_TERM_FUEL_TRIM_BANK1 = 0x3
DIAGNOSTICFLOATSENSORINDEX_SHORT_TERM_FUEL_TRIM_BANK2 = 0x4
DIAGNOSTICFLOATSENSORINDEX_LONG_TERM_FUEL_TRIM_BANK2 = 0x5
DIAGNOSTICFLOATSENSORINDEX_FUEL_PRESSURE = 0x6
DIAGNOSTICFLOATSENSORINDEX_INTAKE_MANIFOLD_ABSOLUTE_PRESSURE = 0x7
DIAGNOSTICFLOATSENSORINDEX_ENGINE_RPM = 0x8
DIAGNOSTICFLOATSENSORINDEX_VEHICLE_SPEED = 0x9
DIAGNOSTICFLOATSENSORINDEX_TIMING_ADVANCE = 0xa
DIAGNOSTICFLOATSENSORINDEX_MAF_AIR_FLOW_RATE = 0xb
DIAGNOSTICFLOATSENSORINDEX_THROTTLE_POSITION = 0xc
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR1_VOLTAGE = 0xd
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR1_SHORT_TERM_FUEL_TRIM = 0xe
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR1_FUEL_AIR_EQUIVALENCE_RATIO = 0xf
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR2_VOLTAGE = 0x10
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR2_SHORT_TERM_FUEL_TRIM = 0x11
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR2_FUEL_AIR_EQUIVALENCE_RATIO = 0x12
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR3_VOLTAGE = 0x13
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR3_SHORT_TERM_FUEL_TRIM = 0x14
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR3_FUEL_AIR_EQUIVALENCE_RATIO = 0x15
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR4_VOLTAGE = 0x16
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR4_SHORT_TERM_FUEL_TRIM = 0x17
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR4_FUEL_AIR_EQUIVALENCE_RATIO = 0x18
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR5_VOLTAGE = 0x19
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR5_SHORT_TERM_FUEL_TRIM = 0x1a
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR5_FUEL_AIR_EQUIVALENCE_RATIO = 0x1b
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR6_VOLTAGE = 0x1c
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR6_SHORT_TERM_FUEL_TRIM = 0x1d
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR6_FUEL_AIR_EQUIVALENCE_RATIO = 0x1e
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR7_VOLTAGE = 0x1f
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR7_SHORT_TERM_FUEL_TRIM = 0x20
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR7_FUEL_AIR_EQUIVALENCE_RATIO = 0x21
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR8_VOLTAGE = 0x22
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR8_SHORT_TERM_FUEL_TRIM = 0x23
DIAGNOSTICFLOATSENSORINDEX_OXYGEN_SENSOR8_FUEL_AIR_EQUIVALENCE_RATIO = 0x24
DIAGNOSTICFLOATSENSORINDEX_FUEL_RAIL_PRESSURE = 0x25
DIAGNOSTICFLOATSENSORINDEX_FUEL_RAIL_GAUGE_PRESSURE = 0x26
DIAGNOSTICFLOATSENSORINDEX_COMMANDED_EXHAUST_GAS_RECIRCULATION = 0x27
DIAGNOSTICFLOATSENSORINDEX_EXHAUST_GAS_RECIRCULATION_ERROR = 0x28
DIAGNOSTICFLOATSENSORINDEX_COMMANDED_EVAPORATIVE_PURGE = 0x29
DIAGNOSTICFLOATSENSORINDEX_FUEL_TANK_LEVEL_INPUT = 0x2a
DIAGNOSTICFLOATSENSORINDEX_EVAPORATION_SYSTEM_VAPOR_PRESSURE = 0x2b
DIAGNOSTICFLOATSENSORINDEX_CATALYST_TEMPERATURE_BANK1_SENSOR1 = 0x2c
DIAGNOSTICFLOATSENSORINDEX_CATALYST_TEMPERATURE_BANK2_SENSOR1 = 0x2d
DIAGNOSTICFLOATSENSORINDEX_CATALYST_TEMPERATURE_BANK1_SENSOR2 = 0x2e
DIAGNOSTICFLOATSENSORINDEX_CATALYST_TEMPERATURE_BANK2_SENSOR2 = 0x2f
DIAGNOSTICFLOATSENSORINDEX_ABSOLUTE_LOAD_VALUE = 0x30
DIAGNOSTICFLOATSENSORINDEX_FUEL_AIR_COMMANDED_EQUIVALENCE_RATIO = 0x31
DIAGNOSTICFLOATSENSORINDEX_RELATIVE_THROTTLE_POSITION = 0x32
DIAGNOSTICFLOATSENSORINDEX_ABSOLUTE_THROTTLE_POSITION_B = 0x33
DIAGNOSTICFLOATSENSORINDEX_ABSOLUTE_THROTTLE_POSITION_C = 0x34
DIAGNOSTICFLOATSENSORINDEX_ACCELERATOR_PEDAL_POSITION_D = 0x35
DIAGNOSTICFLOATSENSORINDEX_ACCELERATOR_PEDAL_POSITION_E = 0x36
DIAGNOSTICFLOATSENSORINDEX_ACCELERATOR_PEDAL_POSITION_F = 0x37
DIAGNOSTICFLOATSENSORINDEX_COMMANDED_THROTTLE_ACTUATOR = 0x38
DIAGNOSTICFLOATSENSORINDEX_ETHANOL_FUEL_PERCENTAGE = 0x39
DIAGNOSTICFLOATSENSORINDEX_ABSOLUTE_EVAPORATION_SYSTEM_VAPOR_PRESSURE = 0x3a
DIAGNOSTICFLOATSENSORINDEX_SHORT_TERM_SECONDARY_OXYGEN_SENSOR_TRIM_BANK1 = 0x3b
DIAGNOSTICFLOATSENSORINDEX_SHORT_TERM_SECONDARY_OXYGEN_SENSOR_TRIM_BANK2 = 0x3c
DIAGNOSTICFLOATSENSORINDEX_SHORT_TERM_SECONDARY_OXYGEN_SENSOR_TRIM_BANK3 = 0x3d
DIAGNOSTICFLOATSENSORINDEX_SHORT_TERM_SECONDARY_OXYGEN_SENSOR_TRIM_BANK4 = 0x3e
DIAGNOSTICFLOATSENSORINDEX_LONG_TERM_SECONDARY_OXYGEN_SENSOR_TRIM_BANK1 = 0x3f
DIAGNOSTICFLOATSENSORINDEX_LONG_TERM_SECONDARY_OXYGEN_SENSOR_TRIM_BANK2 = 0x40
DIAGNOSTICFLOATSENSORINDEX_LONG_TERM_SECONDARY_OXYGEN_SENSOR_TRIM_BANK3 = 0x41
DIAGNOSTICFLOATSENSORINDEX_LONG_TERM_SECONDARY_OXYGEN_SENSOR_TRIM_BANK4 = 0x42
DIAGNOSTICFLOATSENSORINDEX_RELATIVE_ACCELERATOR_PEDAL_POSITION = 0x43
DIAGNOSTICFLOATSENSORINDEX_HYBRID_BATTERY_PACK_REMAINING_LIFE = 0x44
DIAGNOSTICFLOATSENSORINDEX_FUEL_INJECTION_TIMING = 0x45
DIAGNOSTICFLOATSENSORINDEX_ENGINE_FUEL_RATE = 0x46
DIAGNOSTICFLOATSENSORINDEX_LAST_SYSTEM_INDEX = 0x46

# VmsMessageType
VMSMESSAGETYPE_SUBSCRIBE = 0x1
VMSMESSAGETYPE_SUBSCRIBE_TO_PUBLISHER = 0x2
VMSMESSAGETYPE_UNSUBSCRIBE = 0x3
VMSMESSAGETYPE_UNSUBSCRIBE_TO_PUBLISHER = 0x4
VMSMESSAGETYPE_OFFERING = 0x5
VMSMESSAGETYPE_AVAILABILITY_REQUEST = 0x6
VMSMESSAGETYPE_SUBSCRIPTIONS_REQUEST = 0x7
VMSMESSAGETYPE_AVAILABILITY_RESPONSE = 0x8
VMSMESSAGETYPE_AVAILABILITY_CHANGE = 0x9
VMSMESSAGETYPE_SUBSCRIPTIONS_RESPONSE = 0xa
VMSMESSAGETYPE_SUBSCRIPTIONS_CHANGE = 0xb
VMSMESSAGETYPE_DATA = 0xc
VMSMESSAGETYPE_PUBLISHER_ID_REQUEST = 0xd
VMSMESSAGETYPE_PUBLISHER_ID_RESPONSE = 0xe
VMSMESSAGETYPE_PUBLISHER_INFORMATION_REQUEST = 0xf
VMSMESSAGETYPE_PUBLISHER_INFORMATION_RESPONSE = 0x10
VMSMESSAGETYPE_START_SESSION = 0x11
VMSMESSAGETYPE_LAST_VMS_MESSAGE_TYPE = 0x11

# VmsBaseMessageIntegerValuesIndex
VMSBASEMESSAGEINTEGERVALUESINDEX_MESSAGE_TYPE = 0x0

# VmsStartSessionMessageIntegerValuesIndex
VMSSTARTSESSIONMESSAGEINTEGERVALUESINDEX_SERVICE_ID = 0x1
VMSSTARTSESSIONMESSAGEINTEGERVALUESINDEX_CLIENT_ID = 0x2

# VmsMessageWithLayerIntegerValuesIndex
VMSMESSAGEWITHLAYERINTEGERVALUESINDEX_LAYER_TYPE = 0x1
VMSMESSAGEWITHLAYERINTEGERVALUESINDEX_LAYER_SUBTYPE = 0x2
VMSMESSAGEWITHLAYERINTEGERVALUESINDEX_LAYER_VERSION = 0x3

# VmsMessageWithLayerAndPublisherIdIntegerValuesIndex
VMSMESSAGEWITHLAYERANDPUBLISHERIDINTEGERVALUESINDEX_PUBLISHER_ID = 0x4

# VmsOfferingMessageIntegerValuesIndex
VMSOFFERINGMESSAGEINTEGERVALUESINDEX_PUBLISHER_ID = 0x1
VMSOFFERINGMESSAGEINTEGERVALUESINDEX_NUMBER_OF_OFFERS = 0x2
VMSOFFERINGMESSAGEINTEGERVALUESINDEX_OFFERING_START = 0x3

# VmsSubscriptionsStateIntegerValuesIndex
VMSSUBSCRIPTIONSSTATEINTEGERVALUESINDEX_SEQUENCE_NUMBER = 0x1
VMSSUBSCRIPTIONSSTATEINTEGERVALUESINDEX_NUMBER_OF_LAYERS = 0x2
VMSSUBSCRIPTIONSSTATEINTEGERVALUESINDEX_NUMBER_OF_ASSOCIATED_LAYERS = 0x3
VMSSUBSCRIPTIONSSTATEINTEGERVALUESINDEX_SUBSCRIPTIONS_START = 0x4

# VmsAvailabilityStateIntegerValuesIndex
VMSAVAILABILITYSTATEINTEGERVALUESINDEX_SEQUENCE_NUMBER = 0x1
VMSAVAILABILITYSTATEINTEGERVALUESINDEX_NUMBER_OF_ASSOCIATED_LAYERS = 0x2
VMSAVAILABILITYSTATEINTEGERVALUESINDEX_LAYERS_START = 0x3

# VmsPublisherInformationIntegerValuesIndex
VMSPUBLISHERINFORMATIONINTEGERVALUESINDEX_PUBLISHER_ID = 0x1

# UserFlags
USERFLAGS_NONE = 0x0
USERFLAGS_SYSTEM = 0x1
USERFLAGS_GUEST = 0x2
USERFLAGS_EPHEMERAL = 0x4
USERFLAGS_ADMIN = 0x8
USERFLAGS_DISABLED = 0x10
USERFLAGS_PROFILE = 0x20

# InitialUserInfoRequestType
INITIALUSERINFOREQUESTTYPE_FIRST_BOOT = 0x1
INITIALUSERINFOREQUESTTYPE_FIRST_BOOT_AFTER_OTA = 0x2
INITIALUSERINFOREQUESTTYPE_COLD_BOOT = 0x3
INITIALUSERINFOREQUESTTYPE_RESUME = 0x4

# InitialUserInfoResponseAction
INITIALUSERINFORESPONSEACTION_DEFAULT = 0x0
INITIALUSERINFORESPONSEACTION_SWITCH = 0x1
INITIALUSERINFORESPONSEACTION_CREATE = 0x2

# SwitchUserMessageType
SWITCHUSERMESSAGETYPE_LEGACY_ANDROID_SWITCH = 0x1
SWITCHUSERMESSAGETYPE_ANDROID_SWITCH = 0x2
SWITCHUSERMESSAGETYPE_VEHICLE_RESPONSE = 0x3
SWITCHUSERMESSAGETYPE_VEHICLE_REQUEST = 0x4
SWITCHUSERMESSAGETYPE_ANDROID_POST_SWITCH = 0x5

# SwitchUserStatus
SWITCHUSERSTATUS_SUCCESS = 0x1
SWITCHUSERSTATUS_FAILURE = 0x2

# CreateUserStatus
CREATEUSERSTATUS_SUCCESS = 0x1
CREATEUSERSTATUS_FAILURE = 0x2

# UserIdentificationAssociationType
USERIDENTIFICATIONASSOCIATIONTYPE_KEY_FOB = 0x1
USERIDENTIFICATIONASSOCIATIONTYPE_CUSTOM_1 = 0x65
USERIDENTIFICATIONASSOCIATIONTYPE_CUSTOM_2 = 0x66
USERIDENTIFICATIONASSOCIATIONTYPE_CUSTOM_3 = 0x67
USERIDENTIFICATIONASSOCIATIONTYPE_CUSTOM_4 = 0x68

# UserIdentificationAssociationValue
USERIDENTIFICATIONASSOCIATIONVALUE_UNKNOWN = 0x1
USERIDENTIFICATIONASSOCIATIONVALUE_ASSOCIATED_CURRENT_USER = 0x2
USERIDENTIFICATIONASSOCIATIONVALUE_ASSOCIATED_ANOTHER_USER = 0x3
USERIDENTIFICATIONASSOCIATIONVALUE_NOT_ASSOCIATED_ANY_USER = 0x4

# UserIdentificationAssociationSetValue
USERIDENTIFICATIONASSOCIATIONSETVALUE_ASSOCIATE_CURRENT_USER = 0x1
USERIDENTIFICATIONASSOCIATIONSETVALUE_DISASSOCIATE_CURRENT_USER = 0x2
USERIDENTIFICATIONASSOCIATIONSETVALUE_DISASSOCIATE_ALL_USERS = 0x3

# RotaryInputType
ROTARYINPUTTYPE_ROTARY_INPUT_TYPE_SYSTEM_NAVIGATION = 0x0
ROTARYINPUTTYPE_ROTARY_INPUT_TYPE_AUDIO_VOLUME = 0x1

# ProcessTerminationReason
PROCESSTERMINATIONREASON_NOT_RESPONDING = 0x1
PROCESSTERMINATIONREASON_IO_OVERUSE = 0x2
PROCESSTERMINATIONREASON_MEMORY_OVERUSE = 0x3

# CustomInputType
CUSTOMINPUTTYPE_CUSTOM_EVENT_F1 = 0x3e9
CUSTOMINPUTTYPE_CUSTOM_EVENT_F2 = 0x3ea
CUSTOMINPUTTYPE_CUSTOM_EVENT_F3 = 0x3eb
CUSTOMINPUTTYPE_CUSTOM_EVENT_F4 = 0x3ec
CUSTOMINPUTTYPE_CUSTOM_EVENT_F5 = 0x3ed
CUSTOMINPUTTYPE_CUSTOM_EVENT_F6 = 0x3ee
CUSTOMINPUTTYPE_CUSTOM_EVENT_F7 = 0x3ef
CUSTOMINPUTTYPE_CUSTOM_EVENT_F8 = 0x3f0
CUSTOMINPUTTYPE_CUSTOM_EVENT_F9 = 0x3f1
CUSTOMINPUTTYPE_CUSTOM_EVENT_F10 = 0x3f2

# VendorInteriorLightning
VENDORINTERIORLIGHTNING_UNKNOWN = 0x0
VENDORINTERIORLIGHTNING_THEME_BLUE = 0x1
VENDORINTERIORLIGHTNING_THEME_GREEN = 0x2
VENDORINTERIORLIGHTNING_THEME_YELLOW = 0x3

# Create a container of value_type constants to be used by vhal_emulator
class vhal_types_2_0:
    TYPE_STRING  = [VEHICLEPROPERTYTYPE_STRING]
    TYPE_BYTES   = [VEHICLEPROPERTYTYPE_BYTES]
    TYPE_INT32   = [VEHICLEPROPERTYTYPE_BOOLEAN,
                    VEHICLEPROPERTYTYPE_INT32]
    TYPE_INT64   = [VEHICLEPROPERTYTYPE_INT64]
    TYPE_FLOAT   = [VEHICLEPROPERTYTYPE_FLOAT]
    TYPE_INT32S  = [VEHICLEPROPERTYTYPE_INT32_VEC]
    TYPE_INT64S  = [VEHICLEPROPERTYTYPE_INT64_VEC]
    TYPE_FLOATS  = [VEHICLEPROPERTYTYPE_FLOAT_VEC]
    TYPE_MIXED   = [VEHICLEPROPERTYTYPE_MIXED]
