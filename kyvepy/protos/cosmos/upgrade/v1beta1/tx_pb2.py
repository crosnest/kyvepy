# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/upgrade/v1beta1/tx.proto

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
from cosmos.upgrade.v1beta1 import upgrade_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/upgrade/v1beta1/tx.proto',
  package='cosmos.upgrade.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\x1f\x63osmos/upgrade/v1beta1/tx.proto\x12\x16\x63osmos.upgrade.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a$cosmos/upgrade/v1beta1/upgrade.proto\x1a\x17\x63osmos/msg/v1/msg.proto\"\x83\x01\n\x12MsgSoftwareUpgrade\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x30\n\x04plan\x18\x02 \x01(\x0b\x32\x1c.cosmos.upgrade.v1beta1.PlanB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x1c\n\x1aMsgSoftwareUpgradeResponse\"O\n\x10MsgCancelUpgrade\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x0e\x82\xe7\xb0*\tauthority\"\x1a\n\x18MsgCancelUpgradeResponse2\xe5\x01\n\x03Msg\x12q\n\x0fSoftwareUpgrade\x12*.cosmos.upgrade.v1beta1.MsgSoftwareUpgrade\x1a\x32.cosmos.upgrade.v1beta1.MsgSoftwareUpgradeResponse\x12k\n\rCancelUpgrade\x12(.cosmos.upgrade.v1beta1.MsgCancelUpgrade\x1a\x30.cosmos.upgrade.v1beta1.MsgCancelUpgradeResponseB.Z,github.com/cosmos/cosmos-sdk/x/upgrade/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2.DESCRIPTOR,cosmos_dot_msg_dot_v1_dot_msg__pb2.DESCRIPTOR,])




_MSGSOFTWAREUPGRADE = _descriptor.Descriptor(
  name='MsgSoftwareUpgrade',
  full_name='cosmos.upgrade.v1beta1.MsgSoftwareUpgrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='cosmos.upgrade.v1beta1.MsgSoftwareUpgrade.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plan', full_name='cosmos.upgrade.v1beta1.MsgSoftwareUpgrade.plan', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\tauthority')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=303,
)


_MSGSOFTWAREUPGRADERESPONSE = _descriptor.Descriptor(
  name='MsgSoftwareUpgradeResponse',
  full_name='cosmos.upgrade.v1beta1.MsgSoftwareUpgradeResponse',
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
  serialized_start=305,
  serialized_end=333,
)


_MSGCANCELUPGRADE = _descriptor.Descriptor(
  name='MsgCancelUpgrade',
  full_name='cosmos.upgrade.v1beta1.MsgCancelUpgrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='cosmos.upgrade.v1beta1.MsgCancelUpgrade.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\tauthority')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=414,
)


_MSGCANCELUPGRADERESPONSE = _descriptor.Descriptor(
  name='MsgCancelUpgradeResponse',
  full_name='cosmos.upgrade.v1beta1.MsgCancelUpgradeResponse',
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
  serialized_start=416,
  serialized_end=442,
)

_MSGSOFTWAREUPGRADE.fields_by_name['plan'].message_type = cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2._PLAN
DESCRIPTOR.message_types_by_name['MsgSoftwareUpgrade'] = _MSGSOFTWAREUPGRADE
DESCRIPTOR.message_types_by_name['MsgSoftwareUpgradeResponse'] = _MSGSOFTWAREUPGRADERESPONSE
DESCRIPTOR.message_types_by_name['MsgCancelUpgrade'] = _MSGCANCELUPGRADE
DESCRIPTOR.message_types_by_name['MsgCancelUpgradeResponse'] = _MSGCANCELUPGRADERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgSoftwareUpgrade = _reflection.GeneratedProtocolMessageType('MsgSoftwareUpgrade', (_message.Message,), dict(
  DESCRIPTOR = _MSGSOFTWAREUPGRADE,
  __module__ = 'cosmos.upgrade.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.upgrade.v1beta1.MsgSoftwareUpgrade)
  ))
_sym_db.RegisterMessage(MsgSoftwareUpgrade)

MsgSoftwareUpgradeResponse = _reflection.GeneratedProtocolMessageType('MsgSoftwareUpgradeResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGSOFTWAREUPGRADERESPONSE,
  __module__ = 'cosmos.upgrade.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.upgrade.v1beta1.MsgSoftwareUpgradeResponse)
  ))
_sym_db.RegisterMessage(MsgSoftwareUpgradeResponse)

MsgCancelUpgrade = _reflection.GeneratedProtocolMessageType('MsgCancelUpgrade', (_message.Message,), dict(
  DESCRIPTOR = _MSGCANCELUPGRADE,
  __module__ = 'cosmos.upgrade.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.upgrade.v1beta1.MsgCancelUpgrade)
  ))
_sym_db.RegisterMessage(MsgCancelUpgrade)

MsgCancelUpgradeResponse = _reflection.GeneratedProtocolMessageType('MsgCancelUpgradeResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGCANCELUPGRADERESPONSE,
  __module__ = 'cosmos.upgrade.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.upgrade.v1beta1.MsgCancelUpgradeResponse)
  ))
_sym_db.RegisterMessage(MsgCancelUpgradeResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z,github.com/cosmos/cosmos-sdk/x/upgrade/types'))
_MSGSOFTWAREUPGRADE.fields_by_name['authority'].has_options = True
_MSGSOFTWAREUPGRADE.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGSOFTWAREUPGRADE.fields_by_name['plan'].has_options = True
_MSGSOFTWAREUPGRADE.fields_by_name['plan']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_MSGSOFTWAREUPGRADE.has_options = True
_MSGSOFTWAREUPGRADE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\tauthority'))
_MSGCANCELUPGRADE.fields_by_name['authority'].has_options = True
_MSGCANCELUPGRADE.fields_by_name['authority']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGCANCELUPGRADE.has_options = True
_MSGCANCELUPGRADE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\tauthority'))

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='cosmos.upgrade.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=445,
  serialized_end=674,
  methods=[
  _descriptor.MethodDescriptor(
    name='SoftwareUpgrade',
    full_name='cosmos.upgrade.v1beta1.Msg.SoftwareUpgrade',
    index=0,
    containing_service=None,
    input_type=_MSGSOFTWAREUPGRADE,
    output_type=_MSGSOFTWAREUPGRADERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CancelUpgrade',
    full_name='cosmos.upgrade.v1beta1.Msg.CancelUpgrade',
    index=1,
    containing_service=None,
    input_type=_MSGCANCELUPGRADE,
    output_type=_MSGCANCELUPGRADERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
