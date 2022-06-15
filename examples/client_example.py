"""Example of how to use the DSMLP Storage Controller client"""

from os import getenv
from dotenv import load_dotenv
from dsmlpstoragecontrollerclient.client import Client
from dsmlpstoragecontrollerclient.clientargsmanager import ClientArgsManager
from dsmlpstoragecontrollerclient.clientconfig import ClientConfig
from dsmlpstoragecontrollerclient.clientrequestmethods import ClientRequestMethods
from dsmlpstoragecontrollerclient.connectionconfig import ConnectionConfig

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
        ),
        developer_mode=client_args_manager.in_developer_mode(),
        uid=client_args_manager.get_uid(),
        userquota=client_args_manager.get_userquota(),
        gid=client_args_manager.get_gid(),
        groupquota=client_args_manager.get_groupquota(),
        workspace=client_args_manager.get_workspace()
    )
    # Create client with ClientConfig object
    with Client(config) as client:
        request_method = client_args_manager.get_request_method()
        if request_method == ClientRequestMethods.GetPersonalQuota.value:
            personal_quota = client.get_personal_quota()
            print(personal_quota)
        elif request_method == ClientRequestMethods.SetPersonalQuota.value:
            client.set_personal_quota(
                uid=client_args_manager.get_uid(),
                userquota=client_args_manager.get_userquota(),
                workspace=client_args_manager.get_workspace(),
            )
        elif request_method == ClientRequestMethods.GetTeamQuota.value:
            team_quota = client.get_team_quota(
                gid=client_args_manager.get_gid(),
                workspace=client_args_manager.get_workspace(),
            )
            print(team_quota)
        elif request_method == ClientRequestMethods.SetTeamQuota.value:
            client.set_team_quota(
                gid=client_args_manager.get_gid(),
                groupquota=client_args_manager.get_groupquota(),
                workspace=client_args_manager.get_workspace(),
            )
        elif request_method == ClientRequestMethods.GetHomeQuota.value:
            home_quota = client.get_home_quota(uid=client_args_manager.get_uid())
            print(home_quota)
        elif request_method == ClientRequestMethods.SetHomeQuota.value:
            client.set_home_quota(
                uid=client_args_manager.get_uid(),
                userquota=client_args_manager.get_userquota(),
            )
        elif request_method == ClientRequestMethods.CreateWorkspace.value:
            client.create_workspace(workspace=client_args_manager.get_workspace())
        elif request_method == ClientRequestMethods.CreateHomeDirectory.value:
            client.create_home_directory(
                uid=client_args_manager.get_uid(),
                username=client_args_manager.get_username(),
            )
        elif request_method == ClientRequestMethods.ListHomeDirectories.value:
            home_directories = client.get_list_of_home_directories()
            print(home_directories)
