# DSMLP Storage Controller Python Client

## Description

This repository is for the Python client of the DSMLP Storage Controller gRPC Service. The name of the Python package is `dsmlpstoragecontrollerclient`. For more information, please refer to the provided [example](https://github.com/ucsd-ets/dsmlpstoragecontroller-pyclient/blob/main/dsmlpstoragecontrollerclient/example.py).

## Required for Client Operations

### ClientConfig

The `ClientConfig` class stores the configuration data that is used by the `Client` class.

### Client

The `Client` class provides the available gRPC functions for communicating with the server. It must be used as a context manager (`with` statement is required).

### Environment Variables Configuration

1. Create a '.env' file in the 'dsmlpstoragecontrollerclient' directory.
2. Specify the following environment variables in the '.env' file:
    - DSMLP_STORAGE_CONTROLLER_PORT: the port for communicating with the gRPC service
    - DSMLP_STORAGE_CONTROLLER_ADDRESS: the address for communicating with the gRPC service
    - DSMLP_STORAGE_CONTROLLER_CA: the absolute file path of the CA
    - DSMLP_STORAGE_CONTROLLER_CERT: the absolute file path of the CERT
    - DSMLP_STORAGE_CONTROLLER_KEY: the absolute file path of the KEY

.env
```
DSMLP_STORAGE_CONTROLLER_PORT=
DSMLP_STORAGE_CONTROLLER_ADDRESS=
DSMLP_STORAGE_CONTROLLER_CA=
DSMLP_STORAGE_CONTROLLER_CERT=
DSMLP_STORAGE_CONTROLLER_KEY=
```

## Optional: For Command Line Operations

### ClientArgs

The `ClientArgs` class contains command line argument options for `ClientArgsManager`.

### ClientArgsManager

The `ClientArgsManager` class is used for parsing command line arguments, which can then be passed as arguments to the client.