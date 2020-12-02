# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

from auto.conftest import database_connector

from auto.rescources.DatabaseTest.conf import auth_authority


def test_authauthority_columns_exist(database_connector):
    db = database_connector

    res = db.has_columns(auth_authority["table_name"], auth_authority["columns"])
    
    for col in auth_authority["columns"]:
        print("table %s has columns %s ? %s" % (auth_authority["table_name"], col, res[col]))

        assert res[col]
    
def test_authauthority_primary_key(database_connector):
    db = database_connector

    res = db.is_primary_key(auth_authority["table_name"], auth_authority["primary_key"])

    for col in auth_authority["primary_key"]:
        print("table %s primary key is %s ? %s "% (auth_authority["table_name"], col, res[col]))

        assert res[col]

def test_authauthority_nullable(database_connector):
    db = database_connector

    res = db.is_nullable(auth_authority["table_name"], auth_authority["nullable"])

    for col in auth_authority["nullable"]:
        print("table %s column %s is nullable  ? %s "% (auth_authority["table_name"], col, res[col]))

        assert res[col]

# def test_authauthority_default(database_connector):
#     db = database_connector

#     res = db.is_default(auth_authority["table_name"], auth_authority["default"])

#     for col in auth_authority["default"]:
#         print("table %s  column %s has default? %s" % (auth_authority["table_name"], col, res[col]))

#         assert res[col]