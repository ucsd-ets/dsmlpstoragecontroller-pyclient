from argparse import ArgumentParser, Namespace

from clientargs import ClientArgs


class ClientArgsManager():
    """Manage command line arguments for DSMLP Storage Controller client.

    Args:
        ca: The default CA certificate file absolute path.
        cert: The default client certificate file absolute path.
        key: The default client key file absolute path.
    """

    def __init__(self, ca: str, cert: str, key: str):
        """Initialize ClientArgsManager with ca, cert, and key arguments as default values to be used if not provided through the command line"""
        self.__args: Namespace = self.__get_args(ca, cert, key)

    def __get_args(self, ca: str, cert: str, key: str) -> Namespace:
        """Retrieve command line arguments.

        Returns:
            Command line arguments.
        """
        parser = ArgumentParser()
        parser.add_argument(
            ClientArgs.Request.hyphenate(), help="gRPC service request method name"
        )
        parser.add_argument(
            ClientArgs.CA.hyphenate(),
            default=ca,
            help="CA certificate file absolute path",
        )
        parser.add_argument(
            ClientArgs.Key.hyphenate(),
            default=key,
            help="TLS key file absolute path",
        )
        parser.add_argument(
            ClientArgs.Cert.hyphenate(),
            default=cert,
            help="TLS certificate file absolute path",
        )
        parser.add_argument(
            ClientArgs.Port.hyphenate(), default=9000, help="Client port number"
        )
        parser.add_argument(
            ClientArgs.Address.hyphenate(),
            default="localhost",
            help="Address for communicating with the gRPC service",
        )
        parser.add_argument(ClientArgs.Uid.hyphenate(), help="user uid")
        parser.add_argument(
            ClientArgs.Userquota.hyphenate(),
            help='user quota in the format of "-userquota=25G"',
        )
        parser.add_argument(ClientArgs.Username.hyphenate(), help="username")

        parser.add_argument(ClientArgs.Gid.hyphenate(), help="group gid")
        parser.add_argument(
            ClientArgs.Groupquota.hyphenate(),
            help='group quota in the format of "-groupquota=25G"',
        )
        parser.add_argument(ClientArgs.WorkspaceName.hyphenate(), help="name of workspace")

        args = parser.parse_args()
        return args

    def get_request_method(self) -> str:
        """Retrieve name of DSMLP Storage Controller gRPC service method from user input.

        Returns:
            The name of the DSMLP Storage Controller gRPC service request method.

        Raises:
            AttributeError: If the request method name has not been found in the Namespace object.
        """
        try:
            request_method: str = getattr(self.__args, "request")
        except AttributeError as e:
            print("failed to parse request method name")
            raise

        return request_method

    def get_address(self) -> str:
        """Retrieve address for communicating with DSMLP Storage Controller gRPC service from user input.

        Returns:
            The address for communicating with the server.
        """
        address: str = getattr(self.__args, "address", "localhost")

        return address

    def get_port(self) -> int:
        """Retrieve port number for communicating with DSMLP Storage Controller gRPC service from user input.

        Returns:
            The port number of the client.

        Raises:
            ValueError: If the port number cannot be converted to type int.
        """
        port: str | int = getattr(self.__args, "port", 9000)

        try:
            port: int = int(port)
        except ValueError:
            print("failed to convert port to int")
            raise

        return port

    def get_ca(self) -> str:
        """Retrieve path of ca file from user input.

        Returns:
            The path to the CA file for gRPC authentication.
        """
        try:
            ca: str = getattr(self.__args, "ca")
        except AttributeError:
            print("failed to find attribute 'ca'")
            raise

        return ca

    def get_key(self) -> str:
        """Retrieve path of key file from user input.

        Returns:
            The path to the key file for gRPC authentication.
        """
        try:
            key: str = getattr(self.__args, "key")
        except AttributeError:
            print("failed to find attribute 'key'")
            raise

        return key

    def get_cert(self) -> str:
        """Retrieve path of cert file from user input.

        Returns:
            The path to the cert file for gRPC authentication.
        """
        try:
            cert: str = getattr(self.__args, "cert")
        except AttributeError:
            print("failed to find attribute 'cert'")
            raise

        return cert

    def get_uid(self) -> int:
        """Retrieve user uid from user input.

        Returns:
            uid if it is valid

        Raises:
            AttributeError: If the uid has not been found in the Namespace object.
            ValueError: If uid cannot be converted to type int or if uid is not greater than or equal to 0.
        """
        try:
            uid: str | int = getattr(self.__args, "uid")
        except AttributeError as e:
            print("failed to find attribute 'uid'")
            raise

        if isinstance(uid, str):
            try:
                uid: int = int(uid)
                return uid
            except ValueError as e:
                print("failed to convert uid to int")
                raise
        elif isinstance(uid, int):
            if uid < 0:
                raise ValueError("uid must be greater than or equal to 0")
            else:
                return uid
        else:
            raise TypeError("uid command line argument must be of type str or int")

    def get_gid(self) -> int:
        """Retrieve group gid from user input.

        Returns:
            gid if it is valid.

        Raises:
            AttributeError: If gid has not been found in the Namespace object.
            ValueError: If gid cannot be converted to type int or if gid is not greater than or equal to 0.
        """
        try:
            gid: str | int = getattr(self.__args, "gid")
        except AttributeError as e:
            print("failed to find attribute 'gid'")
            raise

        if isinstance(gid, str):
            try:
                gid: int = int(gid)
                return gid
            except ValueError:
                print("failed to convert gid to int")
                raise
        elif isinstance(gid, int):
            if gid < 0:
                raise ValueError("gid must be greater than or equal to 0")
            else:
                return gid
        else:
            raise TypeError("gid command line argument must be of type str or int")

    def get_userquota(self) -> str:
        """Retrieve userquota from user input.

        Returns:
            The userquota from user input.

        Raises:
            AttributeError: If userquota has not been found in the Namespace object.
        """
        try:
            userquota: str = getattr(self.__args, "userquota")
        except AttributeError:
            print("failed to parse userquota")
            raise

        return userquota

    def get_groupquota(self) -> str:
        """Retrieve groupquota from user input.

        Returns:
            The groupquota from user input.

        Raises:
            AttributeError: If groupquota has not been found in the Namespace object.
        """
        try:
            groupquota: str = getattr(self.__args, "groupquota")
        except AttributeError as e:
            print("failed to parse groupquota")
            raise

        return groupquota

    def get_workspace_name(self) -> str:
        """Retrieve workspace name from user input.

        Returns:
            The workspace name from user input.

        Raises:
            AttributeError: If workspace name has not been found in the Namespace object.
        """
        try:
            workspace_name: str = getattr(self.__args, "workspace_name")
        except AttributeError as e:
            print("failed to parse workspace name")
            raise

        return workspace_name

    def get_username(self) -> str:
        """Retrieve username from user input.

        Returns:
            The username from user input.

        Raises:
            AttributeError: If username has not been found in the Namespace object.
        """
        try:
            username: str = getattr(self.__args, "username")
        except AttributeError as e:
            print("failed to parse username")
            raise

        return username
