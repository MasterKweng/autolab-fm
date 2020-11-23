# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

import pytest
from .rescources.DatabaseTest.conf import AUTOLAB
from runner.runner import DBRunner

@pytest.fixture(scope="module")
def database_connector():

    return DBRunner(conn_str=AUTOLAB["conn_str"])

@pytest.fixture
def http_connector():
    pass

@pytest.fixture
def web_socket_connector():
    pass

@pytest.fixture
def tcp_connector():
    pass

@pytest.fixture
def udp_connector():
    pass

@pytest.fixture
def web_connector():
    """
    return selenium webdriver object
    """
    pass