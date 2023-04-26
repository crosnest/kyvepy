# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/feegrant/v1beta1/feegrant.proto

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
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/feegrant/v1beta1/feegrant.proto',
  package='cosmos.feegrant.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n&cosmos/feegrant/v1beta1/feegrant.proto\x12\x17\x63osmos.feegrant.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\xbb\x01\n\x0e\x42\x61sicAllowance\x12`\n\x0bspend_limit\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x34\n\nexpiration\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01:\x11\xca\xb4-\rFeeAllowanceI\"\xa5\x03\n\x11PeriodicAllowance\x12<\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32\'.cosmos.feegrant.v1beta1.BasicAllowanceB\x04\xc8\xde\x1f\x00\x12\x33\n\x06period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\x98\xdf\x1f\x01\xc8\xde\x1f\x00\x12g\n\x12period_spend_limit\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x65\n\x10period_can_spend\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12:\n\x0cperiod_reset\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00:\x11\xca\xb4-\rFeeAllowanceI\"\x82\x01\n\x13\x41llowedMsgAllowance\x12:\n\tallowance\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x11\xca\xb4-\rFeeAllowanceI\x12\x18\n\x10\x61llowed_messages\x18\x02 \x03(\t:\x15\x88\xa0\x1f\x00\xca\xb4-\rFeeAllowanceI\"\x99\x01\n\x05Grant\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\tallowance\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyB\x11\xca\xb4-\rFeeAllowanceIB)Z\'github.com/cosmos/cosmos-sdk/x/feegrantb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_BASICALLOWANCE = _descriptor.Descriptor(
  name='BasicAllowance',
  full_name='cosmos.feegrant.v1beta1.BasicAllowance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spend_limit', full_name='cosmos.feegrant.v1beta1.BasicAllowance.spend_limit', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='cosmos.feegrant.v1beta1.BasicAllowance.expiration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\312\264-\rFeeAllowanceI')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=428,
)


_PERIODICALLOWANCE = _descriptor.Descriptor(
  name='PeriodicAllowance',
  full_name='cosmos.feegrant.v1beta1.PeriodicAllowance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic', full_name='cosmos.feegrant.v1beta1.PeriodicAllowance.basic', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='cosmos.feegrant.v1beta1.PeriodicAllowance.period', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period_spend_limit', full_name='cosmos.feegrant.v1beta1.PeriodicAllowance.period_spend_limit', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period_can_spend', full_name='cosmos.feegrant.v1beta1.PeriodicAllowance.period_can_spend', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period_reset', full_name='cosmos.feegrant.v1beta1.PeriodicAllowance.period_reset', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\312\264-\rFeeAllowanceI')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=852,
)


_ALLOWEDMSGALLOWANCE = _descriptor.Descriptor(
  name='AllowedMsgAllowance',
  full_name='cosmos.feegrant.v1beta1.AllowedMsgAllowance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allowance', full_name='cosmos.feegrant.v1beta1.AllowedMsgAllowance.allowance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\264-\rFeeAllowanceI')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowed_messages', full_name='cosmos.feegrant.v1beta1.AllowedMsgAllowance.allowed_messages', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\312\264-\rFeeAllowanceI')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=855,
  serialized_end=985,
)


_GRANT = _descriptor.Descriptor(
  name='Grant',
  full_name='cosmos.feegrant.v1beta1.Grant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.feegrant.v1beta1.Grant.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.feegrant.v1beta1.Grant.grantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowance', full_name='cosmos.feegrant.v1beta1.Grant.allowance', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\264-\rFeeAllowanceI')), file=DESCRIPTOR),
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
  serialized_start=988,
  serialized_end=1141,
)

