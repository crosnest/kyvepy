# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crisis/v1beta1/genesis.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/crisis/v1beta1/genesis.proto',
  package='cosmos.crisis.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n#cosmos/crisis/v1beta1/genesis.proto\x12\x15\x63osmos.crisis.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"E\n\x0cGenesisState\x12\x35\n\x0c\x63onstant_fee\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x42-Z+github.com/cosmos/cosmos-sdk/x/crisis/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.crisis.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='constant_fee', full_name='cosmos.crisis.v1beta1.GenesisState.constant_fee', index=0,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=116,
  serialized_end=185,
)

_GENESISSTATE.fields_by_name['constant_fee'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), dict(
  DESCRIPTOR = _GENESISSTATE,
  __module__ = 'cosmos.crisis.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crisis.v1beta1.GenesisState)
  ))
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z+github.com/cosmos/cosmos-sdk/x/crisis/types'))
_GENESISSTATE.fields_by_name['constant_fee'].has_options = True
_GENESISSTATE.fields_by_name['constant_fee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)