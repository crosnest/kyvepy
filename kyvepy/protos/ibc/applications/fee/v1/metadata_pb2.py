# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/fee/v1/metadata.proto

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
  name='ibc/applications/fee/v1/metadata.proto',
  package='ibc.applications.fee.v1',
  syntax='proto3',
  serialized_pb=_b('\n&ibc/applications/fee/v1/metadata.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\"d\n\x08Metadata\x12+\n\x0b\x66\x65\x65_version\x18\x01 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"fee_version\"\x12+\n\x0b\x61pp_version\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"app_version\"B7Z5github.com/cosmos/ibc-go/v6/modules/apps/29-fee/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='ibc.applications.fee.v1.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fee_version', full_name='ibc.applications.fee.v1.Metadata.fee_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\022yaml:\"fee_version\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_version', full_name='ibc.applications.fee.v1.Metadata.app_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\022yaml:\"app_version\"')), file=DESCRIPTOR),
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
  serialized_start=89,
  serialized_end=189,
)

DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'ibc.applications.fee.v1.metadata_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.Metadata)
  ))
_sym_db.RegisterMessage(Metadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z5github.com/cosmos/ibc-go/v6/modules/apps/29-fee/types'))
_METADATA.fields_by_name['fee_version'].has_options = True
_METADATA.fields_by_name['fee_version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\022yaml:\"fee_version\"'))
_METADATA.fields_by_name['app_version'].has_options = True
_METADATA.fields_by_name['app_version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\022yaml:\"app_version\"'))
# @@protoc_insertion_point(module_scope)
