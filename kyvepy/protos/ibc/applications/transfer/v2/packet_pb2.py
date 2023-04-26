# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v2/packet.proto

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
  name='ibc/applications/transfer/v2/packet.proto',
  package='ibc.applications.transfer.v2',
  syntax='proto3',
  serialized_pb=_b('\n)ibc/applications/transfer/v2/packet.proto\x12\x1cibc.applications.transfer.v2\"h\n\x17\x46ungibleTokenPacketData\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x10\n\x08receiver\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\tB9Z7github.com/cosmos/ibc-go/v6/modules/apps/transfer/typesb\x06proto3')
)




_FUNGIBLETOKENPACKETDATA = _descriptor.Descriptor(
  name='FungibleTokenPacketData',
  full_name='ibc.applications.transfer.v2.FungibleTokenPacketData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom', full_name='ibc.applications.transfer.v2.FungibleTokenPacketData.denom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ibc.applications.transfer.v2.FungibleTokenPacketData.amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender', full_name='ibc.applications.transfer.v2.FungibleTokenPacketData.sender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='ibc.applications.transfer.v2.FungibleTokenPacketData.receiver', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='ibc.applications.transfer.v2.FungibleTokenPacketData.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=75,
  serialized_end=179,
)

DESCRIPTOR.message_types_by_name['FungibleTokenPacketData'] = _FUNGIBLETOKENPACKETDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FungibleTokenPacketData = _reflection.GeneratedProtocolMessageType('FungibleTokenPacketData', (_message.Message,), dict(
  DESCRIPTOR = _FUNGIBLETOKENPACKETDATA,
  __module__ = 'ibc.applications.transfer.v2.packet_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v2.FungibleTokenPacketData)
  ))
_sym_db.RegisterMessage(FungibleTokenPacketData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z7github.com/cosmos/ibc-go/v6/modules/apps/transfer/types'))
# @@protoc_insertion_point(module_scope)
