from sys import exit
from typing import List

from grpc import ChannelCredentials, secure_channel, ssl_channel_credentials

import dsmlpstoragecontrollerclient.dsmlpstoragecontrollerservice.dsmlpstoragecontrollerservice_pb2 as pb2
from dsmlpstoragecontrollerclient.dsmlpstoragecontrollerservice.dsmlpstoragecontrollerservice_pb2_grpc import (
    DSMLPStorageControllerServiceStub,
)


class Client:
    """The client for the DSMLPStorageController service.

    Args:
        ca: The path of the cert file used for gRPC authentication.
        key: The path of the key file used for gRPC authentication.
        cert: The path of the cert file used for gRPC authentication.
        port: The port of the DSMLPStorageController service.
        address: The address of the DSMLPStorageController service.
    """

    def __init__(
        self, ca: str, key: str, cert: str, port: int, address: str = "localhost"
    ):
        self.__ca = ca
        self.__key = key
        self.__cert = cert
        self.__port = port
        self.__address = address
        self.__creds = self.__create_channel_credentials()

    def __enter__(self):
        self.__channel = secure_channel(f"{self.__address}:{self.__port}", self.__creds)

        try:
            self.__stub = DSMLPStorageControllerServiceStub(self.__channel)
        except Exception as e:
            print(e)
            exit("failed to create stub for channel")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__channel.close()

    def __create_channel_credentials(self) -> ChannelCredentials:
        """Retrieve gRPC SSL channel credentials.
        Args:
            cert: The path of the cert file used for gRPC authentication.

        Returns:
            The gRPC SSL channel credentials.
        """
        if not isinstance(self.__ca, str):
            raise TypeError("'ca' must be of type str")
        if not isinstance(self.__key, str):
            raise TypeError("'key' must be of type str")
        if not isinstance(self.__cert, str):
            raise TypeError("'cert' must be of type str")

        try:
            with open(self.__ca, "rb") as ca_file, open(
                self.__key, "rb"
            ) as key_file, open(self.__cert, "rb") as cert_file:
                creds: ChannelCredentials = ssl_channel_credentials(
                    ca_file.read(), key_file.read(), cert_file.read()
                )
            return creds
        except Exception:
            print("failed to create channel credentials")
            raise

    def __validate_str(arg: str):
        """Check if arg is of type str and is not an empty string.

        Args:
            arg: An object of type str.

        Raises:
            TypeError: If arg is not of type str.
            ValueError: If arg is an empty string.
        """
        if not isinstance(arg, str):
            raise TypeError

        if len(arg) == 0:
            raise ValueError

    def __validate_uid(uid: int):
        """Validate the UID.
        Args:
            uid: The UID to validate.

        Raises:
            TypeError: If the UID is not of type int.
            ValueError: If the UID is not greater than or equal to 0.
        """
        if not isinstance(uid, int):
            raise TypeError("'uid' must be of type int")
        if uid < 0:
            raise ValueError("'uid' must be greater than or equal to 0")

    def __validate_gid(gid: int):
        """Validate the GID.
        Args:
            gid: The GID to validate.

        Raises:
            TypeError: If the GID is not of type int.
            ValueError: If the GID is not greater than or equal to 0.
        """
        if not isinstance(gid, int):
            raise TypeError("'gid' must be of type int")
        if gid < 0:
            raise ValueError("'gid' must be greater than or equal to 0")

    def get_personal_quota(self, uid: int, workspace: str) -> str:
        """Retrieve personal quota from DSMLPStorageController.

        Args:
            uid: The user id.
            workspace: The workspace name.

        Returns:
            The personal quota.
        """
        self.__validate_uid(uid)
        self.__validate_str(workspace)
        try:
            get_personal_quota_request = pb2.GetPersonalQuotaRequest(uid, workspace)
        except Exception:
            print("failed to create GetPersonalQuotaRequest")
            raise
        try:
            response = self.__stub.GetPersonalQuota(get_personal_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def set_personal_quota(self, uid: int, userquota: str, workspace: str) -> str:
        """Set personal quota in DSMLPStorageController.

        Args:
            uid: The user id.
            workspace: The workspace name.
            quota: The quota to set.

        Returns:
            The personal quota.
        """
        self.__validate_uid(uid)
        self.__validate_str(userquota)
        self.__validate_str(workspace)

        try:
            set_personal_quota_request = pb2.SetPersonalQuotaRequest(
                uid, userquota, workspace
            )
        except Exception:
            print("failed to create SetPersonalQuotaRequest")
            raise
        try:
            response = self.__stub.SetPersonalQuota(set_personal_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def get_team_quota(self, gid: int, workspace: str) -> str:
        """Retrieve team quota from DSMLPStorageController.

        Args:
            gid: The group id.
            workspace: The workspace name.

        Returns:
            The groupquota of the team.
        """
        self.__validate_gid(gid)
        self.__validate_str(workspace)

        try:
            get_team_quota_request = pb2.GetTeamQuotaRequest(gid, workspace)
        except Exception:
            print("failed to create GetTeamQuotaRequest")
            raise
        try:
            response = self.__stub.GetTeamQuota(get_team_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def set_team_quota(self, gid: int, groupquota: str, workspace: str):
        """Set team quota in DSMLPStorageController.

        Args:
            gid: The group id.
            groupquota: The groupquota of the team.
            workspace: The workspace name.
        """
        self.__validate_gid(gid)
        self.__validate_str(groupquota)
        self.__validate_str(workspace)

        try:
            set_team_quota_request = pb2.SetTeamQuotaRequest(gid, groupquota, workspace)
        except Exception:
            print("failed to create SetTeamQuotaRequest")
            raise
        try:
            response = self.__stub.SetTeamQuota(set_team_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def get_home_quota(self, uid: int) -> str:
        """Retrieve home quota from DSMLPStorageController.

        Args:
            uid: The user id.

        Returns:
            The home quota.
        """
        self.__validate_uid(uid)
        try:
            get_home_quota_request = pb2.GetHomeQuotaRequest(uid)
        except Exception:
            print("failed to create GetHomeQuotaRequest")
            raise
        try:
            response = self.__stub.GetHomeQuota(get_home_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def set_home_quota(self, uid: int, userquota: str):
        """Set home quota in DSMLPStorageController.

        Args:
            uid: The user id.
            userquota: The user quota to set.
        """
        self.__validate_uid(uid)
        self.__validate_str(userquota)
        try:
            set_home_quota_request = pb2.SetHomeQuotaRequest(uid, userquota)
        except Exception:
            print("failed to create SetHomeQuotaRequest")
            raise
        try:
            response = self.__stub.SetHomeQuota(set_home_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def create_workspace(self, workspace: str):
        """Create a workspace in DSMLPStorageController.

        Args:
            workspace: The workspace name.
        """
        self.__validate_str(workspace)
        try:
            create_workspace_request = pb2.CreateWorkspaceRequest(workspace)
        except Exception:
            print("failed to create CreateWorkspaceRequest")
            raise
        try:
            response = self.__stub.CreateWorkspace(create_workspace_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def create_home_directory(self, uid: int, username: str):
        """Create a home directory in DSMLPStorageController.

        Args:
            uid: The user id.
            username: The username of the user.
        """
        self.__validate_uid(uid)
        self.__validate_str(username)
        try:
            create_home_directory_request = pb2.CreateHomeDirectoryRequest(
                uid, username
            )
        except Exception:
            print("failed to create CreateHomeDirectoryRequest")
            raise
        try:
            response = self.__stub.CreateHomeDirectory(create_home_directory_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def get_list_of_home_directories(self) -> List[str]:
        """Get a list of home directories from DSMLPStorageController.

        Returns:
            A list of home directories.
        """
        try:
            list_home_directories_request = pb2.Void()
        except Exception:
            print("failed to create GetListOfHomeDirectoriesRequest")
            raise
        try:
            response = self.__stub.ListHomeDirectories(list_home_directories_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise
