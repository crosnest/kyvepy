# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/team/v1beta1/team.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/team/v1beta1/team.proto',
  package='kyve.team.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\x1ckyve/team/v1beta1/team.proto\x12\x11kyve.team.v1beta1\";\n\tAuthority\x12\x15\n\rtotal_rewards\x18\x01 \x01(\x04\x12\x17\n\x0frewards_claimed\x18\x02 \x01(\x04\"\xc7\x01\n\x12TeamVestingAccount\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x18\n\x10total_allocation\x18\x02 \x01(\x04\x12\x14\n\x0c\x63ommencement\x18\x03 \x01(\x04\x12\x10\n\x08\x63lawback\x18\x04 \x01(\x04\x12\x18\n\x10unlocked_claimed\x18\x05 \x01(\x04\x12\x19\n\x11last_claimed_time\x18\x06 \x01(\x04\x12\x15\n\rtotal_rewards\x18\x07 \x01(\x04\x12\x17\n\x0frewards_claimed\x18\x08 \x01(\x04\x42+Z)github.com/KYVENetwork/chain/x/team/typesb\x06proto3')
)




_AUTHORITY = _descriptor.Descriptor(
  name='Authority',
  full_name='kyve.team.v1beta1.Authority',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_rewards', full_name='kyve.team.v1beta1.Authority.total_rewards', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rewards_claimed', full_name='kyve.team.v1beta1.Authority.rewards_claimed', index=1,
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
  serialized_start=51,
  serialized_end=110,
)


_TEAMVESTINGACCOUNT = _descriptor.Descriptor(
  name='TeamVestingAccount',
  full_name='kyve.team.v1beta1.TeamVestingAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.team.v1beta1.TeamVestingAccount.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_allocation', full_name='kyve.team.v1beta1.TeamVestingAccount.total_allocation', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commencement', full_name='kyve.team.v1beta1.TeamVestingAccount.commencement', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clawback', full_name='kyve.team.v1beta1.TeamVestingAccount.clawback', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlocked_claimed', full_name='kyve.team.v1beta1.TeamVestingAccount.unlocked_claimed', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_claimed_time', full_name='kyve.team.v1beta1.TeamVestingAccount.last_claimed_time', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_rewards', full_name='kyve.team.v1beta1.TeamVestingAccount.total_rewards', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rewards_claimed', full_name='kyve.team.v1beta1.TeamVestingAccount.rewards_claimed', index=7,
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
  serialized_start=113,
  serialized_end=312,
)

DESCRIPTOR.message_types_by_name['Authority'] = _AUTHORITY
DESCRIPTOR.message_types_by_name['TeamVestingAccount'] = _TEAMVESTINGACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Authority = _reflection.GeneratedProtocolMessageType('Authority', (_message.Message,), dict(
  DESCRIPTOR = _AUTHORITY,
  __module__ = 'kyve.team.v1beta1.team_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.Authority)
  ))
_sym_db.RegisterMessage(Authority)

TeamVestingAccount = _reflection.GeneratedProtocolMessageType('TeamVestingAccount', (_message.Message,), dict(
  DESCRIPTOR = _TEAMVESTINGACCOUNT,
  __module__ = 'kyve.team.v1beta1.team_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.TeamVestingAccount)
  ))
_sym_db.RegisterMessage(TeamVestingAccount)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/KYVENetwork/chain/x/team/types'))
# @@protoc_insertion_point(module_scope)