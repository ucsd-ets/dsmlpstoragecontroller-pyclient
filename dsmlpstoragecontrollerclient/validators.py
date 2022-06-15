def validate_str(arg: str, name: str):
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


def validate_uid_or_gid(id: int, name: str):
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
        raise TypeError(f"'name' argument must have a value of either 'uid' or 'gid'")

    if not isinstance(id, int):
        raise TypeError(f"'{name}' must be of type int")
    if id < 0:
        raise ValueError(f"'{name}' must be greater than or equal to 0")
