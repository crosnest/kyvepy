# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/distribution/v1beta1/distribution.proto

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
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/distribution/v1beta1/distribution.proto',
  package='cosmos.distribution.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n.cosmos/distribution/v1beta1/distribution.proto\x12\x1b\x63osmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xbb\x02\n\x06Params\x12S\n\rcommunity_tax\x18\x01 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12Z\n\x14\x62\x61se_proposer_reward\x18\x02 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12[\n\x15\x62onus_proposer_reward\x18\x03 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x1d\n\x15withdraw_addr_enabled\x18\x04 \x01(\x08:\x04\x98\xa0\x1f\x00\"\xa9\x01\n\x1aValidatorHistoricalRewards\x12r\n\x17\x63umulative_reward_ratio\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12\x17\n\x0freference_count\x18\x02 \x01(\r\"\x8d\x01\n\x17ValidatorCurrentRewards\x12\x62\n\x07rewards\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12\x0e\n\x06period\x18\x02 \x01(\x04\"\x87\x01\n\x1eValidatorAccumulatedCommission\x12\x65\n\ncommission\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\"\x81\x01\n\x1bValidatorOutstandingRewards\x12\x62\n\x07rewards\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\"\x7f\n\x13ValidatorSlashEvent\x12\x18\n\x10validator_period\x18\x01 \x01(\x04\x12N\n\x08\x66raction\x18\x02 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"t\n\x14ValidatorSlashEvents\x12V\n\x16validator_slash_events\x18\x01 \x03(\x0b\x32\x30.cosmos.distribution.v1beta1.ValidatorSlashEventB\x04\xc8\xde\x1f\x00:\x04\x98\xa0\x1f\x00\"t\n\x07\x46\x65\x65Pool\x12i\n\x0e\x63ommunity_pool\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\"\xdc\x01\n\x1a\x43ommunityPoolSpendProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12[\n\x06\x61mount\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:*\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xa2\x01\n\x15\x44\x65legatorStartingInfo\x12\x17\n\x0fprevious_period\x18\x01 \x01(\x04\x12K\n\x05stake\x18\x02 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12#\n\x06height\x18\x03 \x01(\x04\x42\x13\xea\xde\x1f\x0f\x63reation_height\"\xbd\x01\n\x19\x44\x65legationDelegatorReward\x12\x33\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x61\n\x06reward\x18\x02 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01\"\xa7\x01\n%CommunityPoolSpendProposalWithDeposit\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\t\x12\x0f\n\x07\x64\x65posit\x18\x05 \x01(\t:&\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.ContentB7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='cosmos.distribution.v1beta1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='community_tax', full_name='cosmos.distribution.v1beta1.Params.community_tax', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_proposer_reward', full_name='cosmos.distribution.v1beta1.Params.base_proposer_reward', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bonus_proposer_reward', full_name='cosmos.distribution.v1beta1.Params.bonus_proposer_reward', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdraw_addr_enabled', full_name='cosmos.distribution.v1beta1.Params.withdraw_addr_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=476,
)


_VALIDATORHISTORICALREWARDS = _descriptor.Descriptor(
  name='ValidatorHistoricalRewards',
  full_name='cosmos.distribution.v1beta1.ValidatorHistoricalRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cumulative_reward_ratio', full_name='cosmos.distribution.v1beta1.ValidatorHistoricalRewards.cumulative_reward_ratio', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference_count', full_name='cosmos.distribution.v1beta1.ValidatorHistoricalRewards.reference_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=479,
  serialized_end=648,
)


_VALIDATORCURRENTREWARDS = _descriptor.Descriptor(
  name='ValidatorCurrentRewards',
  full_name='cosmos.distribution.v1beta1.ValidatorCurrentRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='cosmos.distribution.v1beta1.ValidatorCurrentRewards.rewards', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='cosmos.distribution.v1beta1.ValidatorCurrentRewards.period', index=1,
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
  serialized_start=651,
  serialized_end=792,
)


_VALIDATORACCUMULATEDCOMMISSION = _descriptor.Descriptor(
  name='ValidatorAccumulatedCommission',
  full_name='cosmos.distribution.v1beta1.ValidatorAccumulatedCommission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commission', full_name='cosmos.distribution.v1beta1.ValidatorAccumulatedCommission.commission', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=795,
  serialized_end=930,
)


_VALIDATOROUTSTANDINGREWARDS = _descriptor.Descriptor(
  name='ValidatorOutstandingRewards',
  full_name='cosmos.distribution.v1beta1.ValidatorOutstandingRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='cosmos.distribution.v1beta1.ValidatorOutstandingRewards.rewards', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=933,
  serialized_end=1062,
)


_VALIDATORSLASHEVENT = _descriptor.Descriptor(
  name='ValidatorSlashEvent',
  full_name='cosmos.distribution.v1beta1.ValidatorSlashEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_period', full_name='cosmos.distribution.v1beta1.ValidatorSlashEvent.validator_period', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fraction', full_name='cosmos.distribution.v1beta1.ValidatorSlashEvent.fraction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=1064,
  serialized_end=1191,
)


