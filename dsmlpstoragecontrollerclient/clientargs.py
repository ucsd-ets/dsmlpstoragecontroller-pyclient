from enum import Enum


class ClientArgs(Enum):
    """Command line arguments for client."""

    Request = "request"
    CA = "ca"
    Key = "key"
    Cert = "cert"
    Port = "port"
    Address = "address"
    DeveloperMode = "developerMode"

    Uid = "uid"
    Userquota = "userquota"
    Username = "username"
    Gid = "gid"
    Groupquota = "groupquota"
    Workspace = "workspace"

    def hyphenate(self) -> str:
        """Prepends '-' to value of enumeration.

        Returns:
            Hyphenated enumeration value.
        """
        return f"-{self.value}"
