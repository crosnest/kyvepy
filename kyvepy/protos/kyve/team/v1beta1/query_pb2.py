# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/team/v1beta1/query.proto

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
from kyve.team.v1beta1 import team_pb2 as kyve_dot_team_dot_v1beta1_dot_team__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/team/v1beta1/query.proto',
  package='kyve.team.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\x1dkyve/team/v1beta1/query.proto\x12\x11kyve.team.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ckyve/team/v1beta1/team.proto\"\x16\n\x14QueryTeamInfoRequest\"\xb8\x03\n\x15QueryTeamInfoResponse\x12\x1c\n\x14\x66oundation_authority\x18\x01 \x01(\t\x12\x15\n\rbcp_authority\x18\x02 \x01(\t\x12\x1d\n\x15total_team_allocation\x18\x03 \x01(\x04\x12\x1e\n\x16issued_team_allocation\x18\x04 \x01(\x04\x12!\n\x19\x61vailable_team_allocation\x18\x05 \x01(\x04\x12\x1f\n\x17total_authority_rewards\x18\x06 \x01(\x04\x12!\n\x19\x63laimed_authority_rewards\x18\x07 \x01(\x04\x12#\n\x1b\x61vailable_authority_rewards\x18\x08 \x01(\x04\x12\x1d\n\x15total_account_rewards\x18\t \x01(\x04\x12\x1f\n\x17\x63laimed_account_rewards\x18\n \x01(\x04\x12!\n\x19\x61vailable_account_rewards\x18\x0b \x01(\x04\x12\x1f\n\x17required_module_balance\x18\x0c \x01(\x04\x12\x1b\n\x13team_module_balance\x18\r \x01(\x04\"!\n\x1fQueryTeamVestingAccountsRequest\"a\n QueryTeamVestingAccountsResponse\x12=\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32%.kyve.team.v1beta1.TeamVestingAccountB\x04\xc8\xde\x1f\x00\",\n\x1eQueryTeamVestingAccountRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"_\n\x1fQueryTeamVestingAccountResponse\x12<\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32%.kyve.team.v1beta1.TeamVestingAccountB\x04\xc8\xde\x1f\x00\"+\n\x1dQueryTeamVestingStatusRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"\xa0\x01\n\x1eQueryTeamVestingStatusResponse\x12\x14\n\x0crequest_date\x18\x01 \x01(\t\x12\x31\n\x04plan\x18\x02 \x01(\x0b\x32#.kyve.team.v1beta1.QueryVestingPlan\x12\x35\n\x06status\x18\x03 \x01(\x0b\x32%.kyve.team.v1beta1.QueryVestingStatus\"?\n#QueryTeamVestingStatusByTimeRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04time\x18\x02 \x01(\x04\"\xa6\x01\n$QueryTeamVestingStatusByTimeResponse\x12\x14\n\x0crequest_date\x18\x01 \x01(\t\x12\x31\n\x04plan\x18\x02 \x01(\x0b\x32#.kyve.team.v1beta1.QueryVestingPlan\x12\x35\n\x06status\x18\x03 \x01(\x0b\x32%.kyve.team.v1beta1.QueryVestingStatus\"\x96\x02\n\x12QueryVestingStatus\x12\x1b\n\x13total_vested_amount\x18\x01 \x01(\x04\x12\x1d\n\x15total_unlocked_amount\x18\x02 \x01(\x04\x12 \n\x18\x63urrent_claimable_amount\x18\x03 \x01(\x04\x12\x1c\n\x14locked_vested_amount\x18\x04 \x01(\x04\x12!\n\x19remaining_unvested_amount\x18\x05 \x01(\x04\x12\x16\n\x0e\x63laimed_amount\x18\x06 \x01(\x04\x12\x15\n\rtotal_rewards\x18\x07 \x01(\x04\x12\x17\n\x0f\x63laimed_rewards\x18\x08 \x01(\x04\x12\x19\n\x11\x61vailable_rewards\x18\t \x01(\x04\"\xeb\x01\n\x10QueryVestingPlan\x12\x14\n\x0c\x63ommencement\x18\x01 \x01(\t\x12\x1b\n\x13token_vesting_start\x18\x02 \x01(\t\x12\x1e\n\x16token_vesting_finished\x18\x03 \x01(\t\x12\x1a\n\x12token_unlock_start\x18\x04 \x01(\t\x12\x1d\n\x15token_unlock_finished\x18\x05 \x01(\t\x12\x10\n\x08\x63lawback\x18\x06 \x01(\x04\x12\x17\n\x0f\x63lawback_amount\x18\x07 \x01(\x04\x12\x1e\n\x16maximum_vesting_amount\x18\x08 \x01(\x04\x32\xf5\x06\n\x05Query\x12\x83\x01\n\x08TeamInfo\x12\'.kyve.team.v1beta1.QueryTeamInfoRequest\x1a(.kyve.team.v1beta1.QueryTeamInfoResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/kyve/team/v1beta1/team_info\x12\xb0\x01\n\x13TeamVestingAccounts\x12\x32.kyve.team.v1beta1.QueryTeamVestingAccountsRequest\x1a\x33.kyve.team.v1beta1.QueryTeamVestingAccountsResponse\"0\x82\xd3\xe4\x93\x02*\x12(/kyve/team/v1beta1/team_vesting_accounts\x12\xb1\x01\n\x12TeamVestingAccount\x12\x31.kyve.team.v1beta1.QueryTeamVestingAccountRequest\x1a\x32.kyve.team.v1beta1.QueryTeamVestingAccountResponse\"4\x82\xd3\xe4\x93\x02.\x12,/kyve/team/v1beta1/team_vesting_account/{id}\x12\xad\x01\n\x11TeamVestingStatus\x12\x30.kyve.team.v1beta1.QueryTeamVestingStatusRequest\x1a\x31.kyve.team.v1beta1.QueryTeamVestingStatusResponse\"3\x82\xd3\xe4\x93\x02-\x12+/kyve/team/v1beta1/team_vesting_status/{id}\x12\xce\x01\n\x17TeamVestingStatusByTime\x12\x36.kyve.team.v1beta1.QueryTeamVestingStatusByTimeRequest\x1a\x37.kyve.team.v1beta1.QueryTeamVestingStatusByTimeResponse\"B\x82\xd3\xe4\x93\x02<\x12:/kyve/team/v1beta1/team_vesting_status_by_time/{id}/{time}B+Z)github.com/KYVENetwork/chain/x/team/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,kyve_dot_team_dot_v1beta1_dot_team__pb2.DESCRIPTOR,])




