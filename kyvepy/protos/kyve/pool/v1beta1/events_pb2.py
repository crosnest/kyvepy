# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kyve/pool/v1beta1/events.proto

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
  name='kyve/pool/v1beta1/events.proto',
  package='kyve.pool.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\x1ekyve/pool/v1beta1/events.proto\x12\x11kyve.pool.v1beta1\"\xa7\x02\n\x0f\x45ventCreatePool\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07runtime\x18\x03 \x01(\t\x12\x0c\n\x04logo\x18\x04 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x05 \x01(\t\x12\x11\n\tstart_key\x18\x06 \x01(\t\x12\x17\n\x0fupload_interval\x18\x07 \x01(\x04\x12\x16\n\x0eoperating_cost\x18\x08 \x01(\x04\x12\x16\n\x0emin_delegation\x18\t \x01(\x04\x12\x17\n\x0fmax_bundle_size\x18\n \x01(\x04\x12\x0f\n\x07version\x18\x0b \x01(\t\x12\x10\n\x08\x62inaries\x18\x0c \x01(\t\x12\x1b\n\x13storage_provider_id\x18\r \x01(\r\x12\x16\n\x0e\x63ompression_id\x18\x0e \x01(\r\"\x1e\n\x10\x45ventPoolEnabled\x12\n\n\x02id\x18\x01 \x01(\x04\"\x1f\n\x11\x45ventPoolDisabled\x12\n\n\x02id\x18\x01 \x01(\x04\"\x92\x01\n\x1c\x45ventRuntimeUpgradeScheduled\x12\x0f\n\x07runtime\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x14\n\x0cscheduled_at\x18\x03 \x01(\x04\x12\x10\n\x08\x64uration\x18\x04 \x01(\x04\x12\x10\n\x08\x62inaries\x18\x05 \x01(\t\x12\x16\n\x0e\x61\x66\x66\x65\x63ted_pools\x18\x06 \x03(\x04\"G\n\x1c\x45ventRuntimeUpgradeCancelled\x12\x0f\n\x07runtime\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x66\x66\x65\x63ted_pools\x18\x02 \x03(\x04\"\x8d\x02\n\x10\x45ventPoolUpdated\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x19\n\x11raw_update_string\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07runtime\x18\x04 \x01(\t\x12\x0c\n\x04logo\x18\x05 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x06 \x01(\t\x12\x17\n\x0fupload_interval\x18\x07 \x01(\x04\x12\x16\n\x0eoperating_cost\x18\x08 \x01(\x04\x12\x16\n\x0emin_delegation\x18\t \x01(\x04\x12\x17\n\x0fmax_bundle_size\x18\n \x01(\x04\x12\x1b\n\x13storage_provider_id\x18\x0b \x01(\r\x12\x16\n\x0e\x63ompression_id\x18\x0c \x01(\r\"A\n\rEventFundPool\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\"C\n\x0f\x45ventDefundPool\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\"I\n\x15\x45ventPoolFundsSlashed\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\"&\n\x13\x45ventPoolOutOfFunds\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x42+Z)github.com/KYVENetwork/chain/x/pool/typesb\x06proto3')
)




_EVENTCREATEPOOL = _descriptor.Descriptor(
  name='EventCreatePool',
  full_name='kyve.pool.v1beta1.EventCreatePool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.pool.v1beta1.EventCreatePool.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='kyve.pool.v1beta1.EventCreatePool.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='kyve.pool.v1beta1.EventCreatePool.runtime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logo', full_name='kyve.pool.v1beta1.EventCreatePool.logo', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='kyve.pool.v1beta1.EventCreatePool.config', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_key', full_name='kyve.pool.v1beta1.EventCreatePool.start_key', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_interval', full_name='kyve.pool.v1beta1.EventCreatePool.upload_interval', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operating_cost', full_name='kyve.pool.v1beta1.EventCreatePool.operating_cost', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_delegation', full_name='kyve.pool.v1beta1.EventCreatePool.min_delegation', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_bundle_size', full_name='kyve.pool.v1beta1.EventCreatePool.max_bundle_size', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kyve.pool.v1beta1.EventCreatePool.version', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binaries', full_name='kyve.pool.v1beta1.EventCreatePool.binaries', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_provider_id', full_name='kyve.pool.v1beta1.EventCreatePool.storage_provider_id', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compression_id', full_name='kyve.pool.v1beta1.EventCreatePool.compression_id', index=13,
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
  serialized_start=54,
  serialized_end=349,
)


_EVENTPOOLENABLED = _descriptor.Descriptor(
  name='EventPoolEnabled',
  full_name='kyve.pool.v1beta1.EventPoolEnabled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.pool.v1beta1.EventPoolEnabled.id', index=0,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=381,
)


