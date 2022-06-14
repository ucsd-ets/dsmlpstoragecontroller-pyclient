# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dsmlpstoragecontrollerservice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#dsmlpstoragecontrollerservice.proto\x12\x1d\x64smlpstoragecontrollerservice\"\x06\n\x04Void\"0\n\tUserQuota\x12\x10\n\x08userused\x18\x01 \x01(\t\x12\x11\n\tuserquota\x18\x02 \x01(\t\"3\n\nGroupQuota\x12\x11\n\tgroupused\x18\x01 \x01(\t\x12\x12\n\ngroupquota\x18\x02 \x01(\t\"=\n\x17GetPersonalQuotaRequest\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x15\n\rworkspaceName\x18\x02 \x01(\t\"S\n\x18GetPersonalQuotaResponse\x12\x37\n\x05quota\x18\x01 \x01(\x0b\x32(.dsmlpstoragecontrollerservice.UserQuota\"P\n\x17SetPersonalQuotaRequest\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x11\n\tuserquota\x18\x02 \x01(\t\x12\x15\n\rworkspaceName\x18\x03 \x01(\t\"9\n\x13GetTeamQuotaRequest\x12\x0b\n\x03gid\x18\x01 \x01(\r\x12\x15\n\rworkspaceName\x18\x02 \x01(\t\"P\n\x14GetTeamQuotaResponse\x12\x38\n\x05quota\x18\x01 \x01(\x0b\x32).dsmlpstoragecontrollerservice.GroupQuota\"M\n\x13SetTeamQuotaRequest\x12\x0b\n\x03gid\x18\x01 \x01(\r\x12\x12\n\ngroupquota\x18\x02 \x01(\t\x12\x15\n\rworkspaceName\x18\x03 \x01(\t\"\"\n\x13GetHomeQuotaRequest\x12\x0b\n\x03uid\x18\x01 \x01(\r\"O\n\x14GetHomeQuotaResponse\x12\x37\n\x05quota\x18\x01 \x01(\x0b\x32(.dsmlpstoragecontrollerservice.UserQuota\"5\n\x13SetHomeQuotaRequest\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x11\n\tuserquota\x18\x02 \x01(\t\"&\n\x16\x43reateWorkspaceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\";\n\x1a\x43reateHomeDirectoryRequest\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x10\n\x08username\x18\x02 \x01(\t\"c\n\rHomeDirectory\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x37\n\x05quota\x18\x03 \x01(\x0b\x32(.dsmlpstoragecontrollerservice.UserQuota\"d\n\x1bListHomeDirectoriesResponse\x12\x45\n\x0fhomeDirectories\x18\x01 \x03(\x0b\x32,.dsmlpstoragecontrollerservice.HomeDirectory2\xb8\x08\n\x1d\x44SMLPStorageControllerService\x12\x83\x01\n\x10GetPersonalQuota\x12\x36.dsmlpstoragecontrollerservice.GetPersonalQuotaRequest\x1a\x37.dsmlpstoragecontrollerservice.GetPersonalQuotaResponse\x12o\n\x10SetPersonalQuota\x12\x36.dsmlpstoragecontrollerservice.SetPersonalQuotaRequest\x1a#.dsmlpstoragecontrollerservice.Void\x12w\n\x0cGetTeamQuota\x12\x32.dsmlpstoragecontrollerservice.GetTeamQuotaRequest\x1a\x33.dsmlpstoragecontrollerservice.GetTeamQuotaResponse\x12g\n\x0cSetTeamQuota\x12\x32.dsmlpstoragecontrollerservice.SetTeamQuotaRequest\x1a#.dsmlpstoragecontrollerservice.Void\x12w\n\x0cGetHomeQuota\x12\x32.dsmlpstoragecontrollerservice.GetHomeQuotaRequest\x1a\x33.dsmlpstoragecontrollerservice.GetHomeQuotaResponse\x12g\n\x0cSetHomeQuota\x12\x32.dsmlpstoragecontrollerservice.SetHomeQuotaRequest\x1a#.dsmlpstoragecontrollerservice.Void\x12m\n\x0f\x43reateWorkspace\x12\x35.dsmlpstoragecontrollerservice.CreateWorkspaceRequest\x1a#.dsmlpstoragecontrollerservice.Void\x12u\n\x13\x43reateHomeDirectory\x12\x39.dsmlpstoragecontrollerservice.CreateHomeDirectoryRequest\x1a#.dsmlpstoragecontrollerservice.Void\x12v\n\x13ListHomeDirectories\x12#.dsmlpstoragecontrollerservice.Void\x1a:.dsmlpstoragecontrollerservice.ListHomeDirectoriesResponseB=Z;dsmlpstoragecontrollerservice/dsmlpstoragecontrollerserviceb\x06proto3')



