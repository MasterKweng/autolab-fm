# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

import pytest
from .rescources.DatabaseTest.conf import AUTOLAB
from .rescources.DatabaseTest.conf import EV_CALL_01
from runner.DBRunner import DBRunner
from runner.HttpRunner import HttpRunner
from auto.rescources.ApiTest.conf import login

@pytest.fixture(scope="module")
def database_connector():

    return DBRunner(conn_str=EV_CALL_01["conn_str"])
    # return DBRunner(conn_str=AUTOLAB["conn_str"])

@pytest.fixture
def http_connector():

    hr = HttpRunner(base_url='https://sit.jshi9.com:17443/api', verify=False)
    # res = hr.request(login["method"], login["uri"], params=login["params"])
    # token = res.json()["data"]["userInfo"]["token"]
    return hr

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