# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evecommon import evecommon_pb2 as evecommon_dot_evecommon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth/auth.proto',
  package='org.lfedge.eve.auth',
  syntax='proto3',
  serialized_options=b'\n\023org.lfedge.eve.authZ\"github.com/lf-edge/eve/api/go/auth',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x61uth/auth.proto\x12\x13org.lfedge.eve.auth\x1a\x19\x65vecommon/evecommon.proto\"\x1b\n\x08\x41uthBody\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\"\xbf\x01\n\rAuthContainer\x12\x37\n\x10protectedPayload\x18\x01 \x01(\x0b\x32\x1d.org.lfedge.eve.auth.AuthBody\x12\x32\n\x04\x61lgo\x18\x02 \x01(\x0e\x32$.org.lfedge.eve.common.HashAlgorithm\x12\x16\n\x0esenderCertHash\x18\x03 \x01(\x0c\x12\x15\n\rsignatureHash\x18\x04 \x01(\x0c\x12\x12\n\nsenderCert\x18\x05 \x01(\x0c\x42\x39\n\x13org.lfedge.eve.authZ\"github.com/lf-edge/eve/api/go/authb\x06proto3'
  ,
  dependencies=[evecommon_dot_evecommon__pb2.DESCRIPTOR,])




_AUTHBODY = _descriptor.Descriptor(
  name='AuthBody',
  full_name='org.lfedge.eve.auth.AuthBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='org.lfedge.eve.auth.AuthBody.payload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=67,
  serialized_end=94,
)


_AUTHCONTAINER = _descriptor.Descriptor(
  name='AuthContainer',
  full_name='org.lfedge.eve.auth.AuthContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protectedPayload', full_name='org.lfedge.eve.auth.AuthContainer.protectedPayload', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='algo', full_name='org.lfedge.eve.auth.AuthContainer.algo', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='senderCertHash', full_name='org.lfedge.eve.auth.AuthContainer.senderCertHash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signatureHash', full_name='org.lfedge.eve.auth.AuthContainer.signatureHash', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='senderCert', full_name='org.lfedge.eve.auth.AuthContainer.senderCert', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=97,
  serialized_end=288,
)

_AUTHCONTAINER.fields_by_name['protectedPayload'].message_type = _AUTHBODY
_AUTHCONTAINER.fields_by_name['algo'].enum_type = evecommon_dot_evecommon__pb2._HASHALGORITHM
DESCRIPTOR.message_types_by_name['AuthBody'] = _AUTHBODY
DESCRIPTOR.message_types_by_name['AuthContainer'] = _AUTHCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthBody = _reflection.GeneratedProtocolMessageType('AuthBody', (_message.Message,), {
  'DESCRIPTOR' : _AUTHBODY,
  '__module__' : 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.auth.AuthBody)
  })
_sym_db.RegisterMessage(AuthBody)

AuthContainer = _reflection.GeneratedProtocolMessageType('AuthContainer', (_message.Message,), {
  'DESCRIPTOR' : _AUTHCONTAINER,
  '__module__' : 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.auth.AuthContainer)
  })
_sym_db.RegisterMessage(AuthContainer)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
