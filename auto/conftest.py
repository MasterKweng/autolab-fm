# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

import pytest
from .rescources.DatabaseTest.conf import AUTOLAB
from .rescources.DatabaseTest.conf import EV_CALL_01
from runner.DBRunner import DBRunner
from runner.HttpRunner import HttpRunner
from auto.rescources.ApiTest.conf import agent_login, create_task_help

'''
    dbtest fixture
'''
@pytest.fixture(scope="module")
def database_connector():

    return DBRunner(conn_str=EV_CALL_01["conn_str"])
    # return DBRunner(conn_str=AUTOLAB["conn_str"])

'''
    apitest fixture
'''
@pytest.fixture
def http_connector():

    # hr = HttpRunner(base_url='https://sit.jshi9.com:17443/api', verify=False)
    hr = HttpRunner(base_url='https://sit.jshi9.com:17443/api', verify=False)
    res = hr.request(agent_login["method"], agent_login["uri"], params=agent_login["params"])
    token = res.json()["data"]["userInfo"]["token"]
    headers = {"token":token}
    hr = HttpRunner(base_url='https://sit.jshi9.com:17443/api', verify=False, headers=headers)

    return hr, token
    # return hr

@pytest.fixture
def agent_login():

    hr = HttpRunner(base_url='https://sit.jshi9.com:17443/api', verify=False)
    res = hr.request(agent_login["method"], agent_login["uri"], params=agent_login["params"])
    token = res.json()["data"]["userInfo"]["token"]
    headers = {"token":token}
    hr = HttpRunner(base_url='https://sit.jshi9.com:17443/api', verify=False, headers=headers)

    return hr, token

@pytest.fixture
def doctor_login():

    pass

@pytest.fixture
def driver_login():

    pass
@pytest.fixture
def create_task_help(agent_login, cache):

    hr = agent_login()
    
    help_id = cache.get("help_id", 0)
    first_dispatch_id = cache.get("dispatch_id", 0)
    if help_id == 0 or first_dispatch_id == 0:
        print("no cahce")
        res = hr.request(create_task_help["method"], create_task_help["uri"], params = create_task_help["params"])
        # print(res.json())
        rj = res.json()
        assert rj["code"] == 1
        cache.set("help_id", rj["data"]["id"])
        cache.set("first_dispatch_id", rj["data"]["dispatchId"])
        help_id = cache.get("help_id", 0)
        first_dispatch_id = cache.get("first_dispatch_id", 0)
    return help_id, first_dispatch_id
    
'''
    websocket fixture
'''
@pytest.fixture
def web_socket_connector():
    pass

'''
    tcp fixture
'''
@pytest.fixture
def tcp_connector():
    pass

'''
    udp fixture
'''
@pytest.fixture
def udp_connector():
    pass

'''
    webdriver fixture
'''
@pytest.fixture
def web_connector():
    """
    return selenium webdriver object
    """
    pass