# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/tendermint/v1beta1/types.proto

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
from tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from tendermint.types import evidence_pb2 as tendermint_dot_types_dot_evidence__pb2
from tendermint.version import types_pb2 as tendermint_dot_version_dot_types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/base/tendermint/v1beta1/types.proto',
  package='cosmos.base.tendermint.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n*cosmos/base/tendermint/v1beta1/types.proto\x12\x1e\x63osmos.base.tendermint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ctendermint/types/types.proto\x1a\x1ftendermint/types/evidence.proto\x1a\x1etendermint/version/types.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd8\x01\n\x05\x42lock\x12<\n\x06header\x18\x01 \x01(\x0b\x32&.cosmos.base.tendermint.v1beta1.HeaderB\x04\xc8\xde\x1f\x00\x12*\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x16.tendermint.types.DataB\x04\xc8\xde\x1f\x00\x12\x36\n\x08\x65vidence\x18\x03 \x01(\x0b\x32\x1e.tendermint.types.EvidenceListB\x04\xc8\xde\x1f\x00\x12-\n\x0blast_commit\x18\x04 \x01(\x0b\x32\x18.tendermint.types.Commit\"\xb3\x03\n\x06Header\x12\x34\n\x07version\x18\x01 \x01(\x0b\x32\x1d.tendermint.version.ConsensusB\x04\xc8\xde\x1f\x00\x12\x1d\n\x08\x63hain_id\x18\x02 \x01(\tB\x0b\xe2\xde\x1f\x07\x43hainID\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\x32\n\x04time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x36\n\rlast_block_id\x18\x05 \x01(\x0b\x32\x19.tendermint.types.BlockIDB\x04\xc8\xde\x1f\x00\x12\x18\n\x10last_commit_hash\x18\x06 \x01(\x0c\x12\x11\n\tdata_hash\x18\x07 \x01(\x0c\x12\x17\n\x0fvalidators_hash\x18\x08 \x01(\x0c\x12\x1c\n\x14next_validators_hash\x18\t \x01(\x0c\x12\x16\n\x0e\x63onsensus_hash\x18\n \x01(\x0c\x12\x10\n\x08\x61pp_hash\x18\x0b \x01(\x0c\x12\x19\n\x11last_results_hash\x18\x0c \x01(\x0c\x12\x15\n\revidence_hash\x18\r \x01(\x0c\x12\x18\n\x10proposer_address\x18\x0e \x01(\tB4Z2github.com/cosmos/cosmos-sdk/client/grpc/tmserviceb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,tendermint_dot_types_dot_types__pb2.DESCRIPTOR,tendermint_dot_types_dot_evidence__pb2.DESCRIPTOR,tendermint_dot_version_dot_types__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='cosmos.base.tendermint.v1beta1.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='cosmos.base.tendermint.v1beta1.Block.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cosmos.base.tendermint.v1beta1.Block.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evidence', full_name='cosmos.base.tendermint.v1beta1.Block.evidence', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_commit', full_name='cosmos.base.tendermint.v1beta1.Block.last_commit', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=229,
  serialized_end=445,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='cosmos.base.tendermint.v1beta1.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='cosmos.base.tendermint.v1beta1.Header.version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='cosmos.base.tendermint.v1beta1.Header.chain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\007ChainID')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='cosmos.base.tendermint.v1beta1.Header.height', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='cosmos.base.tendermint.v1beta1.Header.time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\220\337\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_block_id', full_name='cosmos.base.tendermint.v1beta1.Header.last_block_id', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_commit_hash', full_name='cosmos.base.tendermint.v1beta1.Header.last_commit_hash', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_hash', full_name='cosmos.base.tendermint.v1beta1.Header.data_hash', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validators_hash', full_name='cosmos.base.tendermint.v1beta1.Header.validators_hash', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_validators_hash', full_name='cosmos.base.tendermint.v1beta1.Header.next_validators_hash', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consensus_hash', full_name='cosmos.base.tendermint.v1beta1.Header.consensus_hash', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_hash', full_name='cosmos.base.tendermint.v1beta1.Header.app_hash', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_results_hash', full_name='cosmos.base.tendermint.v1beta1.Header.last_results_hash', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evidence_hash', full_name='cosmos.base.tendermint.v1beta1.Header.evidence_hash', index=12,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposer_address', full_name='cosmos.base.tendermint.v1beta1.Header.proposer_address', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_start=448,
  serialized_end=883,
)

_BLOCK.fields_by_name['header'].message_type = _HEADER
_BLOCK.fields_by_name['data'].message_type = tendermint_dot_types_dot_types__pb2._DATA
_BLOCK.fields_by_name['evidence'].message_type = tendermint_dot_types_dot_evidence__pb2._EVIDENCELIST
_BLOCK.fields_by_name['last_commit'].message_type = tendermint_dot_types_dot_types__pb2._COMMIT
_HEADER.fields_by_name['version'].message_type = tendermint_dot_version_dot_types__pb2._CONSENSUS
_HEADER.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HEADER.fields_by_name['last_block_id'].message_type = tendermint_dot_types_dot_types__pb2._BLOCKID
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'cosmos.base.tendermint.v1beta1.types_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.Block)
  ))
_sym_db.RegisterMessage(Block)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'cosmos.base.tendermint.v1beta1.types_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.Header)
  ))
_sym_db.RegisterMessage(Header)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z2github.com/cosmos/cosmos-sdk/client/grpc/tmservice'))
_BLOCK.fields_by_name['header'].has_options = True
_BLOCK.fields_by_name['header']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_BLOCK.fields_by_name['data'].has_options = True
_BLOCK.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_BLOCK.fields_by_name['evidence'].has_options = True
_BLOCK.fields_by_name['evidence']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_HEADER.fields_by_name['version'].has_options = True
_HEADER.fields_by_name['version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_HEADER.fields_by_name['chain_id'].has_options = True
_HEADER.fields_by_name['chain_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\007ChainID'))
_HEADER.fields_by_name['time'].has_options = True
_HEADER.fields_by_name['time']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\220\337\037\001'))
_HEADER.fields_by_name['last_block_id'].has_options = True
_HEADER.fields_by_name['last_block_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
