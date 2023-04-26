# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/delegation/v1beta1/events.proto

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
from kyve.delegation.v1beta1 import delegation_pb2 as kyve_dot_delegation_dot_v1beta1_dot_delegation__pb2
from kyve.delegation.v1beta1 import params_pb2 as kyve_dot_delegation_dot_v1beta1_dot_params__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/delegation/v1beta1/events.proto',
  package='kyve.delegation.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n$kyve/delegation/v1beta1/events.proto\x12\x17kyve.delegation.v1beta1\x1a\x14gogoproto/gogo.proto\x1a(kyve/delegation/v1beta1/delegation.proto\x1a$kyve/delegation/v1beta1/params.proto\"\x9a\x01\n\x11\x45ventUpdateParams\x12\x39\n\nold_params\x18\x01 \x01(\x0b\x32\x1f.kyve.delegation.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12\x39\n\nnew_params\x18\x02 \x01(\x0b\x32\x1f.kyve.delegation.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12\x0f\n\x07payload\x18\x03 \x01(\t\"@\n\rEventDelegate\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06staker\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\"n\n\x16\x45ventStartUndelegation\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06staker\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\x12#\n\x1b\x65stimated_undelegation_date\x18\x04 \x01(\x04\"B\n\x0f\x45ventUndelegate\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06staker\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\"Z\n\x0f\x45ventRedelegate\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x13\n\x0b\x66rom_staker\x18\x02 \x01(\t\x12\x11\n\tto_staker\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\"G\n\x14\x45ventWithdrawRewards\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06staker\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\"u\n\nEventSlash\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x0e\n\x06staker\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\x12\x36\n\nslash_type\x18\x04 \x01(\x0e\x32\".kyve.delegation.v1beta1.SlashTypeB1Z/github.com/KYVENetwork/chain/x/delegation/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,kyve_dot_delegation_dot_v1beta1_dot_delegation__pb2.DESCRIPTOR,kyve_dot_delegation_dot_v1beta1_dot_params__pb2.DESCRIPTOR,])




_EVENTUPDATEPARAMS = _descriptor.Descriptor(
  name='EventUpdateParams',
  full_name='kyve.delegation.v1beta1.EventUpdateParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='old_params', full_name='kyve.delegation.v1beta1.EventUpdateParams.old_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_params', full_name='kyve.delegation.v1beta1.EventUpdateParams.new_params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='kyve.delegation.v1beta1.EventUpdateParams.payload', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=168,
  serialized_end=322,
)


_EVENTDELEGATE = _descriptor.Descriptor(
  name='EventDelegate',
  full_name='kyve.delegation.v1beta1.EventDelegate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='kyve.delegation.v1beta1.EventDelegate.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.delegation.v1beta1.EventDelegate.staker', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.delegation.v1beta1.EventDelegate.amount', index=2,
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
  serialized_start=324,
  serialized_end=388,
)


_EVENTSTARTUNDELEGATION = _descriptor.Descriptor(
  name='EventStartUndelegation',
  full_name='kyve.delegation.v1beta1.EventStartUndelegation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='kyve.delegation.v1beta1.EventStartUndelegation.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.delegation.v1beta1.EventStartUndelegation.staker', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.delegation.v1beta1.EventStartUndelegation.amount', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='estimated_undelegation_date', full_name='kyve.delegation.v1beta1.EventStartUndelegation.estimated_undelegation_date', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=390,
  serialized_end=500,
)


_EVENTUNDELEGATE = _descriptor.Descriptor(
  name='EventUndelegate',
  full_name='kyve.delegation.v1beta1.EventUndelegate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='kyve.delegation.v1beta1.EventUndelegate.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.delegation.v1beta1.EventUndelegate.staker', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.delegation.v1beta1.EventUndelegate.amount', index=2,
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
  serialized_start=502,
  serialized_end=568,
)


_EVENTREDELEGATE = _descriptor.Descriptor(
  name='EventRedelegate',
  full_name='kyve.delegation.v1beta1.EventRedelegate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='kyve.delegation.v1beta1.EventRedelegate.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_staker', full_name='kyve.delegation.v1beta1.EventRedelegate.from_staker', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_staker', full_name='kyve.delegation.v1beta1.EventRedelegate.to_staker', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.delegation.v1beta1.EventRedelegate.amount', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=570,
  serialized_end=660,
)


_EVENTWITHDRAWREWARDS = _descriptor.Descriptor(
  name='EventWithdrawRewards',
  full_name='kyve.delegation.v1beta1.EventWithdrawRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='kyve.delegation.v1beta1.EventWithdrawRewards.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.delegation.v1beta1.EventWithdrawRewards.staker', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.delegation.v1beta1.EventWithdrawRewards.amount', index=2,
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
  serialized_start=662,
  serialized_end=733,
)