_QUERYTEAMINFOREQUEST = _descriptor.Descriptor(
  name='QueryTeamInfoRequest',
  full_name='kyve.team.v1beta1.QueryTeamInfoRequest',
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
  serialized_start=134,
  serialized_end=156,
)


_QUERYTEAMINFORESPONSE = _descriptor.Descriptor(
  name='QueryTeamInfoResponse',
  full_name='kyve.team.v1beta1.QueryTeamInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='foundation_authority', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.foundation_authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bcp_authority', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.bcp_authority', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_team_allocation', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.total_team_allocation', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issued_team_allocation', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.issued_team_allocation', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_team_allocation', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.available_team_allocation', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_authority_rewards', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.total_authority_rewards', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claimed_authority_rewards', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.claimed_authority_rewards', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_authority_rewards', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.available_authority_rewards', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_account_rewards', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.total_account_rewards', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claimed_account_rewards', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.claimed_account_rewards', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_account_rewards', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.available_account_rewards', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required_module_balance', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.required_module_balance', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='team_module_balance', full_name='kyve.team.v1beta1.QueryTeamInfoResponse.team_module_balance', index=12,
      number=13, type=4, cpp_type=4, label=1,
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
  serialized_start=159,
  serialized_end=599,
)


_QUERYTEAMVESTINGACCOUNTSREQUEST = _descriptor.Descriptor(
  name='QueryTeamVestingAccountsRequest',
  full_name='kyve.team.v1beta1.QueryTeamVestingAccountsRequest',
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
  serialized_start=601,
  serialized_end=634,
)


_QUERYTEAMVESTINGACCOUNTSRESPONSE = _descriptor.Descriptor(
  name='QueryTeamVestingAccountsResponse',
  full_name='kyve.team.v1beta1.QueryTeamVestingAccountsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accounts', full_name='kyve.team.v1beta1.QueryTeamVestingAccountsResponse.accounts', index=0,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=733,
)


_QUERYTEAMVESTINGACCOUNTREQUEST = _descriptor.Descriptor(
  name='QueryTeamVestingAccountRequest',
  full_name='kyve.team.v1beta1.QueryTeamVestingAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.team.v1beta1.QueryTeamVestingAccountRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_end=779,
)


_QUERYTEAMVESTINGACCOUNTRESPONSE = _descriptor.Descriptor(
  name='QueryTeamVestingAccountResponse',
  full_name='kyve.team.v1beta1.QueryTeamVestingAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='kyve.team.v1beta1.QueryTeamVestingAccountResponse.account', index=0,
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
  serialized_start=781,
  serialized_end=876,
)


