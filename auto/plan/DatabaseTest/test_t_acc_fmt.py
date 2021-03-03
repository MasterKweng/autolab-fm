# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

import pytest

from auto.conftest import database_connector

from runner.DBRunner import DBRunner

from auto.rescources.DatabaseTest.conf import FMERP_T_ACC_FMT

def test_t_acc_fmt_columns_exist(database_connector):
    db = database_connector

    res = db.has_columns(FMERP_T_ACC_FMT["table_name"], FMERP_T_ACC_FMT["columns"])
    for col in FMERP_T_ACC_FMT["columns"]:
        print("exist column: %s --> %s" %(col, res[col]))

        assert res[col]

def test_t_acc_fmt_primary_key(database_connector):
    db = database_connector

    res = db.is_primary_key(FMERP_T_ACC_FMT["table_name"], FMERP_T_ACC_FMT["primary_key"])

    for col in FMERP_T_ACC_FMT["primary_key"]:
        print("exist primary key: %s --> %s" %(col, res[col]))

        assert res[col]

def test_t_acc_fmt_nullable(database_connector):
    db = database_connector

    res = db.is_nullable(FMERP_T_ACC_FMT["table_name"], FMERP_T_ACC_FMT["nullable"])

    for col in FMERP_T_ACC_FMT["nullable"]:
        print("%s is nullable --> %s" %(col, res[col]))

        assert res[col]
        
def test_t_acc_fmt_default(database_connector):
    db = database_connector

    res = db.is_default(FMERP_T_ACC_FMT["table_name"], FMERP_T_ACC_FMT["default"])
    print(FMERP_T_ACC_FMT["default"])

    for col in FMERP_T_ACC_FMT["default"]:
        print(col)
        # k,v = col.popitem()
        print("table %s  column %s has default? %s" % (FMERP_T_ACC_FMT["table_name"], col, res[col]))

        assert res[col]
