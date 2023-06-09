# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/team/v1beta1/genesis.proto

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
from kyve.team.v1beta1 import team_pb2 as kyve_dot_team_dot_v1beta1_dot_team__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/team/v1beta1/genesis.proto',
  package='kyve.team.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\x1fkyve/team/v1beta1/genesis.proto\x12\x11kyve.team.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ckyve/team/v1beta1/team.proto\"\x9f\x01\n\x0cGenesisState\x12\x35\n\tauthority\x18\x02 \x01(\x0b\x32\x1c.kyve.team.v1beta1.AuthorityB\x04\xc8\xde\x1f\x00\x12\x41\n\x0c\x61\x63\x63ount_list\x18\x03 \x03(\x0b\x32%.kyve.team.v1beta1.TeamVestingAccountB\x04\xc8\xde\x1f\x00\x12\x15\n\raccount_count\x18\x04 \x01(\x04\x42+Z)github.com/KYVENetwork/chain/x/team/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,kyve_dot_team_dot_v1beta1_dot_team__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='kyve.team.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.team.v1beta1.GenesisState.authority', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_list', full_name='kyve.team.v1beta1.GenesisState.account_list', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_count', full_name='kyve.team.v1beta1.GenesisState.account_count', index=2,
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
  serialized_start=107,
  serialized_end=266,
)

_GENESISSTATE.fields_by_name['authority'].message_type = kyve_dot_team_dot_v1beta1_dot_team__pb2._AUTHORITY
_GENESISSTATE.fields_by_name['account_list'].message_type = kyve_dot_team_dot_v1beta1_dot_team__pb2._TEAMVESTINGACCOUNT
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), dict(
  DESCRIPTOR = _GENESISSTATE,
  __module__ = 'kyve.team.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:kyve.team.v1beta1.GenesisState)
  ))
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/KYVENetwork/chain/x/team/types'))
_GENESISSTATE.fields_by_name['authority'].has_options = True
_GENESISSTATE.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_GENESISSTATE.fields_by_name['account_list'].has_options = True
_GENESISSTATE.fields_by_name['account_list']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
