# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/interchain_accounts/controller/v1/query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ibc.applications.interchain_accounts.controller.v1 import controller_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_controller__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/applications/interchain_accounts/controller/v1/query.proto',
  package='ibc.applications.interchain_accounts.controller.v1',
  syntax='proto3',
  serialized_pb=_b('\n>ibc/applications/interchain_accounts/controller/v1/query.proto\x12\x32ibc.applications.interchain_accounts.controller.v1\x1a\x43ibc/applications/interchain_accounts/controller/v1/controller.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\"_\n\x1dQueryInterchainAccountRequest\x12\r\n\x05owner\x18\x01 \x01(\t\x12/\n\rconnection_id\x18\x02 \x01(\tB\x18\xf2\xde\x1f\x14yaml:\"connection_id\"\"1\n\x1eQueryInterchainAccountResponse\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\x14\n\x12QueryParamsRequest\"a\n\x13QueryParamsResponse\x12J\n\x06params\x18\x01 \x01(\x0b\x32:.ibc.applications.interchain_accounts.controller.v1.Params2\xfc\x03\n\x05Query\x12\x9a\x02\n\x11InterchainAccount\x12Q.ibc.applications.interchain_accounts.controller.v1.QueryInterchainAccountRequest\x1aR.ibc.applications.interchain_accounts.controller.v1.QueryInterchainAccountResponse\"^\x82\xd3\xe4\x93\x02X\x12V/ibc/apps/interchain_accounts/controller/v1/owners/{owner}/connections/{connection_id}\x12\xd5\x01\n\x06Params\x12\x46.ibc.applications.interchain_accounts.controller.v1.QueryParamsRequest\x1aG.ibc.applications.interchain_accounts.controller.v1.QueryParamsResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/ibc/apps/interchain_accounts/controller/v1/paramsBRZPgithub.com/cosmos/ibc-go/v6/modules/apps/27-interchain-accounts/controller/typesb\x06proto3')
  ,
  dependencies=[ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_controller__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_QUERYINTERCHAINACCOUNTREQUEST = _descriptor.Descriptor(
  name='QueryInterchainAccountRequest',
  full_name='ibc.applications.interchain_accounts.controller.v1.QueryInterchainAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='ibc.applications.interchain_accounts.controller.v1.QueryInterchainAccountRequest.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='ibc.applications.interchain_accounts.controller.v1.QueryInterchainAccountRequest.connection_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\024yaml:\"connection_id\"')), file=DESCRIPTOR),
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
  serialized_start=239,
  serialized_end=334,
)


_QUERYINTERCHAINACCOUNTRESPONSE = _descriptor.Descriptor(
  name='QueryInterchainAccountResponse',
  full_name='ibc.applications.interchain_accounts.controller.v1.QueryInterchainAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='ibc.applications.interchain_accounts.controller.v1.QueryInterchainAccountResponse.address', index=0,
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
  serialized_start=336,
  serialized_end=385,
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='ibc.applications.interchain_accounts.controller.v1.QueryParamsRequest',
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
  serialized_start=387,
  serialized_end=407,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='ibc.applications.interchain_accounts.controller.v1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='ibc.applications.interchain_accounts.controller.v1.QueryParamsResponse.params', index=0,
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
  serialized_start=409,
  serialized_end=506,
)

_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_controller__pb2._PARAMS
DESCRIPTOR.message_types_by_name['QueryInterchainAccountRequest'] = _QUERYINTERCHAINACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['QueryInterchainAccountResponse'] = _QUERYINTERCHAINACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryInterchainAccountRequest = _reflection.GeneratedProtocolMessageType('QueryInterchainAccountRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYINTERCHAINACCOUNTREQUEST,
  __module__ = 'ibc.applications.interchain_accounts.controller.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.interchain_accounts.controller.v1.QueryInterchainAccountRequest)
  ))
_sym_db.RegisterMessage(QueryInterchainAccountRequest)

QueryInterchainAccountResponse = _reflection.GeneratedProtocolMessageType('QueryInterchainAccountResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYINTERCHAINACCOUNTRESPONSE,
  __module__ = 'ibc.applications.interchain_accounts.controller.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.interchain_accounts.controller.v1.QueryInterchainAccountResponse)
  ))
_sym_db.RegisterMessage(QueryInterchainAccountResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYPARAMSREQUEST,
  __module__ = 'ibc.applications.interchain_accounts.controller.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.interchain_accounts.controller.v1.QueryParamsRequest)
  ))
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYPARAMSRESPONSE,
  __module__ = 'ibc.applications.interchain_accounts.controller.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.interchain_accounts.controller.v1.QueryParamsResponse)
  ))
_sym_db.RegisterMessage(QueryParamsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('ZPgithub.com/cosmos/ibc-go/v6/modules/apps/27-interchain-accounts/controller/types'))
_QUERYINTERCHAINACCOUNTREQUEST.fields_by_name['connection_id'].has_options = True
_QUERYINTERCHAINACCOUNTREQUEST.fields_by_name['connection_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\024yaml:\"connection_id\"'))

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='ibc.applications.interchain_accounts.controller.v1.Query',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=509,
  serialized_end=1017,
  methods=[
  _descriptor.MethodDescriptor(
    name='InterchainAccount',
    full_name='ibc.applications.interchain_accounts.controller.v1.Query.InterchainAccount',
    index=0,
    containing_service=None,
    input_type=_QUERYINTERCHAINACCOUNTREQUEST,
    output_type=_QUERYINTERCHAINACCOUNTRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002X\022V/ibc/apps/interchain_accounts/controller/v1/owners/{owner}/connections/{connection_id}')),
  ),
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='ibc.applications.interchain_accounts.controller.v1.Query.Params',
    index=1,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0024\0222/ibc/apps/interchain_accounts/controller/v1/params')),
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)