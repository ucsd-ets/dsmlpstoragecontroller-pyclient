from argparse import ArgumentParser, Namespace
from sys import exit

from dsmlpstoragecontrollerclient.clientargs import ClientArgs
from dsmlpstoragecontrollerclient.validators import validate_str


class ClientArgsManager(ClientArgs):
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
        validate_str(ca)
        validate_str(cert)
        validate_str(key)

        parser = ArgumentParser()
        parser.add_argument(
            self.Request.hyphenate(), help="gRPC service request method name"
        )
        parser.add_argument(
            self.CA.hyphenate(),
            default=ca,
            help="CA certificate file absolute path",
        )
        parser.add_argument(
            self.Key.hyphenate(),
            default=key,
            help="TLS key file absolute path",
        )
        parser.add_argument(
            self.Cert.hyphenate(),
            default=cert,
            help="TLS certificate file absolute path",
        )
        parser.add_argument(
            self.Port.hyphenate(), default=9000, help="Client port number"
        )
        parser.add_argument(
            self.Address.hyphenate(),
            default=9000,
            help="Address for communicating with the gRPC service",
        )
        parser.add_argument(self.DeveloperMode.hyphenate(), help="developer mode")

        parser.add_argument(self.Uid.hyphenate(), help="user uid")
        parser.add_argument(
            self.Userquota.hyphenate(),
            help='user quota in the format of "-userquota=25G"',
        )
        parser.add_argument(self.Username.hyphenate(), help="username")

        parser.add_argument(self.Gid.hyphenate(), help="group gid")
        parser.add_argument(
            self.Groupquota.hyphenate(),
            help='group quota in the format of "-groupquota=25G"',
        )
        parser.add_argument(self.Workspace.hyphenate(), help="name of workspace")

        args = parser.parse_args()
        return args

    def __validate_str(arg: str):
        """Check if arg is of type str and is not an empty string.

        Args:
            arg: An object of type str.

        Raises:
            TypeError: If arg is not of type str.
        """
        if not isinstance(arg, str):
            raise TypeError

        if len(arg) == 0:
            raise ValueError

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
            print(e)
            exit("failed to parse request method name")

        validate_str(request_method)

        return request_method

    def get_address(self) -> str:
        """Retrieve address for communicating with DSMLP Storage Controller gRPC service from user input.

        Returns:
            The address for communicating with the server.
        """
        address: str = getattr(self.__args, "address", "localhost")

        validate_str(address)

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
            exit("failed to convert port to int")

        return port

    def get_ca(self) -> str:
        """Retrieve path of ca file from user input.

        Returns:
            The path to the CA file for gRPC authentication.
        """
        try:
            ca: str = getattr(self.__args, "ca")
        except AttributeError as e:
            print(e)
            raise

        validate_str(ca)

        return ca

    def get_cert(self) -> str:
        """Retrieve path of cert file from user input.

        Returns:
            The path to the cert file for gRPC authentication.
        """
        try:
            cert: str = getattr(self.__args, "cert")
        except AttributeError as e:
            print(e)
            raise

        validate_str(cert)

        return cert

    def get_key(self) -> str:
        """Retrieve path of key file from user input.

        Returns:
            The path to the key file for gRPC authentication.
        """
        try:
            key: str = getattr(self.__args, "key")
        except AttributeError as e:
            print(e)
            raise

        validate_str(key)

        return key

    def get_uid(self) -> int:
        """Retrieve user uid from user input.

        Returns:
            uid if it is valid and -1 if uid is invalid.

        Raises:
            AttributeError: If the uid has not been found in the Namespace object.
            ValueError: If uid cannot be converted to type int or if uid is not greater than or equal to 0.
        """
        try:
            uid: str | int = getattr(self.__args, "uid")
        except AttributeError as e:
            return -1

        if isinstance(uid, str):
            try:
                uid: int = int(uid)
                return uid
            except ValueError as e:
                print(e)
                exit("failed to convert uid to int")
        elif isinstance(uid, int):
            if uid < 0:
                raise ValueError("uid must be greater than or equal to 0")
            else:
                return uid

        return -1

    def get_gid(self) -> int:
        """Retrieve group gid from user input.

        Returns:
            gid if it is valid. -1 if gid is invalid.

        Raises:
            AttributeError: If gid has not been found in the Namespace object.
            ValueError: If gid cannot be converted to type int or if gid is not greater than or equal to 0.
        """
        try:
            gid: str | int = getattr(self.__args, "gid")
        except AttributeError as e:
            return -1

        if isinstance(gid, str):
            try:
                gid: int = int(gid)
                return gid
            except ValueError as e:
                print(e)
                exit("failed to convert gid to int")
        elif isinstance(gid, int):
            if gid < 0:
                raise ValueError("gid must be greater than or equal to 0")
            else:
                return gid

        return -1

    def get_userquota(self) -> str:
        """Retrieve userquota from user input.

        Returns:
            The userquota from user input.

        Raises:
            AttributeError: If userquota has not been found in the Namespace object.
        """
        try:
            userquota: str = getattr(self.__args, "userquota")
        except AttributeError as e:
            print(e)
            exit("failed to parse userquota")

        validate_str(userquota)

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
            print(e)
            exit("failed to parse groupquota")

        validate_str(groupquota)

        return groupquota

    def get_workspace(self) -> str:
        """Retrieve workspace from user input.

        Returns:
            The workspace from user input.

        Raises:
            AttributeError: If workspace name has not been found in the Namespace object.
        """
        try:
            workspace: str = getattr(self.__args, "workspace")
        except AttributeError as e:
            print(e)
            exit("failed to parse workspace name")

        validate_str(workspace)

        return workspace

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
            print(e)
            exit("failed to parse username")

        validate_str(username)

        return username

    def in_developer_mode(self) -> bool:
        """Check if client should be in developer mode from user input.

        Returns:
            Whether or not the client should be in developer mode.

        Raises:
            AttributeError: If developer_mode has not been found in the Namespace object.
        """
        try:
            developer_mode: bool = getattr(self.__args, "developer_mode")
        except AttributeError as e:
            print(e)
            exit("failed to parse developer_mode")

        if not isinstance(developer_mode, bool):
            raise TypeError("'developer_mode' must be of type bool")

        return developer_mode
