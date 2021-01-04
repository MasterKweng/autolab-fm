# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

from utils.notify import send_dingtalk_msg

def assertAndNotify(code, case, reason):
    try:
        assert code == 1
    except Exception as e:
        msg = "EVCALL Test Faild \nCase:"+case+ "\nReason:"+reason+""
        send_dingtalk_msg(msg)
