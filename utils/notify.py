# -*- coding:utf-8 -*-

__author__ = "YukwengRu"

import json

import requests

from conf.conf import DINGTALK_URL

# 发送钉钉文本通知
def send_dingtalk_msg(msg):
    print("2")
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text":{
            "content": msg
        }
    }
    print("3")
    res=requests.post(DINGTALK_URL,data=json.dumps(data),headers=headers)
    print("4")

    print(res.text)

# send_dingtalk_msg("123")