# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

# from auto.conftest import http_connector

# hr, token = http_connector

agent_login = {
    "method": "POST",
    "uri": "/accountLogin/gen/unit/agent",
    "params": {
        "userType":"agent", "account":"0000", "loginMode":"job", "password":"123456", "unitId":"76"
    }
}

create_task_help = {
    "method": "POST",
    "uri": "/help/agent/create",
    "params": {
        "phone": "11111111111", "remark": "auto_hub_jsfj"
    }
}

assign = {
    "method": "POST",
    "uri": "/carOut/agent/assign"
}

onTask_my = {
    "method": "GET",
    "uri": "/help/agent/onTask",
    "params": {
        "type": 1
    }
}

cancel = {

}