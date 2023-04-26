# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/fee/v1/genesis.proto

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
from ibc.applications.fee.v1 import fee_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_fee__pb2
from ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/applications/fee/v1/genesis.proto',
  package='ibc.applications.fee.v1',
  syntax='proto3',
  serialized_pb=_b('\n%ibc/applications/fee/v1/genesis.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\x1a!ibc/applications/fee/v1/fee.proto\x1a!ibc/core/channel/v1/channel.proto\"\xc5\x04\n\x0cGenesisState\x12\x66\n\x0fidentified_fees\x18\x01 \x03(\x0b\x32-.ibc.applications.fee.v1.IdentifiedPacketFeesB\x1e\xf2\xde\x1f\x16yaml:\"identified_fees\"\xc8\xde\x1f\x00\x12m\n\x14\x66\x65\x65_enabled_channels\x18\x02 \x03(\x0b\x32*.ibc.applications.fee.v1.FeeEnabledChannelB#\xf2\xde\x1f\x1byaml:\"fee_enabled_channels\"\xc8\xde\x1f\x00\x12\x65\n\x11registered_payees\x18\x03 \x03(\x0b\x32(.ibc.applications.fee.v1.RegisteredPayeeB \xf2\xde\x1f\x18yaml:\"registered_payees\"\xc8\xde\x1f\x00\x12\x8b\x01\n\x1eregistered_counterparty_payees\x18\x04 \x03(\x0b\x32\x34.ibc.applications.fee.v1.RegisteredCounterpartyPayeeB-\xf2\xde\x1f%yaml:\"registered_counterparty_payees\"\xc8\xde\x1f\x00\x12i\n\x10\x66orward_relayers\x18\x05 \x03(\x0b\x32..ibc.applications.fee.v1.ForwardRelayerAddressB\x1f\xf2\xde\x1f\x17yaml:\"forward_relayers\"\xc8\xde\x1f\x00\"c\n\x11\x46\x65\x65\x45nabledChannel\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\"\\\n\x0fRegisteredPayee\x12)\n\nchannel_id\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12\x0f\n\x07relayer\x18\x02 \x01(\t\x12\r\n\x05payee\x18\x03 \x01(\t\"\x94\x01\n\x1bRegisteredCounterpartyPayee\x12)\n\nchannel_id\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12\x0f\n\x07relayer\x18\x02 \x01(\t\x12\x39\n\x12\x63ounterparty_payee\x18\x03 \x01(\tB\x1d\xf2\xde\x1f\x19yaml:\"counterparty_payee\"\"t\n\x15\x46orwardRelayerAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12J\n\tpacket_id\x18\x02 \x01(\x0b\x32\x1d.ibc.core.channel.v1.PacketIdB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"packet_id\"B7Z5github.com/cosmos/ibc-go/v6/modules/apps/29-fee/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,ibc_dot_applications_dot_fee_dot_v1_dot_fee__pb2.DESCRIPTOR,ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='ibc.applications.fee.v1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identified_fees', full_name='ibc.applications.fee.v1.GenesisState.identified_fees', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\026yaml:\"identified_fees\"\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_enabled_channels', full_name='ibc.applications.fee.v1.GenesisState.fee_enabled_channels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\033yaml:\"fee_enabled_channels\"\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registered_payees', full_name='ibc.applications.fee.v1.GenesisState.registered_payees', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\030yaml:\"registered_payees\"\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registered_counterparty_payees', full_name='ibc.applications.fee.v1.GenesisState.registered_counterparty_payees', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037%yaml:\"registered_counterparty_payees\"\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forward_relayers', full_name='ibc.applications.fee.v1.GenesisState.forward_relayers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\027yaml:\"forward_relayers\"\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_end=740,
)


_FEEENABLEDCHANNEL = _descriptor.Descriptor(
  name='FeeEnabledChannel',
  full_name='ibc.applications.fee.v1.FeeEnabledChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_id', full_name='ibc.applications.fee.v1.FeeEnabledChannel.port_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\016yaml:\"port_id\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='ibc.applications.fee.v1.FeeEnabledChannel.channel_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\021yaml:\"channel_id\"')), file=DESCRIPTOR),
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
  serialized_start=742,
  serialized_end=841,
)


_REGISTEREDPAYEE = _descriptor.Descriptor(
  name='RegisteredPayee',
  full_name='ibc.applications.fee.v1.RegisteredPayee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='ibc.applications.fee.v1.RegisteredPayee.channel_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\021yaml:\"channel_id\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relayer', full_name='ibc.applications.fee.v1.RegisteredPayee.relayer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payee', full_name='ibc.applications.fee.v1.RegisteredPayee.payee', index=2,
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
  serialized_start=843,
  serialized_end=935,
)


_REGISTEREDCOUNTERPARTYPAYEE = _descriptor.Descriptor(
  name='RegisteredCounterpartyPayee',
  full_name='ibc.applications.fee.v1.RegisteredCounterpartyPayee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='ibc.applications.fee.v1.RegisteredCounterpartyPayee.channel_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\021yaml:\"channel_id\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relayer', full_name='ibc.applications.fee.v1.RegisteredCounterpartyPayee.relayer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counterparty_payee', full_name='ibc.applications.fee.v1.RegisteredCounterpartyPayee.counterparty_payee', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\031yaml:\"counterparty_payee\"')), file=DESCRIPTOR),
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
  serialized_start=938,
  serialized_end=1086,
)


_FORWARDRELAYERADDRESS = _descriptor.Descriptor(
  name='ForwardRelayerAddress',
  full_name='ibc.applications.fee.v1.ForwardRelayerAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='ibc.applications.fee.v1.ForwardRelayerAddress.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packet_id', full_name='ibc.applications.fee.v1.ForwardRelayerAddress.packet_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\362\336\037\020yaml:\"packet_id\"')), file=DESCRIPTOR),
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
  serialized_start=1088,
  serialized_end=1204,
)

