# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logs/log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='logs/log.proto',
  package='org.lfedge.eve.logs',
  syntax='proto3',
  serialized_options=b'\n\023org.lfedge.eve.logsZ\"github.com/lf-edge/eve/api/go/logs',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0elogs/log.proto\x12\x13org.lfedge.eve.logs\x1a\x1fgoogle/protobuf/timestamp.proto\"\x90\x02\n\x08LogEntry\x12\x10\n\x08severity\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0b\n\x03iid\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\r\n\x05msgid\x18\x05 \x01(\x04\x12\x35\n\x04tags\x18\x06 \x03(\x0b\x32\'.org.lfedge.eve.logs.LogEntry.TagsEntry\x12-\n\ttimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x66ilename\x18\x08 \x01(\t\x12\x10\n\x08\x66unction\x18\t \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x98\x01\n\tLogBundle\x12\r\n\x05\x64\x65vID\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12*\n\x03log\x18\x03 \x03(\x0b\x32\x1d.org.lfedge.eve.logs.LogEntry\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\neveVersion\x18\x05 \x01(\t\"q\n\x14\x41ppInstanceLogBundle\x12*\n\x03log\x18\x01 \x03(\x0b\x32\x1d.org.lfedge.eve.logs.LogEntry\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"G\n\rServerMetrics\x12\x16\n\x0e\x63pu_percentage\x18\x01 \x01(\x02\x12\x1e\n\x16log_process_delay_msec\x18\x02 \x01(\rB9\n\x13org.lfedge.eve.logsZ\"github.com/lf-edge/eve/api/go/logsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_LOGENTRY_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='org.lfedge.eve.logs.LogEntry.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='org.lfedge.eve.logs.LogEntry.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='org.lfedge.eve.logs.LogEntry.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=302,
  serialized_end=345,
)

_LOGENTRY = _descriptor.Descriptor(
  name='LogEntry',
  full_name='org.lfedge.eve.logs.LogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='severity', full_name='org.lfedge.eve.logs.LogEntry.severity', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='org.lfedge.eve.logs.LogEntry.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iid', full_name='org.lfedge.eve.logs.LogEntry.iid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='org.lfedge.eve.logs.LogEntry.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msgid', full_name='org.lfedge.eve.logs.LogEntry.msgid', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='org.lfedge.eve.logs.LogEntry.tags', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='org.lfedge.eve.logs.LogEntry.timestamp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filename', full_name='org.lfedge.eve.logs.LogEntry.filename', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='function', full_name='org.lfedge.eve.logs.LogEntry.function', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LOGENTRY_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=345,
)


_LOGBUNDLE = _descriptor.Descriptor(
  name='LogBundle',
  full_name='org.lfedge.eve.logs.LogBundle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='devID', full_name='org.lfedge.eve.logs.LogBundle.devID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='org.lfedge.eve.logs.LogBundle.image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log', full_name='org.lfedge.eve.logs.LogBundle.log', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='org.lfedge.eve.logs.LogBundle.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eveVersion', full_name='org.lfedge.eve.logs.LogBundle.eveVersion', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=348,
  serialized_end=500,
)


_APPINSTANCELOGBUNDLE = _descriptor.Descriptor(
  name='AppInstanceLogBundle',
  full_name='org.lfedge.eve.logs.AppInstanceLogBundle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log', full_name='org.lfedge.eve.logs.AppInstanceLogBundle.log', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='org.lfedge.eve.logs.AppInstanceLogBundle.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=615,
)


_SERVERMETRICS = _descriptor.Descriptor(
  name='ServerMetrics',
  full_name='org.lfedge.eve.logs.ServerMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu_percentage', full_name='org.lfedge.eve.logs.ServerMetrics.cpu_percentage', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log_process_delay_msec', full_name='org.lfedge.eve.logs.ServerMetrics.log_process_delay_msec', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=617,
  serialized_end=688,
)

_LOGENTRY_TAGSENTRY.containing_type = _LOGENTRY
_LOGENTRY.fields_by_name['tags'].message_type = _LOGENTRY_TAGSENTRY
_LOGENTRY.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGBUNDLE.fields_by_name['log'].message_type = _LOGENTRY
_LOGBUNDLE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_APPINSTANCELOGBUNDLE.fields_by_name['log'].message_type = _LOGENTRY
_APPINSTANCELOGBUNDLE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['LogEntry'] = _LOGENTRY
DESCRIPTOR.message_types_by_name['LogBundle'] = _LOGBUNDLE
DESCRIPTOR.message_types_by_name['AppInstanceLogBundle'] = _APPINSTANCELOGBUNDLE
DESCRIPTOR.message_types_by_name['ServerMetrics'] = _SERVERMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogEntry = _reflection.GeneratedProtocolMessageType('LogEntry', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOGENTRY_TAGSENTRY,
    '__module__' : 'logs.log_pb2'
    # @@protoc_insertion_point(class_scope:org.lfedge.eve.logs.LogEntry.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _LOGENTRY,
  '__module__' : 'logs.log_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.logs.LogEntry)
  })
_sym_db.RegisterMessage(LogEntry)
_sym_db.RegisterMessage(LogEntry.TagsEntry)

LogBundle = _reflection.GeneratedProtocolMessageType('LogBundle', (_message.Message,), {
  'DESCRIPTOR' : _LOGBUNDLE,
  '__module__' : 'logs.log_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.logs.LogBundle)
  })
_sym_db.RegisterMessage(LogBundle)

AppInstanceLogBundle = _reflection.GeneratedProtocolMessageType('AppInstanceLogBundle', (_message.Message,), {
  'DESCRIPTOR' : _APPINSTANCELOGBUNDLE,
  '__module__' : 'logs.log_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.logs.AppInstanceLogBundle)
  })
_sym_db.RegisterMessage(AppInstanceLogBundle)

ServerMetrics = _reflection.GeneratedProtocolMessageType('ServerMetrics', (_message.Message,), {
  'DESCRIPTOR' : _SERVERMETRICS,
  '__module__' : 'logs.log_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.logs.ServerMetrics)
  })
_sym_db.RegisterMessage(ServerMetrics)


DESCRIPTOR._options = None
_LOGENTRY_TAGSENTRY._options = None
# @@protoc_insertion_point(module_scope)
