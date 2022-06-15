from grpc import ChannelCredentials, ssl_channel_credentials


class ClientConfig:
    """Config for DSMLP Storage Controller client
    Args:
        ca: The path of the CA file used for gRPC authentication.
        key: The path of the key file used for gRPC authentication.
        cert: The path of the cert file used for gRPC authentication.
        port: The port used for communicating with the DSMLP Storage Controller gRPC Service.
        address: The address used for communicating with the DSMLP Storage Controller gRPC Service.
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
        ca: str,
        key: str,
        cert: str,
        port: int,
        address: str = "localhost",
        developer_mode = False,
        uid: int | None = None,
        userquota: str | None = None,
        username: str | None = None,
        gid: int | None = None,
        groupquota: str | None = None,
        workspace: str | None = None,
    ):

        self.ca: str = ca
        self.key: str = key
        self.cert: str = cert
        self.port: str = port
        self.address: str = address
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
            self.creds: ChannelCredentials = self.create_channel_credentials()
        else:
            self.__creds = None

    @property
    def ca(self) -> str:
        return self.__ca

    @ca.setter
    def ca(self, ca: str):
        self.__validate_str(ca, "ca")
        self.__ca = ca

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__validate_str(key, "key")
        self.__key = key

    @property
    def cert(self) -> str:
        return self.__cert

    @cert.setter
    def cert(self, cert: str):
        self.__validate_str(cert, "cert")
        self.__cert = cert

    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        if not isinstance(port, int):
            raise TypeError("'port' must be of type int")
        if port < 0:
            raise ValueError("'port' must be greater than or equal to 0")
        self.__port = port

    @property
    def address(self) -> str | None:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__validate_str(address, "address")
        self.__address = address

    @property
    def uid(self) -> int | None:
        return self.__uid

    @uid.setter
    def uid(self, uid: int):
        self.__validate_uid_or_gid(uid, "uid")
        self.__uid = uid

    @property
    def userquota(self) -> str | None:
        return self.__userquota

    @userquota.setter
    def userquota(self, userquota: str):
        self.__validate_str(userquota, "userquota")
        self.__userquota = userquota

    @property
    def username(self) -> str | None:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__validate_str(username, "username")
        self.__username = username

    @property
    def gid(self) -> int | None:
        return self.__gid

    @gid.setter
    def gid(self, gid: int):
        self.__validate_uid_or_gid(gid, "gid")
        self.__gid = gid

    @property
    def workspace(self) -> str | None:
        return self.__workspace

    @workspace.setter
    def workspace(self, workspace: str):
        self.__validate_str(workspace, "workspace")
        self.__workspace = workspace

    @property
    def groupquota(self) -> str | None:
        return self.__groupquota

    @groupquota.setter
    def groupquota(self, groupquota: str):
        self.__validate_str(groupquota, "groupquota")
        self.__groupquota = groupquota

    @property
    def creds(self) -> str | None:
        return self.__creds

    @creds.setter
    def creds(self, creds: ChannelCredentials):
        if not isinstance(creds, ChannelCredentials):
            raise TypeError(f"'creds' must be of type ChannelCredentials")
        self.__creds = creds

    @property
    def developer_mode(self) -> bool:
        return self.__developer_mode

    @developer_mode.setter
    def developer_mode(self, developer_mode: bool):
        if not isinstance(developer_mode, bool):
            raise TypeError("'developer_mode' must be of type bool")
        self.__developer_mode = developer_mode

    @staticmethod
    def __validate_str(arg: str, name: str):
        """Check if arg is of type str and is not an empty string.

        Args:
            arg: An object of type str.
            name: The name of the argument.

        Raises:
            TypeError: If name or arg is not of type str.
            ValueError: If name or arg is an empty string.
        """
        if not isinstance(name, str):
            raise TypeError(f"'name' argument must be of type str")

        if len(name) == 0:
            raise ValueError(f"'name' argument must not be an empty string")

        if not isinstance(arg, str):
            raise TypeError(f"'arg' argument must be of type str")

        if len(arg) == 0:
            raise ValueError(f"'arg' argument must not be an empty string")

    @staticmethod
    def __validate_uid_or_gid(id: int, name: str):
        """Validate a UID or GID.
        Args:
            id: The UID or GID to validate.
            name: Either 'uid' or 'gid'.

        Raises:
            TypeError: If the UID or GID is not of type int.
            ValueError: If the UID or GID is not greater than or equal to 0.
        """
        if not isinstance(name, str):
            raise TypeError(f"'name' argument must be of type str")

        if name != "uid" and name != "gid":
            raise TypeError(
                f"'name' argument must have a value of either 'uid' or 'gid'"
            )

        if not isinstance(id, int):
            raise TypeError(f"'{name}' must be of type int")
        if id < 0:
            raise ValueError(f"'{name}' must be greater than or equal to 0")

    def create_channel_credentials(self) -> ChannelCredentials:
        """Retrieve gRPC SSL channel credentials.
        Args:
            cert: The path of the cert file used for gRPC authentication.

        Returns:
            The gRPC SSL channel credentials.
        """
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
