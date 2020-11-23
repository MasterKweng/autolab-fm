# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

AUTOLAB = {
    "conn_str": "mysql+pymysql://root:123456@localhost:3306/autolab",
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
    "default": {"user": "ryk", "unique_id": None}
}
