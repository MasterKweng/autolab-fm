#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

'''
    1、创建求救任务
    2、指派出车
'''
from auto.rescources.ApiTest.conf import assign

from auto.rescources.ApiTest.conf_task_code import unit_dict

from utils.assertAndNotify import assertAndNotify

import pytest

def test_assign(create_task_help_fix):
    '''
        指派出车并获取caroutid
        后续优化点：从可指派出车接口中取出车辆数据，用来指派，避免发生车辆已被指派的情况
    '''

    hr, help_id, fist_dis_id = create_task_help_fix
    ambId = unit_dict["center"]["siteId"][82]["ambId"][0]
    # print(dispatch_id)
    res = hr.request(assign["method"], assign["uri"], params = {"ambId":ambId, "dispatchId":fist_dis_id, "type": "first"})
    rj = res.json()
    # print(rj)
    # reason = rj["msg"]
    assertAndNotify(rj["code"], "test_assign", rj["msg"])
    # try:
    #     assert rj["code"] == 1
    # except Exception as e:
    #     msg = "Test Faild \nCase:test_assign \nReason:"
    #     send_dingtalk_msg(msg)
    # assert rj["code"] == 1
    # print("task car out id is : %s \n" % (rj["data"]))