__author__ = "YuKwengRu"

import pytest

from runner.DBRunner import DBRunner

from auto.rescources.DatabaseTest.conf import EV_CALL_01

from utils.myassert import for_assertTrue

def test_evcall01_tables(database_connector):

    for_assertTrue(database_connector.has_tables(EV_CALL_01["tables"]))