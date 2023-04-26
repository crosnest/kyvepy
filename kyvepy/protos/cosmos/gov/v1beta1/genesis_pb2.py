# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1beta1/genesis.proto

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
from cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/gov/v1beta1/genesis.proto',
  package='cosmos.gov.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n cosmos/gov/v1beta1/genesis.proto\x12\x12\x63osmos.gov.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmos/gov/v1beta1/gov.proto\"\xa6\x03\n\x0cGenesisState\x12\x1c\n\x14starting_proposal_id\x18\x01 \x01(\x04\x12?\n\x08\x64\x65posits\x18\x02 \x03(\x0b\x32\x1b.cosmos.gov.v1beta1.DepositB\x10\xaa\xdf\x1f\x08\x44\x65posits\xc8\xde\x1f\x00\x12\x36\n\x05votes\x18\x03 \x03(\x0b\x32\x18.cosmos.gov.v1beta1.VoteB\r\xaa\xdf\x1f\x05Votes\xc8\xde\x1f\x00\x12\x42\n\tproposals\x18\x04 \x03(\x0b\x32\x1c.cosmos.gov.v1beta1.ProposalB\x11\xaa\xdf\x1f\tProposals\xc8\xde\x1f\x00\x12?\n\x0e\x64\x65posit_params\x18\x05 \x01(\x0b\x32!.cosmos.gov.v1beta1.DepositParamsB\x04\xc8\xde\x1f\x00\x12=\n\rvoting_params\x18\x06 \x01(\x0b\x32 .cosmos.gov.v1beta1.VotingParamsB\x04\xc8\xde\x1f\x00\x12;\n\x0ctally_params\x18\x07 \x01(\x0b\x32\x1f.cosmos.gov.v1beta1.TallyParamsB\x04\xc8\xde\x1f\x00\x42\x32Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1b\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_gov_dot_v1beta1_dot_gov__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.gov.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='starting_proposal_id', full_name='cosmos.gov.v1beta1.GenesisState.starting_proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deposits', full_name='cosmos.gov.v1beta1.GenesisState.deposits', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\010Deposits\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='votes', full_name='cosmos.gov.v1beta1.GenesisState.votes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\005Votes\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposals', full_name='cosmos.gov.v1beta1.GenesisState.proposals', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\tProposals\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deposit_params', full_name='cosmos.gov.v1beta1.GenesisState.deposit_params', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voting_params', full_name='cosmos.gov.v1beta1.GenesisState.voting_params', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tally_params', full_name='cosmos.gov.v1beta1.GenesisState.tally_params', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=109,
  serialized_end=531,
)

_GENESISSTATE.fields_by_name['deposits'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._DEPOSIT
_GENESISSTATE.fields_by_name['votes'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._VOTE
_GENESISSTATE.fields_by_name['proposals'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._PROPOSAL
_GENESISSTATE.fields_by_name['deposit_params'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._DEPOSITPARAMS
_GENESISSTATE.fields_by_name['voting_params'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._VOTINGPARAMS
_GENESISSTATE.fields_by_name['tally_params'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._TALLYPARAMS
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), dict(
  DESCRIPTOR = _GENESISSTATE,
  __module__ = 'cosmos.gov.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.GenesisState)
  ))
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1'))
_GENESISSTATE.fields_by_name['deposits'].has_options = True
_GENESISSTATE.fields_by_name['deposits']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\010Deposits\310\336\037\000'))
_GENESISSTATE.fields_by_name['votes'].has_options = True
_GENESISSTATE.fields_by_name['votes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\005Votes\310\336\037\000'))
_GENESISSTATE.fields_by_name['proposals'].has_options = True
_GENESISSTATE.fields_by_name['proposals']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\tProposals\310\336\037\000'))
_GENESISSTATE.fields_by_name['deposit_params'].has_options = True
_GENESISSTATE.fields_by_name['deposit_params']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_GENESISSTATE.fields_by_name['voting_params'].has_options = True
_GENESISSTATE.fields_by_name['voting_params']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_GENESISSTATE.fields_by_name['tally_params'].has_options = True
_GENESISSTATE.fields_by_name['tally_params']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
