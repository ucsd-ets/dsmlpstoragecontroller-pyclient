# DSMLP Storage Controller Python Client

## Description

The name of the Python package is `dsmlpstoragecontrollerclient`. The `ClientArgsManager` class is used for parsing command line arguments, which can then be passed as arguments to the client. The `Client` class provides the available gRPC functions for communicating with the server. It must be used as a context manager (`with` statement is required). Please refer to `client_example.py` in the examples directory.

# Environment Variables Configuration
1. Create a `.env` file in the `dsmlpstoragecontrollerclient` directory.
2. Specify the following environment variables in the '.env' file:
    - PORT: the port for communicating with the gRPC service
    - ADDRESS: the address for communicating with the gRPC service
    - CA: the absolute file path of the CA
    - CERT: the absolute file path of the CERT
    - KEY: the absolute file path of the KEY

.env
```
PORT=
ADDRESS=
CA=
CERT=
KEY=
```