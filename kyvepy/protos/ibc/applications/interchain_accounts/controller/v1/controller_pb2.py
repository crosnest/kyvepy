# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/interchain_accounts/controller/v1/controller.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/applications/interchain_accounts/controller/v1/controller.proto',
  package='ibc.applications.interchain_accounts.controller.v1',
  syntax='proto3',
  serialized_pb=_b('\nCibc/applications/interchain_accounts/controller/v1/controller.proto\x12\x32ibc.applications.interchain_accounts.controller.v1\x1a\x14gogoproto/gogo.proto\"C\n\x06Params\x12\x39\n\x12\x63ontroller_enabled\x18\x01 \x01(\x08\x42\x1d\xf2\xde\x1f\x19yaml:\"controller_enabled\"BRZPgithub.com/cosmos/ibc-go/v6/modules/apps/27-interchain-accounts/controller/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='ibc.applications.interchain_accounts.controller.v1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='controller_enabled', full_name='ibc.applications.interchain_accounts.controller.v1.Params.controller_enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\031yaml:\"controller_enabled\"')), file=DESCRIPTOR),
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
  serialized_start=145,
  serialized_end=212,
)

DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
  DESCRIPTOR = _PARAMS,
  __module__ = 'ibc.applications.interchain_accounts.controller.v1.controller_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.interchain_accounts.controller.v1.Params)
  ))
_sym_db.RegisterMessage(Params)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('ZPgithub.com/cosmos/ibc-go/v6/modules/apps/27-interchain-accounts/controller/types'))
_PARAMS.fields_by_name['controller_enabled'].has_options = True
_PARAMS.fields_by_name['controller_enabled']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\031yaml:\"controller_enabled\"'))
# @@protoc_insertion_point(module_scope)