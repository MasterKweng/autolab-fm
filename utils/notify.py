# -*- coding:utf-8 -*-

__author__ = "YukwengRu"

import json

import requests

from conf.conf import DINGTALK_URL

# 发送钉钉文本通知
def send_dingtalk_msg(msg):
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text":{
            "content": msg
        }
    }
    res=requests.post(DINGTALK_URL,data=json.dumps(data),headers=headers)