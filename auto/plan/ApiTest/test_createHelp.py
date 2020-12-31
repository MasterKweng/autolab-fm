#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

'''
    1、创建求救任务
    2、指派出车
'''
from auto.rescources.ApiTest.conf import agent_login, create_task_help, assign

from auto.conftest import http_connector

from auto.rescources.ApiTest.conf_task_code import unit_dict

import pytest

help_id = 0
dispatch_id = 0


def test_create(http_connector):
    '''
        创建任务并获取help_id和dispatch_id
    '''

    global help_id,dispatch_id

    hc, token = http_connector
    
    res = hc.request(create["method"], create["uri"], params = create["params"])
    # print(res.json())
    rj = res.json()
    assert rj["code"] == 1
    help_id = rj["data"]["id"]
    dispatch_id = rj["data"]["dispatchId"]
    print("create success! \ntask help id is: %s\ntask dispatch id is: %s" % (help_id, dispatch_id))

def test_assign(http_connector):
    '''
        指派出车并获取caroutid
        后续优化点：从可指派出车接口中取出车辆数据，用来指派，避免发生车辆已被指派的情况
    '''

    hc, token = http_connector
    ambId = unit_dict["center"]["siteId"][82]["ambId"][0]
    # print(dispatch_id)
    res = hc.request(assign["method"], assign["uri"], params = {"ambId":ambId, "dispatchId":dispatch_id, "type": "first"})
    rj = res.json()
    print(rj)
    assert rj["code"] == 1
    print("task car out id is : %s \n" % (rj["data"]))
    