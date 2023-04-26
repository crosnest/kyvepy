# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/pool/v1beta1/tx.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kyve/pool/v1beta1/tx.proto',
  package='kyve.pool.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\x1akyve/pool/v1beta1/tx.proto\x12\x11kyve.pool.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\":\n\x0bMsgFundPool\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\"\x15\n\x13MsgFundPoolResponse\"<\n\rMsgDefundPool\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\"\x17\n\x15MsgDefundPoolResponse\"\xc6\x02\n\rMsgCreatePool\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07runtime\x18\x03 \x01(\t\x12\x0c\n\x04logo\x18\x04 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x05 \x01(\t\x12\x11\n\tstart_key\x18\x06 \x01(\t\x12\x17\n\x0fupload_interval\x18\x07 \x01(\x04\x12\x16\n\x0eoperating_cost\x18\x08 \x01(\x04\x12\x16\n\x0emin_delegation\x18\t \x01(\x04\x12\x17\n\x0fmax_bundle_size\x18\n \x01(\x04\x12\x0f\n\x07version\x18\x0b \x01(\t\x12\x10\n\x08\x62inaries\x18\x0c \x01(\t\x12\x1b\n\x13storage_provider_id\x18\r \x01(\r\x12\x16\n\x0e\x63ompression_id\x18\x0e \x01(\r\"\x17\n\x15MsgCreatePoolResponse\"Y\n\rMsgUpdatePool\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0f\n\x07payload\x18\x03 \x01(\t\"\x17\n\x15MsgUpdatePoolResponse\"I\n\x0eMsgDisablePool\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\n\n\x02id\x18\x02 \x01(\x04\"\x18\n\x16MsgDisablePoolResponse\"H\n\rMsgEnablePool\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\n\n\x02id\x18\x02 \x01(\x04\"\x17\n\x15MsgEnablePoolResponse\"\xa4\x01\n\x19MsgScheduleRuntimeUpgrade\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0f\n\x07runtime\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x14\n\x0cscheduled_at\x18\x04 \x01(\x04\x12\x10\n\x08\x64uration\x18\x05 \x01(\x04\x12\x10\n\x08\x62inaries\x18\x06 \x01(\t\"#\n!MsgScheduleRuntimeUpgradeResponse\"W\n\x17MsgCancelRuntimeUpgrade\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0f\n\x07runtime\x18\x02 \x01(\t\"!\n\x1fMsgCancelRuntimeUpgradeResponse2\x94\x06\n\x03Msg\x12R\n\x08\x46undPool\x12\x1e.kyve.pool.v1beta1.MsgFundPool\x1a&.kyve.pool.v1beta1.MsgFundPoolResponse\x12X\n\nDefundPool\x12 .kyve.pool.v1beta1.MsgDefundPool\x1a(.kyve.pool.v1beta1.MsgDefundPoolResponse\x12X\n\nCreatePool\x12 .kyve.pool.v1beta1.MsgCreatePool\x1a(.kyve.pool.v1beta1.MsgCreatePoolResponse\x12X\n\nUpdatePool\x12 .kyve.pool.v1beta1.MsgUpdatePool\x1a(.kyve.pool.v1beta1.MsgUpdatePoolResponse\x12[\n\x0b\x44isablePool\x12!.kyve.pool.v1beta1.MsgDisablePool\x1a).kyve.pool.v1beta1.MsgDisablePoolResponse\x12X\n\nEnablePool\x12 .kyve.pool.v1beta1.MsgEnablePool\x1a(.kyve.pool.v1beta1.MsgEnablePoolResponse\x12|\n\x16ScheduleRuntimeUpgrade\x12,.kyve.pool.v1beta1.MsgScheduleRuntimeUpgrade\x1a\x34.kyve.pool.v1beta1.MsgScheduleRuntimeUpgradeResponse\x12v\n\x14\x43\x61ncelRuntimeUpgrade\x12*.kyve.pool.v1beta1.MsgCancelRuntimeUpgrade\x1a\x32.kyve.pool.v1beta1.MsgCancelRuntimeUpgradeResponseB+Z)github.com/KYVENetwork/chain/x/pool/typesb\x06proto3')
  ,
  dependencies=[cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_MSGFUNDPOOL = _descriptor.Descriptor(
  name='MsgFundPool',
  full_name='kyve.pool.v1beta1.MsgFundPool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creator', full_name='kyve.pool.v1beta1.MsgFundPool.creator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.pool.v1beta1.MsgFundPool.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.pool.v1beta1.MsgFundPool.amount', index=2,
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
  serialized_start=76,
  serialized_end=134,
)


_MSGFUNDPOOLRESPONSE = _descriptor.Descriptor(
  name='MsgFundPoolResponse',
  full_name='kyve.pool.v1beta1.MsgFundPoolResponse',
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
  serialized_start=136,
  serialized_end=157,
)


_MSGDEFUNDPOOL = _descriptor.Descriptor(
  name='MsgDefundPool',
  full_name='kyve.pool.v1beta1.MsgDefundPool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creator', full_name='kyve.pool.v1beta1.MsgDefundPool.creator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.pool.v1beta1.MsgDefundPool.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.pool.v1beta1.MsgDefundPool.amount', index=2,
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
  serialized_start=159,
  serialized_end=219,
)


_MSGDEFUNDPOOLRESPONSE = _descriptor.Descriptor(
  name='MsgDefundPoolResponse',
  full_name='kyve.pool.v1beta1.MsgDefundPoolResponse',
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
  serialized_start=221,
  serialized_end=244,
)


_MSGCREATEPOOL = _descriptor.Descriptor(
  name='MsgCreatePool',
  full_name='kyve.pool.v1beta1.MsgCreatePool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.pool.v1beta1.MsgCreatePool.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='kyve.pool.v1beta1.MsgCreatePool.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='kyve.pool.v1beta1.MsgCreatePool.runtime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logo', full_name='kyve.pool.v1beta1.MsgCreatePool.logo', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='kyve.pool.v1beta1.MsgCreatePool.config', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_key', full_name='kyve.pool.v1beta1.MsgCreatePool.start_key', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_interval', full_name='kyve.pool.v1beta1.MsgCreatePool.upload_interval', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operating_cost', full_name='kyve.pool.v1beta1.MsgCreatePool.operating_cost', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_delegation', full_name='kyve.pool.v1beta1.MsgCreatePool.min_delegation', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_bundle_size', full_name='kyve.pool.v1beta1.MsgCreatePool.max_bundle_size', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kyve.pool.v1beta1.MsgCreatePool.version', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binaries', full_name='kyve.pool.v1beta1.MsgCreatePool.binaries', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_provider_id', full_name='kyve.pool.v1beta1.MsgCreatePool.storage_provider_id', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compression_id', full_name='kyve.pool.v1beta1.MsgCreatePool.compression_id', index=13,
      number=14, type=13, cpp_type=3, label=1,
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
  serialized_start=247,
  serialized_end=573,
)


_MSGCREATEPOOLRESPONSE = _descriptor.Descriptor(
  name='MsgCreatePoolResponse',
  full_name='kyve.pool.v1beta1.MsgCreatePoolResponse',
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
  serialized_start=575,
  serialized_end=598,
)


_MSGUPDATEPOOL = _descriptor.Descriptor(
  name='MsgUpdatePool',
  full_name='kyve.pool.v1beta1.MsgUpdatePool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.pool.v1beta1.MsgUpdatePool.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.pool.v1beta1.MsgUpdatePool.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='kyve.pool.v1beta1.MsgUpdatePool.payload', index=2,
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
  serialized_start=600,
  serialized_end=689,
)


_MSGUPDATEPOOLRESPONSE = _descriptor.Descriptor(
  name='MsgUpdatePoolResponse',
  full_name='kyve.pool.v1beta1.MsgUpdatePoolResponse',
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
  serialized_start=691,
  serialized_end=714,
)


_MSGDISABLEPOOL = _descriptor.Descriptor(
  name='MsgDisablePool',
  full_name='kyve.pool.v1beta1.MsgDisablePool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.pool.v1beta1.MsgDisablePool.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.pool.v1beta1.MsgDisablePool.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=716,
  serialized_end=789,
)


_MSGDISABLEPOOLRESPONSE = _descriptor.Descriptor(
  name='MsgDisablePoolResponse',
  full_name='kyve.pool.v1beta1.MsgDisablePoolResponse',
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
  serialized_start=791,
  serialized_end=815,
)


_MSGENABLEPOOL = _descriptor.Descriptor(
  name='MsgEnablePool',
  full_name='kyve.pool.v1beta1.MsgEnablePool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.pool.v1beta1.MsgEnablePool.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.pool.v1beta1.MsgEnablePool.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=817,
  serialized_end=889,
)


_MSGENABLEPOOLRESPONSE = _descriptor.Descriptor(
  name='MsgEnablePoolResponse',
  full_name='kyve.pool.v1beta1.MsgEnablePoolResponse',
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
  serialized_start=891,
  serialized_end=914,
)


_MSGSCHEDULERUNTIMEUPGRADE = _descriptor.Descriptor(
  name='MsgScheduleRuntimeUpgrade',
  full_name='kyve.pool.v1beta1.MsgScheduleRuntimeUpgrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.pool.v1beta1.MsgScheduleRuntimeUpgrade.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='kyve.pool.v1beta1.MsgScheduleRuntimeUpgrade.runtime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kyve.pool.v1beta1.MsgScheduleRuntimeUpgrade.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheduled_at', full_name='kyve.pool.v1beta1.MsgScheduleRuntimeUpgrade.scheduled_at', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='kyve.pool.v1beta1.MsgScheduleRuntimeUpgrade.duration', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binaries', full_name='kyve.pool.v1beta1.MsgScheduleRuntimeUpgrade.binaries', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=917,
  serialized_end=1081,
)


_MSGSCHEDULERUNTIMEUPGRADERESPONSE = _descriptor.Descriptor(
  name='MsgScheduleRuntimeUpgradeResponse',
  full_name='kyve.pool.v1beta1.MsgScheduleRuntimeUpgradeResponse',
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
  serialized_start=1083,
  serialized_end=1118,
)


_MSGCANCELRUNTIMEUPGRADE = _descriptor.Descriptor(
  name='MsgCancelRuntimeUpgrade',
  full_name='kyve.pool.v1beta1.MsgCancelRuntimeUpgrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='kyve.pool.v1beta1.MsgCancelRuntimeUpgrade.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='kyve.pool.v1beta1.MsgCancelRuntimeUpgrade.runtime', index=1,
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
  serialized_start=1120,
  serialized_end=1207,
)


_MSGCANCELRUNTIMEUPGRADERESPONSE = _descriptor.Descriptor(
  name='MsgCancelRuntimeUpgradeResponse',
  full_name='kyve.pool.v1beta1.MsgCancelRuntimeUpgradeResponse',
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
  serialized_start=1209,
  serialized_end=1242,
)

DESCRIPTOR.message_types_by_name['MsgFundPool'] = _MSGFUNDPOOL
DESCRIPTOR.message_types_by_name['MsgFundPoolResponse'] = _MSGFUNDPOOLRESPONSE
DESCRIPTOR.message_types_by_name['MsgDefundPool'] = _MSGDEFUNDPOOL
DESCRIPTOR.message_types_by_name['MsgDefundPoolResponse'] = _MSGDEFUNDPOOLRESPONSE
DESCRIPTOR.message_types_by_name['MsgCreatePool'] = _MSGCREATEPOOL
DESCRIPTOR.message_types_by_name['MsgCreatePoolResponse'] = _MSGCREATEPOOLRESPONSE
DESCRIPTOR.message_types_by_name['MsgUpdatePool'] = _MSGUPDATEPOOL
DESCRIPTOR.message_types_by_name['MsgUpdatePoolResponse'] = _MSGUPDATEPOOLRESPONSE
DESCRIPTOR.message_types_by_name['MsgDisablePool'] = _MSGDISABLEPOOL
DESCRIPTOR.message_types_by_name['MsgDisablePoolResponse'] = _MSGDISABLEPOOLRESPONSE
DESCRIPTOR.message_types_by_name['MsgEnablePool'] = _MSGENABLEPOOL
DESCRIPTOR.message_types_by_name['MsgEnablePoolResponse'] = _MSGENABLEPOOLRESPONSE
DESCRIPTOR.message_types_by_name['MsgScheduleRuntimeUpgrade'] = _MSGSCHEDULERUNTIMEUPGRADE
DESCRIPTOR.message_types_by_name['MsgScheduleRuntimeUpgradeResponse'] = _MSGSCHEDULERUNTIMEUPGRADERESPONSE
DESCRIPTOR.message_types_by_name['MsgCancelRuntimeUpgrade'] = _MSGCANCELRUNTIMEUPGRADE
DESCRIPTOR.message_types_by_name['MsgCancelRuntimeUpgradeResponse'] = _MSGCANCELRUNTIMEUPGRADERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgFundPool = _reflection.GeneratedProtocolMessageType('MsgFundPool', (_message.Message,), dict(
  DESCRIPTOR = _MSGFUNDPOOL,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgFundPool)
  ))
