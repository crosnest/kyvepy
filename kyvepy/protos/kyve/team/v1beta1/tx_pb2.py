# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/team/v1beta1/tx.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/team/v1beta1/tx.proto',
  package='kyve.team.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\x1akyve/team/v1beta1/tx.proto\x12\x11kyve.team.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\"\x88\x01\n\x10MsgClaimUnlocked\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\x12+\n\trecipient\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"\x1a\n\x18MsgClaimUnlockedResponse\"\x84\x01\n\x18MsgClaimAuthorityRewards\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\x12+\n\trecipient\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"\"\n MsgClaimAuthorityRewardsResponse\"\x8e\x01\n\x16MsgClaimAccountRewards\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\x12+\n\trecipient\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\" \n\x1eMsgClaimAccountRewardsResponse\"X\n\x0bMsgClawback\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x10\n\x08\x63lawback\x18\x03 \x01(\x04\"\x15\n\x13MsgClawbackResponse\"z\n\x1bMsgCreateTeamVestingAccount\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x18\n\x10total_allocation\x18\x02 \x01(\x04\x12\x14\n\x0c\x63ommencement\x18\x03 \x01(\x04\"%\n#MsgCreateTeamVestingAccountResponse2\xb1\x04\n\x03Msg\x12\x61\n\rClaimUnlocked\x12#.kyve.team.v1beta1.MsgClaimUnlocked\x1a+.kyve.team.v1beta1.MsgClaimUnlockedResponse\x12R\n\x08\x43lawback\x12\x1e.kyve.team.v1beta1.MsgClawback\x1a&.kyve.team.v1beta1.MsgClawbackResponse\x12\x82\x01\n\x18\x43reateTeamVestingAccount\x12..kyve.team.v1beta1.MsgCreateTeamVestingAccount\x1a\x36.kyve.team.v1beta1.MsgCreateTeamVestingAccountResponse\x12y\n\x15\x43laimAuthorityRewards\x12+.kyve.team.v1beta1.MsgClaimAuthorityRewards\x1a\x33.kyve.team.v1beta1.MsgClaimAuthorityRewardsResponse\x12s\n\x13\x43laimAccountRewards\x12).kyve.team.v1beta1.MsgClaimAccountRewards\x1a\x31.kyve.team.v1beta1.MsgClaimAccountRewardsResponseB+Z)github.com/KYVENetwork/chain/x/team/typesb\x06proto3')
  ,
  dependencies=[cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_MSGCLAIMUNLOCKED = _descriptor.Descriptor(
  name='MsgClaimUnlocked',
  full_name='kyve.team.v1beta1.MsgClaimUnlocked',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.team.v1beta1.MsgClaimUnlocked.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.team.v1beta1.MsgClaimUnlocked.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.team.v1beta1.MsgClaimUnlocked.amount', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='kyve.team.v1beta1.MsgClaimUnlocked.recipient', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=77,
  serialized_end=213,
)


_MSGCLAIMUNLOCKEDRESPONSE = _descriptor.Descriptor(
  name='MsgClaimUnlockedResponse',
  full_name='kyve.team.v1beta1.MsgClaimUnlockedResponse',
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
  serialized_start=215,
  serialized_end=241,
)


_MSGCLAIMAUTHORITYREWARDS = _descriptor.Descriptor(
  name='MsgClaimAuthorityRewards',
  full_name='kyve.team.v1beta1.MsgClaimAuthorityRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.team.v1beta1.MsgClaimAuthorityRewards.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.team.v1beta1.MsgClaimAuthorityRewards.amount', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='kyve.team.v1beta1.MsgClaimAuthorityRewards.recipient', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=244,
  serialized_end=376,
)


_MSGCLAIMAUTHORITYREWARDSRESPONSE = _descriptor.Descriptor(
  name='MsgClaimAuthorityRewardsResponse',
  full_name='kyve.team.v1beta1.MsgClaimAuthorityRewardsResponse',
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
  serialized_start=378,
  serialized_end=412,
)


_MSGCLAIMACCOUNTREWARDS = _descriptor.Descriptor(
  name='MsgClaimAccountRewards',
  full_name='kyve.team.v1beta1.MsgClaimAccountRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.team.v1beta1.MsgClaimAccountRewards.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.team.v1beta1.MsgClaimAccountRewards.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.team.v1beta1.MsgClaimAccountRewards.amount', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='kyve.team.v1beta1.MsgClaimAccountRewards.recipient', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=415,
  serialized_end=557,
)


_MSGCLAIMACCOUNTREWARDSRESPONSE = _descriptor.Descriptor(
  name='MsgClaimAccountRewardsResponse',
  full_name='kyve.team.v1beta1.MsgClaimAccountRewardsResponse',
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
  serialized_start=559,
  serialized_end=591,
)


_MSGCLAWBACK = _descriptor.Descriptor(
  name='MsgClawback',
  full_name='kyve.team.v1beta1.MsgClawback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.team.v1beta1.MsgClawback.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.team.v1beta1.MsgClawback.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clawback', full_name='kyve.team.v1beta1.MsgClawback.clawback', index=2,
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
  serialized_start=593,
  serialized_end=681,
)


_MSGCLAWBACKRESPONSE = _descriptor.Descriptor(
  name='MsgClawbackResponse',
  full_name='kyve.team.v1beta1.MsgClawbackResponse',
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
  serialized_start=683,
  serialized_end=704,
)


_MSGCREATETEAMVESTINGACCOUNT = _descriptor.Descriptor(
  name='MsgCreateTeamVestingAccount',
  full_name='kyve.team.v1beta1.MsgCreateTeamVestingAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.team.v1beta1.MsgCreateTeamVestingAccount.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_allocation', full_name='kyve.team.v1beta1.MsgCreateTeamVestingAccount.total_allocation', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commencement', full_name='kyve.team.v1beta1.MsgCreateTeamVestingAccount.commencement', index=2,
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
  serialized_start=706,
  serialized_end=828,
)


_MSGCREATETEAMVESTINGACCOUNTRESPONSE = _descriptor.Descriptor(
  name='MsgCreateTeamVestingAccountResponse',
  full_name='kyve.team.v1beta1.MsgCreateTeamVestingAccountResponse',
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
  serialized_start=830,
  serialized_end=867,
)

DESCRIPTOR.message_types_by_name['MsgClaimUnlocked'] = _MSGCLAIMUNLOCKED
DESCRIPTOR.message_types_by_name['MsgClaimUnlockedResponse'] = _MSGCLAIMUNLOCKEDRESPONSE
DESCRIPTOR.message_types_by_name['MsgClaimAuthorityRewards'] = _MSGCLAIMAUTHORITYREWARDS
DESCRIPTOR.message_types_by_name['MsgClaimAuthorityRewardsResponse'] = _MSGCLAIMAUTHORITYREWARDSRESPONSE
DESCRIPTOR.message_types_by_name['MsgClaimAccountRewards'] = _MSGCLAIMACCOUNTREWARDS
DESCRIPTOR.message_types_by_name['MsgClaimAccountRewardsResponse'] = _MSGCLAIMACCOUNTREWARDSRESPONSE
DESCRIPTOR.message_types_by_name['MsgClawback'] = _MSGCLAWBACK
DESCRIPTOR.message_types_by_name['MsgClawbackResponse'] = _MSGCLAWBACKRESPONSE
DESCRIPTOR.message_types_by_name['MsgCreateTeamVestingAccount'] = _MSGCREATETEAMVESTINGACCOUNT
DESCRIPTOR.message_types_by_name['MsgCreateTeamVestingAccountResponse'] = _MSGCREATETEAMVESTINGACCOUNTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgClaimUnlocked = _reflection.GeneratedProtocolMessageType('MsgClaimUnlocked', (_message.Message,), dict(
  DESCRIPTOR = _MSGCLAIMUNLOCKED,
  __module__ = 'kyve.team.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.MsgClaimUnlocked)
  ))
_sym_db.RegisterMessage(MsgClaimUnlocked)

MsgClaimUnlockedResponse = _reflection.GeneratedProtocolMessageType('MsgClaimUnlockedResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGCLAIMUNLOCKEDRESPONSE,
  __module__ = 'kyve.team.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.MsgClaimUnlockedResponse)
  ))
_sym_db.RegisterMessage(MsgClaimUnlockedResponse)

MsgClaimAuthorityRewards = _reflection.GeneratedProtocolMessageType('MsgClaimAuthorityRewards', (_message.Message,), dict(
  DESCRIPTOR = _MSGCLAIMAUTHORITYREWARDS,
  __module__ = 'kyve.team.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.MsgClaimAuthorityRewards)
  ))
_sym_db.RegisterMessage(MsgClaimAuthorityRewards)

MsgClaimAuthorityRewardsResponse = _reflection.GeneratedProtocolMessageType('MsgClaimAuthorityRewardsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGCLAIMAUTHORITYREWARDSRESPONSE,
  __module__ = 'kyve.team.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.MsgClaimAuthorityRewardsResponse)
  ))
_sym_db.RegisterMessage(MsgClaimAuthorityRewardsResponse)

MsgClaimAccountRewards = _reflection.GeneratedProtocolMessageType('MsgClaimAccountRewards', (_message.Message,), dict(
  DESCRIPTOR = _MSGCLAIMACCOUNTREWARDS,
  __module__ = 'kyve.team.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.MsgClaimAccountRewards)
  ))
_sym_db.RegisterMessage(MsgClaimAccountRewards)

MsgClaimAccountRewardsResponse = _reflection.GeneratedProtocolMessageType('MsgClaimAccountRewardsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGCLAIMACCOUNTREWARDSRESPONSE,
  __module__ = 'kyve.team.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.MsgClaimAccountRewardsResponse)
  ))
