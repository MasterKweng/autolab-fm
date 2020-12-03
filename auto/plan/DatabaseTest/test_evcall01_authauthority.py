# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

from auto.conftest import database_connector
from auto.rescources.DatabaseTest.conf import auth_authority
from runnerFunction.DBTestFunc import DBTestFunc

# authority = DBTestFunc(database_connector)

def test_auth_authority_columns_exist(database_connector):

    authority = DBTestFunc(database_connector)

    authority.table_columns_exist(auth_authority["table_name"], auth_authority["columns"], database_connector())

# def test_authauthority_primary_key():

#     authority.table_primary_key(auth_authority["table_name"], auth_authority["primary_key"])

# def test_authauthority_nullable():

#     authority.table_nullable(auth_authority["table_name"], auth_authority["nullable"])

# def test_authauthority_default():

#     authority.table_default(auth_authority["table_name"], auth_authority["default"])