_GENESISSTATE.fields_by_name['identified_fees'].message_type = ibc_dot_applications_dot_fee_dot_v1_dot_fee__pb2._IDENTIFIEDPACKETFEES
_GENESISSTATE.fields_by_name['fee_enabled_channels'].message_type = _FEEENABLEDCHANNEL
_GENESISSTATE.fields_by_name['registered_payees'].message_type = _REGISTEREDPAYEE
_GENESISSTATE.fields_by_name['registered_counterparty_payees'].message_type = _REGISTEREDCOUNTERPARTYPAYEE
_GENESISSTATE.fields_by_name['forward_relayers'].message_type = _FORWARDRELAYERADDRESS
_FORWARDRELAYERADDRESS.fields_by_name['packet_id'].message_type = ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2._PACKETID
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
DESCRIPTOR.message_types_by_name['FeeEnabledChannel'] = _FEEENABLEDCHANNEL
DESCRIPTOR.message_types_by_name['RegisteredPayee'] = _REGISTEREDPAYEE
DESCRIPTOR.message_types_by_name['RegisteredCounterpartyPayee'] = _REGISTEREDCOUNTERPARTYPAYEE
DESCRIPTOR.message_types_by_name['ForwardRelayerAddress'] = _FORWARDRELAYERADDRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), dict(
  DESCRIPTOR = _GENESISSTATE,
  __module__ = 'ibc.applications.fee.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.GenesisState)
  ))
_sym_db.RegisterMessage(GenesisState)

FeeEnabledChannel = _reflection.GeneratedProtocolMessageType('FeeEnabledChannel', (_message.Message,), dict(
  DESCRIPTOR = _FEEENABLEDCHANNEL,
  __module__ = 'ibc.applications.fee.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.FeeEnabledChannel)
  ))
_sym_db.RegisterMessage(FeeEnabledChannel)

RegisteredPayee = _reflection.GeneratedProtocolMessageType('RegisteredPayee', (_message.Message,), dict(
  DESCRIPTOR = _REGISTEREDPAYEE,
  __module__ = 'ibc.applications.fee.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.RegisteredPayee)
  ))
_sym_db.RegisterMessage(RegisteredPayee)

RegisteredCounterpartyPayee = _reflection.GeneratedProtocolMessageType('RegisteredCounterpartyPayee', (_message.Message,), dict(
  DESCRIPTOR = _REGISTEREDCOUNTERPARTYPAYEE,
  __module__ = 'ibc.applications.fee.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.RegisteredCounterpartyPayee)
  ))
_sym_db.RegisterMessage(RegisteredCounterpartyPayee)

ForwardRelayerAddress = _reflection.GeneratedProtocolMessageType('ForwardRelayerAddress', (_message.Message,), dict(
  DESCRIPTOR = _FORWARDRELAYERADDRESS,
  __module__ = 'ibc.applications.fee.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.ForwardRelayerAddress)
  ))
_sym_db.RegisterMessage(ForwardRelayerAddress)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z5github.com/cosmos/ibc-go/v6/modules/apps/29-fee/types'))
_GENESISSTATE.fields_by_name['identified_fees'].has_options = True
_GENESISSTATE.fields_by_name['identified_fees']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\026yaml:\"identified_fees\"\310\336\037\000'))
_GENESISSTATE.fields_by_name['fee_enabled_channels'].has_options = True
_GENESISSTATE.fields_by_name['fee_enabled_channels']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\033yaml:\"fee_enabled_channels\"\310\336\037\000'))
_GENESISSTATE.fields_by_name['registered_payees'].has_options = True
_GENESISSTATE.fields_by_name['registered_payees']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\030yaml:\"registered_payees\"\310\336\037\000'))
_GENESISSTATE.fields_by_name['registered_counterparty_payees'].has_options = True
_GENESISSTATE.fields_by_name['registered_counterparty_payees']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037%yaml:\"registered_counterparty_payees\"\310\336\037\000'))
_GENESISSTATE.fields_by_name['forward_relayers'].has_options = True
_GENESISSTATE.fields_by_name['forward_relayers']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\027yaml:\"forward_relayers\"\310\336\037\000'))
_FEEENABLEDCHANNEL.fields_by_name['port_id'].has_options = True
_FEEENABLEDCHANNEL.fields_by_name['port_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\016yaml:\"port_id\"'))
_FEEENABLEDCHANNEL.fields_by_name['channel_id'].has_options = True
_FEEENABLEDCHANNEL.fields_by_name['channel_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\021yaml:\"channel_id\"'))
_REGISTEREDPAYEE.fields_by_name['channel_id'].has_options = True
_REGISTEREDPAYEE.fields_by_name['channel_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\021yaml:\"channel_id\"'))
_REGISTEREDCOUNTERPARTYPAYEE.fields_by_name['channel_id'].has_options = True
_REGISTEREDCOUNTERPARTYPAYEE.fields_by_name['channel_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\021yaml:\"channel_id\"'))
_REGISTEREDCOUNTERPARTYPAYEE.fields_by_name['counterparty_payee'].has_options = True
_REGISTEREDCOUNTERPARTYPAYEE.fields_by_name['counterparty_payee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\031yaml:\"counterparty_payee\"'))
_FORWARDRELAYERADDRESS.fields_by_name['packet_id'].has_options = True
_FORWARDRELAYERADDRESS.fields_by_name['packet_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\362\336\037\020yaml:\"packet_id\"'))
# @@protoc_insertion_point(module_scope)
