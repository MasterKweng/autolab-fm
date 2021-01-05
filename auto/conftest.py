# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

import pytest
from .rescources.DatabaseTest.conf import AUTOLAB
from .rescources.DatabaseTest.conf import EV_CALL_01
from runner.DBRunner import DBRunner
from runner.HttpRunner import HttpRunner
from auto.rescources.ApiTest.conf import agent_login, doctor_login, driver_login, create_task_help, is_work
from utils.assertAndNotify import assertAndNotify

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
@pytest.fixture()
def http_connector_fix():

    hr = HttpRunner(base_url='https://sit.jshi9.com:17443/api', verify=False)
    # print("hc init success")
    return hr

@pytest.fixture
def agent_login_fix(http_connector_fix, cache):
    hr = http_connector_fix

    agent_token = cache.get("agent_token", None)
    if agent_token is None:
        print("no cache agent_token")
        res = hr.request(agent_login["method"], agent_login["uri"], params=agent_login["params"])
        rs = str(res)[-5:-2]
        assertAndNotify(rs,"200", "agent_login_fix", rs)
        agent_token = res.json()["data"]["userInfo"]["token"]
        cache.set("agent_token", agent_token)
        agent_token = cache.get("agent_token", None)

    headers = {"token":agent_token}
    hr = HttpRunner(base_url='https://sit.jshi9.com:17443/api', verify=False, headers=headers)
    return hr, agent_token

@pytest.fixture
def doctor_login_fix(http_connector_fix, cache):
    hr = http_connector_fix

    doctor_token = cache.get("doctor_token", None)
    if doctor_token is None:
        print("no cache doctor_token")
        res = hr.request(doctor_login["method"], doctor_login["uri"], params=doctor_login["params"])
        rs = str(res)[-5:-2]
        assertAndNotify(rs,"200", "agent_login_fix", rs)
        doctor_token = res.json()["data"]["userInfo"]["token"]
        cache.set("doctor_token", doctor_token)
        doctor_token = cache.get("doctor_token", None)

    headers = {"token":doctor_token}
    hr = HttpRunner(base_url='https://sit.jshi9.com:17443/api', verify=False, headers=headers)
    res = hr.request(is_work["method"], is_work["uri"])
    workstate = res.json()["data"]

    return hr, doctor_token, workstate

@pytest.fixture
def driver_login_fix(http_connector_fix, cache):
    hr = http_connector_fix

    driver_token = cache.get("driver_token", None)
    if driver_token is None:
        print("no cache driver_token")
        res = hr.request(driver_login["method"], driver_login["uri"], params=driver_login["params"])
        rs = str(res)[-5:-2]
        assertAndNotify(rs,"200", "agent_login_fix", rs)
        driver_token = res.json()["data"]["userInfo"]["token"]
        cache.set("driver_token", driver_token)
        driver_token = cache.get("driver_token", None)

    headers = {"token":driver_token}
    hr = HttpRunner(base_url='https://sit.jshi9.com:17443/api', verify=False, headers=headers)
    res = hr.request(is_work["method"], is_work["uri"])
    workstate = res.json()["data"]

    return hr, driver_token, workstate

@pytest.fixture
def create_task_help_fix(agent_login_fix, cache):

    hr, token = agent_login_fix

    help_id = cache.get("help_id", 0)
    first_dispatch_id = cache.get("first_dispatch_id", 0)
    if help_id == 0 or first_dispatch_id == 0:
        print("no cahce")
        res = hr.request(create_task_help["method"], create_task_help["uri"], params = create_task_help["params"])
        rj = res.json()
        rs = str(res)[-5:-2]
        assertAndNotify(rs,"200", "agent_login_fix", rs)
        cache.set("help_id", rj["data"]["id"])
        cache.set("first_dispatch_id", rj["data"]["dispatchId"])
        help_id = cache.get("help_id", 0)
        first_dispatch_id = cache.get("first_dispatch_id", 0)
    return hr, help_id, first_dispatch_id
    
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