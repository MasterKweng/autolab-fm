# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

from auto.rescources.DatabaseTest.conf import auth_permit_user

from auto.conftest import database_connector

from runnerFunction.DBTestFunc import DBTestFunc

print("table %s begain ----------" %(auth_permit_user["table_name"]))

def test_authpermituser_columns_exist(database_connector):

    authpermituser = DBTestFunc(database_connector)

    authpermituser.table_columns_exist(auth_permit_user["table_name"], auth_permit_user["columns"])

def test_authpermituser_primary_key(database_connector):

    authpermituser = DBTestFunc(database_connector)
    
    authpermituser.table_primary_key(auth_permit_user["table_name"], auth_permit_user["primary_key"])

def test_authpermituser_nullable(database_connector):

    authpermituser = DBTestFunc(database_connector)

    authpermituser.table_nullable(auth_permit_user["table_name"], auth_permit_user["nullable"])

def test_authpermituser_default(database_connector):

    authpermituser = DBTestFunc(database_connector)

    authpermituser.table_default(auth_permit_user["table_name"], auth_permit_user["default"])

