# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: devconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import devcommon_pb2 as devcommon__pb2
import appconfig_pb2 as appconfig__pb2
import baseosconfig_pb2 as baseosconfig__pb2
import netconfig_pb2 as netconfig__pb2
import storage_pb2 as storage__pb2
import service_pb2 as service__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='devconfig.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x64\x65vconfig.proto\x1a\x0f\x64\x65vcommon.proto\x1a\x0f\x61ppconfig.proto\x1a\x12\x62\x61seosconfig.proto\x1a\x0fnetconfig.proto\x1a\rstorage.proto\x1a\rservice.proto\"1\n\tMapServer\x12\x10\n\x08NameOrIp\x18\x01 \x01(\t\x12\x12\n\nCredential\x18\x02 \x01(\t\"*\n\tZedServer\x12\x10\n\x08HostName\x18\x01 \x01(\t\x12\x0b\n\x03\x45ID\x18\x02 \x03(\t\"\xf5\x01\n\x11\x44\x65viceLispDetails\x12\"\n\x0eLispMapServers\x18\x01 \x03(\x0b\x32\n.MapServer\x12\x14\n\x0cLispInstance\x18\x02 \x01(\r\x12\x0b\n\x03\x45ID\x18\x04 \x01(\t\x12\x12\n\nEIDHashLen\x18\x05 \x01(\r\x12\x1e\n\nZedServers\x18\x06 \x03(\x0b\x32\n.ZedServer\x12\x1b\n\x13\x45idAllocationPrefix\x18\x08 \x01(\x0c\x12\x1e\n\x16\x45idAllocationPrefixLen\x18\t \x01(\r\x12\x12\n\nClientAddr\x18\n \x01(\t\x12\x14\n\x0c\x45xperimental\x18\x14 \x01(\x08\"F\n\x0c\x44\x65viceOpsCmd\x12\x0f\n\x07\x63ounter\x18\x02 \x01(\r\x12\x14\n\x0c\x64\x65siredState\x18\x03 \x01(\x08\x12\x0f\n\x07opsTime\x18\x04 \x01(\t\"S\n\x0fsWAdapterParams\x12\x1d\n\x05\x61Type\x18\x01 \x01(\x0e\x32\x0e.sWAdapterType\x12\x0e\n\x06vlanId\x18\t \x01(\r\x12\x11\n\tbondgroup\x18\n \x03(\t\"\x8c\x01\n\rSystemAdapter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x0c\x61llocDetails\x18\x14 \x01(\x0b\x32\x10.sWAdapterParams\x12\x12\n\nfreeUplink\x18\x02 \x01(\x08\x12\x0e\n\x06uplink\x18\x03 \x01(\x08\x12\x13\n\x0bnetworkUUID\x18\x04 \x01(\t\x12\x0c\n\x04\x61\x64\x64r\x18\x05 \x01(\t\"\xc3\x03\n\rEdgeDevConfig\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.UUIDandVersion\x12\x17\n\x0f\x64\x65vConfigSha256\x18\x02 \x01(\x0c\x12\x1a\n\x12\x64\x65vConfigSignature\x18\x03 \x01(\x0c\x12 \n\x04\x61pps\x18\x04 \x03(\x0b\x32\x12.AppInstanceConfig\x12 \n\x08networks\x18\x05 \x03(\x0b\x32\x0e.NetworkConfig\x12$\n\ndatastores\x18\x06 \x03(\x0b\x32\x10.DatastoreConfig\x12$\n\x08lispInfo\x18\x07 \x01(\x0b\x32\x12.DeviceLispDetails\x12\x1b\n\x04\x62\x61se\x18\x08 \x03(\x0b\x32\r.BaseOSConfig\x12\x1d\n\x06reboot\x18\t \x01(\x0b\x32\r.DeviceOpsCmd\x12\x1d\n\x06\x62\x61\x63kup\x18\n \x01(\x0b\x32\r.DeviceOpsCmd\x12 \n\x0b\x63onfigItems\x18\x0b \x03(\x0b\x32\x0b.ConfigItem\x12)\n\x11systemAdapterList\x18\x0c \x03(\x0b\x32\x0e.SystemAdapter\x12(\n\x08services\x18\r \x03(\x0b\x32\x16.ServiceInstanceConfig\"\x9c\x01\n\nConfigItem\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x13\n\tboolValue\x18\x03 \x01(\x08H\x00\x12\x15\n\x0buint32Value\x18\x04 \x01(\rH\x00\x12\x15\n\x0buint64Value\x18\x05 \x01(\x04H\x00\x12\x14\n\nfloatValue\x18\x06 \x01(\x02H\x00\x12\x15\n\x0bstringValue\x18\x07 \x01(\tH\x00\x42\x11\n\x0f\x63onfigItemValue\"#\n\rConfigRequest\x12\x12\n\nconfigHash\x18\x01 \x01(\t\"D\n\x0e\x43onfigResponse\x12\x1e\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x0e.EdgeDevConfig\x12\x12\n\nconfigHash\x18\x02 \x01(\t*/\n\rsWAdapterType\x12\n\n\x06IGNORE\x10\x00\x12\x08\n\x04VLAN\x10\x01\x12\x08\n\x04\x42OND\x10\x02\x42@\n\x1f\x63om.zededa.cloud.uservice.protoZ\x1dgithub.com/zededa/api/zconfigb\x06proto3')
  ,
  dependencies=[devcommon__pb2.DESCRIPTOR,appconfig__pb2.DESCRIPTOR,baseosconfig__pb2.DESCRIPTOR,netconfig__pb2.DESCRIPTOR,storage__pb2.DESCRIPTOR,service__pb2.DESCRIPTOR,])

