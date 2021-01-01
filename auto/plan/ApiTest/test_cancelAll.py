#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

'''
    1、查询当前中心坐席下所有任务
    2、中心取消所有任务
'''

from auto.rescources.ApiTest.conf import cancel, onTask_my

from auto.conftest import http_connector

from auto.rescources.ApiTest.conf_task_code import unit_dict

help_task_lists = []
def test_myHelpTask(http_connector):
    '''
        查询当前用户所有任务
    '''

    global help_task_lists

    hc, token = http_connector

    res = hc.request(onTask_my["method"], )
# GET /api/help/agent/onTask?type=1 HTTP/1.1
# Host: sit.jshi9.com:17443
# Connection: keep-alive
# Accept: application/json, text/plain, */*
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
# Token: 16092308542471cb79acd146e4724b56dcfa76590431d
# Sec-Fetch-Site: same-origin
# Sec-Fetch-Mode: cors
# Sec-Fetch-Dest: empty
# Referer: https://sit.jshi9.com:17443/dispatch/v4.1.0/
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9
# Cookie: _c_tphone_ip=192.168.0.30; _c_tphone_agent=1000; _dispatch_point=112.14466,37.157092; dispatch_ringType=headset; dispatch_name=0000; dispatch_pw=123456; dispatch_hospital=[76]; dispatch_currentNav=1; jsj_dispatch_theme=light; experimentation_subject_id=IjNmNTAyOGI2LTE3MWUtNDEzOC1iMzc1LTUxNjc0YzM5MjY2MyI%3D--b5527d1b95ee577b16800ef36e49aeaaac40e944; jsj_dispatch_token=16092308542471cb79acd146e4724b56dcfa76590431d


# def test_cancel(http_connector):
# dispatchId=3963&cancelReason=auto_test
# POST /api/dispatch/agent/cancel HTTP/1.1
# Host: sit.jshi9.com:17443
# Connection: keep-alive
# Content-Length: 38
# Accept: application/json, text/plain, */*
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
# Token: 16092308542471cb79acd146e4724b56dcfa76590431d
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# Origin: https://sit.jshi9.com:17443
# Sec-Fetch-Site: same-origin
# Sec-Fetch-Mode: cors
# Sec-Fetch-Dest: empty
# Referer: https://sit.jshi9.com:17443/dispatch/v4.1.0/
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9
# Cookie: _c_tphone_ip=192.168.0.30; _c_tphone_agent=1000; _dispatch_point=112.14466,37.157092; dispatch_ringType=headset; dispatch_name=0000; dispatch_pw=123456; dispatch_hospital=[76]; dispatch_currentNav=1; jsj_dispatch_theme=light; experimentation_subject_id=IjNmNTAyOGI2LTE3MWUtNDEzOC1iMzc1LTUxNjc0YzM5MjY2MyI%3D--b5527d1b95ee577b16800ef36e49aeaaac40e944; jsj_dispatch_token=16092308542471cb79acd146e4724b56dcfa76590431d


