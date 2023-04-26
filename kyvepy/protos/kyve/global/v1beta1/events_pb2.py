# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/global/v1beta1/events.proto

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
import importlib
kyve_dot_global_dot_v1beta1_dot_global__pb2 = importlib.import_module('kyve.global.v1beta1.global_pb2')


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/global/v1beta1/events.proto',
  package='kyve.global.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n kyve/global/v1beta1/events.proto\x12\x13kyve.global.v1beta1\x1a\x14gogoproto/gogo.proto\x1a kyve/global/v1beta1/global.proto\"\x92\x01\n\x11\x45ventUpdateParams\x12\x35\n\nold_params\x18\x01 \x01(\x0b\x32\x1b.kyve.global.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12\x35\n\nnew_params\x18\x02 \x01(\x0b\x32\x1b.kyve.global.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12\x0f\n\x07payload\x18\x03 \x01(\tB-Z+github.com/KYVENetwork/chain/x/global/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,kyve_dot_global_dot_v1beta1_dot_global__pb2.DESCRIPTOR,])




_EVENTUPDATEPARAMS = _descriptor.Descriptor(
  name='EventUpdateParams',
  full_name='kyve.global.v1beta1.EventUpdateParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='old_params', full_name='kyve.global.v1beta1.EventUpdateParams.old_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_params', full_name='kyve.global.v1beta1.EventUpdateParams.new_params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='kyve.global.v1beta1.EventUpdateParams.payload', index=2,
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
  serialized_start=114,
  serialized_end=260,
)

_EVENTUPDATEPARAMS.fields_by_name['old_params'].message_type = kyve_dot_global_dot_v1beta1_dot_global__pb2._PARAMS
_EVENTUPDATEPARAMS.fields_by_name['new_params'].message_type = kyve_dot_global_dot_v1beta1_dot_global__pb2._PARAMS
DESCRIPTOR.message_types_by_name['EventUpdateParams'] = _EVENTUPDATEPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventUpdateParams = _reflection.GeneratedProtocolMessageType('EventUpdateParams', (_message.Message,), dict(
  DESCRIPTOR = _EVENTUPDATEPARAMS,
  __module__ = 'kyve.global.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.global.v1beta1.EventUpdateParams)
  ))
_sym_db.RegisterMessage(EventUpdateParams)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z+github.com/KYVENetwork/chain/x/global/types'))
_EVENTUPDATEPARAMS.fields_by_name['old_params'].has_options = True
_EVENTUPDATEPARAMS.fields_by_name['old_params']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_EVENTUPDATEPARAMS.fields_by_name['new_params'].has_options = True
_EVENTUPDATEPARAMS.fields_by_name['new_params']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)