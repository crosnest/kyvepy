# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/delegation/v1beta1/delegation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/delegation/v1beta1/delegation.proto',
  package='kyve.delegation.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n(kyve/delegation/v1beta1/delegation.proto\x12\x17kyve.delegation.v1beta1\x1a\x14gogoproto/gogo.proto\"W\n\tDelegator\x12\x0e\n\x06staker\x18\x01 \x01(\t\x12\x11\n\tdelegator\x18\x02 \x01(\t\x12\x0f\n\x07k_index\x18\x03 \x01(\x04\x12\x16\n\x0einitial_amount\x18\x04 \x01(\x04\"q\n\x0f\x44\x65legationEntry\x12\x0e\n\x06staker\x18\x01 \x01(\t\x12\x0f\n\x07k_index\x18\x02 \x01(\x04\x12=\n\x05value\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\xab\x01\n\x0e\x44\x65legationData\x12\x0e\n\x06staker\x18\x01 \x01(\t\x12\x17\n\x0f\x63urrent_rewards\x18\x02 \x01(\x04\x12\x18\n\x10total_delegation\x18\x03 \x01(\x04\x12\x16\n\x0elatest_index_k\x18\x04 \x01(\x04\x12\x17\n\x0f\x64\x65legator_count\x18\x05 \x01(\x04\x12%\n\x1dlatest_index_was_undelegation\x18\x06 \x01(\x08\"t\n\x0f\x44\x65legationSlash\x12\x0e\n\x06staker\x18\x01 \x01(\t\x12\x0f\n\x07k_index\x18\x02 \x01(\x04\x12@\n\x08\x66raction\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"q\n\x16UndelegationQueueEntry\x12\r\n\x05index\x18\x01 \x01(\x04\x12\x0e\n\x06staker\x18\x02 \x01(\t\x12\x11\n\tdelegator\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x15\n\rcreation_time\x18\x05 \x01(\x04\"3\n\nQueueState\x12\x11\n\tlow_index\x18\x01 \x01(\x04\x12\x12\n\nhigh_index\x18\x02 \x01(\x04\">\n\x14RedelegationCooldown\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x15\n\rcreation_date\x18\x02 \x01(\x04*q\n\tSlashType\x12\x1a\n\x16SLASH_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12SLASH_TYPE_TIMEOUT\x10\x01\x12\x13\n\x0fSLASH_TYPE_VOTE\x10\x02\x12\x15\n\x11SLASH_TYPE_UPLOAD\x10\x03\x1a\x04\x88\xa3\x1e\x00\x42\x31Z/github.com/KYVENetwork/chain/x/delegation/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])

_SLASHTYPE = _descriptor.EnumDescriptor(
  name='SlashType',
  full_name='kyve.delegation.v1beta1.SlashType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SLASH_TYPE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLASH_TYPE_TIMEOUT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLASH_TYPE_VOTE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLASH_TYPE_UPLOAD', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\210\243\036\000')),
  serialized_start=819,
  serialized_end=932,
)
_sym_db.RegisterEnumDescriptor(_SLASHTYPE)

SlashType = enum_type_wrapper.EnumTypeWrapper(_SLASHTYPE)
SLASH_TYPE_UNSPECIFIED = 0
SLASH_TYPE_TIMEOUT = 1
SLASH_TYPE_VOTE = 2
SLASH_TYPE_UPLOAD = 3



_DELEGATOR = _descriptor.Descriptor(
  name='Delegator',
  full_name='kyve.delegation.v1beta1.Delegator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.delegation.v1beta1.Delegator.staker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegator', full_name='kyve.delegation.v1beta1.Delegator.delegator', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k_index', full_name='kyve.delegation.v1beta1.Delegator.k_index', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_amount', full_name='kyve.delegation.v1beta1.Delegator.initial_amount', index=3,
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
  serialized_start=91,
  serialized_end=178,
)


_DELEGATIONENTRY = _descriptor.Descriptor(
  name='DelegationEntry',
  full_name='kyve.delegation.v1beta1.DelegationEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.delegation.v1beta1.DelegationEntry.staker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k_index', full_name='kyve.delegation.v1beta1.DelegationEntry.k_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kyve.delegation.v1beta1.DelegationEntry.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=180,
  serialized_end=293,
)


_DELEGATIONDATA = _descriptor.Descriptor(
  name='DelegationData',
  full_name='kyve.delegation.v1beta1.DelegationData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.delegation.v1beta1.DelegationData.staker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_rewards', full_name='kyve.delegation.v1beta1.DelegationData.current_rewards', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_delegation', full_name='kyve.delegation.v1beta1.DelegationData.total_delegation', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latest_index_k', full_name='kyve.delegation.v1beta1.DelegationData.latest_index_k', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegator_count', full_name='kyve.delegation.v1beta1.DelegationData.delegator_count', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latest_index_was_undelegation', full_name='kyve.delegation.v1beta1.DelegationData.latest_index_was_undelegation', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=296,
  serialized_end=467,
)


_DELEGATIONSLASH = _descriptor.Descriptor(
  name='DelegationSlash',
  full_name='kyve.delegation.v1beta1.DelegationSlash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.delegation.v1beta1.DelegationSlash.staker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k_index', full_name='kyve.delegation.v1beta1.DelegationSlash.k_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fraction', full_name='kyve.delegation.v1beta1.DelegationSlash.fraction', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=469,
  serialized_end=585,
)