_sym_db.RegisterMessage(MsgFundPool)

MsgFundPoolResponse = _reflection.GeneratedProtocolMessageType('MsgFundPoolResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGFUNDPOOLRESPONSE,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgFundPoolResponse)
  ))
_sym_db.RegisterMessage(MsgFundPoolResponse)

MsgDefundPool = _reflection.GeneratedProtocolMessageType('MsgDefundPool', (_message.Message,), dict(
  DESCRIPTOR = _MSGDEFUNDPOOL,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgDefundPool)
  ))
_sym_db.RegisterMessage(MsgDefundPool)

MsgDefundPoolResponse = _reflection.GeneratedProtocolMessageType('MsgDefundPoolResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGDEFUNDPOOLRESPONSE,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgDefundPoolResponse)
  ))
_sym_db.RegisterMessage(MsgDefundPoolResponse)

MsgCreatePool = _reflection.GeneratedProtocolMessageType('MsgCreatePool', (_message.Message,), dict(
  DESCRIPTOR = _MSGCREATEPOOL,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgCreatePool)
  ))
_sym_db.RegisterMessage(MsgCreatePool)

MsgCreatePoolResponse = _reflection.GeneratedProtocolMessageType('MsgCreatePoolResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGCREATEPOOLRESPONSE,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgCreatePoolResponse)
  ))
