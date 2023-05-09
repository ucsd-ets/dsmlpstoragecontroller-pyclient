# DSMLP Storage Controller Python Client

## Description

This repository is for the Python client of the <a href="https://github.com/ucsd-ets/dsmlpstoragecontroller" target="_blank">DSMLP Storage Controller gRPC Service</a>. The name of the Python package is [dsmlpstoragecontrollerclient](https://github.com/ucsd-ets/dsmlpstoragecontroller-pyclient/tree/main/src/dsmlpstoragecontrollerclient). If you would like to use the client with command line arguments, please refer to [client.py](https://github.com/ucsd-ets/dsmlpstoragecontroller-pyclient/blob/main/src/dsmlpstoragecontrollerclient/client.py).

**Minimum Python Version:** 3.11.0

## Proto Files

Proto file generation is automated in the Dev Container. If the proto file is compiled without the Dev Container, the import statements will need to be edited manually.

## Required for Client Operations

### ClientConfig

The [ClientConfig](https://github.com/ucsd-ets/dsmlpstoragecontroller-pyclient/blob/main/src/dsmlpstoragecontrollerclient/clientconfig.py) class stores the configuration data that is used by the [Client](#client) class.

### Client

The [Client](https://github.com/ucsd-ets/dsmlpstoragecontroller-pyclient/blob/main/src/dsmlpstoragecontrollerclient/client.py) class provides the available gRPC functions for communicating with the <a href="https://github.com/ucsd-ets/dsmlpstoragecontroller" target="_blank">server</a>. It must be used as a context manager (`with` statement is required).

### Environment Variables Configuration

Set the values for all of the following environment variables in the development/production environment (values not provided here):
- DSMLP_STORAGE_CONTROLLER_CA: the absolute file path of the CA
- DSMLP_STORAGE_CONTROLLER_CERT: the absolute file path of the server CERT
- DSMLP_STORAGE_CONTROLLER_KEY: the absolute file path of the server KEY
- DSMLP_STORAGE_CONTROLLER_PORT: the port for communicating with the gRPC service
- DSMLP_STORAGE_CONTROLLER_DNS: the address for communicating with the gRPC service
- DSMLP_STORAGE_CONTROLLER_CLIENT_CERT: the absolute file path of the client CERT
- DSMLP_STORAGE_CONTROLLER_CLIENT_KEY: the absolute file path of the client KEY

## Optional: For Command Line Operations

### ClientArgs

The [ClientArgs](https://github.com/ucsd-ets/dsmlpstoragecontroller-pyclient/blob/main/src/dsmlpstoragecontrollerclient/clientargs.py) class contains command line argument options for the [client](#client).

### ClientArgsManager

The [ClientArgsManager](https://github.com/ucsd-ets/dsmlpstoragecontroller-pyclient/blob/main/src/dsmlpstoragecontrollerclient/clientargsmanager.py) class is used for parsing command line arguments, which can then be passed as arguments to the [client](#client).

### Command Line Operation Example for GetWorkspaceHomeQuota

After installing dsmlpstoragecontrollerclient with pip, you can directly run commands using the package.
```bash
python -m dsmlpstoragecontrollerclient -ca="/your/ca/location/ca.crt" -cert="/your/cert/location/$DNS-client.crt" -key="/your/key/location/$DNS-client.key" -port=9092 -address="$DNS" -request="GetWorkspaceHomeQuota" -uid=12 -workspace_name="testing"
```