_VOID = DESCRIPTOR.message_types_by_name['Void']
_USERQUOTA = DESCRIPTOR.message_types_by_name['UserQuota']
_GROUPQUOTA = DESCRIPTOR.message_types_by_name['GroupQuota']
_GETPERSONALQUOTAREQUEST = DESCRIPTOR.message_types_by_name['GetPersonalQuotaRequest']
_GETPERSONALQUOTARESPONSE = DESCRIPTOR.message_types_by_name['GetPersonalQuotaResponse']
_SETPERSONALQUOTAREQUEST = DESCRIPTOR.message_types_by_name['SetPersonalQuotaRequest']
_GETTEAMQUOTAREQUEST = DESCRIPTOR.message_types_by_name['GetTeamQuotaRequest']
_GETTEAMQUOTARESPONSE = DESCRIPTOR.message_types_by_name['GetTeamQuotaResponse']
_SETTEAMQUOTAREQUEST = DESCRIPTOR.message_types_by_name['SetTeamQuotaRequest']
_GETHOMEQUOTAREQUEST = DESCRIPTOR.message_types_by_name['GetHomeQuotaRequest']
_GETHOMEQUOTARESPONSE = DESCRIPTOR.message_types_by_name['GetHomeQuotaResponse']
_SETHOMEQUOTAREQUEST = DESCRIPTOR.message_types_by_name['SetHomeQuotaRequest']
_CREATEWORKSPACEREQUEST = DESCRIPTOR.message_types_by_name['CreateWorkspaceRequest']
_CREATEHOMEDIRECTORYREQUEST = DESCRIPTOR.message_types_by_name['CreateHomeDirectoryRequest']
_HOMEDIRECTORY = DESCRIPTOR.message_types_by_name['HomeDirectory']
_LISTHOMEDIRECTORIESRESPONSE = DESCRIPTOR.message_types_by_name['ListHomeDirectoriesResponse']
Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.Void)
  })
_sym_db.RegisterMessage(Void)

UserQuota = _reflection.GeneratedProtocolMessageType('UserQuota', (_message.Message,), {
  'DESCRIPTOR' : _USERQUOTA,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.UserQuota)
  })
_sym_db.RegisterMessage(UserQuota)

GroupQuota = _reflection.GeneratedProtocolMessageType('GroupQuota', (_message.Message,), {
  'DESCRIPTOR' : _GROUPQUOTA,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.GroupQuota)
  })
_sym_db.RegisterMessage(GroupQuota)

GetPersonalQuotaRequest = _reflection.GeneratedProtocolMessageType('GetPersonalQuotaRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPERSONALQUOTAREQUEST,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.GetPersonalQuotaRequest)
  })
_sym_db.RegisterMessage(GetPersonalQuotaRequest)

GetPersonalQuotaResponse = _reflection.GeneratedProtocolMessageType('GetPersonalQuotaResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPERSONALQUOTARESPONSE,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.GetPersonalQuotaResponse)
  })
_sym_db.RegisterMessage(GetPersonalQuotaResponse)

SetPersonalQuotaRequest = _reflection.GeneratedProtocolMessageType('SetPersonalQuotaRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPERSONALQUOTAREQUEST,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.SetPersonalQuotaRequest)
  })
_sym_db.RegisterMessage(SetPersonalQuotaRequest)

GetTeamQuotaRequest = _reflection.GeneratedProtocolMessageType('GetTeamQuotaRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTEAMQUOTAREQUEST,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.GetTeamQuotaRequest)
  })
_sym_db.RegisterMessage(GetTeamQuotaRequest)

GetTeamQuotaResponse = _reflection.GeneratedProtocolMessageType('GetTeamQuotaResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTEAMQUOTARESPONSE,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.GetTeamQuotaResponse)
  })
_sym_db.RegisterMessage(GetTeamQuotaResponse)

SetTeamQuotaRequest = _reflection.GeneratedProtocolMessageType('SetTeamQuotaRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETTEAMQUOTAREQUEST,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.SetTeamQuotaRequest)
  })
_sym_db.RegisterMessage(SetTeamQuotaRequest)

