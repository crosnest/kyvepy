# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/delegation/v1beta1/query.proto

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
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from kyve.delegation.v1beta1 import params_pb2 as kyve_dot_delegation_dot_v1beta1_dot_params__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/delegation/v1beta1/query.proto',
  package='kyve.delegation.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n#kyve/delegation/v1beta1/query.proto\x12\x17kyve.delegation.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a$kyve/delegation/v1beta1/params.proto\"\x14\n\x12QueryParamsRequest\"L\n\x13QueryParamsResponse\x12\x35\n\x06params\x18\x01 \x01(\x0b\x32\x1f.kyve.delegation.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x32\x96\x01\n\x05Query\x12\x8c\x01\n\x06Params\x12+.kyve.delegation.v1beta1.QueryParamsRequest\x1a,.kyve.delegation.v1beta1.QueryParamsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/kyve/delegation/v1beta1/paramsB1Z/github.com/KYVENetwork/chain/x/delegation/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,kyve_dot_delegation_dot_v1beta1_dot_params__pb2.DESCRIPTOR,])




_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='kyve.delegation.v1beta1.QueryParamsRequest',
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
  serialized_start=154,
  serialized_end=174,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='kyve.delegation.v1beta1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='kyve.delegation.v1beta1.QueryParamsResponse.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=176,
  serialized_end=252,
)

_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = kyve_dot_delegation_dot_v1beta1_dot_params__pb2._PARAMS
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYPARAMSREQUEST,
  __module__ = 'kyve.delegation.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.QueryParamsRequest)
  ))
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYPARAMSRESPONSE,
  __module__ = 'kyve.delegation.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.QueryParamsResponse)
  ))
_sym_db.RegisterMessage(QueryParamsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z/github.com/KYVENetwork/chain/x/delegation/types'))
_QUERYPARAMSRESPONSE.fields_by_name['params'].has_options = True
_QUERYPARAMSRESPONSE.fields_by_name['params']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='kyve.delegation.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=255,
  serialized_end=405,
  methods=[
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='kyve.delegation.v1beta1.Query.Params',
    index=0,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002!\022\037/kyve/delegation/v1beta1/params')),
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
