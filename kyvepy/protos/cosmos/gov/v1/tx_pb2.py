# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1/tx.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.gov.v1 import gov_pb2 as cosmos_dot_gov_dot_v1_dot_gov__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/gov/v1/tx.proto',
  package='cosmos.gov.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x63osmos/gov/v1/tx.proto\x12\rcosmos.gov.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17\x63osmos/gov/v1/gov.proto\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x19google/protobuf/any.proto\x1a\x17\x63osmos/msg/v1/msg.proto\"\xc2\x01\n\x11MsgSubmitProposal\x12&\n\x08messages\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x38\n\x0finitial_deposit\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12*\n\x08proposer\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x10\n\x08metadata\x18\x04 \x01(\t:\r\x82\xe7\xb0*\x08proposer\"0\n\x19MsgSubmitProposalResponse\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\"m\n\x14MsgExecLegacyContent\x12\x32\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x0b\xca\xb4-\x07\x43ontent\x12\x11\n\tauthority\x18\x02 \x01(\t:\x0e\x82\xe7\xb0*\tauthority\"\x1e\n\x1cMsgExecLegacyContentResponse\"\xa1\x01\n\x07MsgVote\x12$\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x0f\xea\xde\x1f\x0bproposal_id\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x06option\x18\x03 \x01(\x0e\x32\x19.cosmos.gov.v1.VoteOption\x12\x10\n\x08metadata\x18\x04 \x01(\t:\n\x82\xe7\xb0*\x05voter\"\x11\n\x0fMsgVoteResponse\"\xb2\x01\n\x0fMsgVoteWeighted\x12$\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x0f\xea\xde\x1f\x0bproposal_id\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x32\n\x07options\x18\x03 \x03(\x0b\x32!.cosmos.gov.v1.WeightedVoteOption\x12\x10\n\x08metadata\x18\x04 \x01(\t:\n\x82\xe7\xb0*\x05voter\"\x19\n\x17MsgVoteWeightedResponse\"\xa0\x01\n\nMsgDeposit\x12$\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x0f\xea\xde\x1f\x0bproposal_id\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12/\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tdepositor\"\x14\n\x12MsgDepositResponse2\xab\x03\n\x03Msg\x12\\\n\x0eSubmitProposal\x12 .cosmos.gov.v1.MsgSubmitProposal\x1a(.cosmos.gov.v1.MsgSubmitProposalResponse\x12\x65\n\x11\x45xecLegacyContent\x12#.cosmos.gov.v1.MsgExecLegacyContent\x1a+.cosmos.gov.v1.MsgExecLegacyContentResponse\x12>\n\x04Vote\x12\x16.cosmos.gov.v1.MsgVote\x1a\x1e.cosmos.gov.v1.MsgVoteResponse\x12V\n\x0cVoteWeighted\x12\x1e.cosmos.gov.v1.MsgVoteWeighted\x1a&.cosmos.gov.v1.MsgVoteWeightedResponse\x12G\n\x07\x44\x65posit\x12\x19.cosmos.gov.v1.MsgDeposit\x1a!.cosmos.gov.v1.MsgDepositResponseB-Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1b\x06proto3')
  ,
  dependencies=[cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,cosmos_dot_gov_dot_v1_dot_gov__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,cosmos_dot_msg_dot_v1_dot_msg__pb2.DESCRIPTOR,])




_MSGSUBMITPROPOSAL = _descriptor.Descriptor(
  name='MsgSubmitProposal',
  full_name='cosmos.gov.v1.MsgSubmitProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='cosmos.gov.v1.MsgSubmitProposal.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_deposit', full_name='cosmos.gov.v1.MsgSubmitProposal.initial_deposit', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposer', full_name='cosmos.gov.v1.MsgSubmitProposal.proposer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='cosmos.gov.v1.MsgSubmitProposal.metadata', index=3,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\010proposer')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=394,
)


_MSGSUBMITPROPOSALRESPONSE = _descriptor.Descriptor(
  name='MsgSubmitProposalResponse',
  full_name='cosmos.gov.v1.MsgSubmitProposalResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='cosmos.gov.v1.MsgSubmitProposalResponse.proposal_id', index=0,
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
  serialized_start=396,
  serialized_end=444,
)


_MSGEXECLEGACYCONTENT = _descriptor.Descriptor(
  name='MsgExecLegacyContent',
  full_name='cosmos.gov.v1.MsgExecLegacyContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='cosmos.gov.v1.MsgExecLegacyContent.content', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\264-\007Content')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authority', full_name='cosmos.gov.v1.MsgExecLegacyContent.authority', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\tauthority')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=555,
)


_MSGEXECLEGACYCONTENTRESPONSE = _descriptor.Descriptor(
  name='MsgExecLegacyContentResponse',
  full_name='cosmos.gov.v1.MsgExecLegacyContentResponse',
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
  serialized_start=557,
  serialized_end=587,
)


_MSGVOTE = _descriptor.Descriptor(
  name='MsgVote',
  full_name='cosmos.gov.v1.MsgVote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='cosmos.gov.v1.MsgVote.proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\013proposal_id')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voter', full_name='cosmos.gov.v1.MsgVote.voter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='option', full_name='cosmos.gov.v1.MsgVote.option', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='cosmos.gov.v1.MsgVote.metadata', index=3,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\005voter')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=751,
)


