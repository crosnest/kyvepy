# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/evidence/v1beta1/evidence.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cosmos/evidence/v1beta1/evidence.proto\x12\x17\x63osmos.evidence.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xa4\x01\n\x0c\x45quivocation\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x32\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\r\n\x05power\x18\x03 \x01(\x03\x12\x33\n\x11\x63onsensus_address\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x0c\x98\xa0\x1f\x00\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x42\x33Z-github.com/cosmos/cosmos-sdk/x/evidence/types\xa8\xe2\x1e\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.evidence.v1beta1.evidence_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/evidence/types\250\342\036\001'
  _EQUIVOCATION.fields_by_name['time']._options = None
  _EQUIVOCATION.fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _EQUIVOCATION.fields_by_name['consensus_address']._options = None
  _EQUIVOCATION.fields_by_name['consensus_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _EQUIVOCATION._options = None
  _EQUIVOCATION._serialized_options = b'\230\240\037\000\210\240\037\000\350\240\037\000'
  _EQUIVOCATION._serialized_start=150
  _EQUIVOCATION._serialized_end=314
# @@protoc_insertion_point(module_scope)