_sym_db.RegisterMessage(MsgCreatePoolResponse)

MsgUpdatePool = _reflection.GeneratedProtocolMessageType('MsgUpdatePool', (_message.Message,), dict(
  DESCRIPTOR = _MSGUPDATEPOOL,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgUpdatePool)
  ))
_sym_db.RegisterMessage(MsgUpdatePool)

MsgUpdatePoolResponse = _reflection.GeneratedProtocolMessageType('MsgUpdatePoolResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGUPDATEPOOLRESPONSE,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgUpdatePoolResponse)
  ))
_sym_db.RegisterMessage(MsgUpdatePoolResponse)

MsgDisablePool = _reflection.GeneratedProtocolMessageType('MsgDisablePool', (_message.Message,), dict(
  DESCRIPTOR = _MSGDISABLEPOOL,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgDisablePool)
  ))
_sym_db.RegisterMessage(MsgDisablePool)

MsgDisablePoolResponse = _reflection.GeneratedProtocolMessageType('MsgDisablePoolResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGDISABLEPOOLRESPONSE,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgDisablePoolResponse)
  ))
_sym_db.RegisterMessage(MsgDisablePoolResponse)

MsgEnablePool = _reflection.GeneratedProtocolMessageType('MsgEnablePool', (_message.Message,), dict(
  DESCRIPTOR = _MSGENABLEPOOL,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgEnablePool)
  ))
