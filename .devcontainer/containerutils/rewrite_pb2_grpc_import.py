"""This module is for rewriting the broken gRPC statement that is automatically generated
by the 'dsmlpstoragecontroller_pb2_grpc.py' file
"""

import argparse

def retrieve_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="DSMLP Storage Controller Python Proto File Rewriter",
        description="""This module rewrites the import of 'dsmlpstoragecontrollerservice_pb2.py'
                    inside of 'dsmlpstoragecontrollerservice_pb2_grpc.py' and updates the code
                    using the module to reflect the change in import statement syntax.
                    """,
        add_help=True,
        allow_abbrev=True,
        exit_on_error=True
    )
    
    parser.add_argument(
        "-p",
        "--pb2_grpc_path",
        type=str,
        default="/tmp/protos/build/dsmlpstoragecontrollerservice_pb2_grpc.py",
        help="Absolute path of 'dsmlpstoragecontrollerservice_pb2_grpc.py'"
    )

    args = parser.parse_args()

    if not hasattr(args, "pb2_grpc_path"):
        raise AttributeError("'pb2_grpc_path' argument is missing")
    
    return args

def rewrite_import(pb2_grpc_path: str) -> None:
    """Rewrites broken gRPC import statement found on line 5 and
    modifies the rest of the file to match the new import statement.
    """
    with open(pb2_grpc_path, mode="r+", encoding="UTF-8") as pb2_grpc_file:
        lines = pb2_grpc_file.readlines()

    if (
        "import dsmlpstoragecontrollerservice_pb2 as dsmlpstoragecontrollerservice__pb2"
        not in lines[4]
    ):
        raise Exception(
            f"""Import statement not found in 'dsmlpstoragecontrollerservice_pb2_grpc.py' file. 
            Check if the gRPC proto compiler output has changed.
            Line 5: {lines[4]}
            """
        )

    lines[4] = "from .dsmlpstoragecontrollerservice_pb2 import *"

    for i in range(4, len(lines)):
        lines[i] = lines[i].replace("dsmlpstoragecontrollerservice__pb2.", "")

    with open(pb2_grpc_path, mode="w+", encoding="UTF-8") as pb2_grpc_file:
        pb2_grpc_file.writelines(lines)


if __name__ == "__main__":
    args: argparse.Namespace = retrieve_args()
    pb2_grpc_path: str = getattr(args, "pb2_grpc_path")
    rewrite_import(pb2_grpc_path)