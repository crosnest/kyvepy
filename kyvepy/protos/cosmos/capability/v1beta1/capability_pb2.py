# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/capability/v1beta1/capability.proto

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
  name='cosmos/capability/v1beta1/capability.proto',
  package='cosmos.capability.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n*cosmos/capability/v1beta1/capability.proto\x12\x19\x63osmos.capability.v1beta1\x1a\x14gogoproto/gogo.proto\"!\n\nCapability\x12\r\n\x05index\x18\x01 \x01(\x04:\x04\x98\xa0\x1f\x00\"/\n\x05Owner\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t:\x08\x98\xa0\x1f\x00\x88\xa0\x1f\x00\"J\n\x10\x43\x61pabilityOwners\x12\x36\n\x06owners\x18\x01 \x03(\x0b\x32 .cosmos.capability.v1beta1.OwnerB\x04\xc8\xde\x1f\x00\x42\x31Z/github.com/cosmos/cosmos-sdk/x/capability/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_CAPABILITY = _descriptor.Descriptor(
  name='Capability',
  full_name='cosmos.capability.v1beta1.Capability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='cosmos.capability.v1beta1.Capability.index', index=0,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=128,
)


_OWNER = _descriptor.Descriptor(
  name='Owner',
  full_name='cosmos.capability.v1beta1.Owner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='module', full_name='cosmos.capability.v1beta1.Owner.module', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cosmos.capability.v1beta1.Owner.name', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000\210\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=177,
)


_CAPABILITYOWNERS = _descriptor.Descriptor(
  name='CapabilityOwners',
  full_name='cosmos.capability.v1beta1.CapabilityOwners',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owners', full_name='cosmos.capability.v1beta1.CapabilityOwners.owners', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=253,
)

_CAPABILITYOWNERS.fields_by_name['owners'].message_type = _OWNER
DESCRIPTOR.message_types_by_name['Capability'] = _CAPABILITY
DESCRIPTOR.message_types_by_name['Owner'] = _OWNER
DESCRIPTOR.message_types_by_name['CapabilityOwners'] = _CAPABILITYOWNERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Capability = _reflection.GeneratedProtocolMessageType('Capability', (_message.Message,), dict(
  DESCRIPTOR = _CAPABILITY,
  __module__ = 'cosmos.capability.v1beta1.capability_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.capability.v1beta1.Capability)
  ))
_sym_db.RegisterMessage(Capability)

Owner = _reflection.GeneratedProtocolMessageType('Owner', (_message.Message,), dict(
  DESCRIPTOR = _OWNER,
  __module__ = 'cosmos.capability.v1beta1.capability_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.capability.v1beta1.Owner)
  ))
_sym_db.RegisterMessage(Owner)

CapabilityOwners = _reflection.GeneratedProtocolMessageType('CapabilityOwners', (_message.Message,), dict(
  DESCRIPTOR = _CAPABILITYOWNERS,
  __module__ = 'cosmos.capability.v1beta1.capability_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.capability.v1beta1.CapabilityOwners)
  ))
_sym_db.RegisterMessage(CapabilityOwners)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z/github.com/cosmos/cosmos-sdk/x/capability/types'))
_CAPABILITY.has_options = True
_CAPABILITY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000'))
_OWNER.has_options = True
_OWNER._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000\210\240\037\000'))
_CAPABILITYOWNERS.fields_by_name['owners'].has_options = True
_CAPABILITYOWNERS.fields_by_name['owners']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
