# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='admin_message.proto',
  package='messaging.proto',
  serialized_pb='\n\x13\x61\x64min_message.proto\x12\x0fmessaging.proto\"*\n\x0c\x41\x64minControl\x12\x1a\n\x12\x61uthentication_key\x18\x01 \x02(\t\"n\n\x0c\x41\x64minCommand\x12\x0c\n\x04user\x18\x01 \x02(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x02(\t\x12.\n\x07\x63ontrol\x18\x03 \x02(\x0b\x32\x1d.messaging.proto.AdminControl\x12\x0f\n\x07options\x18\x04 \x01(\t')




_ADMINCONTROL = _descriptor.Descriptor(
  name='AdminControl',
  full_name='messaging.proto.AdminControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authentication_key', full_name='messaging.proto.AdminControl.authentication_key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=40,
  serialized_end=82,
)


_ADMINCOMMAND = _descriptor.Descriptor(
  name='AdminCommand',
  full_name='messaging.proto.AdminCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='messaging.proto.AdminCommand.user', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command', full_name='messaging.proto.AdminCommand.command', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='control', full_name='messaging.proto.AdminCommand.control', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='options', full_name='messaging.proto.AdminCommand.options', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=84,
  serialized_end=194,
)

_ADMINCOMMAND.fields_by_name['control'].message_type = _ADMINCONTROL
DESCRIPTOR.message_types_by_name['AdminControl'] = _ADMINCONTROL
DESCRIPTOR.message_types_by_name['AdminCommand'] = _ADMINCOMMAND

class AdminControl(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADMINCONTROL

  # @@protoc_insertion_point(class_scope:messaging.proto.AdminControl)

class AdminCommand(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADMINCOMMAND

  # @@protoc_insertion_point(class_scope:messaging.proto.AdminCommand)


# @@protoc_insertion_point(module_scope) 