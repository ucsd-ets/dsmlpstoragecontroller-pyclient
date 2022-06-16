from enum import Enum


class ClientArgs(Enum):
    """Command line arguments for client."""

    Request = "request"
    CA = "ca"
    Key = "key"
    Cert = "cert"
    Port = "port"
    Address = "address"

    Uid = "uid"
    Userquota = "userquota"
    Username = "username"
    Gid = "gid"
    Groupquota = "groupquota"
    WorkspaceName = "workspace_name"

    def hyphenate(self) -> str:
        """Prepends '-' to value of enumeration.

        Returns:
            Hyphenated enumeration value.
        """
        return f"-{self.value}"
