# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/query/v1beta1/delegation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from kyve.query.v1beta1 import query_pb2 as kyve_dot_query_dot_v1beta1_dot_query__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/query/v1beta1/delegation.proto',
  package='kyve.query.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n#kyve/query/v1beta1/delegation.proto\x12\x12kyve.query.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ekyve/query/v1beta1/query.proto\":\n\x15QueryDelegatorRequest\x12\x0e\n\x06staker\x18\x01 \x01(\t\x12\x11\n\tdelegator\x18\x02 \x01(\t\"X\n\x16QueryDelegatorResponse\x12>\n\tdelegator\x18\x01 \x01(\x0b\x32+.kyve.query.v1beta1.StakerDelegatorResponse\"o\n\x17StakerDelegatorResponse\x12\x11\n\tdelegator\x18\x01 \x01(\t\x12\x16\n\x0e\x63urrent_reward\x18\x02 \x01(\x04\x12\x19\n\x11\x64\x65legation_amount\x18\x03 \x01(\x04\x12\x0e\n\x06staker\x18\x04 \x01(\t\"l\n\x1eQueryDelegatorsByStakerRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x12\x0e\n\x06staker\x18\x02 \x01(\t\"\xde\x01\n\x1fQueryDelegatorsByStakerResponse\x12\x45\n\ndelegators\x18\x01 \x03(\x0b\x32+.kyve.query.v1beta1.StakerDelegatorResponseB\x04\xc8\xde\x1f\x00\x12\x18\n\x10total_delegation\x18\x02 \x01(\x04\x12\x1d\n\x15total_delegator_count\x18\x03 \x01(\x04\x12;\n\npagination\x18\x04 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"o\n\x1eQueryStakersByDelegatorRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x12\x11\n\tdelegator\x18\x02 \x01(\t\"\xb9\x01\n\x1fQueryStakersByDelegatorResponse\x12\x11\n\tdelegator\x18\x01 \x01(\t\x12\x46\n\x07stakers\x18\x02 \x03(\x0b\x32/.kyve.query.v1beta1.DelegationForStakerResponseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x03 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x80\x01\n\x1b\x44\x65legationForStakerResponse\x12.\n\x06staker\x18\x01 \x01(\x0b\x32\x1e.kyve.query.v1beta1.FullStaker\x12\x16\n\x0e\x63urrent_reward\x18\x02 \x01(\x04\x12\x19\n\x11\x64\x65legation_amount\x18\x03 \x01(\x04\x32\xab\x04\n\x0fQueryDelegation\x12\x9e\x01\n\tDelegator\x12).kyve.query.v1beta1.QueryDelegatorRequest\x1a*.kyve.query.v1beta1.QueryDelegatorResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/kyve/query/v1beta1/delegator/{staker}/{delegator}\x12\xb8\x01\n\x12\x44\x65legatorsByStaker\x12\x32.kyve.query.v1beta1.QueryDelegatorsByStakerRequest\x1a\x33.kyve.query.v1beta1.QueryDelegatorsByStakerResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/kyve/query/v1beta1/delegators_by_staker/{staker}\x12\xbb\x01\n\x12StakersByDelegator\x12\x32.kyve.query.v1beta1.QueryStakersByDelegatorRequest\x1a\x33.kyve.query.v1beta1.QueryStakersByDelegatorResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/kyve/query/v1beta1/stakers_by_delegator/{delegator}B,Z*github.com/KYVENetwork/chain/x/query/typesb\x06proto3')
  ,
  dependencies=[cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,kyve_dot_query_dot_v1beta1_dot_query__pb2.DESCRIPTOR,])




_QUERYDELEGATORREQUEST = _descriptor.Descriptor(
  name='QueryDelegatorRequest',
  full_name='kyve.query.v1beta1.QueryDelegatorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.query.v1beta1.QueryDelegatorRequest.staker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegator', full_name='kyve.query.v1beta1.QueryDelegatorRequest.delegator', index=1,
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
  serialized_start=187,
  serialized_end=245,
)


_QUERYDELEGATORRESPONSE = _descriptor.Descriptor(
  name='QueryDelegatorResponse',
  full_name='kyve.query.v1beta1.QueryDelegatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delegator', full_name='kyve.query.v1beta1.QueryDelegatorResponse.delegator', index=0,
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
  serialized_start=247,
  serialized_end=335,
)


_STAKERDELEGATORRESPONSE = _descriptor.Descriptor(
  name='StakerDelegatorResponse',
  full_name='kyve.query.v1beta1.StakerDelegatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delegator', full_name='kyve.query.v1beta1.StakerDelegatorResponse.delegator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_reward', full_name='kyve.query.v1beta1.StakerDelegatorResponse.current_reward', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegation_amount', full_name='kyve.query.v1beta1.StakerDelegatorResponse.delegation_amount', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.query.v1beta1.StakerDelegatorResponse.staker', index=3,
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
  serialized_start=337,
  serialized_end=448,
)


