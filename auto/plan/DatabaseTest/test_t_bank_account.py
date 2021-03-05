
__author__ = "gaomao"

import pytest

from auto.conftest import database_connector

from runner.DBRunner import DBRunner

from auto.rescources.DatabaseTest.conf import FMERP_T_BANK_ACCOUNT



def test_t_bank_account_has_columns(database_connector):
    db = database_connector
    res = db.has_columns(FMERP_T_BANK_ACCOUNT["table_name"], FMERP_T_BANK_ACCOUNT["columns"])
    for col in FMERP_T_BANK_ACCOUNT["columns"]:
        print("exist column: %s --> %s" % (col, res[col]))
        assert res[col]

def test_t_bank_account_has_primary_key(database_connector):
    db = database_connector
    res = db.is_primary_key(FMERP_T_BANK_ACCOUNT["table_name"], FMERP_T_BANK_ACCOUNT["primary_key"])
    for col in FMERP_T_BANK_ACCOUNT["primary_key"]:
        print("exist primary key: %s --> %s" % (col, res[col]))
        assert res[col]

def test_t_bank_account_is_nullable(database_connector):
    db = database_connector
    res = db.is_nullable(FMERP_T_BANK_ACCOUNT["table_name"], FMERP_T_BANK_ACCOUNT["nullable"])
    for col in FMERP_T_BANK_ACCOUNT["nullable"]:
        print("%s is nullable-->  %s" % (col, res[col]))
        assert  res[col]


def test_t_bank_account_is_default(database_connector):
    db = database_connector
    res = db.is_nullable(FMERP_T_BANK_ACCOUNT["table_name"], FMERP_T_BANK_ACCOUNT["default"])
    for col in FMERP_T_BANK_ACCOUNT["default"]:
        print("table %s  column %s is default? %s" % (FMERP_T_BANK_ACCOUNT["table_name"], col, res[col]))
