# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/feegrant/v1beta1/query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.feegrant.v1beta1 import feegrant_pb2 as cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/feegrant/v1beta1/query.proto',
  package='cosmos.feegrant.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n#cosmos/feegrant/v1beta1/query.proto\x12\x17\x63osmos.feegrant.v1beta1\x1a&cosmos/feegrant/v1beta1/feegrant.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19\x63osmos_proto/cosmos.proto\"m\n\x15QueryAllowanceRequest\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"K\n\x16QueryAllowanceResponse\x12\x31\n\tallowance\x18\x01 \x01(\x0b\x32\x1e.cosmos.feegrant.v1beta1.Grant\"\x7f\n\x16QueryAllowancesRequest\x12)\n\x07grantee\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x8a\x01\n\x17QueryAllowancesResponse\x12\x32\n\nallowances\x18\x01 \x03(\x0b\x32\x1e.cosmos.feegrant.v1beta1.Grant\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x88\x01\n\x1fQueryAllowancesByGranterRequest\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x93\x01\n QueryAllowancesByGranterResponse\x12\x32\n\nallowances\x18\x01 \x03(\x0b\x32\x1e.cosmos.feegrant.v1beta1.Grant\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\x9f\x04\n\x05Query\x12\xac\x01\n\tAllowance\x12..cosmos.feegrant.v1beta1.QueryAllowanceRequest\x1a/.cosmos.feegrant.v1beta1.QueryAllowanceResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/cosmos/feegrant/v1beta1/allowance/{granter}/{grantee}\x12\xa6\x01\n\nAllowances\x12/.cosmos.feegrant.v1beta1.QueryAllowancesRequest\x1a\x30.cosmos.feegrant.v1beta1.QueryAllowancesResponse\"5\x82\xd3\xe4\x93\x02/\x12-/cosmos/feegrant/v1beta1/allowances/{grantee}\x12\xbd\x01\n\x13\x41llowancesByGranter\x12\x38.cosmos.feegrant.v1beta1.QueryAllowancesByGranterRequest\x1a\x39.cosmos.feegrant.v1beta1.QueryAllowancesByGranterResponse\"1\x82\xd3\xe4\x93\x02+\x12)/cosmos/feegrant/v1beta1/issued/{granter}B)Z\'github.com/cosmos/cosmos-sdk/x/feegrantb\x06proto3')
  ,
  dependencies=[cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2.DESCRIPTOR,cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_QUERYALLOWANCEREQUEST = _descriptor.Descriptor(
  name='QueryAllowanceRequest',
  full_name='cosmos.feegrant.v1beta1.QueryAllowanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.feegrant.v1beta1.QueryAllowanceRequest.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.feegrant.v1beta1.QueryAllowanceRequest.grantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
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
  serialized_start=205,
  serialized_end=314,
)


_QUERYALLOWANCERESPONSE = _descriptor.Descriptor(
  name='QueryAllowanceResponse',
  full_name='cosmos.feegrant.v1beta1.QueryAllowanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allowance', full_name='cosmos.feegrant.v1beta1.QueryAllowanceResponse.allowance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=316,
  serialized_end=391,
)


_QUERYALLOWANCESREQUEST = _descriptor.Descriptor(
  name='QueryAllowancesRequest',
  full_name='cosmos.feegrant.v1beta1.QueryAllowancesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.feegrant.v1beta1.QueryAllowancesRequest.grantee', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.feegrant.v1beta1.QueryAllowancesRequest.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=393,
  serialized_end=520,
)


_QUERYALLOWANCESRESPONSE = _descriptor.Descriptor(
  name='QueryAllowancesResponse',
  full_name='cosmos.feegrant.v1beta1.QueryAllowancesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allowances', full_name='cosmos.feegrant.v1beta1.QueryAllowancesResponse.allowances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.feegrant.v1beta1.QueryAllowancesResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=523,
  serialized_end=661,
)


_QUERYALLOWANCESBYGRANTERREQUEST = _descriptor.Descriptor(
  name='QueryAllowancesByGranterRequest',
  full_name='cosmos.feegrant.v1beta1.QueryAllowancesByGranterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.feegrant.v1beta1.QueryAllowancesByGranterRequest.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.feegrant.v1beta1.QueryAllowancesByGranterRequest.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=664,
  serialized_end=800,
)


_QUERYALLOWANCESBYGRANTERRESPONSE = _descriptor.Descriptor(
  name='QueryAllowancesByGranterResponse',
  full_name='cosmos.feegrant.v1beta1.QueryAllowancesByGranterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allowances', full_name='cosmos.feegrant.v1beta1.QueryAllowancesByGranterResponse.allowances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.feegrant.v1beta1.QueryAllowancesByGranterResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=803,
  serialized_end=950,
)

_QUERYALLOWANCERESPONSE.fields_by_name['allowance'].message_type = cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2._GRANT
_QUERYALLOWANCESREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYALLOWANCESRESPONSE.fields_by_name['allowances'].message_type = cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2._GRANT
_QUERYALLOWANCESRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYALLOWANCESBYGRANTERREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYALLOWANCESBYGRANTERRESPONSE.fields_by_name['allowances'].message_type = cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2._GRANT
_QUERYALLOWANCESBYGRANTERRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
DESCRIPTOR.message_types_by_name['QueryAllowanceRequest'] = _QUERYALLOWANCEREQUEST
DESCRIPTOR.message_types_by_name['QueryAllowanceResponse'] = _QUERYALLOWANCERESPONSE
DESCRIPTOR.message_types_by_name['QueryAllowancesRequest'] = _QUERYALLOWANCESREQUEST
DESCRIPTOR.message_types_by_name['QueryAllowancesResponse'] = _QUERYALLOWANCESRESPONSE
DESCRIPTOR.message_types_by_name['QueryAllowancesByGranterRequest'] = _QUERYALLOWANCESBYGRANTERREQUEST
DESCRIPTOR.message_types_by_name['QueryAllowancesByGranterResponse'] = _QUERYALLOWANCESBYGRANTERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryAllowanceRequest = _reflection.GeneratedProtocolMessageType('QueryAllowanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYALLOWANCEREQUEST,
  __module__ = 'cosmos.feegrant.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.QueryAllowanceRequest)
  ))
