#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

from auto.rescources.ApiTest.conf import login, create

from auto.conftest import http_connector

import pytest

# def test_demo_login(http_connector):

#     res = http_connector.request(login["method"], login["uri"])
# #     , params=login["params"]
#     rj = res.json()
# #     print(rj)
# #     print(rj["data"])
# #     print(rj["data"]["userInfo"]["token"])
class Testdemo():
    def __init__(self):

        help_id = None
        # def init(self):
        hc1 = http_connector

    def test_create(self):
        
        # print(token)
        res = self.hc1.request(create["method"], create["uri"], params = create["params"])
        print(res.json())
        rj = res.json()
        assert rj["code"] == 1
        help_id = rj["data"]["id"]
        dispatch_id = rj["data"]["dispatchId"]
        print("task help: %s \n" % (help_id))

    def test_dispatch(self):

        # res = http_connector
        print(help_id)
    
    # if __name__=="__main__":
    #     pytest.main()