_QUERYTEAMVESTINGSTATUSREQUEST = _descriptor.Descriptor(
  name='QueryTeamVestingStatusRequest',
  full_name='kyve.team.v1beta1.QueryTeamVestingStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.team.v1beta1.QueryTeamVestingStatusRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=878,
  serialized_end=921,
)


_QUERYTEAMVESTINGSTATUSRESPONSE = _descriptor.Descriptor(
  name='QueryTeamVestingStatusResponse',
  full_name='kyve.team.v1beta1.QueryTeamVestingStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_date', full_name='kyve.team.v1beta1.QueryTeamVestingStatusResponse.request_date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plan', full_name='kyve.team.v1beta1.QueryTeamVestingStatusResponse.plan', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='kyve.team.v1beta1.QueryTeamVestingStatusResponse.status', index=2,
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
  serialized_start=924,
  serialized_end=1084,
)


_QUERYTEAMVESTINGSTATUSBYTIMEREQUEST = _descriptor.Descriptor(
  name='QueryTeamVestingStatusByTimeRequest',
  full_name='kyve.team.v1beta1.QueryTeamVestingStatusByTimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.team.v1beta1.QueryTeamVestingStatusByTimeRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='kyve.team.v1beta1.QueryTeamVestingStatusByTimeRequest.time', index=1,
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
  serialized_start=1086,
  serialized_end=1149,
)


_QUERYTEAMVESTINGSTATUSBYTIMERESPONSE = _descriptor.Descriptor(
  name='QueryTeamVestingStatusByTimeResponse',
  full_name='kyve.team.v1beta1.QueryTeamVestingStatusByTimeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_date', full_name='kyve.team.v1beta1.QueryTeamVestingStatusByTimeResponse.request_date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plan', full_name='kyve.team.v1beta1.QueryTeamVestingStatusByTimeResponse.plan', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='kyve.team.v1beta1.QueryTeamVestingStatusByTimeResponse.status', index=2,
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
  serialized_start=1152,
  serialized_end=1318,
)


_QUERYVESTINGSTATUS = _descriptor.Descriptor(
  name='QueryVestingStatus',
  full_name='kyve.team.v1beta1.QueryVestingStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_vested_amount', full_name='kyve.team.v1beta1.QueryVestingStatus.total_vested_amount', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_unlocked_amount', full_name='kyve.team.v1beta1.QueryVestingStatus.total_unlocked_amount', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_claimable_amount', full_name='kyve.team.v1beta1.QueryVestingStatus.current_claimable_amount', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locked_vested_amount', full_name='kyve.team.v1beta1.QueryVestingStatus.locked_vested_amount', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remaining_unvested_amount', full_name='kyve.team.v1beta1.QueryVestingStatus.remaining_unvested_amount', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claimed_amount', full_name='kyve.team.v1beta1.QueryVestingStatus.claimed_amount', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_rewards', full_name='kyve.team.v1beta1.QueryVestingStatus.total_rewards', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claimed_rewards', full_name='kyve.team.v1beta1.QueryVestingStatus.claimed_rewards', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_rewards', full_name='kyve.team.v1beta1.QueryVestingStatus.available_rewards', index=8,
      number=9, type=4, cpp_type=4, label=1,
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
  serialized_start=1321,
  serialized_end=1599,
)


_QUERYVESTINGPLAN = _descriptor.Descriptor(
  name='QueryVestingPlan',
  full_name='kyve.team.v1beta1.QueryVestingPlan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commencement', full_name='kyve.team.v1beta1.QueryVestingPlan.commencement', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_vesting_start', full_name='kyve.team.v1beta1.QueryVestingPlan.token_vesting_start', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_vesting_finished', full_name='kyve.team.v1beta1.QueryVestingPlan.token_vesting_finished', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_unlock_start', full_name='kyve.team.v1beta1.QueryVestingPlan.token_unlock_start', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_unlock_finished', full_name='kyve.team.v1beta1.QueryVestingPlan.token_unlock_finished', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clawback', full_name='kyve.team.v1beta1.QueryVestingPlan.clawback', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clawback_amount', full_name='kyve.team.v1beta1.QueryVestingPlan.clawback_amount', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum_vesting_amount', full_name='kyve.team.v1beta1.QueryVestingPlan.maximum_vesting_amount', index=7,
      number=8, type=4, cpp_type=4, label=1,
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
  serialized_start=1602,
  serialized_end=1837,
)

