# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

from auto.conftest import database_connector

from auto.rescources.DatabaseTest.conf import auth_authority

from runnerFunction.DBTestFunc import DBTestFunc


def test_authauthority_columns_exist(database_connector):

    authority = DBTestFunc(database_connector)

    authority.table_columns_exist(auth_authority["table_name"], auth_authority["columns"])

def test_authauthority_primary_key(database_connector):

    authority = DBTestFunc(database_connector)

    authority.table_primary_key(auth_authority["table_name"], auth_authority["primary_key"])

def test_authauthority_nullable(database_connector):

    authority = DBTestFunc(database_connector)

    authority.table_nullable(auth_authority["table_name"], auth_authority["nullable"])

def test_authauthority_default(database_connector):

    authority = DBTestFunc(database_connector)

    authority.table_default(auth_authority["table_name"], auth_authority["default"])