_MSGVOTERESPONSE = _descriptor.Descriptor(
  name='MsgVoteResponse',
  full_name='cosmos.gov.v1.MsgVoteResponse',
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
  serialized_start=753,
  serialized_end=770,
)


_MSGVOTEWEIGHTED = _descriptor.Descriptor(
  name='MsgVoteWeighted',
  full_name='cosmos.gov.v1.MsgVoteWeighted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='cosmos.gov.v1.MsgVoteWeighted.proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\013proposal_id')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voter', full_name='cosmos.gov.v1.MsgVoteWeighted.voter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='cosmos.gov.v1.MsgVoteWeighted.options', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='cosmos.gov.v1.MsgVoteWeighted.metadata', index=3,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\005voter')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=773,
  serialized_end=951,
)


_MSGVOTEWEIGHTEDRESPONSE = _descriptor.Descriptor(
  name='MsgVoteWeightedResponse',
  full_name='cosmos.gov.v1.MsgVoteWeightedResponse',
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
  serialized_start=953,
  serialized_end=978,
)


_MSGDEPOSIT = _descriptor.Descriptor(
  name='MsgDeposit',
  full_name='cosmos.gov.v1.MsgDeposit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='cosmos.gov.v1.MsgDeposit.proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\013proposal_id')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depositor', full_name='cosmos.gov.v1.MsgDeposit.depositor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.gov.v1.MsgDeposit.amount', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\tdepositor')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=981,
  serialized_end=1141,
)


_MSGDEPOSITRESPONSE = _descriptor.Descriptor(
  name='MsgDepositResponse',
  full_name='cosmos.gov.v1.MsgDepositResponse',
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
  serialized_start=1143,
  serialized_end=1163,
)

_MSGSUBMITPROPOSAL.fields_by_name['messages'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MSGSUBMITPROPOSAL.fields_by_name['initial_deposit'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_MSGEXECLEGACYCONTENT.fields_by_name['content'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MSGVOTE.fields_by_name['option'].enum_type = cosmos_dot_gov_dot_v1_dot_gov__pb2._VOTEOPTION
_MSGVOTEWEIGHTED.fields_by_name['options'].message_type = cosmos_dot_gov_dot_v1_dot_gov__pb2._WEIGHTEDVOTEOPTION
_MSGDEPOSIT.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name['MsgSubmitProposal'] = _MSGSUBMITPROPOSAL
DESCRIPTOR.message_types_by_name['MsgSubmitProposalResponse'] = _MSGSUBMITPROPOSALRESPONSE
DESCRIPTOR.message_types_by_name['MsgExecLegacyContent'] = _MSGEXECLEGACYCONTENT
DESCRIPTOR.message_types_by_name['MsgExecLegacyContentResponse'] = _MSGEXECLEGACYCONTENTRESPONSE
DESCRIPTOR.message_types_by_name['MsgVote'] = _MSGVOTE
DESCRIPTOR.message_types_by_name['MsgVoteResponse'] = _MSGVOTERESPONSE
DESCRIPTOR.message_types_by_name['MsgVoteWeighted'] = _MSGVOTEWEIGHTED
DESCRIPTOR.message_types_by_name['MsgVoteWeightedResponse'] = _MSGVOTEWEIGHTEDRESPONSE
DESCRIPTOR.message_types_by_name['MsgDeposit'] = _MSGDEPOSIT
DESCRIPTOR.message_types_by_name['MsgDepositResponse'] = _MSGDEPOSITRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgSubmitProposal = _reflection.GeneratedProtocolMessageType('MsgSubmitProposal', (_message.Message,), dict(
  DESCRIPTOR = _MSGSUBMITPROPOSAL,
  __module__ = 'cosmos.gov.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1.MsgSubmitProposal)
  ))
_sym_db.RegisterMessage(MsgSubmitProposal)

MsgSubmitProposalResponse = _reflection.GeneratedProtocolMessageType('MsgSubmitProposalResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGSUBMITPROPOSALRESPONSE,
  __module__ = 'cosmos.gov.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1.MsgSubmitProposalResponse)
  ))
_sym_db.RegisterMessage(MsgSubmitProposalResponse)

MsgExecLegacyContent = _reflection.GeneratedProtocolMessageType('MsgExecLegacyContent', (_message.Message,), dict(
  DESCRIPTOR = _MSGEXECLEGACYCONTENT,
  __module__ = 'cosmos.gov.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1.MsgExecLegacyContent)
  ))
_sym_db.RegisterMessage(MsgExecLegacyContent)

MsgExecLegacyContentResponse = _reflection.GeneratedProtocolMessageType('MsgExecLegacyContentResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGEXECLEGACYCONTENTRESPONSE,
  __module__ = 'cosmos.gov.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1.MsgExecLegacyContentResponse)
  ))
_sym_db.RegisterMessage(MsgExecLegacyContentResponse)

MsgVote = _reflection.GeneratedProtocolMessageType('MsgVote', (_message.Message,), dict(
  DESCRIPTOR = _MSGVOTE,
  __module__ = 'cosmos.gov.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1.MsgVote)
  ))
_sym_db.RegisterMessage(MsgVote)

MsgVoteResponse = _reflection.GeneratedProtocolMessageType('MsgVoteResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGVOTERESPONSE,
  __module__ = 'cosmos.gov.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1.MsgVoteResponse)
  ))