_VALIDATORSLASHEVENTS = _descriptor.Descriptor(
  name='ValidatorSlashEvents',
  full_name='cosmos.distribution.v1beta1.ValidatorSlashEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_slash_events', full_name='cosmos.distribution.v1beta1.ValidatorSlashEvents.validator_slash_events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1193,
  serialized_end=1309,
)


_FEEPOOL = _descriptor.Descriptor(
  name='FeePool',
  full_name='cosmos.distribution.v1beta1.FeePool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='community_pool', full_name='cosmos.distribution.v1beta1.FeePool.community_pool', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins')), file=DESCRIPTOR),
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
  serialized_start=1311,
  serialized_end=1427,
)


_COMMUNITYPOOLSPENDPROPOSAL = _descriptor.Descriptor(
  name='CommunityPoolSpendProposal',
  full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposal.recipient', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposal.amount', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\350\240\037\000\210\240\037\000\230\240\037\000\312\264-\032cosmos.gov.v1beta1.Content')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1430,
  serialized_end=1650,
)


_DELEGATORSTARTINGINFO = _descriptor.Descriptor(
  name='DelegatorStartingInfo',
  full_name='cosmos.distribution.v1beta1.DelegatorStartingInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='previous_period', full_name='cosmos.distribution.v1beta1.DelegatorStartingInfo.previous_period', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stake', full_name='cosmos.distribution.v1beta1.DelegatorStartingInfo.stake', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='cosmos.distribution.v1beta1.DelegatorStartingInfo.height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\017creation_height')), file=DESCRIPTOR),
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
  serialized_start=1653,
  serialized_end=1815,
)


_DELEGATIONDELEGATORREWARD = _descriptor.Descriptor(
  name='DelegationDelegatorReward',
  full_name='cosmos.distribution.v1beta1.DelegationDelegatorReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_address', full_name='cosmos.distribution.v1beta1.DelegationDelegatorReward.validator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='cosmos.distribution.v1beta1.DelegationDelegatorReward.reward', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\230\240\037\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1818,
  serialized_end=2007,
)


_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT = _descriptor.Descriptor(
  name='CommunityPoolSpendProposalWithDeposit',
  full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit.recipient', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit.amount', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deposit', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit.deposit', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\230\240\037\001\312\264-\032cosmos.gov.v1beta1.Content')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2010,
  serialized_end=2177,
)

_VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_VALIDATORCURRENTREWARDS.fields_by_name['rewards'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events'].message_type = _VALIDATORSLASHEVENT
_FEEPOOL.fields_by_name['community_pool'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_DELEGATIONDELEGATORREWARD.fields_by_name['reward'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
DESCRIPTOR.message_types_by_name['ValidatorHistoricalRewards'] = _VALIDATORHISTORICALREWARDS
DESCRIPTOR.message_types_by_name['ValidatorCurrentRewards'] = _VALIDATORCURRENTREWARDS
DESCRIPTOR.message_types_by_name['ValidatorAccumulatedCommission'] = _VALIDATORACCUMULATEDCOMMISSION
DESCRIPTOR.message_types_by_name['ValidatorOutstandingRewards'] = _VALIDATOROUTSTANDINGREWARDS
DESCRIPTOR.message_types_by_name['ValidatorSlashEvent'] = _VALIDATORSLASHEVENT
DESCRIPTOR.message_types_by_name['ValidatorSlashEvents'] = _VALIDATORSLASHEVENTS
DESCRIPTOR.message_types_by_name['FeePool'] = _FEEPOOL
DESCRIPTOR.message_types_by_name['CommunityPoolSpendProposal'] = _COMMUNITYPOOLSPENDPROPOSAL
DESCRIPTOR.message_types_by_name['DelegatorStartingInfo'] = _DELEGATORSTARTINGINFO
DESCRIPTOR.message_types_by_name['DelegationDelegatorReward'] = _DELEGATIONDELEGATORREWARD
DESCRIPTOR.message_types_by_name['CommunityPoolSpendProposalWithDeposit'] = _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
  DESCRIPTOR = _PARAMS,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.Params)
  ))
_sym_db.RegisterMessage(Params)

ValidatorHistoricalRewards = _reflection.GeneratedProtocolMessageType('ValidatorHistoricalRewards', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATORHISTORICALREWARDS,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorHistoricalRewards)
  ))
_sym_db.RegisterMessage(ValidatorHistoricalRewards)

ValidatorCurrentRewards = _reflection.GeneratedProtocolMessageType('ValidatorCurrentRewards', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATORCURRENTREWARDS,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorCurrentRewards)
  ))
_sym_db.RegisterMessage(ValidatorCurrentRewards)

ValidatorAccumulatedCommission = _reflection.GeneratedProtocolMessageType('ValidatorAccumulatedCommission', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATORACCUMULATEDCOMMISSION,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorAccumulatedCommission)
  ))
