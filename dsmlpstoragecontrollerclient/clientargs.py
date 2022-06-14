from enum import Enum


class ClientArgs(Enum):
    """Command line arguments for client."""

    Request = "request"
    Address = "address"
    Port = "port"
    CA = "ca"
    Cert = "cert"
    Key = "key"
    Verify = "verify"
    Uid = "uid"
    Gid = "gid"
    Userquota = "userquota"
    Groupquota = "groupquota"
    Workspace = "workspace"
    Username = "username"
    DeveloperMode = "developerMode"

    def hyphenate(self) -> str:
        """Prepends '-' to value of enumeration.

        Returns:
            Hyphenated enumeration value.
        """
        return f"-{self.value}"
