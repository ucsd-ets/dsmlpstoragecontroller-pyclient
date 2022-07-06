from enum import Enum


class ClientRequestMethods(Enum):
    """DSMLPStorageControllerService gRPC request methods."""

    GetPersonalQuota = "GetPersonalQuota"
    SetPersonalQuota = "SetPersonalQuota"
    GetTeamQuota = "GetTeamQuota"
    SetTeamQuota = "SetTeamQuota"
    GetHomeQuota = "GetHomeQuota"
    SetHomeQuota = "SetHomeQuota"
    CreateWorkspace = "CreateWorkspace"
    CreateHomeDirectory = "CreateHomeDirectory"
    ListHomeDirectories = "ListHomeDirectories"
