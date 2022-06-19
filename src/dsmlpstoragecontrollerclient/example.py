"""Example of how to use the DSMLP Storage Controller client"""

from os import getenv
from dotenv import load_dotenv
from client import Client
from clientargsmanager import ClientArgsManager
from clientconfig import ClientConfig
from clientrequestmethods import ClientRequestMethods
from connectionconfig import ConnectionConfig

if __name__ == "__main__":
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
