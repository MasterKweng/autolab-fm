#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

'''
    1、下班同时解绑车辆
'''
from auto.rescources.ApiTest.conf import off_work

from auto.rescources.ApiTest.conf_task_code import unit_dict

from utils.assertAndNotify import assertAndNotify

from time import sleep

def test_docOffWork(doctor_login_fix):

    hr, token, workstate = doctor_login_fix

    if workstate:        
        res = hr.request(off_work["method"], off_work["uri"])
        rj = res.json()
        assertAndNotify(rj["code"], 1, "test_docToWork", rj["msg"])
    else:
        pass
    sleep(10)
    
def test_driOffWork(driver_login_fix):

    hr, token, workstate = driver_login_fix

    if workstate:
        res = hr.request(off_work["method"], off_work["uri"])
        rj = res.json()
        assertAndNotify(rj["code"], 1, "test_driOffWork", rj["msg"])
    else:
        pass
    sleep(10)