_EVENTPOOLDISABLED = _descriptor.Descriptor(
  name='EventPoolDisabled',
  full_name='kyve.pool.v1beta1.EventPoolDisabled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.pool.v1beta1.EventPoolDisabled.id', index=0,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=414,
)


_EVENTRUNTIMEUPGRADESCHEDULED = _descriptor.Descriptor(
  name='EventRuntimeUpgradeScheduled',
  full_name='kyve.pool.v1beta1.EventRuntimeUpgradeScheduled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='runtime', full_name='kyve.pool.v1beta1.EventRuntimeUpgradeScheduled.runtime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kyve.pool.v1beta1.EventRuntimeUpgradeScheduled.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheduled_at', full_name='kyve.pool.v1beta1.EventRuntimeUpgradeScheduled.scheduled_at', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='kyve.pool.v1beta1.EventRuntimeUpgradeScheduled.duration', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binaries', full_name='kyve.pool.v1beta1.EventRuntimeUpgradeScheduled.binaries', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='affected_pools', full_name='kyve.pool.v1beta1.EventRuntimeUpgradeScheduled.affected_pools', index=5,
      number=6, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=417,
  serialized_end=563,
)


_EVENTRUNTIMEUPGRADECANCELLED = _descriptor.Descriptor(
  name='EventRuntimeUpgradeCancelled',
  full_name='kyve.pool.v1beta1.EventRuntimeUpgradeCancelled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='runtime', full_name='kyve.pool.v1beta1.EventRuntimeUpgradeCancelled.runtime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='affected_pools', full_name='kyve.pool.v1beta1.EventRuntimeUpgradeCancelled.affected_pools', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=565,
  serialized_end=636,
)


_EVENTPOOLUPDATED = _descriptor.Descriptor(
  name='EventPoolUpdated',
  full_name='kyve.pool.v1beta1.EventPoolUpdated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kyve.pool.v1beta1.EventPoolUpdated.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_update_string', full_name='kyve.pool.v1beta1.EventPoolUpdated.raw_update_string', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='kyve.pool.v1beta1.EventPoolUpdated.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='kyve.pool.v1beta1.EventPoolUpdated.runtime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logo', full_name='kyve.pool.v1beta1.EventPoolUpdated.logo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='kyve.pool.v1beta1.EventPoolUpdated.config', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_interval', full_name='kyve.pool.v1beta1.EventPoolUpdated.upload_interval', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operating_cost', full_name='kyve.pool.v1beta1.EventPoolUpdated.operating_cost', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_delegation', full_name='kyve.pool.v1beta1.EventPoolUpdated.min_delegation', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_bundle_size', full_name='kyve.pool.v1beta1.EventPoolUpdated.max_bundle_size', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_provider_id', full_name='kyve.pool.v1beta1.EventPoolUpdated.storage_provider_id', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compression_id', full_name='kyve.pool.v1beta1.EventPoolUpdated.compression_id', index=11,
      number=12, type=13, cpp_type=3, label=1,
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
  serialized_start=639,
  serialized_end=908,
)


_EVENTFUNDPOOL = _descriptor.Descriptor(
  name='EventFundPool',
  full_name='kyve.pool.v1beta1.EventFundPool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pool_id', full_name='kyve.pool.v1beta1.EventFundPool.pool_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='kyve.pool.v1beta1.EventFundPool.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.pool.v1beta1.EventFundPool.amount', index=2,
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
  serialized_start=910,
  serialized_end=975,
)


_EVENTDEFUNDPOOL = _descriptor.Descriptor(
  name='EventDefundPool',
  full_name='kyve.pool.v1beta1.EventDefundPool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pool_id', full_name='kyve.pool.v1beta1.EventDefundPool.pool_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='kyve.pool.v1beta1.EventDefundPool.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.pool.v1beta1.EventDefundPool.amount', index=2,
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
  serialized_start=977,
  serialized_end=1044,
)


_EVENTPOOLFUNDSSLASHED = _descriptor.Descriptor(
  name='EventPoolFundsSlashed',
  full_name='kyve.pool.v1beta1.EventPoolFundsSlashed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pool_id', full_name='kyve.pool.v1beta1.EventPoolFundsSlashed.pool_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='kyve.pool.v1beta1.EventPoolFundsSlashed.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='kyve.pool.v1beta1.EventPoolFundsSlashed.amount', index=2,
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
  serialized_start=1046,
  serialized_end=1119,
)


_EVENTPOOLOUTOFFUNDS = _descriptor.Descriptor(
  name='EventPoolOutOfFunds',
  full_name='kyve.pool.v1beta1.EventPoolOutOfFunds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pool_id', full_name='kyve.pool.v1beta1.EventPoolOutOfFunds.pool_id', index=0,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1121,
  serialized_end=1159,
)

DESCRIPTOR.message_types_by_name['EventCreatePool'] = _EVENTCREATEPOOL
DESCRIPTOR.message_types_by_name['EventPoolEnabled'] = _EVENTPOOLENABLED
DESCRIPTOR.message_types_by_name['EventPoolDisabled'] = _EVENTPOOLDISABLED
DESCRIPTOR.message_types_by_name['EventRuntimeUpgradeScheduled'] = _EVENTRUNTIMEUPGRADESCHEDULED
DESCRIPTOR.message_types_by_name['EventRuntimeUpgradeCancelled'] = _EVENTRUNTIMEUPGRADECANCELLED
DESCRIPTOR.message_types_by_name['EventPoolUpdated'] = _EVENTPOOLUPDATED
DESCRIPTOR.message_types_by_name['EventFundPool'] = _EVENTFUNDPOOL
DESCRIPTOR.message_types_by_name['EventDefundPool'] = _EVENTDEFUNDPOOL
DESCRIPTOR.message_types_by_name['EventPoolFundsSlashed'] = _EVENTPOOLFUNDSSLASHED
DESCRIPTOR.message_types_by_name['EventPoolOutOfFunds'] = _EVENTPOOLOUTOFFUNDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventCreatePool = _reflection.GeneratedProtocolMessageType('EventCreatePool', (_message.Message,), dict(
  DESCRIPTOR = _EVENTCREATEPOOL,
  __module__ = 'kyve.pool.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.EventCreatePool)
  ))
_sym_db.RegisterMessage(EventCreatePool)

EventPoolEnabled = _reflection.GeneratedProtocolMessageType('EventPoolEnabled', (_message.Message,), dict(
  DESCRIPTOR = _EVENTPOOLENABLED,
  __module__ = 'kyve.pool.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.EventPoolEnabled)
  ))
_sym_db.RegisterMessage(EventPoolEnabled)

EventPoolDisabled = _reflection.GeneratedProtocolMessageType('EventPoolDisabled', (_message.Message,), dict(
  DESCRIPTOR = _EVENTPOOLDISABLED,
  __module__ = 'kyve.pool.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.EventPoolDisabled)
  ))
_sym_db.RegisterMessage(EventPoolDisabled)

EventRuntimeUpgradeScheduled = _reflection.GeneratedProtocolMessageType('EventRuntimeUpgradeScheduled', (_message.Message,), dict(
  DESCRIPTOR = _EVENTRUNTIMEUPGRADESCHEDULED,
  __module__ = 'kyve.pool.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.EventRuntimeUpgradeScheduled)
  ))
_sym_db.RegisterMessage(EventRuntimeUpgradeScheduled)

EventRuntimeUpgradeCancelled = _reflection.GeneratedProtocolMessageType('EventRuntimeUpgradeCancelled', (_message.Message,), dict(
  DESCRIPTOR = _EVENTRUNTIMEUPGRADECANCELLED,
  __module__ = 'kyve.pool.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.EventRuntimeUpgradeCancelled)
  ))
_sym_db.RegisterMessage(EventRuntimeUpgradeCancelled)

EventPoolUpdated = _reflection.GeneratedProtocolMessageType('EventPoolUpdated', (_message.Message,), dict(
  DESCRIPTOR = _EVENTPOOLUPDATED,
  __module__ = 'kyve.pool.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.EventPoolUpdated)
  ))
_sym_db.RegisterMessage(EventPoolUpdated)

EventFundPool = _reflection.GeneratedProtocolMessageType('EventFundPool', (_message.Message,), dict(
  DESCRIPTOR = _EVENTFUNDPOOL,
  __module__ = 'kyve.pool.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.EventFundPool)
  ))
_sym_db.RegisterMessage(EventFundPool)

EventDefundPool = _reflection.GeneratedProtocolMessageType('EventDefundPool', (_message.Message,), dict(
  DESCRIPTOR = _EVENTDEFUNDPOOL,
  __module__ = 'kyve.pool.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.EventDefundPool)
  ))
_sym_db.RegisterMessage(EventDefundPool)

EventPoolFundsSlashed = _reflection.GeneratedProtocolMessageType('EventPoolFundsSlashed', (_message.Message,), dict(
  DESCRIPTOR = _EVENTPOOLFUNDSSLASHED,
  __module__ = 'kyve.pool.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.EventPoolFundsSlashed)
  ))
_sym_db.RegisterMessage(EventPoolFundsSlashed)

EventPoolOutOfFunds = _reflection.GeneratedProtocolMessageType('EventPoolOutOfFunds', (_message.Message,), dict(
  DESCRIPTOR = _EVENTPOOLOUTOFFUNDS,
  __module__ = 'kyve.pool.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:kyve.pool.v1beta1.EventPoolOutOfFunds)
  ))
_sym_db.RegisterMessage(EventPoolOutOfFunds)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/KYVENetwork/chain/x/pool/types'))
# @@protoc_insertion_point(module_scope)