GetHomeQuotaRequest = _reflection.GeneratedProtocolMessageType('GetHomeQuotaRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETHOMEQUOTAREQUEST,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.GetHomeQuotaRequest)
  })
_sym_db.RegisterMessage(GetHomeQuotaRequest)

GetHomeQuotaResponse = _reflection.GeneratedProtocolMessageType('GetHomeQuotaResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETHOMEQUOTARESPONSE,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.GetHomeQuotaResponse)
  })
_sym_db.RegisterMessage(GetHomeQuotaResponse)

SetHomeQuotaRequest = _reflection.GeneratedProtocolMessageType('SetHomeQuotaRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETHOMEQUOTAREQUEST,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.SetHomeQuotaRequest)
  })
_sym_db.RegisterMessage(SetHomeQuotaRequest)

CreateWorkspaceRequest = _reflection.GeneratedProtocolMessageType('CreateWorkspaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWORKSPACEREQUEST,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.CreateWorkspaceRequest)
  })
_sym_db.RegisterMessage(CreateWorkspaceRequest)

CreateHomeDirectoryRequest = _reflection.GeneratedProtocolMessageType('CreateHomeDirectoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEHOMEDIRECTORYREQUEST,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.CreateHomeDirectoryRequest)
  })
_sym_db.RegisterMessage(CreateHomeDirectoryRequest)

HomeDirectory = _reflection.GeneratedProtocolMessageType('HomeDirectory', (_message.Message,), {
  'DESCRIPTOR' : _HOMEDIRECTORY,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.HomeDirectory)
  })
_sym_db.RegisterMessage(HomeDirectory)

ListHomeDirectoriesResponse = _reflection.GeneratedProtocolMessageType('ListHomeDirectoriesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTHOMEDIRECTORIESRESPONSE,
  '__module__' : 'dsmlpstoragecontrollerservice_pb2'
  # @@protoc_insertion_point(class_scope:dsmlpstoragecontrollerservice.ListHomeDirectoriesResponse)
  })
_sym_db.RegisterMessage(ListHomeDirectoriesResponse)

_DSMLPSTORAGECONTROLLERSERVICE = DESCRIPTOR.services_by_name['DSMLPStorageControllerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z;dsmlpstoragecontrollerservice/dsmlpstoragecontrollerservice'
  _VOID._serialized_start=70
  _VOID._serialized_end=76
  _USERQUOTA._serialized_start=78
  _USERQUOTA._serialized_end=126
  _GROUPQUOTA._serialized_start=128
  _GROUPQUOTA._serialized_end=179
  _GETPERSONALQUOTAREQUEST._serialized_start=181
  _GETPERSONALQUOTAREQUEST._serialized_end=242
  _GETPERSONALQUOTARESPONSE._serialized_start=244
  _GETPERSONALQUOTARESPONSE._serialized_end=327
  _SETPERSONALQUOTAREQUEST._serialized_start=329
  _SETPERSONALQUOTAREQUEST._serialized_end=409
  _GETTEAMQUOTAREQUEST._serialized_start=411
  _GETTEAMQUOTAREQUEST._serialized_end=468
  _GETTEAMQUOTARESPONSE._serialized_start=470
  _GETTEAMQUOTARESPONSE._serialized_end=550
  _SETTEAMQUOTAREQUEST._serialized_start=552
  _SETTEAMQUOTAREQUEST._serialized_end=629
  _GETHOMEQUOTAREQUEST._serialized_start=631
  _GETHOMEQUOTAREQUEST._serialized_end=665
  _GETHOMEQUOTARESPONSE._serialized_start=667
  _GETHOMEQUOTARESPONSE._serialized_end=746
  _SETHOMEQUOTAREQUEST._serialized_start=748
  _SETHOMEQUOTAREQUEST._serialized_end=801
  _CREATEWORKSPACEREQUEST._serialized_start=803
  _CREATEWORKSPACEREQUEST._serialized_end=841
  _CREATEHOMEDIRECTORYREQUEST._serialized_start=843
  _CREATEHOMEDIRECTORYREQUEST._serialized_end=902
  _HOMEDIRECTORY._serialized_start=904
  _HOMEDIRECTORY._serialized_end=1003
  _LISTHOMEDIRECTORIESRESPONSE._serialized_start=1005
  _LISTHOMEDIRECTORIESRESPONSE._serialized_end=1105
  _DSMLPSTORAGECONTROLLERSERVICE._serialized_start=1108
  _DSMLPSTORAGECONTROLLERSERVICE._serialized_end=2188
# @@protoc_insertion_point(module_scope)
