from grpc import ChannelCredentials, ssl_channel_credentials


class ConnectionConfig:
    """The connection config for the client.

    Args:
        ca: The path of the CA file used for gRPC authentication.
        key: The path of the key file used for gRPC authentication.
        cert: The path of the cert file used for gRPC authentication.
        port: The port used for communicating with the DSMLP Storage Controller gRPC Service.
        address: The address used for communicating with the DSMLP Storage Controller gRPC Service.
    """
    def __init__(
        self, ca: str, key: str, cert: str, port: int, address: str = "localhost"
    ):
        self.ca: str = ca
        self.key: str = key
        self.cert: str = cert
        self.port: int = port
        self.address: str = address
        self.__creds: ChannelCredentials | None = None

    @property
    def ca(self) -> str:
        return self.__ca

    @ca.setter
    def ca(self, ca: str):
        self.__ca = ca

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def cert(self) -> str:
        return self.__cert

    @cert.setter
    def cert(self, cert: str):
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
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def creds(self) -> ChannelCredentials:
        return self.__creds

    @creds.setter
    def creds(self, creds: ChannelCredentials):
        if not isinstance(creds, ChannelCredentials):
            raise TypeError(f"'creds' must be of type ChannelCredentials")
        self.__creds = creds

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
