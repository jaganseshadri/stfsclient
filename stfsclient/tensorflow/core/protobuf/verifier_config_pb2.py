# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stfsclient/tensorflow/core/protobuf/verifier_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stfsclient/tensorflow/core/protobuf/verifier_config.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=_b('\n\030org.tensorflow.frameworkB\024VerifierConfigProtosP\001\370\001\001'),
  serialized_pb=_b('\n9stfsclient/tensorflow/core/protobuf/verifier_config.proto\x12\ntensorflow\"\x9b\x01\n\x0eVerifierConfig\x12\"\n\x1averification_timeout_in_ms\x18\x01 \x01(\x03\x12=\n\x12structure_verifier\x18\x02 \x01(\x0e\x32!.tensorflow.VerifierConfig.Toggle\"&\n\x06Toggle\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x06\n\x02ON\x10\x01\x12\x07\n\x03OFF\x10\x02\x42\x35\n\x18org.tensorflow.frameworkB\x14VerifierConfigProtosP\x01\xf8\x01\x01\x62\x06proto3')
)



_VERIFIERCONFIG_TOGGLE = _descriptor.EnumDescriptor(
  name='Toggle',
  full_name='tensorflow.VerifierConfig.Toggle',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFF', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=191,
  serialized_end=229,
)
_sym_db.RegisterEnumDescriptor(_VERIFIERCONFIG_TOGGLE)


_VERIFIERCONFIG = _descriptor.Descriptor(
  name='VerifierConfig',
  full_name='tensorflow.VerifierConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='verification_timeout_in_ms', full_name='tensorflow.VerifierConfig.verification_timeout_in_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='structure_verifier', full_name='tensorflow.VerifierConfig.structure_verifier', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VERIFIERCONFIG_TOGGLE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=229,
)

_VERIFIERCONFIG.fields_by_name['structure_verifier'].enum_type = _VERIFIERCONFIG_TOGGLE
_VERIFIERCONFIG_TOGGLE.containing_type = _VERIFIERCONFIG
DESCRIPTOR.message_types_by_name['VerifierConfig'] = _VERIFIERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VerifierConfig = _reflection.GeneratedProtocolMessageType('VerifierConfig', (_message.Message,), {
  'DESCRIPTOR' : _VERIFIERCONFIG,
  '__module__' : 'stfsclient.tensorflow.core.protobuf.verifier_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.VerifierConfig)
  })
_sym_db.RegisterMessage(VerifierConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