_sym_db.RegisterMessage(MsgEnablePool)

MsgEnablePoolResponse = _reflection.GeneratedProtocolMessageType('MsgEnablePoolResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGENABLEPOOLRESPONSE,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgEnablePoolResponse)
  ))
_sym_db.RegisterMessage(MsgEnablePoolResponse)

MsgScheduleRuntimeUpgrade = _reflection.GeneratedProtocolMessageType('MsgScheduleRuntimeUpgrade', (_message.Message,), dict(
  DESCRIPTOR = _MSGSCHEDULERUNTIMEUPGRADE,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgScheduleRuntimeUpgrade)
  ))
_sym_db.RegisterMessage(MsgScheduleRuntimeUpgrade)

MsgScheduleRuntimeUpgradeResponse = _reflection.GeneratedProtocolMessageType('MsgScheduleRuntimeUpgradeResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGSCHEDULERUNTIMEUPGRADERESPONSE,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgScheduleRuntimeUpgradeResponse)
  ))
_sym_db.RegisterMessage(MsgScheduleRuntimeUpgradeResponse)

MsgCancelRuntimeUpgrade = _reflection.GeneratedProtocolMessageType('MsgCancelRuntimeUpgrade', (_message.Message,), dict(
  DESCRIPTOR = _MSGCANCELRUNTIMEUPGRADE,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgCancelRuntimeUpgrade)
  ))
