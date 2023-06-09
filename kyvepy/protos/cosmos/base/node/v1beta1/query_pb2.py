# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/node/v1beta1/query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/base/node/v1beta1/query.proto',
  package='cosmos.base.node.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n$cosmos/base/node/v1beta1/query.proto\x12\x18\x63osmos.base.node.v1beta1\x1a\x1cgoogle/api/annotations.proto\"\x0f\n\rConfigRequest\"+\n\x0e\x43onfigResponse\x12\x19\n\x11minimum_gas_price\x18\x01 \x01(\t2\x91\x01\n\x07Service\x12\x85\x01\n\x06\x43onfig\x12\'.cosmos.base.node.v1beta1.ConfigRequest\x1a(.cosmos.base.node.v1beta1.ConfigResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /cosmos/base/node/v1beta1/configB/Z-github.com/cosmos/cosmos-sdk/client/grpc/nodeb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CONFIGREQUEST = _descriptor.Descriptor(
  name='ConfigRequest',
  full_name='cosmos.base.node.v1beta1.ConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=96,
  serialized_end=111,
)


_CONFIGRESPONSE = _descriptor.Descriptor(
  name='ConfigResponse',
  full_name='cosmos.base.node.v1beta1.ConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimum_gas_price', full_name='cosmos.base.node.v1beta1.ConfigResponse.minimum_gas_price', index=0,
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
  serialized_start=113,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['ConfigRequest'] = _CONFIGREQUEST
DESCRIPTOR.message_types_by_name['ConfigResponse'] = _CONFIGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGREQUEST,
  __module__ = 'cosmos.base.node.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.node.v1beta1.ConfigRequest)
  ))
_sym_db.RegisterMessage(ConfigRequest)

ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGRESPONSE,
  __module__ = 'cosmos.base.node.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.node.v1beta1.ConfigResponse)
  ))
_sym_db.RegisterMessage(ConfigResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z-github.com/cosmos/cosmos-sdk/client/grpc/node'))

_SERVICE = _descriptor.ServiceDescriptor(
  name='Service',
  full_name='cosmos.base.node.v1beta1.Service',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=159,
  serialized_end=304,
  methods=[
  _descriptor.MethodDescriptor(
    name='Config',
    full_name='cosmos.base.node.v1beta1.Service.Config',
    index=0,
    containing_service=None,
    input_type=_CONFIGREQUEST,
    output_type=_CONFIGRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\"\022 /cosmos/base/node/v1beta1/config')),
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICE)

DESCRIPTOR.services_by_name['Service'] = _SERVICE

# @@protoc_insertion_point(module_scope)