_EVENTSLASH = _descriptor.Descriptor(
  name='EventSlash',
  full_name='kyve.delegation.v1beta1.EventSlash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pool_id', full_name='kyve.delegation.v1beta1.EventSlash.pool_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.delegation.v1beta1.EventSlash.staker', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.delegation.v1beta1.EventSlash.amount', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slash_type', full_name='kyve.delegation.v1beta1.EventSlash.slash_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=735,
  serialized_end=852,
)

_EVENTUPDATEPARAMS.fields_by_name['old_params'].message_type = kyve_dot_delegation_dot_v1beta1_dot_params__pb2._PARAMS
_EVENTUPDATEPARAMS.fields_by_name['new_params'].message_type = kyve_dot_delegation_dot_v1beta1_dot_params__pb2._PARAMS
_EVENTSLASH.fields_by_name['slash_type'].enum_type = kyve_dot_delegation_dot_v1beta1_dot_delegation__pb2._SLASHTYPE
DESCRIPTOR.message_types_by_name['EventUpdateParams'] = _EVENTUPDATEPARAMS
DESCRIPTOR.message_types_by_name['EventDelegate'] = _EVENTDELEGATE
DESCRIPTOR.message_types_by_name['EventStartUndelegation'] = _EVENTSTARTUNDELEGATION
DESCRIPTOR.message_types_by_name['EventUndelegate'] = _EVENTUNDELEGATE
DESCRIPTOR.message_types_by_name['EventRedelegate'] = _EVENTREDELEGATE
DESCRIPTOR.message_types_by_name['EventWithdrawRewards'] = _EVENTWITHDRAWREWARDS
DESCRIPTOR.message_types_by_name['EventSlash'] = _EVENTSLASH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventUpdateParams = _reflection.GeneratedProtocolMessageType('EventUpdateParams', (_message.Message,), dict(
  DESCRIPTOR = _EVENTUPDATEPARAMS,
  __module__ = 'kyve.delegation.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.EventUpdateParams)
  ))
_sym_db.RegisterMessage(EventUpdateParams)

EventDelegate = _reflection.GeneratedProtocolMessageType('EventDelegate', (_message.Message,), dict(
  DESCRIPTOR = _EVENTDELEGATE,
  __module__ = 'kyve.delegation.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.EventDelegate)
  ))
_sym_db.RegisterMessage(EventDelegate)

EventStartUndelegation = _reflection.GeneratedProtocolMessageType('EventStartUndelegation', (_message.Message,), dict(
  DESCRIPTOR = _EVENTSTARTUNDELEGATION,
  __module__ = 'kyve.delegation.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.EventStartUndelegation)
  ))
_sym_db.RegisterMessage(EventStartUndelegation)

EventUndelegate = _reflection.GeneratedProtocolMessageType('EventUndelegate', (_message.Message,), dict(
  DESCRIPTOR = _EVENTUNDELEGATE,
  __module__ = 'kyve.delegation.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.EventUndelegate)
  ))
_sym_db.RegisterMessage(EventUndelegate)

EventRedelegate = _reflection.GeneratedProtocolMessageType('EventRedelegate', (_message.Message,), dict(
  DESCRIPTOR = _EVENTREDELEGATE,
  __module__ = 'kyve.delegation.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.EventRedelegate)
  ))
_sym_db.RegisterMessage(EventRedelegate)

EventWithdrawRewards = _reflection.GeneratedProtocolMessageType('EventWithdrawRewards', (_message.Message,), dict(
  DESCRIPTOR = _EVENTWITHDRAWREWARDS,
  __module__ = 'kyve.delegation.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.EventWithdrawRewards)
  ))
_sym_db.RegisterMessage(EventWithdrawRewards)

EventSlash = _reflection.GeneratedProtocolMessageType('EventSlash', (_message.Message,), dict(
  DESCRIPTOR = _EVENTSLASH,
  __module__ = 'kyve.delegation.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.EventSlash)
  ))
_sym_db.RegisterMessage(EventSlash)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z/github.com/KYVENetwork/chain/x/delegation/types'))
_EVENTUPDATEPARAMS.fields_by_name['old_params'].has_options = True
_EVENTUPDATEPARAMS.fields_by_name['old_params']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_EVENTUPDATEPARAMS.fields_by_name['new_params'].has_options = True
_EVENTUPDATEPARAMS.fields_by_name['new_params']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
