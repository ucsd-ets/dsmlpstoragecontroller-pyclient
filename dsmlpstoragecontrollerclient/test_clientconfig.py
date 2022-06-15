from typing import Any
from dsmlpstoragecontrollerclient.clientconfig import ClientConfig
import pytest


@pytest.fixture
def correct_attributes_config():
    return {
        "ca": "example_ca_path",
        "key": "example_key_path",
        "cert": "example_cert_path",
        "port": 9000,
        "address": "localhost",
        "developer_mode": True,
        "uid": 0,
        "userquota": "10G",
        "username": "example_username",
        "gid": 0,
        "groupquota": "10G",
        "workspace": "example_workspace_name"
    }


@pytest.fixture
def incorrect_types_config():
    return {
        "ca": -1,
        "key": -1,
        "cert": -1,
        "port": "9000",
        "address": -1,
        "developmer_mode": True,
        "uid": "0",
        "userquota": -1,
        "username": -1,
        "gid": "0",
        "groupquota": -1,
        "workspace": -1
    }


@pytest.fixture
def incorrect_values_config():
    return {
        "ca": "",
        "key": "",
        "cert": "",
        "port": -1,
        "address": "",
        "developer_mode": True,
        "uid": -1,
        "userquota": "",
        "username": "",
        "gid": -1,
        "groupquota": "",
        "workspace": ""
    }

@pytest.fixture
def only_required_values_config():
    return {
        "ca": "example_ca_path",
        "key": "example_key_path",
        "cert": "example_cert_path",
        "port": 9000,
        "address": "localhost",
        "developer_mode": True
    }


def test_correct_attributes_config(correct_attributes_config):
    config_kwargs: dict[str, Any] = correct_attributes_config
    client_config = ClientConfig(**config_kwargs)


def test_incorrect_types_config(incorrect_types_config):
    config_kwargs: dict[str, Any] = incorrect_types_config
    exeception_occurred = False

    try:
        client_config = ClientConfig(**config_kwargs)
    except TypeError:
        exeception_occurred = True

    assert exeception_occurred


def test_incorrect_values_config(incorrect_values_config):
    config_kwargs: dict[str, Any] = incorrect_values_config
    exeception_occurred = False

    try:
        client_config = ClientConfig(**config_kwargs)
    except ValueError:
        exeception_occurred = True

    assert exeception_occurred

def test_only_required_values_config(only_required_values_config):
    config_kwargs: dict[str, Any] = only_required_values_config
    client_config = ClientConfig(**config_kwargs)