_SWADAPTERTYPE = _descriptor.EnumDescriptor(
  name='sWAdapterType',
  full_name='sWAdapterType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IGNORE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VLAN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOND', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1483,
  serialized_end=1530,
)
_sym_db.RegisterEnumDescriptor(_SWADAPTERTYPE)

sWAdapterType = enum_type_wrapper.EnumTypeWrapper(_SWADAPTERTYPE)
IGNORE = 0
VLAN = 1
BOND = 2



_MAPSERVER = _descriptor.Descriptor(
  name='MapServer',
  full_name='MapServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='NameOrIp', full_name='MapServer.NameOrIp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Credential', full_name='MapServer.Credential', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=169,
)


_ZEDSERVER = _descriptor.Descriptor(
  name='ZedServer',
  full_name='ZedServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='HostName', full_name='ZedServer.HostName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EID', full_name='ZedServer.EID', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=213,
)


_DEVICELISPDETAILS = _descriptor.Descriptor(
  name='DeviceLispDetails',
  full_name='DeviceLispDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='LispMapServers', full_name='DeviceLispDetails.LispMapServers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LispInstance', full_name='DeviceLispDetails.LispInstance', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EID', full_name='DeviceLispDetails.EID', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EIDHashLen', full_name='DeviceLispDetails.EIDHashLen', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ZedServers', full_name='DeviceLispDetails.ZedServers', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EidAllocationPrefix', full_name='DeviceLispDetails.EidAllocationPrefix', index=5,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EidAllocationPrefixLen', full_name='DeviceLispDetails.EidAllocationPrefixLen', index=6,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ClientAddr', full_name='DeviceLispDetails.ClientAddr', index=7,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Experimental', full_name='DeviceLispDetails.Experimental', index=8,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=461,
)


_DEVICEOPSCMD = _descriptor.Descriptor(
  name='DeviceOpsCmd',
  full_name='DeviceOpsCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='counter', full_name='DeviceOpsCmd.counter', index=0,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desiredState', full_name='DeviceOpsCmd.desiredState', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opsTime', full_name='DeviceOpsCmd.opsTime', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=463,
  serialized_end=533,
)


_SWADAPTERPARAMS = _descriptor.Descriptor(
  name='sWAdapterParams',
  full_name='sWAdapterParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aType', full_name='sWAdapterParams.aType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vlanId', full_name='sWAdapterParams.vlanId', index=1,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bondgroup', full_name='sWAdapterParams.bondgroup', index=2,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=618,
)


_SYSTEMADAPTER = _descriptor.Descriptor(
  name='SystemAdapter',
  full_name='SystemAdapter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SystemAdapter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocDetails', full_name='SystemAdapter.allocDetails', index=1,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freeUplink', full_name='SystemAdapter.freeUplink', index=2,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uplink', full_name='SystemAdapter.uplink', index=3,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='networkUUID', full_name='SystemAdapter.networkUUID', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addr', full_name='SystemAdapter.addr', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=621,
  serialized_end=761,
)


