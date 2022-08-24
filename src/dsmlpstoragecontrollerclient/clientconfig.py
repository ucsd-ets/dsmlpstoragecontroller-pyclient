from dsmlpstoragecontrollerclient.connectionconfig import ConnectionConfig


class ClientConfig:
    """Config for DSMLP Storage Controller client
    Args:
        connection_config: The connection config for the DSMLP Storage Controller gRPC Service.
        uid: The user id.
        userquota: The user quota.
        username: The username.
        gid: The group id.
        groupquota: The group quota.
        workspace_name: Name of the workspace.
    """

    def __init__(
        self,
        connection_config: ConnectionConfig,
        uid: int = None,
        userquota: str = None,
        username: str = None,
        gid: int = None,
        groupquota: str = None,
        workspace_name: str = None,
    ):

        self.connection_config: ConnectionConfig = connection_config

        if uid is not None:
            self.uid: int = uid
        else:
            self.__uid = None

        if userquota is not None:
            self.userquota: str = userquota
        else:
            self.__userquota = None

        if username is not None:
            self.username: str = username
        else:
            self.__username = None

        if gid is not None:
            self.gid: int = gid
        else:
            self.__gid = None

        if groupquota is not None:
            self.groupquota: str = groupquota
        else:
            self.__groupquota = None

        if workspace_name is not None:
            self.workspace_name: str = workspace_name
        else:
            self.__workspace_name = None

        self.connection_config.creds = (
            self.connection_config.create_channel_credentials()
        )

    @property
    def connection_config(self) -> ConnectionConfig:
        return self.__connection_config

    @connection_config.setter
    def connection_config(self, connection_config: ConnectionConfig):
        self.__validate_connection_config(connection_config)
        self.__connection_config = connection_config

    @property
    def uid(self) -> int:
        return self.__uid

    @uid.setter
    def uid(self, uid: int):
        self.__uid = uid

    @property
    def userquota(self) -> str:
        return self.__userquota

    @userquota.setter
    def userquota(self, userquota: str):
        self.__userquota = userquota

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def gid(self) -> int:
        return self.__gid

    @gid.setter
    def gid(self, gid: int):
        self.__gid = gid

    @property
    def workspace_name(self) -> str:
        return self.__workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name: str):
        self.__workspace_name = workspace_name

    @property
    def groupquota(self) -> str:
        return self.__groupquota

    @groupquota.setter
    def groupquota(self, groupquota: str):
        self.__groupquota = groupquota

    @staticmethod
    def __validate_connection_config(connection_config: ConnectionConfig):
        """Validate the connection config.
        Args:
            connection_config: The connection config to validate.

        Raises:
            TypeError: If the connection config is not of type ConnectionConfig.
        """

        if not isinstance(connection_config, ConnectionConfig):
            raise TypeError(f"'connection_config' must be of type ConnectionConfig")
