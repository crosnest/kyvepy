# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/pool/v1beta1/genesis.proto

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
from kyve.pool.v1beta1 import pool_pb2 as kyve_dot_pool_dot_v1beta1_dot_pool__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/pool/v1beta1/genesis.proto',
  package='kyve.pool.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\x1fkyve/pool/v1beta1/genesis.proto\x12\x11kyve.pool.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ckyve/pool/v1beta1/pool.proto\"b\n\x0cGenesisState\x12\x30\n\tpool_list\x18\x02 \x03(\x0b\x32\x17.kyve.pool.v1beta1.PoolB\x04\xc8\xde\x1f\x00\x12\x12\n\npool_count\x18\x03 \x01(\x04J\x04\x08\x01\x10\x02R\x06paramsB+Z)github.com/KYVENetwork/chain/x/pool/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,kyve_dot_pool_dot_v1beta1_dot_pool__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='kyve.pool.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pool_list', full_name='kyve.pool.v1beta1.GenesisState.pool_list', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pool_count', full_name='kyve.pool.v1beta1.GenesisState.pool_count', index=1,
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
  serialized_start=106,
  serialized_end=204,
)

_GENESISSTATE.fields_by_name['pool_list'].message_type = kyve_dot_pool_dot_v1beta1_dot_pool__pb2._POOL
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), dict(
  DESCRIPTOR = _GENESISSTATE,
  __module__ = 'kyve.pool.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.GenesisState)
  ))
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/KYVENetwork/chain/x/pool/types'))
_GENESISSTATE.fields_by_name['pool_list'].has_options = True
_GENESISSTATE.fields_by_name['pool_list']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
