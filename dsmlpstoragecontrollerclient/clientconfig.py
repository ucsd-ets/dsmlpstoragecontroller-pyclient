from dsmlpstoragecontrollerclient.connectionconfig import ConnectionConfig

from dsmlpstoragecontrollerclient.validators import validate_str, validate_uid_or_gid


class ClientConfig:
    """Config for DSMLP Storage Controller client
    Args:
        connection_config: The connection config for the DSMLP Storage Controller gRPC Service.
        developer_mode: Whether or not the client is in developer mode.
        uid: The user id.
        userquota: The user quota.
        username: The username.
        gid: The group id.
        groupquota: The group quota.
        workspace: Name of the workspace.
    """

    def __init__(
        self,
        connection_config: ConnectionConfig,
        developer_mode=False,
        uid: int | None = None,
        userquota: str | None = None,
        username: str | None = None,
        gid: int | None = None,
        groupquota: str | None = None,
        workspace: str | None = None,
    ):

        self.connection_config: ConnectionConfig = connection_config
        self.developer_mode: bool = developer_mode

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

        if workspace is not None:
            self.workspace: str = workspace
        else:
            self.__workspace = None

        if not self.developer_mode:
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
    def uid(self) -> int | None:
        return self.__uid

    @uid.setter
    def uid(self, uid: int):
        validate_uid_or_gid(uid, "uid")
        self.__uid = uid

    @property
    def userquota(self) -> str | None:
        return self.__userquota

    @userquota.setter
    def userquota(self, userquota: str):
        validate_str(userquota, "userquota")
        self.__userquota = userquota

    @property
    def username(self) -> str | None:
        return self.__username

    @username.setter
    def username(self, username: str):
        validate_str(username, "username")
        self.__username = username

    @property
    def gid(self) -> int | None:
        return self.__gid

    @gid.setter
    def gid(self, gid: int):
        validate_uid_or_gid(gid, "gid")
        self.__gid = gid

    @property
    def workspace(self) -> str | None:
        return self.__workspace

    @workspace.setter
    def workspace(self, workspace: str):
        validate_str(workspace, "workspace")
        self.__workspace = workspace

    @property
    def groupquota(self) -> str | None:
        return self.__groupquota

    @groupquota.setter
    def groupquota(self, groupquota: str):
        validate_str(groupquota, "groupquota")
        self.__groupquota = groupquota

    @property
    def developer_mode(self) -> bool:
        return self.__developer_mode

    @developer_mode.setter
    def developer_mode(self, developer_mode: bool):
        if not isinstance(developer_mode, bool):
            raise TypeError("'developer_mode' must be of type bool")
        self.__developer_mode = developer_mode

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