_EDGEDEVCONFIG = _descriptor.Descriptor(
  name='EdgeDevConfig',
  full_name='EdgeDevConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EdgeDevConfig.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devConfigSha256', full_name='EdgeDevConfig.devConfigSha256', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devConfigSignature', full_name='EdgeDevConfig.devConfigSignature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apps', full_name='EdgeDevConfig.apps', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='networks', full_name='EdgeDevConfig.networks', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datastores', full_name='EdgeDevConfig.datastores', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lispInfo', full_name='EdgeDevConfig.lispInfo', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base', full_name='EdgeDevConfig.base', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reboot', full_name='EdgeDevConfig.reboot', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backup', full_name='EdgeDevConfig.backup', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configItems', full_name='EdgeDevConfig.configItems', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systemAdapterList', full_name='EdgeDevConfig.systemAdapterList', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='services', full_name='EdgeDevConfig.services', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=764,
  serialized_end=1215,
)


_CONFIGITEM = _descriptor.Descriptor(
  name='ConfigItem',
  full_name='ConfigItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ConfigItem.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolValue', full_name='ConfigItem.boolValue', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint32Value', full_name='ConfigItem.uint32Value', index=2,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64Value', full_name='ConfigItem.uint64Value', index=3,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floatValue', full_name='ConfigItem.floatValue', index=4,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stringValue', full_name='ConfigItem.stringValue', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='configItemValue', full_name='ConfigItem.configItemValue',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1218,
  serialized_end=1374,
)


_CONFIGREQUEST = _descriptor.Descriptor(
  name='ConfigRequest',
  full_name='ConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configHash', full_name='ConfigRequest.configHash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1376,
  serialized_end=1411,
)


_CONFIGRESPONSE = _descriptor.Descriptor(
  name='ConfigResponse',
  full_name='ConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='ConfigResponse.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configHash', full_name='ConfigResponse.configHash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1413,
  serialized_end=1481,
)

_DEVICELISPDETAILS.fields_by_name['LispMapServers'].message_type = _MAPSERVER
_DEVICELISPDETAILS.fields_by_name['ZedServers'].message_type = _ZEDSERVER
_SWADAPTERPARAMS.fields_by_name['aType'].enum_type = _SWADAPTERTYPE
_SYSTEMADAPTER.fields_by_name['allocDetails'].message_type = _SWADAPTERPARAMS
_EDGEDEVCONFIG.fields_by_name['id'].message_type = devcommon__pb2._UUIDANDVERSION
_EDGEDEVCONFIG.fields_by_name['apps'].message_type = appconfig__pb2._APPINSTANCECONFIG
_EDGEDEVCONFIG.fields_by_name['networks'].message_type = netconfig__pb2._NETWORKCONFIG
_EDGEDEVCONFIG.fields_by_name['datastores'].message_type = storage__pb2._DATASTORECONFIG
_EDGEDEVCONFIG.fields_by_name['lispInfo'].message_type = _DEVICELISPDETAILS
_EDGEDEVCONFIG.fields_by_name['base'].message_type = baseosconfig__pb2._BASEOSCONFIG
_EDGEDEVCONFIG.fields_by_name['reboot'].message_type = _DEVICEOPSCMD
_EDGEDEVCONFIG.fields_by_name['backup'].message_type = _DEVICEOPSCMD
_EDGEDEVCONFIG.fields_by_name['configItems'].message_type = _CONFIGITEM
_EDGEDEVCONFIG.fields_by_name['systemAdapterList'].message_type = _SYSTEMADAPTER
_EDGEDEVCONFIG.fields_by_name['services'].message_type = service__pb2._SERVICEINSTANCECONFIG
_CONFIGITEM.oneofs_by_name['configItemValue'].fields.append(
  _CONFIGITEM.fields_by_name['boolValue'])
_CONFIGITEM.fields_by_name['boolValue'].containing_oneof = _CONFIGITEM.oneofs_by_name['configItemValue']
_CONFIGITEM.oneofs_by_name['configItemValue'].fields.append(
  _CONFIGITEM.fields_by_name['uint32Value'])
_CONFIGITEM.fields_by_name['uint32Value'].containing_oneof = _CONFIGITEM.oneofs_by_name['configItemValue']
_CONFIGITEM.oneofs_by_name['configItemValue'].fields.append(
  _CONFIGITEM.fields_by_name['uint64Value'])
_CONFIGITEM.fields_by_name['uint64Value'].containing_oneof = _CONFIGITEM.oneofs_by_name['configItemValue']
_CONFIGITEM.oneofs_by_name['configItemValue'].fields.append(
  _CONFIGITEM.fields_by_name['floatValue'])
_CONFIGITEM.fields_by_name['floatValue'].containing_oneof = _CONFIGITEM.oneofs_by_name['configItemValue']
_CONFIGITEM.oneofs_by_name['configItemValue'].fields.append(
  _CONFIGITEM.fields_by_name['stringValue'])
