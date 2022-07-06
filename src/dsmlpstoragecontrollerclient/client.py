from typing import List

from grpc import secure_channel
from dsmlpstoragecontrollerclient.clientconfig import ClientConfig

from .dsmlpstoragecontrollerservice_pb2 import *
from .dsmlpstoragecontrollerservice_pb2_grpc import DSMLPStorageControllerServiceStub


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
                gid=self.config.gid, groupquota=self.config.groupquota, workspaceName=self.config.workspace_name
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

    def create_workspace_name(self):
        """Create a workspace name in DSMLPStorageController."""
        try:
            create_workspace_request = CreateWorkspaceRequest(workspaceName=self.config.workspace_name)
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

if __name__ == "__main__":
    from os import getenv
    from dotenv import load_dotenv
    from clientargsmanager import ClientArgsManager
    from clientrequestmethods import ClientRequestMethods
    from connectionconfig import ConnectionConfig

    # Load environment variables from .env file
    load_dotenv()
    CA = getenv("DSMLP_STORAGE_CONTROLLER_CA")
    CERT = getenv("DSMLP_STORAGE_CONTROLLER_CERT")
    KEY = getenv("DSMLP_STORAGE_CONTROLLER_KEY")

    # Retrieve command line arguments using ClientArgsManager
    client_args_manager = ClientArgsManager(ca=CA, cert=CERT, key=KEY)

    # Create ClientConfig object
    config = ClientConfig(
        connection_config=ConnectionConfig(
            ca=client_args_manager.get_ca(),
            key=client_args_manager.get_key(),
            cert=client_args_manager.get_cert(),
            port=client_args_manager.get_port(),
            address=client_args_manager.get_address()
        )
    )
    # Create client with ClientConfig object
    with Client(config) as client:
        request_method = client_args_manager.get_request_method()
        if request_method == ClientRequestMethods.GetPersonalQuota.value:
            config.uid = client_args_manager.get_uid()
            config.workspace_name = client_args_manager.get_workspace_name()
            personal_quota = client.get_personal_quota()
            print(personal_quota)
        elif request_method == ClientRequestMethods.SetPersonalQuota.value:
            config.uid = client_args_manager.get_uid()
            config.userquota = client_args_manager.get_userquota()
            config.workspace_name= client_args_manager.get_workspace_name()
            client.set_personal_quota()
        elif request_method == ClientRequestMethods.GetTeamQuota.value:
            config.gid = client_args_manager.get_gid()
            config.workspace_name= client_args_manager.get_workspace_name()
            team_quota = client.get_team_quota()
            print(team_quota)
        elif request_method == ClientRequestMethods.SetTeamQuota.value:
            config.gid = client_args_manager.get_gid()
            config.groupquota = client_args_manager.get_groupquota()
            config.workspace_name= client_args_manager.get_workspace_name()
            client.set_team_quota()
        elif request_method == ClientRequestMethods.GetHomeQuota.value:
            config.uid = client_args_manager.get_uid()
            home_quota = client.get_home_quota()
            print(home_quota)
        elif request_method == ClientRequestMethods.SetHomeQuota.value:
            config.uid = client_args_manager.get_uid()
            config.userquota = client_args_manager.get_userquota()
            client.set_home_quota()
        elif request_method == ClientRequestMethods.CreateWorkspace.value:
            config.workspace_name= client_args_manager.get_workspace_name()
            client.create_workspace()
        elif request_method == ClientRequestMethods.CreateHomeDirectory.value:
            config.uid = client_args_manager.get_uid()
            config.username = client_args_manager.get_username()
            client.create_home_directory()
        elif request_method == ClientRequestMethods.ListHomeDirectories.value:
            home_directories = client.get_list_of_home_directories()
            print(home_directories)