_BASICALLOWANCE.fields_by_name['spend_limit'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_BASICALLOWANCE.fields_by_name['expiration'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PERIODICALLOWANCE.fields_by_name['basic'].message_type = _BASICALLOWANCE
_PERIODICALLOWANCE.fields_by_name['period'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PERIODICALLOWANCE.fields_by_name['period_spend_limit'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_PERIODICALLOWANCE.fields_by_name['period_can_spend'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_PERIODICALLOWANCE.fields_by_name['period_reset'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ALLOWEDMSGALLOWANCE.fields_by_name['allowance'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_GRANT.fields_by_name['allowance'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['BasicAllowance'] = _BASICALLOWANCE
DESCRIPTOR.message_types_by_name['PeriodicAllowance'] = _PERIODICALLOWANCE
DESCRIPTOR.message_types_by_name['AllowedMsgAllowance'] = _ALLOWEDMSGALLOWANCE
DESCRIPTOR.message_types_by_name['Grant'] = _GRANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BasicAllowance = _reflection.GeneratedProtocolMessageType('BasicAllowance', (_message.Message,), dict(
  DESCRIPTOR = _BASICALLOWANCE,
  __module__ = 'cosmos.feegrant.v1beta1.feegrant_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.BasicAllowance)
  ))
_sym_db.RegisterMessage(BasicAllowance)

PeriodicAllowance = _reflection.GeneratedProtocolMessageType('PeriodicAllowance', (_message.Message,), dict(
  DESCRIPTOR = _PERIODICALLOWANCE,
  __module__ = 'cosmos.feegrant.v1beta1.feegrant_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.PeriodicAllowance)
  ))
_sym_db.RegisterMessage(PeriodicAllowance)

AllowedMsgAllowance = _reflection.GeneratedProtocolMessageType('AllowedMsgAllowance', (_message.Message,), dict(
  DESCRIPTOR = _ALLOWEDMSGALLOWANCE,
  __module__ = 'cosmos.feegrant.v1beta1.feegrant_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.AllowedMsgAllowance)
  ))
_sym_db.RegisterMessage(AllowedMsgAllowance)

Grant = _reflection.GeneratedProtocolMessageType('Grant', (_message.Message,), dict(
  DESCRIPTOR = _GRANT,
  __module__ = 'cosmos.feegrant.v1beta1.feegrant_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.Grant)
  ))
_sym_db.RegisterMessage(Grant)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\'github.com/cosmos/cosmos-sdk/x/feegrant'))
_BASICALLOWANCE.fields_by_name['spend_limit'].has_options = True
_BASICALLOWANCE.fields_by_name['spend_limit']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'))
_BASICALLOWANCE.fields_by_name['expiration'].has_options = True
_BASICALLOWANCE.fields_by_name['expiration']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001'))
_BASICALLOWANCE.has_options = True
_BASICALLOWANCE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\312\264-\rFeeAllowanceI'))
_PERIODICALLOWANCE.fields_by_name['basic'].has_options = True
_PERIODICALLOWANCE.fields_by_name['basic']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_PERIODICALLOWANCE.fields_by_name['period'].has_options = True
_PERIODICALLOWANCE.fields_by_name['period']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\000'))
_PERIODICALLOWANCE.fields_by_name['period_spend_limit'].has_options = True
_PERIODICALLOWANCE.fields_by_name['period_spend_limit']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'))
_PERIODICALLOWANCE.fields_by_name['period_can_spend'].has_options = True
_PERIODICALLOWANCE.fields_by_name['period_can_spend']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'))
_PERIODICALLOWANCE.fields_by_name['period_reset'].has_options = True
_PERIODICALLOWANCE.fields_by_name['period_reset']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000'))
_PERIODICALLOWANCE.has_options = True
_PERIODICALLOWANCE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\312\264-\rFeeAllowanceI'))
_ALLOWEDMSGALLOWANCE.fields_by_name['allowance'].has_options = True
_ALLOWEDMSGALLOWANCE.fields_by_name['allowance']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\264-\rFeeAllowanceI'))
_ALLOWEDMSGALLOWANCE.has_options = True
_ALLOWEDMSGALLOWANCE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\312\264-\rFeeAllowanceI'))
_GRANT.fields_by_name['granter'].has_options = True
_GRANT.fields_by_name['granter']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_GRANT.fields_by_name['grantee'].has_options = True
_GRANT.fields_by_name['grantee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_GRANT.fields_by_name['allowance'].has_options = True
_GRANT.fields_by_name['allowance']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\264-\rFeeAllowanceI'))
# @@protoc_insertion_point(module_scope)