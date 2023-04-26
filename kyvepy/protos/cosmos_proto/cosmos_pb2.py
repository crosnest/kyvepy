# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos_proto/cosmos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos_proto/cosmos.proto',
  package='cosmos_proto',
  syntax='proto3',
  serialized_pb=_b('\n\x19\x63osmos_proto/cosmos.proto\x12\x0c\x63osmos_proto\x1a google/protobuf/descriptor.proto\"8\n\x13InterfaceDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x82\x01\n\x10ScalarDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12,\n\nfield_type\x18\x03 \x03(\x0e\x32\x18.cosmos_proto.ScalarType\x12\x1d\n\x15legacy_amino_encoding\x18\x04 \x01(\t*X\n\nScalarType\x12\x1b\n\x17SCALAR_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12SCALAR_TYPE_STRING\x10\x01\x12\x15\n\x11SCALAR_TYPE_BYTES\x10\x02:?\n\x14implements_interface\x12\x1f.google.protobuf.MessageOptions\x18\xc9\xd6\x05 \x03(\t::\n\x11\x61\x63\x63\x65pts_interface\x12\x1d.google.protobuf.FieldOptions\x18\xc9\xd6\x05 \x01(\t:/\n\x06scalar\x12\x1d.google.protobuf.FieldOptions\x18\xca\xd6\x05 \x01(\t:\\\n\x11\x64\x65\x63lare_interface\x12\x1c.google.protobuf.FileOptions\x18\xbd\xb3\x30 \x03(\x0b\x32!.cosmos_proto.InterfaceDescriptor:V\n\x0e\x64\x65\x63lare_scalar\x12\x1c.google.protobuf.FileOptions\x18\xbe\xb3\x30 \x03(\x0b\x32\x1e.cosmos_proto.ScalarDescriptorB-Z+github.com/cosmos/cosmos-proto;cosmos_protob\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_SCALARTYPE = _descriptor.EnumDescriptor(
  name='ScalarType',
  full_name='cosmos_proto.ScalarType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_STRING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_BYTES', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=268,
  serialized_end=356,
)
_sym_db.RegisterEnumDescriptor(_SCALARTYPE)

ScalarType = enum_type_wrapper.EnumTypeWrapper(_SCALARTYPE)
SCALAR_TYPE_UNSPECIFIED = 0
SCALAR_TYPE_STRING = 1
SCALAR_TYPE_BYTES = 2

IMPLEMENTS_INTERFACE_FIELD_NUMBER = 93001
implements_interface = _descriptor.FieldDescriptor(
  name='implements_interface', full_name='cosmos_proto.implements_interface', index=0,
  number=93001, type=9, cpp_type=9, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
ACCEPTS_INTERFACE_FIELD_NUMBER = 93001
accepts_interface = _descriptor.FieldDescriptor(
  name='accepts_interface', full_name='cosmos_proto.accepts_interface', index=1,
  number=93001, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
SCALAR_FIELD_NUMBER = 93002
scalar = _descriptor.FieldDescriptor(
  name='scalar', full_name='cosmos_proto.scalar', index=2,
  number=93002, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
DECLARE_INTERFACE_FIELD_NUMBER = 793021
declare_interface = _descriptor.FieldDescriptor(
  name='declare_interface', full_name='cosmos_proto.declare_interface', index=3,
  number=793021, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
DECLARE_SCALAR_FIELD_NUMBER = 793022
declare_scalar = _descriptor.FieldDescriptor(
  name='declare_scalar', full_name='cosmos_proto.declare_scalar', index=4,
  number=793022, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)


_INTERFACEDESCRIPTOR = _descriptor.Descriptor(
  name='InterfaceDescriptor',
  full_name='cosmos_proto.InterfaceDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cosmos_proto.InterfaceDescriptor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='cosmos_proto.InterfaceDescriptor.description', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=133,
)


_SCALARDESCRIPTOR = _descriptor.Descriptor(
  name='ScalarDescriptor',
  full_name='cosmos_proto.ScalarDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cosmos_proto.ScalarDescriptor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='cosmos_proto.ScalarDescriptor.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_type', full_name='cosmos_proto.ScalarDescriptor.field_type', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='legacy_amino_encoding', full_name='cosmos_proto.ScalarDescriptor.legacy_amino_encoding', index=3,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=266,
)

_SCALARDESCRIPTOR.fields_by_name['field_type'].enum_type = _SCALARTYPE
DESCRIPTOR.message_types_by_name['InterfaceDescriptor'] = _INTERFACEDESCRIPTOR
DESCRIPTOR.message_types_by_name['ScalarDescriptor'] = _SCALARDESCRIPTOR
DESCRIPTOR.enum_types_by_name['ScalarType'] = _SCALARTYPE
DESCRIPTOR.extensions_by_name['implements_interface'] = implements_interface
DESCRIPTOR.extensions_by_name['accepts_interface'] = accepts_interface
DESCRIPTOR.extensions_by_name['scalar'] = scalar
DESCRIPTOR.extensions_by_name['declare_interface'] = declare_interface
DESCRIPTOR.extensions_by_name['declare_scalar'] = declare_scalar
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InterfaceDescriptor = _reflection.GeneratedProtocolMessageType('InterfaceDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _INTERFACEDESCRIPTOR,
  __module__ = 'cosmos_proto.cosmos_pb2'
  # @@protoc_insertion_point(class_scope:cosmos_proto.InterfaceDescriptor)
  ))
_sym_db.RegisterMessage(InterfaceDescriptor)

ScalarDescriptor = _reflection.GeneratedProtocolMessageType('ScalarDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _SCALARDESCRIPTOR,
  __module__ = 'cosmos_proto.cosmos_pb2'
  # @@protoc_insertion_point(class_scope:cosmos_proto.ScalarDescriptor)
  ))
_sym_db.RegisterMessage(ScalarDescriptor)

google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(implements_interface)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(accepts_interface)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(scalar)
declare_interface.message_type = _INTERFACEDESCRIPTOR
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(declare_interface)
declare_scalar.message_type = _SCALARDESCRIPTOR
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(declare_scalar)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z+github.com/cosmos/cosmos-proto;cosmos_proto'))
# @@protoc_insertion_point(module_scope)