_UNDELEGATIONQUEUEENTRY = _descriptor.Descriptor(
  name='UndelegationQueueEntry',
  full_name='kyve.delegation.v1beta1.UndelegationQueueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='kyve.delegation.v1beta1.UndelegationQueueEntry.index', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staker', full_name='kyve.delegation.v1beta1.UndelegationQueueEntry.staker', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegator', full_name='kyve.delegation.v1beta1.UndelegationQueueEntry.delegator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.delegation.v1beta1.UndelegationQueueEntry.amount', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='kyve.delegation.v1beta1.UndelegationQueueEntry.creation_time', index=4,
      number=5, type=4, cpp_type=4, label=1,
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
  serialized_start=587,
  serialized_end=700,
)


_QUEUESTATE = _descriptor.Descriptor(
  name='QueueState',
  full_name='kyve.delegation.v1beta1.QueueState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='low_index', full_name='kyve.delegation.v1beta1.QueueState.low_index', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high_index', full_name='kyve.delegation.v1beta1.QueueState.high_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=702,
  serialized_end=753,
)


_REDELEGATIONCOOLDOWN = _descriptor.Descriptor(
  name='RedelegationCooldown',
  full_name='kyve.delegation.v1beta1.RedelegationCooldown',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='kyve.delegation.v1beta1.RedelegationCooldown.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='kyve.delegation.v1beta1.RedelegationCooldown.creation_date', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=755,
  serialized_end=817,
)

DESCRIPTOR.message_types_by_name['Delegator'] = _DELEGATOR
DESCRIPTOR.message_types_by_name['DelegationEntry'] = _DELEGATIONENTRY
DESCRIPTOR.message_types_by_name['DelegationData'] = _DELEGATIONDATA
DESCRIPTOR.message_types_by_name['DelegationSlash'] = _DELEGATIONSLASH
DESCRIPTOR.message_types_by_name['UndelegationQueueEntry'] = _UNDELEGATIONQUEUEENTRY
DESCRIPTOR.message_types_by_name['QueueState'] = _QUEUESTATE
DESCRIPTOR.message_types_by_name['RedelegationCooldown'] = _REDELEGATIONCOOLDOWN
DESCRIPTOR.enum_types_by_name['SlashType'] = _SLASHTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Delegator = _reflection.GeneratedProtocolMessageType('Delegator', (_message.Message,), dict(
  DESCRIPTOR = _DELEGATOR,
  __module__ = 'kyve.delegation.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.Delegator)
  ))
_sym_db.RegisterMessage(Delegator)

DelegationEntry = _reflection.GeneratedProtocolMessageType('DelegationEntry', (_message.Message,), dict(
  DESCRIPTOR = _DELEGATIONENTRY,
  __module__ = 'kyve.delegation.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.DelegationEntry)
  ))
_sym_db.RegisterMessage(DelegationEntry)

DelegationData = _reflection.GeneratedProtocolMessageType('DelegationData', (_message.Message,), dict(
  DESCRIPTOR = _DELEGATIONDATA,
  __module__ = 'kyve.delegation.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.DelegationData)
  ))
_sym_db.RegisterMessage(DelegationData)

DelegationSlash = _reflection.GeneratedProtocolMessageType('DelegationSlash', (_message.Message,), dict(
  DESCRIPTOR = _DELEGATIONSLASH,
  __module__ = 'kyve.delegation.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.DelegationSlash)
  ))
_sym_db.RegisterMessage(DelegationSlash)

UndelegationQueueEntry = _reflection.GeneratedProtocolMessageType('UndelegationQueueEntry', (_message.Message,), dict(
  DESCRIPTOR = _UNDELEGATIONQUEUEENTRY,
  __module__ = 'kyve.delegation.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.UndelegationQueueEntry)
  ))
_sym_db.RegisterMessage(UndelegationQueueEntry)

QueueState = _reflection.GeneratedProtocolMessageType('QueueState', (_message.Message,), dict(
  DESCRIPTOR = _QUEUESTATE,
  __module__ = 'kyve.delegation.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.QueueState)
  ))
_sym_db.RegisterMessage(QueueState)

RedelegationCooldown = _reflection.GeneratedProtocolMessageType('RedelegationCooldown', (_message.Message,), dict(
  DESCRIPTOR = _REDELEGATIONCOOLDOWN,
  __module__ = 'kyve.delegation.v1beta1.delegation_pb2'
  # @@protoc_insertion_point(class_scope:kyve.delegation.v1beta1.RedelegationCooldown)
  ))
_sym_db.RegisterMessage(RedelegationCooldown)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z/github.com/KYVENetwork/chain/x/delegation/types'))
_SLASHTYPE.has_options = True
_SLASHTYPE._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\210\243\036\000'))
_DELEGATIONENTRY.fields_by_name['value'].has_options = True
_DELEGATIONENTRY.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'))
_DELEGATIONSLASH.fields_by_name['fraction'].has_options = True
_DELEGATIONSLASH.fields_by_name['fraction']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
