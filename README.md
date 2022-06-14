# DSMLP Storage Controller Python Client

## Description

The name of the Python package is `dsmlpstoragecontrollerclient`. The `ClientArgsManager` class is used for parsing command line arguments, which can then be passed as arguments to the client. The `Client` class provides the available gRPC functions for communicating with the server. It must be used as a context manager (`with` statement is required). Please refer to `client_example.py` in the examples directory.