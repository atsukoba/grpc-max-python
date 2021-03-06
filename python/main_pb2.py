# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='main.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmain.proto\"n\n\tCandidate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x04rate\x18\x02 \x01(\x0e\x32\x0f.Candidate.Rate\x12\x11\n\tinput_num\x18\x03 \x01(\x05\"!\n\x04Rate\x12\x08\n\x04GOOD\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x07\n\x03\x42\x41\x44\x10\x02\"%\n\x10\x43\x61ndidateRequest\x12\x11\n\trequester\x18\x01 \x01(\x05\"A\n\x11\x43\x61ndidateResponse\x12\x0c\n\x04memo\x18\x01 \x01(\t\x12\x1e\n\ncandidates\x18\x02 \x03(\x0b\x32\n.Candidate2@\n\rSearchService\x12/\n\x06Search\x12\x11.CandidateRequest\x1a\x12.CandidateResponseb\x06proto3'
)



_CANDIDATE_RATE = _descriptor.EnumDescriptor(
  name='Rate',
  full_name='Candidate.Rate',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GOOD', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BAD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=91,
  serialized_end=124,
)
_sym_db.RegisterEnumDescriptor(_CANDIDATE_RATE)


_CANDIDATE = _descriptor.Descriptor(
  name='Candidate',
  full_name='Candidate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Candidate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate', full_name='Candidate.rate', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_num', full_name='Candidate.input_num', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CANDIDATE_RATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=124,
)


_CANDIDATEREQUEST = _descriptor.Descriptor(
  name='CandidateRequest',
  full_name='CandidateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='requester', full_name='CandidateRequest.requester', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=163,
)


_CANDIDATERESPONSE = _descriptor.Descriptor(
  name='CandidateResponse',
  full_name='CandidateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='memo', full_name='CandidateResponse.memo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='candidates', full_name='CandidateResponse.candidates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=230,
)

_CANDIDATE.fields_by_name['rate'].enum_type = _CANDIDATE_RATE
_CANDIDATE_RATE.containing_type = _CANDIDATE
_CANDIDATERESPONSE.fields_by_name['candidates'].message_type = _CANDIDATE
DESCRIPTOR.message_types_by_name['Candidate'] = _CANDIDATE
DESCRIPTOR.message_types_by_name['CandidateRequest'] = _CANDIDATEREQUEST
DESCRIPTOR.message_types_by_name['CandidateResponse'] = _CANDIDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Candidate = _reflection.GeneratedProtocolMessageType('Candidate', (_message.Message,), {
  'DESCRIPTOR' : _CANDIDATE,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:Candidate)
  })
_sym_db.RegisterMessage(Candidate)

CandidateRequest = _reflection.GeneratedProtocolMessageType('CandidateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANDIDATEREQUEST,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:CandidateRequest)
  })
_sym_db.RegisterMessage(CandidateRequest)

CandidateResponse = _reflection.GeneratedProtocolMessageType('CandidateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANDIDATERESPONSE,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:CandidateResponse)
  })
_sym_db.RegisterMessage(CandidateResponse)



_SEARCHSERVICE = _descriptor.ServiceDescriptor(
  name='SearchService',
  full_name='SearchService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=232,
  serialized_end=296,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='SearchService.Search',
    index=0,
    containing_service=None,
    input_type=_CANDIDATEREQUEST,
    output_type=_CANDIDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCHSERVICE)

DESCRIPTOR.services_by_name['SearchService'] = _SEARCHSERVICE

# @@protoc_insertion_point(module_scope)