_sym_db.RegisterMessage(MsgCancelRuntimeUpgrade)

MsgCancelRuntimeUpgradeResponse = _reflection.GeneratedProtocolMessageType('MsgCancelRuntimeUpgradeResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGCANCELRUNTIMEUPGRADERESPONSE,
  __module__ = 'kyve.pool.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.MsgCancelRuntimeUpgradeResponse)
  ))
_sym_db.RegisterMessage(MsgCancelRuntimeUpgradeResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/KYVENetwork/chain/x/pool/types'))
_MSGCREATEPOOL.fields_by_name['authority'].has_options = True
_MSGCREATEPOOL.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGUPDATEPOOL.fields_by_name['authority'].has_options = True
_MSGUPDATEPOOL.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGDISABLEPOOL.fields_by_name['authority'].has_options = True
_MSGDISABLEPOOL.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGENABLEPOOL.fields_by_name['authority'].has_options = True
_MSGENABLEPOOL.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGSCHEDULERUNTIMEUPGRADE.fields_by_name['authority'].has_options = True
_MSGSCHEDULERUNTIMEUPGRADE.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGCANCELRUNTIMEUPGRADE.fields_by_name['authority'].has_options = True
_MSGCANCELRUNTIMEUPGRADE.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='kyve.pool.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1245,
  serialized_end=2033,
  methods=[
  _descriptor.MethodDescriptor(
    name='FundPool',
    full_name='kyve.pool.v1beta1.Msg.FundPool',
    index=0,
    containing_service=None,
    input_type=_MSGFUNDPOOL,
    output_type=_MSGFUNDPOOLRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DefundPool',
    full_name='kyve.pool.v1beta1.Msg.DefundPool',
    index=1,
    containing_service=None,
    input_type=_MSGDEFUNDPOOL,
    output_type=_MSGDEFUNDPOOLRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreatePool',
    full_name='kyve.pool.v1beta1.Msg.CreatePool',
    index=2,
    containing_service=None,
    input_type=_MSGCREATEPOOL,
    output_type=_MSGCREATEPOOLRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdatePool',
    full_name='kyve.pool.v1beta1.Msg.UpdatePool',
    index=3,
    containing_service=None,
    input_type=_MSGUPDATEPOOL,
    output_type=_MSGUPDATEPOOLRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DisablePool',
    full_name='kyve.pool.v1beta1.Msg.DisablePool',
    index=4,
    containing_service=None,
    input_type=_MSGDISABLEPOOL,
    output_type=_MSGDISABLEPOOLRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EnablePool',
    full_name='kyve.pool.v1beta1.Msg.EnablePool',
    index=5,
    containing_service=None,
    input_type=_MSGENABLEPOOL,
    output_type=_MSGENABLEPOOLRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ScheduleRuntimeUpgrade',
    full_name='kyve.pool.v1beta1.Msg.ScheduleRuntimeUpgrade',
    index=6,
    containing_service=None,
    input_type=_MSGSCHEDULERUNTIMEUPGRADE,
    output_type=_MSGSCHEDULERUNTIMEUPGRADERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CancelRuntimeUpgrade',
    full_name='kyve.pool.v1beta1.Msg.CancelRuntimeUpgrade',
    index=7,
    containing_service=None,
    input_type=_MSGCANCELRUNTIMEUPGRADE,
    output_type=_MSGCANCELRUNTIMEUPGRADERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
