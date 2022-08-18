from typing import List

from grpc import secure_channel
from dsmlpstoragecontrollerclient.clientconfig import ClientConfig

from dsmlpstoragecontrollerclient.dsmlpstoragecontrollerservice_pb2 import *
from dsmlpstoragecontrollerclient.dsmlpstoragecontrollerservice_pb2_grpc import DSMLPStorageControllerServiceStub


class Client:
    """The client for the DSMLPStorageController service.

    Args:
        config: The configuration for the client.
    """

    def __init__(self, config: ClientConfig):
        self.config = config

    @property
    def config(self) -> ClientConfig:
        return self.__config

    @config.setter
    def config(self, config: ClientConfig):
        self.__validate_config(config)
        self.__config = config

    def __enter__(self):
        self.__channel = secure_channel(
            target=f"{self.config.connection_config.address}:{self.config.connection_config.port}",
            credentials=self.config.connection_config.creds,
            options=[('grpc.max_receive_message_length', (1024*1024*8))]
        )

        try:
            self.__stub = DSMLPStorageControllerServiceStub(self.__channel)
        except Exception:
            print("failed to create stub for channel")
            raise

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__channel.close()

    @staticmethod
    def __validate_config(config: ClientConfig):
        """Check if config is of type ClientConfig.

        Args:
            config: An object of type ClientConfig.

        Raises:
            TypeError: If config is not of type ClientConfig.
        """
        if not isinstance(config, ClientConfig):
            raise TypeError("'config' must be of type ClientConfig")

    def get_personal_quota(self) -> str:
        """Retrieve personal quota from DSMLPStorageController.

        Returns:
            The personal quota.
        """
        try:
            get_personal_quota_request = GetPersonalQuotaRequest(
                uid=self.config.uid, workspaceName=self.config.workspace_name
            )
        except Exception:
            print("failed to create GetPersonalQuotaRequest")
            raise
        try:
            response = self.__stub.GetPersonalQuota(get_personal_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def set_personal_quota(self) -> str:
        """Set personal quota in DSMLPStorageController.

        Returns:
            The personal quota.
        """
        try:
            set_personal_quota_request = SetPersonalQuotaRequest(
                uid=self.config.uid, userquota=self.config.userquota, workspaceName=self.config.workspace_name
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

    def get_team_quota(self) -> str:
        """Retrieve team quota from DSMLPStorageController.

        Returns:
            The groupquota of the team.
        """
        try:
            get_team_quota_request = GetTeamQuotaRequest(
                gid=self.config.gid, workspaceName=self.config.workspace_name
            )
        except Exception:
            print("failed to create GetTeamQuotaRequest")
            raise
        try:
            response = self.__stub.GetTeamQuota(get_team_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def set_team_quota(self):
        """Set team quota in DSMLPStorageController."""
        try:
            set_team_quota_request = SetTeamQuotaRequest(
                gid=self.config.gid,
                groupquota=self.config.groupquota,
                workspaceName=self.config.workspace_name
            )
        except Exception:
            print("failed to create SetTeamQuotaRequest")
            raise
        try:
            response = self.__stub.SetTeamQuota(set_team_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def get_home_quota(self) -> str:
        """Retrieve home quota from DSMLPStorageController.

        Returns:
            The home quota.
        """
        try:
            get_home_quota_request = GetHomeQuotaRequest(uid=self.config.uid)
        except Exception:
            print("failed to create GetHomeQuotaRequest")
            raise
        try:
            response = self.__stub.GetHomeQuota(get_home_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def set_home_quota(self):
        """Set home quota in DSMLPStorageController."""
        try:
            set_home_quota_request = SetHomeQuotaRequest(
                uid=self.config.uid, userquota=self.config.userquota
            )
        except Exception:
            print("failed to create SetHomeQuotaRequest")
            raise
        try:
            response = self.__stub.SetHomeQuota(set_home_quota_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def create_workspace(self):
        """Create a workspace with the given name in DSMLPStorageController."""
        try:
            create_workspace_request = CreateWorkspaceRequest(uid=self.config.uid, name=self.config.workspace_name)
        except Exception:
            print("failed to create CreateWorkspaceRequest")
            raise
        try:
            response = self.__stub.CreateWorkspace(create_workspace_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise

    def create_home_directory(self):
        """Create a home directory in DSMLPStorageController."""
        try:
            create_home_directory_request = CreateHomeDirectoryRequest(
                uid=self.config.uid, username=self.config.username
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
            list_home_directories_request = Void()
        except Exception:
            print("failed to create GetListOfHomeDirectoriesRequest")
            raise
        try:
            response = self.__stub.ListHomeDirectories(list_home_directories_request)
            return response
        except Exception:
            print("error occurred while processing request")
            raise