_sym_db.RegisterMessage(MsgClaimAccountRewardsResponse)

MsgClawback = _reflection.GeneratedProtocolMessageType('MsgClawback', (_message.Message,), dict(
  DESCRIPTOR = _MSGCLAWBACK,
  __module__ = 'kyve.team.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.MsgClawback)
  ))
_sym_db.RegisterMessage(MsgClawback)

MsgClawbackResponse = _reflection.GeneratedProtocolMessageType('MsgClawbackResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGCLAWBACKRESPONSE,
  __module__ = 'kyve.team.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.MsgClawbackResponse)
  ))
_sym_db.RegisterMessage(MsgClawbackResponse)

MsgCreateTeamVestingAccount = _reflection.GeneratedProtocolMessageType('MsgCreateTeamVestingAccount', (_message.Message,), dict(
  DESCRIPTOR = _MSGCREATETEAMVESTINGACCOUNT,
  __module__ = 'kyve.team.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.MsgCreateTeamVestingAccount)
  ))
_sym_db.RegisterMessage(MsgCreateTeamVestingAccount)

MsgCreateTeamVestingAccountResponse = _reflection.GeneratedProtocolMessageType('MsgCreateTeamVestingAccountResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGCREATETEAMVESTINGACCOUNTRESPONSE,
  __module__ = 'kyve.team.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.MsgCreateTeamVestingAccountResponse)
  ))
_sym_db.RegisterMessage(MsgCreateTeamVestingAccountResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/KYVENetwork/chain/x/team/types'))
_MSGCLAIMUNLOCKED.fields_by_name['authority'].has_options = True
_MSGCLAIMUNLOCKED.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGCLAIMUNLOCKED.fields_by_name['recipient'].has_options = True
_MSGCLAIMUNLOCKED.fields_by_name['recipient']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGCLAIMAUTHORITYREWARDS.fields_by_name['authority'].has_options = True
_MSGCLAIMAUTHORITYREWARDS.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGCLAIMAUTHORITYREWARDS.fields_by_name['recipient'].has_options = True
_MSGCLAIMAUTHORITYREWARDS.fields_by_name['recipient']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGCLAIMACCOUNTREWARDS.fields_by_name['authority'].has_options = True
_MSGCLAIMACCOUNTREWARDS.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGCLAIMACCOUNTREWARDS.fields_by_name['recipient'].has_options = True
_MSGCLAIMACCOUNTREWARDS.fields_by_name['recipient']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGCLAWBACK.fields_by_name['authority'].has_options = True
_MSGCLAWBACK.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGCREATETEAMVESTINGACCOUNT.fields_by_name['authority'].has_options = True
_MSGCREATETEAMVESTINGACCOUNT.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='kyve.team.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=870,
  serialized_end=1431,
  methods=[
  _descriptor.MethodDescriptor(
    name='ClaimUnlocked',
    full_name='kyve.team.v1beta1.Msg.ClaimUnlocked',
    index=0,
    containing_service=None,
    input_type=_MSGCLAIMUNLOCKED,
    output_type=_MSGCLAIMUNLOCKEDRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Clawback',
    full_name='kyve.team.v1beta1.Msg.Clawback',
    index=1,
    containing_service=None,
    input_type=_MSGCLAWBACK,
    output_type=_MSGCLAWBACKRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTeamVestingAccount',
    full_name='kyve.team.v1beta1.Msg.CreateTeamVestingAccount',
    index=2,
    containing_service=None,
    input_type=_MSGCREATETEAMVESTINGACCOUNT,
    output_type=_MSGCREATETEAMVESTINGACCOUNTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClaimAuthorityRewards',
    full_name='kyve.team.v1beta1.Msg.ClaimAuthorityRewards',
    index=3,
    containing_service=None,
    input_type=_MSGCLAIMAUTHORITYREWARDS,
    output_type=_MSGCLAIMAUTHORITYREWARDSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClaimAccountRewards',
    full_name='kyve.team.v1beta1.Msg.ClaimAccountRewards',
    index=4,
    containing_service=None,
    input_type=_MSGCLAIMACCOUNTREWARDS,
    output_type=_MSGCLAIMACCOUNTREWARDSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
