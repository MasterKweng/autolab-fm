# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

import time

AUTOLAB = {
    "conn_str": "mysql+pymysql://root:jsfj120JSFJ!@)@192.168.2.230:3306/autolab",
    "encoding": "utf-8",
    "echo": False,
    "tables": ["demo"]
}

AUTOLAB_DEMO = {
    "table_name": "demo",
    "columns": ["id","user", "name", "unique_id"],
    "primary_key": ["id"],
    "nullable": ["id"],
    "unique": ["user", "unique_id"],
    "index": ["id", "user", "unique_id"],
    "default": [{"user": "ryk"},{"unique_id": None}]
}

EV_CALL_01 = {
    "conn_str": "mysql+pymysql://root:jsfj120JSFJ!@)@192.168.2.230:3306/ev-call-01",
    "encoding": "utf-8",
    "echo": False,
    "tables": ["auth_authority", "auth_permit_role", "auth_permit_user", "auth_role", "auth_role_user", ]
}

auth_authority = {
    "table_name": "auth_authority",
    "columns": ["id", "code", "name", "parent_code", "parent_name", "icon", "href", "type", "status", "remark", "system_code", "system_name", "create_time", "creator", "update_time", "updater"],
    "primary_key": ["id"],
    "nullable": ["name"],
    "index": [""],
    "default": [{"name":None}, {"parent_code":None}, {"parent_name":None}, {"icon":None}, {"href":None}, {"type":None}, {"status":None}, {"remark":None}, {"create_time":"CURRENT_TIMESTAMP"}, {"creator":None}, {"update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"}, {"updater":None}]
}