_QUERYDELEGATORSBYSTAKERREQUEST = _descriptor.Descriptor(
  name='QueryDelegatorsByStakerRequest',
  full_name='kyve.query.v1beta1.QueryDelegatorsByStakerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='kyve.query.v1beta1.QueryDelegatorsByStakerRequest.pagination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.query.v1beta1.QueryDelegatorsByStakerRequest.staker', index=1,
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
  serialized_start=450,
  serialized_end=558,
)


_QUERYDELEGATORSBYSTAKERRESPONSE = _descriptor.Descriptor(
  name='QueryDelegatorsByStakerResponse',
  full_name='kyve.query.v1beta1.QueryDelegatorsByStakerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delegators', full_name='kyve.query.v1beta1.QueryDelegatorsByStakerResponse.delegators', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_delegation', full_name='kyve.query.v1beta1.QueryDelegatorsByStakerResponse.total_delegation', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_delegator_count', full_name='kyve.query.v1beta1.QueryDelegatorsByStakerResponse.total_delegator_count', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='kyve.query.v1beta1.QueryDelegatorsByStakerResponse.pagination', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=561,
  serialized_end=783,
)


_QUERYSTAKERSBYDELEGATORREQUEST = _descriptor.Descriptor(
  name='QueryStakersByDelegatorRequest',
  full_name='kyve.query.v1beta1.QueryStakersByDelegatorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='kyve.query.v1beta1.QueryStakersByDelegatorRequest.pagination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegator', full_name='kyve.query.v1beta1.QueryStakersByDelegatorRequest.delegator', index=1,
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
  serialized_start=785,
  serialized_end=896,
)


_QUERYSTAKERSBYDELEGATORRESPONSE = _descriptor.Descriptor(
  name='QueryStakersByDelegatorResponse',
  full_name='kyve.query.v1beta1.QueryStakersByDelegatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delegator', full_name='kyve.query.v1beta1.QueryStakersByDelegatorResponse.delegator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stakers', full_name='kyve.query.v1beta1.QueryStakersByDelegatorResponse.stakers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='kyve.query.v1beta1.QueryStakersByDelegatorResponse.pagination', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=899,
  serialized_end=1084,
)


_DELEGATIONFORSTAKERRESPONSE = _descriptor.Descriptor(
  name='DelegationForStakerResponse',
  full_name='kyve.query.v1beta1.DelegationForStakerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.query.v1beta1.DelegationForStakerResponse.staker', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_reward', full_name='kyve.query.v1beta1.DelegationForStakerResponse.current_reward', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegation_amount', full_name='kyve.query.v1beta1.DelegationForStakerResponse.delegation_amount', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1087,
  serialized_end=1215,
)

_QUERYDELEGATORRESPONSE.fields_by_name['delegator'].message_type = _STAKERDELEGATORRESPONSE
_QUERYDELEGATORSBYSTAKERREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYDELEGATORSBYSTAKERRESPONSE.fields_by_name['delegators'].message_type = _STAKERDELEGATORRESPONSE
_QUERYDELEGATORSBYSTAKERRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYSTAKERSBYDELEGATORREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYSTAKERSBYDELEGATORRESPONSE.fields_by_name['stakers'].message_type = _DELEGATIONFORSTAKERRESPONSE
_QUERYSTAKERSBYDELEGATORRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_DELEGATIONFORSTAKERRESPONSE.fields_by_name['staker'].message_type = kyve_dot_query_dot_v1beta1_dot_query__pb2._FULLSTAKER
DESCRIPTOR.message_types_by_name['QueryDelegatorRequest'] = _QUERYDELEGATORREQUEST
DESCRIPTOR.message_types_by_name['QueryDelegatorResponse'] = _QUERYDELEGATORRESPONSE
DESCRIPTOR.message_types_by_name['StakerDelegatorResponse'] = _STAKERDELEGATORRESPONSE
DESCRIPTOR.message_types_by_name['QueryDelegatorsByStakerRequest'] = _QUERYDELEGATORSBYSTAKERREQUEST
DESCRIPTOR.message_types_by_name['QueryDelegatorsByStakerResponse'] = _QUERYDELEGATORSBYSTAKERRESPONSE
DESCRIPTOR.message_types_by_name['QueryStakersByDelegatorRequest'] = _QUERYSTAKERSBYDELEGATORREQUEST
DESCRIPTOR.message_types_by_name['QueryStakersByDelegatorResponse'] = _QUERYSTAKERSBYDELEGATORRESPONSE
DESCRIPTOR.message_types_by_name['DelegationForStakerResponse'] = _DELEGATIONFORSTAKERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryDelegatorRequest = _reflection.GeneratedProtocolMessageType('QueryDelegatorRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYDELEGATORREQUEST,
  __module__ = 'kyve.query.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.query.v1beta1.QueryDelegatorRequest)
  ))
