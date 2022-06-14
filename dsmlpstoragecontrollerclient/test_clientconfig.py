from typing import Any
from dsmlpstoragecontrollerclient.clientconfig import ClientConfig
import pytest

@pytest.fixture
def correct_config():
    return {
        "uid": 0,
        "userquota": "10G",
        "gid": 0,
        "groupquota": "10G",
        "workspace": "workspace_name",
        "ca": "example_ca_path",
        "key": "example_key_path",
        "cert": "example_cert_path",
        "port": 9000,
        "address": "localhost",
        "developer_mode": True
    }

@pytest.fixture
def incorrect_type_config():
    return {
        "uid": "0",
        "userquota": -1,
        "gid": "0",
        "groupquota": -1,
        "workspace": -1,
        "ca": -1,
        "key": -1,
        "cert": -1,
        "port": "9000",
        "address": -1,
        "developmer_mode": True
    }

@pytest.fixture
def incorrect_value_config():
    return {
        "uid": -1,
        "userquota": "",
        "gid": -1,
        "groupquota": "",
        "workspace": "",
        "ca": "",
        "key": "",
        "cert": "",
        "port": -1,
        "address": "",
        "developer_mode": True
    }

def test_correct_config(correct_config):
    config_kwargs: dict[str, Any] = correct_config
    client_config = ClientConfig(**config_kwargs)

def test_incorrect_type_config(incorrect_type_config):
    config_kwargs: dict[str, Any] = incorrect_type_config
    exeception_occurred = False
    
    try:
        client_config = ClientConfig(**config_kwargs)
    except TypeError:
        exeception_occurred = True
    
    assert exeception_occurred


def test_incorrect_value_config(incorrect_value_config):
    config_kwargs: dict[str, Any] = incorrect_value_config
    exeception_occurred = False

    try:
        client_config = ClientConfig(**config_kwargs)
    except ValueError:
        exeception_occurred = True
    
    assert exeception_occurred