_sym_db.RegisterMessage(MsgVoteResponse)

MsgVoteWeighted = _reflection.GeneratedProtocolMessageType('MsgVoteWeighted', (_message.Message,), dict(
  DESCRIPTOR = _MSGVOTEWEIGHTED,
  __module__ = 'cosmos.gov.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1.MsgVoteWeighted)
  ))
_sym_db.RegisterMessage(MsgVoteWeighted)

MsgVoteWeightedResponse = _reflection.GeneratedProtocolMessageType('MsgVoteWeightedResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGVOTEWEIGHTEDRESPONSE,
  __module__ = 'cosmos.gov.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1.MsgVoteWeightedResponse)
  ))
_sym_db.RegisterMessage(MsgVoteWeightedResponse)

MsgDeposit = _reflection.GeneratedProtocolMessageType('MsgDeposit', (_message.Message,), dict(
  DESCRIPTOR = _MSGDEPOSIT,
  __module__ = 'cosmos.gov.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1.MsgDeposit)
  ))
_sym_db.RegisterMessage(MsgDeposit)

MsgDepositResponse = _reflection.GeneratedProtocolMessageType('MsgDepositResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGDEPOSITRESPONSE,
  __module__ = 'cosmos.gov.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1.MsgDepositResponse)
  ))
_sym_db.RegisterMessage(MsgDepositResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1'))
_MSGSUBMITPROPOSAL.fields_by_name['initial_deposit'].has_options = True
_MSGSUBMITPROPOSAL.fields_by_name['initial_deposit']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_MSGSUBMITPROPOSAL.fields_by_name['proposer'].has_options = True
_MSGSUBMITPROPOSAL.fields_by_name['proposer']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGSUBMITPROPOSAL.has_options = True
_MSGSUBMITPROPOSAL._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\010proposer'))
_MSGEXECLEGACYCONTENT.fields_by_name['content'].has_options = True
_MSGEXECLEGACYCONTENT.fields_by_name['content']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\264-\007Content'))
_MSGEXECLEGACYCONTENT.has_options = True
_MSGEXECLEGACYCONTENT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\tauthority'))
_MSGVOTE.fields_by_name['proposal_id'].has_options = True
_MSGVOTE.fields_by_name['proposal_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\013proposal_id'))
_MSGVOTE.fields_by_name['voter'].has_options = True
_MSGVOTE.fields_by_name['voter']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGVOTE.has_options = True
_MSGVOTE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\005voter'))
_MSGVOTEWEIGHTED.fields_by_name['proposal_id'].has_options = True
_MSGVOTEWEIGHTED.fields_by_name['proposal_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\013proposal_id'))
_MSGVOTEWEIGHTED.fields_by_name['voter'].has_options = True
_MSGVOTEWEIGHTED.fields_by_name['voter']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGVOTEWEIGHTED.has_options = True
_MSGVOTEWEIGHTED._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\005voter'))
_MSGDEPOSIT.fields_by_name['proposal_id'].has_options = True
_MSGDEPOSIT.fields_by_name['proposal_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\013proposal_id'))
_MSGDEPOSIT.fields_by_name['depositor'].has_options = True
_MSGDEPOSIT.fields_by_name['depositor']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGDEPOSIT.fields_by_name['amount'].has_options = True
_MSGDEPOSIT.fields_by_name['amount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_MSGDEPOSIT.has_options = True
_MSGDEPOSIT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\tdepositor'))

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='cosmos.gov.v1.Msg',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1166,
  serialized_end=1593,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubmitProposal',
    full_name='cosmos.gov.v1.Msg.SubmitProposal',
    index=0,
    containing_service=None,
    input_type=_MSGSUBMITPROPOSAL,
    output_type=_MSGSUBMITPROPOSALRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ExecLegacyContent',
    full_name='cosmos.gov.v1.Msg.ExecLegacyContent',
    index=1,
    containing_service=None,
    input_type=_MSGEXECLEGACYCONTENT,
    output_type=_MSGEXECLEGACYCONTENTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Vote',
    full_name='cosmos.gov.v1.Msg.Vote',
    index=2,
    containing_service=None,
    input_type=_MSGVOTE,
    output_type=_MSGVOTERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='VoteWeighted',
    full_name='cosmos.gov.v1.Msg.VoteWeighted',
    index=3,
    containing_service=None,
    input_type=_MSGVOTEWEIGHTED,
    output_type=_MSGVOTEWEIGHTEDRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Deposit',
    full_name='cosmos.gov.v1.Msg.Deposit',
    index=4,
    containing_service=None,
    input_type=_MSGDEPOSIT,
    output_type=_MSGDEPOSITRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)