_QUERYTEAMVESTINGACCOUNTSRESPONSE.fields_by_name['accounts'].message_type = kyve_dot_team_dot_v1beta1_dot_team__pb2._TEAMVESTINGACCOUNT
_QUERYTEAMVESTINGACCOUNTRESPONSE.fields_by_name['account'].message_type = kyve_dot_team_dot_v1beta1_dot_team__pb2._TEAMVESTINGACCOUNT
_QUERYTEAMVESTINGSTATUSRESPONSE.fields_by_name['plan'].message_type = _QUERYVESTINGPLAN
_QUERYTEAMVESTINGSTATUSRESPONSE.fields_by_name['status'].message_type = _QUERYVESTINGSTATUS
_QUERYTEAMVESTINGSTATUSBYTIMERESPONSE.fields_by_name['plan'].message_type = _QUERYVESTINGPLAN
_QUERYTEAMVESTINGSTATUSBYTIMERESPONSE.fields_by_name['status'].message_type = _QUERYVESTINGSTATUS
DESCRIPTOR.message_types_by_name['QueryTeamInfoRequest'] = _QUERYTEAMINFOREQUEST
DESCRIPTOR.message_types_by_name['QueryTeamInfoResponse'] = _QUERYTEAMINFORESPONSE
DESCRIPTOR.message_types_by_name['QueryTeamVestingAccountsRequest'] = _QUERYTEAMVESTINGACCOUNTSREQUEST
DESCRIPTOR.message_types_by_name['QueryTeamVestingAccountsResponse'] = _QUERYTEAMVESTINGACCOUNTSRESPONSE
DESCRIPTOR.message_types_by_name['QueryTeamVestingAccountRequest'] = _QUERYTEAMVESTINGACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['QueryTeamVestingAccountResponse'] = _QUERYTEAMVESTINGACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['QueryTeamVestingStatusRequest'] = _QUERYTEAMVESTINGSTATUSREQUEST
DESCRIPTOR.message_types_by_name['QueryTeamVestingStatusResponse'] = _QUERYTEAMVESTINGSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['QueryTeamVestingStatusByTimeRequest'] = _QUERYTEAMVESTINGSTATUSBYTIMEREQUEST
DESCRIPTOR.message_types_by_name['QueryTeamVestingStatusByTimeResponse'] = _QUERYTEAMVESTINGSTATUSBYTIMERESPONSE
DESCRIPTOR.message_types_by_name['QueryVestingStatus'] = _QUERYVESTINGSTATUS
DESCRIPTOR.message_types_by_name['QueryVestingPlan'] = _QUERYVESTINGPLAN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryTeamInfoRequest = _reflection.GeneratedProtocolMessageType('QueryTeamInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTEAMINFOREQUEST,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryTeamInfoRequest)
  ))
_sym_db.RegisterMessage(QueryTeamInfoRequest)

QueryTeamInfoResponse = _reflection.GeneratedProtocolMessageType('QueryTeamInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTEAMINFORESPONSE,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryTeamInfoResponse)
  ))
_sym_db.RegisterMessage(QueryTeamInfoResponse)

QueryTeamVestingAccountsRequest = _reflection.GeneratedProtocolMessageType('QueryTeamVestingAccountsRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTEAMVESTINGACCOUNTSREQUEST,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryTeamVestingAccountsRequest)
  ))
_sym_db.RegisterMessage(QueryTeamVestingAccountsRequest)

QueryTeamVestingAccountsResponse = _reflection.GeneratedProtocolMessageType('QueryTeamVestingAccountsResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTEAMVESTINGACCOUNTSRESPONSE,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryTeamVestingAccountsResponse)
  ))
_sym_db.RegisterMessage(QueryTeamVestingAccountsResponse)

QueryTeamVestingAccountRequest = _reflection.GeneratedProtocolMessageType('QueryTeamVestingAccountRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTEAMVESTINGACCOUNTREQUEST,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryTeamVestingAccountRequest)
  ))
_sym_db.RegisterMessage(QueryTeamVestingAccountRequest)

QueryTeamVestingAccountResponse = _reflection.GeneratedProtocolMessageType('QueryTeamVestingAccountResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTEAMVESTINGACCOUNTRESPONSE,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryTeamVestingAccountResponse)
  ))
_sym_db.RegisterMessage(QueryTeamVestingAccountResponse)

