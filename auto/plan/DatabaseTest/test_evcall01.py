__author__ = "YuKwengRu"

import pytest

from runner.DBRunner import DBRunner

from auto.rescources.DatabaseTest.conf import EV_CALL_01

def test_evcall01_tables(database_connector):
    db = database_connector

    res = db.has_tables(EV_CALL_01["tables"])

    for table in EV_CALL_01["tables"]:
        print("table %s in database!" % table)

        assert res[table]