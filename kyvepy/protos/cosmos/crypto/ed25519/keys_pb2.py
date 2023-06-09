# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/ed25519/keys.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/crypto/ed25519/keys.proto',
  package='cosmos.crypto.ed25519',
  syntax='proto3',
  serialized_pb=_b('\n cosmos/crypto/ed25519/keys.proto\x12\x15\x63osmos.crypto.ed25519\x1a\x14gogoproto/gogo.proto\"9\n\x06PubKey\x12)\n\x03key\x18\x01 \x01(\x0c\x42\x1c\xfa\xde\x1f\x18\x63rypto/ed25519.PublicKey:\x04\x98\xa0\x1f\x00\"5\n\x07PrivKey\x12*\n\x03key\x18\x01 \x01(\x0c\x42\x1d\xfa\xde\x1f\x19\x63rypto/ed25519.PrivateKeyB2Z0github.com/cosmos/cosmos-sdk/crypto/keys/ed25519b\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PUBKEY = _descriptor.Descriptor(
  name='PubKey',
  full_name='cosmos.crypto.ed25519.PubKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cosmos.crypto.ed25519.PubKey.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\336\037\030crypto/ed25519.PublicKey')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=138,
)


_PRIVKEY = _descriptor.Descriptor(
  name='PrivKey',
  full_name='cosmos.crypto.ed25519.PrivKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cosmos.crypto.ed25519.PrivKey.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\336\037\031crypto/ed25519.PrivateKey')), file=DESCRIPTOR),
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
  serialized_start=140,
  serialized_end=193,
)

DESCRIPTOR.message_types_by_name['PubKey'] = _PUBKEY
DESCRIPTOR.message_types_by_name['PrivKey'] = _PRIVKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PubKey = _reflection.GeneratedProtocolMessageType('PubKey', (_message.Message,), dict(
  DESCRIPTOR = _PUBKEY,
  __module__ = 'cosmos.crypto.ed25519.keys_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crypto.ed25519.PubKey)
  ))
_sym_db.RegisterMessage(PubKey)

PrivKey = _reflection.GeneratedProtocolMessageType('PrivKey', (_message.Message,), dict(
  DESCRIPTOR = _PRIVKEY,
  __module__ = 'cosmos.crypto.ed25519.keys_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crypto.ed25519.PrivKey)
  ))
_sym_db.RegisterMessage(PrivKey)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z0github.com/cosmos/cosmos-sdk/crypto/keys/ed25519'))
_PUBKEY.fields_by_name['key'].has_options = True
_PUBKEY.fields_by_name['key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\336\037\030crypto/ed25519.PublicKey'))
_PUBKEY.has_options = True
_PUBKEY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000'))
_PRIVKEY.fields_by_name['key'].has_options = True
_PRIVKEY.fields_by_name['key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\336\037\031crypto/ed25519.PrivateKey'))
# @@protoc_insertion_point(module_scope)
