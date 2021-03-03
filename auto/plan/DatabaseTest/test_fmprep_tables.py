__author__ = "YuKwengRu"

import pytest

from runner.DBRunner import DBRunner

from auto.rescources.DatabaseTest.conf import FMERP

def test_FMERP_tables(database_connector):
    db = database_connector

    res = db.has_tables(FMERP["tables"])

    for table in FMERP["tables"]:
        print("table %s in database!" % table)

        assert res[table]