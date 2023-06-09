# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crisis/v1beta1/tx.proto

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
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/crisis/v1beta1/tx.proto',
  package='cosmos.crisis.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\x1e\x63osmos/crisis/v1beta1/tx.proto\x12\x15\x63osmos.crisis.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\"\x8b\x01\n\x12MsgVerifyInvariant\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x1d\n\x15invariant_module_name\x18\x02 \x01(\t\x12\x17\n\x0finvariant_route\x18\x03 \x01(\t:\x13\x82\xe7\xb0*\x06sender\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1c\n\x1aMsgVerifyInvariantResponse2v\n\x03Msg\x12o\n\x0fVerifyInvariant\x12).cosmos.crisis.v1beta1.MsgVerifyInvariant\x1a\x31.cosmos.crisis.v1beta1.MsgVerifyInvariantResponseB-Z+github.com/cosmos/cosmos-sdk/x/crisis/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_msg_dot_v1_dot_msg__pb2.DESCRIPTOR,])




_MSGVERIFYINVARIANT = _descriptor.Descriptor(
  name='MsgVerifyInvariant',
  full_name='cosmos.crisis.v1beta1.MsgVerifyInvariant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='cosmos.crisis.v1beta1.MsgVerifyInvariant.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invariant_module_name', full_name='cosmos.crisis.v1beta1.MsgVerifyInvariant.invariant_module_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invariant_route', full_name='cosmos.crisis.v1beta1.MsgVerifyInvariant.invariant_route', index=2,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\006sender\350\240\037\000\210\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=271,
)


_MSGVERIFYINVARIANTRESPONSE = _descriptor.Descriptor(
  name='MsgVerifyInvariantResponse',
  full_name='cosmos.crisis.v1beta1.MsgVerifyInvariantResponse',
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
  serialized_start=273,
  serialized_end=301,
)

DESCRIPTOR.message_types_by_name['MsgVerifyInvariant'] = _MSGVERIFYINVARIANT
DESCRIPTOR.message_types_by_name['MsgVerifyInvariantResponse'] = _MSGVERIFYINVARIANTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgVerifyInvariant = _reflection.GeneratedProtocolMessageType('MsgVerifyInvariant', (_message.Message,), dict(
  DESCRIPTOR = _MSGVERIFYINVARIANT,
  __module__ = 'cosmos.crisis.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crisis.v1beta1.MsgVerifyInvariant)
  ))
_sym_db.RegisterMessage(MsgVerifyInvariant)

MsgVerifyInvariantResponse = _reflection.GeneratedProtocolMessageType('MsgVerifyInvariantResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGVERIFYINVARIANTRESPONSE,
  __module__ = 'cosmos.crisis.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crisis.v1beta1.MsgVerifyInvariantResponse)
  ))
_sym_db.RegisterMessage(MsgVerifyInvariantResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z+github.com/cosmos/cosmos-sdk/x/crisis/types'))
_MSGVERIFYINVARIANT.fields_by_name['sender'].has_options = True
_MSGVERIFYINVARIANT.fields_by_name['sender']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGVERIFYINVARIANT.has_options = True
_MSGVERIFYINVARIANT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\006sender\350\240\037\000\210\240\037\000'))

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='cosmos.crisis.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=303,
  serialized_end=421,
  methods=[
  _descriptor.MethodDescriptor(
    name='VerifyInvariant',
    full_name='cosmos.crisis.v1beta1.Msg.VerifyInvariant',
    index=0,
    containing_service=None,
    input_type=_MSGVERIFYINVARIANT,
    output_type=_MSGVERIFYINVARIANTRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