_sym_db.RegisterMessage(QueryAllowanceRequest)

QueryAllowanceResponse = _reflection.GeneratedProtocolMessageType('QueryAllowanceResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYALLOWANCERESPONSE,
  __module__ = 'cosmos.feegrant.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.QueryAllowanceResponse)
  ))
_sym_db.RegisterMessage(QueryAllowanceResponse)

QueryAllowancesRequest = _reflection.GeneratedProtocolMessageType('QueryAllowancesRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYALLOWANCESREQUEST,
  __module__ = 'cosmos.feegrant.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.QueryAllowancesRequest)
  ))
_sym_db.RegisterMessage(QueryAllowancesRequest)

QueryAllowancesResponse = _reflection.GeneratedProtocolMessageType('QueryAllowancesResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYALLOWANCESRESPONSE,
  __module__ = 'cosmos.feegrant.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.QueryAllowancesResponse)
  ))
_sym_db.RegisterMessage(QueryAllowancesResponse)

QueryAllowancesByGranterRequest = _reflection.GeneratedProtocolMessageType('QueryAllowancesByGranterRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYALLOWANCESBYGRANTERREQUEST,
  __module__ = 'cosmos.feegrant.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.QueryAllowancesByGranterRequest)
  ))
_sym_db.RegisterMessage(QueryAllowancesByGranterRequest)

QueryAllowancesByGranterResponse = _reflection.GeneratedProtocolMessageType('QueryAllowancesByGranterResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYALLOWANCESBYGRANTERRESPONSE,
  __module__ = 'cosmos.feegrant.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.QueryAllowancesByGranterResponse)
  ))
_sym_db.RegisterMessage(QueryAllowancesByGranterResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\'github.com/cosmos/cosmos-sdk/x/feegrant'))
_QUERYALLOWANCEREQUEST.fields_by_name['granter'].has_options = True
_QUERYALLOWANCEREQUEST.fields_by_name['granter']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_QUERYALLOWANCEREQUEST.fields_by_name['grantee'].has_options = True
_QUERYALLOWANCEREQUEST.fields_by_name['grantee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_QUERYALLOWANCESREQUEST.fields_by_name['grantee'].has_options = True
_QUERYALLOWANCESREQUEST.fields_by_name['grantee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_QUERYALLOWANCESBYGRANTERREQUEST.fields_by_name['granter'].has_options = True
_QUERYALLOWANCESBYGRANTERREQUEST.fields_by_name['granter']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='cosmos.feegrant.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=953,
  serialized_end=1496,
  methods=[
  _descriptor.MethodDescriptor(
    name='Allowance',
    full_name='cosmos.feegrant.v1beta1.Query.Allowance',
    index=0,
    containing_service=None,
    input_type=_QUERYALLOWANCEREQUEST,
    output_type=_QUERYALLOWANCERESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0028\0226/cosmos/feegrant/v1beta1/allowance/{granter}/{grantee}')),
  ),
  _descriptor.MethodDescriptor(
    name='Allowances',
    full_name='cosmos.feegrant.v1beta1.Query.Allowances',
    index=1,
    containing_service=None,
    input_type=_QUERYALLOWANCESREQUEST,
    output_type=_QUERYALLOWANCESRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002/\022-/cosmos/feegrant/v1beta1/allowances/{grantee}')),
  ),
  _descriptor.MethodDescriptor(
    name='AllowancesByGranter',
    full_name='cosmos.feegrant.v1beta1.Query.AllowancesByGranter',
    index=2,
    containing_service=None,
    input_type=_QUERYALLOWANCESBYGRANTERREQUEST,
    output_type=_QUERYALLOWANCESBYGRANTERRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002+\022)/cosmos/feegrant/v1beta1/issued/{granter}')),
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
