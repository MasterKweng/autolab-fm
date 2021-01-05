#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

'''
    1、下班同时解绑车辆
'''
from auto.rescources.ApiTest.conf import off_work

from auto.rescources.ApiTest.conf_task_code import unit_dict

from utils.assertAndNotify import assertAndNotify


def test_docOffWork(doctor_login_fix):

    hr, token, workstate = doctor_login_fix

    if workstate:        
        res = hr.request(off_work["method"], off_work["uri"])
        rj = res.json()
        assertAndNotify(rj["code"], "test_docToWork", rj["msg"])
    else:
        pass
    
def test_driOffWork(driver_login_fix):

    hr, token, workstate = driver_login_fix

    if workstate:
        res = hr.request(off_work["method"], off_work["uri"])
        rj = res.json()
        assertAndNotify(rj["code"], "test_driToWork", rj["msg"])
    else:
        pass
