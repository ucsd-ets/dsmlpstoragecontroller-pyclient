from enum import Enum


class ClientRequestMethods(Enum):
    """DSMLPStorageControllerService gRPC request methods."""

    GetWorkspaceHomeQuota = "GetWorkspaceHomeQuota"
    SetWorkspaceHomeQuota = "SetWorkspaceHomeQuota"
    GetTeamQuota = "GetTeamQuota"
    SetTeamQuota = "SetTeamQuota"
    GetPersonalQuota = "GetPersonalQuota"
    SetPersonalQuota = "SetPersonalQuota"
    CreateWorkspace = "CreateWorkspace"
    CreateHomeDirectory = "CreateHomeDirectory"
    ListHomeDirectories = "ListHomeDirectories"
