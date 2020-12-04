# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

from auto.conftest import database_connector

from auto.rescources.DatabaseTest.conf import auth_permit_role

from runnerFunction.DBTestFunc import DBTestFunc

def test_authpermitrole_columns(database_connector):

    authpermitrole = DBTestFunc(database_connector)

    authpermitrole.table_columns_exist(auth_permit_role["table_name"], auth_permit_role["columns"])

def test_authpermitrole_primary_key(database_connector):

    authpermitrole = DBTestFunc(database_connector)

    authpermitrole.table_primary_key(auth_permit_role["table_name"], auth_permit_role["primary_key"])

def test_authpermitrole_nullable(database_connector):

    authpermitrole = DBTestFunc(database_connector)

    authpermitrole.table_nullable(auth_permit_role["table_name"], auth_permit_role["nullable"])

def test_authpermitrole_default(database_connector):

    authpermitrole = DBTestFunc(database_connector)
    
    authpermitrole.table_default(auth_permit_role["table_name"], auth_permit_role["default"])