QueryTeamVestingStatusRequest = _reflection.GeneratedProtocolMessageType('QueryTeamVestingStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTEAMVESTINGSTATUSREQUEST,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryTeamVestingStatusRequest)
  ))
_sym_db.RegisterMessage(QueryTeamVestingStatusRequest)

QueryTeamVestingStatusResponse = _reflection.GeneratedProtocolMessageType('QueryTeamVestingStatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTEAMVESTINGSTATUSRESPONSE,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryTeamVestingStatusResponse)
  ))
_sym_db.RegisterMessage(QueryTeamVestingStatusResponse)

QueryTeamVestingStatusByTimeRequest = _reflection.GeneratedProtocolMessageType('QueryTeamVestingStatusByTimeRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTEAMVESTINGSTATUSBYTIMEREQUEST,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryTeamVestingStatusByTimeRequest)
  ))
_sym_db.RegisterMessage(QueryTeamVestingStatusByTimeRequest)

QueryTeamVestingStatusByTimeResponse = _reflection.GeneratedProtocolMessageType('QueryTeamVestingStatusByTimeResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTEAMVESTINGSTATUSBYTIMERESPONSE,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryTeamVestingStatusByTimeResponse)
  ))
_sym_db.RegisterMessage(QueryTeamVestingStatusByTimeResponse)

QueryVestingStatus = _reflection.GeneratedProtocolMessageType('QueryVestingStatus', (_message.Message,), dict(
  DESCRIPTOR = _QUERYVESTINGSTATUS,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryVestingStatus)
  ))
_sym_db.RegisterMessage(QueryVestingStatus)

QueryVestingPlan = _reflection.GeneratedProtocolMessageType('QueryVestingPlan', (_message.Message,), dict(
  DESCRIPTOR = _QUERYVESTINGPLAN,
  __module__ = 'kyve.team.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.QueryVestingPlan)
  ))
_sym_db.RegisterMessage(QueryVestingPlan)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/KYVENetwork/chain/x/team/types'))
_QUERYTEAMVESTINGACCOUNTSRESPONSE.fields_by_name['accounts'].has_options = True
_QUERYTEAMVESTINGACCOUNTSRESPONSE.fields_by_name['accounts']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_QUERYTEAMVESTINGACCOUNTRESPONSE.fields_by_name['account'].has_options = True
_QUERYTEAMVESTINGACCOUNTRESPONSE.fields_by_name['account']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='kyve.team.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1840,
  serialized_end=2725,
  methods=[
  _descriptor.MethodDescriptor(
    name='TeamInfo',
    full_name='kyve.team.v1beta1.Query.TeamInfo',
    index=0,
    containing_service=None,
    input_type=_QUERYTEAMINFOREQUEST,
    output_type=_QUERYTEAMINFORESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\036\022\034/kyve/team/v1beta1/team_info')),
  ),
  _descriptor.MethodDescriptor(
    name='TeamVestingAccounts',
    full_name='kyve.team.v1beta1.Query.TeamVestingAccounts',
    index=1,
    containing_service=None,
    input_type=_QUERYTEAMVESTINGACCOUNTSREQUEST,
    output_type=_QUERYTEAMVESTINGACCOUNTSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002*\022(/kyve/team/v1beta1/team_vesting_accounts')),
  ),
  _descriptor.MethodDescriptor(
    name='TeamVestingAccount',
    full_name='kyve.team.v1beta1.Query.TeamVestingAccount',
    index=2,
    containing_service=None,
    input_type=_QUERYTEAMVESTINGACCOUNTREQUEST,
    output_type=_QUERYTEAMVESTINGACCOUNTRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002.\022,/kyve/team/v1beta1/team_vesting_account/{id}')),
  ),
  _descriptor.MethodDescriptor(
    name='TeamVestingStatus',
    full_name='kyve.team.v1beta1.Query.TeamVestingStatus',
    index=3,
    containing_service=None,
    input_type=_QUERYTEAMVESTINGSTATUSREQUEST,
    output_type=_QUERYTEAMVESTINGSTATUSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002-\022+/kyve/team/v1beta1/team_vesting_status/{id}')),
  ),
  _descriptor.MethodDescriptor(
    name='TeamVestingStatusByTime',
    full_name='kyve.team.v1beta1.Query.TeamVestingStatusByTime',
    index=4,
    containing_service=None,
    input_type=_QUERYTEAMVESTINGSTATUSBYTIMEREQUEST,
    output_type=_QUERYTEAMVESTINGSTATUSBYTIMERESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002<\022:/kyve/team/v1beta1/team_vesting_status_by_time/{id}/{time}')),
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
