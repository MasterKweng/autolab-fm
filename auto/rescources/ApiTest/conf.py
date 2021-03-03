# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

# from auto.rescources.ApiTest.conf_task_code import unit_dict

# hr, token = http_connector

agent_login = {
    "method": "POST",
    "uri": "/accountLogin/gen/unit/agent",
    "params":{
        "userType":"agent", "account":"0000", "loginMode":"job", "password":"123456", "unitId":"76"
    }
}