_sym_db.RegisterMessage(QueryDelegatorRequest)

QueryDelegatorResponse = _reflection.GeneratedProtocolMessageType('QueryDelegatorResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYDELEGATORRESPONSE,
  __module__ = 'kyve.query.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.query.v1beta1.QueryDelegatorResponse)
  ))
_sym_db.RegisterMessage(QueryDelegatorResponse)

StakerDelegatorResponse = _reflection.GeneratedProtocolMessageType('StakerDelegatorResponse', (_message.Message,), dict(
  DESCRIPTOR = _STAKERDELEGATORRESPONSE,
  __module__ = 'kyve.query.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.query.v1beta1.StakerDelegatorResponse)
  ))
_sym_db.RegisterMessage(StakerDelegatorResponse)

QueryDelegatorsByStakerRequest = _reflection.GeneratedProtocolMessageType('QueryDelegatorsByStakerRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYDELEGATORSBYSTAKERREQUEST,
  __module__ = 'kyve.query.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.query.v1beta1.QueryDelegatorsByStakerRequest)
  ))
_sym_db.RegisterMessage(QueryDelegatorsByStakerRequest)

QueryDelegatorsByStakerResponse = _reflection.GeneratedProtocolMessageType('QueryDelegatorsByStakerResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYDELEGATORSBYSTAKERRESPONSE,
  __module__ = 'kyve.query.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.query.v1beta1.QueryDelegatorsByStakerResponse)
  ))
_sym_db.RegisterMessage(QueryDelegatorsByStakerResponse)

QueryStakersByDelegatorRequest = _reflection.GeneratedProtocolMessageType('QueryStakersByDelegatorRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYSTAKERSBYDELEGATORREQUEST,
  __module__ = 'kyve.query.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.query.v1beta1.QueryStakersByDelegatorRequest)
  ))
_sym_db.RegisterMessage(QueryStakersByDelegatorRequest)

QueryStakersByDelegatorResponse = _reflection.GeneratedProtocolMessageType('QueryStakersByDelegatorResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYSTAKERSBYDELEGATORRESPONSE,
  __module__ = 'kyve.query.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.query.v1beta1.QueryStakersByDelegatorResponse)
  ))
_sym_db.RegisterMessage(QueryStakersByDelegatorResponse)

DelegationForStakerResponse = _reflection.GeneratedProtocolMessageType('DelegationForStakerResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELEGATIONFORSTAKERRESPONSE,
  __module__ = 'kyve.query.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.query.v1beta1.DelegationForStakerResponse)
  ))
_sym_db.RegisterMessage(DelegationForStakerResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z*github.com/KYVENetwork/chain/x/query/types'))
_QUERYDELEGATORSBYSTAKERRESPONSE.fields_by_name['delegators'].has_options = True
_QUERYDELEGATORSBYSTAKERRESPONSE.fields_by_name['delegators']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_QUERYSTAKERSBYDELEGATORRESPONSE.fields_by_name['stakers'].has_options = True
_QUERYSTAKERSBYDELEGATORRESPONSE.fields_by_name['stakers']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))

_QUERYDELEGATION = _descriptor.ServiceDescriptor(
  name='QueryDelegation',
  full_name='kyve.query.v1beta1.QueryDelegation',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1218,
  serialized_end=1773,
  methods=[
  _descriptor.MethodDescriptor(
    name='Delegator',
    full_name='kyve.query.v1beta1.QueryDelegation.Delegator',
    index=0,
    containing_service=None,
    input_type=_QUERYDELEGATORREQUEST,
    output_type=_QUERYDELEGATORRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0024\0222/kyve/query/v1beta1/delegator/{staker}/{delegator}')),
  ),
  _descriptor.MethodDescriptor(
    name='DelegatorsByStaker',
    full_name='kyve.query.v1beta1.QueryDelegation.DelegatorsByStaker',
    index=1,
    containing_service=None,
    input_type=_QUERYDELEGATORSBYSTAKERREQUEST,
    output_type=_QUERYDELEGATORSBYSTAKERRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0023\0221/kyve/query/v1beta1/delegators_by_staker/{staker}')),
  ),
  _descriptor.MethodDescriptor(
    name='StakersByDelegator',
    full_name='kyve.query.v1beta1.QueryDelegation.StakersByDelegator',
    index=2,
    containing_service=None,
    input_type=_QUERYSTAKERSBYDELEGATORREQUEST,
    output_type=_QUERYSTAKERSBYDELEGATORRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0026\0224/kyve/query/v1beta1/stakers_by_delegator/{delegator}')),
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERYDELEGATION)

DESCRIPTOR.services_by_name['QueryDelegation'] = _QUERYDELEGATION

# @@protoc_insertion_point(module_scope)