_CONFIGITEM.fields_by_name['stringValue'].containing_oneof = _CONFIGITEM.oneofs_by_name['configItemValue']
_CONFIGRESPONSE.fields_by_name['config'].message_type = _EDGEDEVCONFIG
DESCRIPTOR.message_types_by_name['MapServer'] = _MAPSERVER
DESCRIPTOR.message_types_by_name['ZedServer'] = _ZEDSERVER
DESCRIPTOR.message_types_by_name['DeviceLispDetails'] = _DEVICELISPDETAILS
DESCRIPTOR.message_types_by_name['DeviceOpsCmd'] = _DEVICEOPSCMD
DESCRIPTOR.message_types_by_name['sWAdapterParams'] = _SWADAPTERPARAMS
DESCRIPTOR.message_types_by_name['SystemAdapter'] = _SYSTEMADAPTER
DESCRIPTOR.message_types_by_name['EdgeDevConfig'] = _EDGEDEVCONFIG
DESCRIPTOR.message_types_by_name['ConfigItem'] = _CONFIGITEM
DESCRIPTOR.message_types_by_name['ConfigRequest'] = _CONFIGREQUEST
DESCRIPTOR.message_types_by_name['ConfigResponse'] = _CONFIGRESPONSE
DESCRIPTOR.enum_types_by_name['sWAdapterType'] = _SWADAPTERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MapServer = _reflection.GeneratedProtocolMessageType('MapServer', (_message.Message,), dict(
  DESCRIPTOR = _MAPSERVER,
  __module__ = 'devconfig_pb2'
  # @@protoc_insertion_point(class_scope:MapServer)
  ))
_sym_db.RegisterMessage(MapServer)

ZedServer = _reflection.GeneratedProtocolMessageType('ZedServer', (_message.Message,), dict(
  DESCRIPTOR = _ZEDSERVER,
  __module__ = 'devconfig_pb2'
  # @@protoc_insertion_point(class_scope:ZedServer)
  ))
_sym_db.RegisterMessage(ZedServer)

DeviceLispDetails = _reflection.GeneratedProtocolMessageType('DeviceLispDetails', (_message.Message,), dict(
  DESCRIPTOR = _DEVICELISPDETAILS,
  __module__ = 'devconfig_pb2'
  # @@protoc_insertion_point(class_scope:DeviceLispDetails)
  ))
_sym_db.RegisterMessage(DeviceLispDetails)

DeviceOpsCmd = _reflection.GeneratedProtocolMessageType('DeviceOpsCmd', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEOPSCMD,
  __module__ = 'devconfig_pb2'
  # @@protoc_insertion_point(class_scope:DeviceOpsCmd)
  ))
_sym_db.RegisterMessage(DeviceOpsCmd)

sWAdapterParams = _reflection.GeneratedProtocolMessageType('sWAdapterParams', (_message.Message,), dict(
  DESCRIPTOR = _SWADAPTERPARAMS,
  __module__ = 'devconfig_pb2'
  # @@protoc_insertion_point(class_scope:sWAdapterParams)
  ))
_sym_db.RegisterMessage(sWAdapterParams)

SystemAdapter = _reflection.GeneratedProtocolMessageType('SystemAdapter', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMADAPTER,
  __module__ = 'devconfig_pb2'
  # @@protoc_insertion_point(class_scope:SystemAdapter)
  ))
_sym_db.RegisterMessage(SystemAdapter)

EdgeDevConfig = _reflection.GeneratedProtocolMessageType('EdgeDevConfig', (_message.Message,), dict(
  DESCRIPTOR = _EDGEDEVCONFIG,
  __module__ = 'devconfig_pb2'
  # @@protoc_insertion_point(class_scope:EdgeDevConfig)
  ))
_sym_db.RegisterMessage(EdgeDevConfig)

ConfigItem = _reflection.GeneratedProtocolMessageType('ConfigItem', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGITEM,
  __module__ = 'devconfig_pb2'
  # @@protoc_insertion_point(class_scope:ConfigItem)
  ))
_sym_db.RegisterMessage(ConfigItem)

ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGREQUEST,
  __module__ = 'devconfig_pb2'
  # @@protoc_insertion_point(class_scope:ConfigRequest)
  ))
_sym_db.RegisterMessage(ConfigRequest)

ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGRESPONSE,
  __module__ = 'devconfig_pb2'
  # @@protoc_insertion_point(class_scope:ConfigResponse)
  ))
_sym_db.RegisterMessage(ConfigResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037com.zededa.cloud.uservice.protoZ\035github.com/zededa/api/zconfig'))
# @@protoc_insertion_point(module_scope)
