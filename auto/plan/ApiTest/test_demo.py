#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

from auto.rescources.ApiTest.conf import login, create

from auto.conftest import http_connector

def test_demo_login(http_connector):

    res = http_connector.request(login["method"], login["uri"])
#     , params=login["params"]
    rj = res.json()
#     print(rj)
#     print(rj["data"])
#     print(rj["data"]["userInfo"]["token"])

def test_create(http_connector):

    a = http_connector.request(create["method"], create["uri"])
    print(a.json())
# def test_create(http_connector):

#         a = http_connector.request(create["method"], create["uri"])
#         # params = create["params"]
#         print(a)