_sym_db.RegisterMessage(ValidatorAccumulatedCommission)

ValidatorOutstandingRewards = _reflection.GeneratedProtocolMessageType('ValidatorOutstandingRewards', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATOROUTSTANDINGREWARDS,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorOutstandingRewards)
  ))
_sym_db.RegisterMessage(ValidatorOutstandingRewards)

ValidatorSlashEvent = _reflection.GeneratedProtocolMessageType('ValidatorSlashEvent', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATORSLASHEVENT,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorSlashEvent)
  ))
_sym_db.RegisterMessage(ValidatorSlashEvent)

ValidatorSlashEvents = _reflection.GeneratedProtocolMessageType('ValidatorSlashEvents', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATORSLASHEVENTS,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorSlashEvents)
  ))
_sym_db.RegisterMessage(ValidatorSlashEvents)

FeePool = _reflection.GeneratedProtocolMessageType('FeePool', (_message.Message,), dict(
  DESCRIPTOR = _FEEPOOL,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.FeePool)
  ))
_sym_db.RegisterMessage(FeePool)

CommunityPoolSpendProposal = _reflection.GeneratedProtocolMessageType('CommunityPoolSpendProposal', (_message.Message,), dict(
  DESCRIPTOR = _COMMUNITYPOOLSPENDPROPOSAL,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.CommunityPoolSpendProposal)
  ))
_sym_db.RegisterMessage(CommunityPoolSpendProposal)

DelegatorStartingInfo = _reflection.GeneratedProtocolMessageType('DelegatorStartingInfo', (_message.Message,), dict(
  DESCRIPTOR = _DELEGATORSTARTINGINFO,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.DelegatorStartingInfo)
  ))
_sym_db.RegisterMessage(DelegatorStartingInfo)

DelegationDelegatorReward = _reflection.GeneratedProtocolMessageType('DelegationDelegatorReward', (_message.Message,), dict(
  DESCRIPTOR = _DELEGATIONDELEGATORREWARD,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.DelegationDelegatorReward)
  ))
_sym_db.RegisterMessage(DelegationDelegatorReward)

CommunityPoolSpendProposalWithDeposit = _reflection.GeneratedProtocolMessageType('CommunityPoolSpendProposalWithDeposit', (_message.Message,), dict(
  DESCRIPTOR = _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT,
  __module__ = 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit)
  ))
_sym_db.RegisterMessage(CommunityPoolSpendProposalWithDeposit)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z1github.com/cosmos/cosmos-sdk/x/distribution/types\250\342\036\001'))
_PARAMS.fields_by_name['community_tax'].has_options = True
_PARAMS.fields_by_name['community_tax']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'))
_PARAMS.fields_by_name['base_proposer_reward'].has_options = True
_PARAMS.fields_by_name['base_proposer_reward']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'))
_PARAMS.fields_by_name['bonus_proposer_reward'].has_options = True
_PARAMS.fields_by_name['bonus_proposer_reward']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'))
_PARAMS.has_options = True
_PARAMS._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000'))
_VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio'].has_options = True
_VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000'))
_VALIDATORCURRENTREWARDS.fields_by_name['rewards'].has_options = True
_VALIDATORCURRENTREWARDS.fields_by_name['rewards']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000'))
_VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission'].has_options = True
_VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000'))
_VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards'].has_options = True
_VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000'))
_VALIDATORSLASHEVENT.fields_by_name['fraction'].has_options = True
_VALIDATORSLASHEVENT.fields_by_name['fraction']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'))
_VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events'].has_options = True
_VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_VALIDATORSLASHEVENTS.has_options = True
_VALIDATORSLASHEVENTS._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000'))
_FEEPOOL.fields_by_name['community_pool'].has_options = True
_FEEPOOL.fields_by_name['community_pool']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins'))
_COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount'].has_options = True
_COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'))
_COMMUNITYPOOLSPENDPROPOSAL.has_options = True
_COMMUNITYPOOLSPENDPROPOSAL._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\350\240\037\000\210\240\037\000\230\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'))
_DELEGATORSTARTINGINFO.fields_by_name['stake'].has_options = True
_DELEGATORSTARTINGINFO.fields_by_name['stake']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'))
_DELEGATORSTARTINGINFO.fields_by_name['height'].has_options = True
_DELEGATORSTARTINGINFO.fields_by_name['height']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\017creation_height'))
_DELEGATIONDELEGATORREWARD.fields_by_name['validator_address'].has_options = True
_DELEGATIONDELEGATORREWARD.fields_by_name['validator_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_DELEGATIONDELEGATORREWARD.fields_by_name['reward'].has_options = True
_DELEGATIONDELEGATORREWARD.fields_by_name['reward']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000'))
_DELEGATIONDELEGATORREWARD.has_options = True
_DELEGATIONDELEGATORREWARD._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\230\240\037\001'))
_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.has_options = True
_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\230\240\037\001\312\264-\032cosmos.gov.v1beta1.Content'))
# @@protoc_insertion_point(module_scope)
