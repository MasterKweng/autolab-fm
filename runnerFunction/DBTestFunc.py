# -*- coding:utf-8 -*-

"""
    初步封装，减少重复代码
"""
__author__ = "YuKwengRu"

from auto.conftest import database_connector

class DBTestFunc(object):

    def __init__(self, conn_str):

        self.conn_str = conn_str

    

    def table_columns_exist(self, table_name, columns):

        res = self.conn_str.has_columns(table_name, columns)
    
        for col in columns:
            print("table %s has columns %s ? %s" % (table_name, col, res[col]))

            assert res[col]

    def table_primary_key(self, table_name, primary_key):

        res = self.conn_str.is_primary_key(table_name, primary_key)

        for col in primary_key:
            print("table %s primary key is %s ? %s "% (table_name, col, res[col]))

            assert res[col]

    def table_nullable(self, table_name, nullable):

        res = self.conn_str.is_nullable(table_name, nullable)

        for col in nullable:
            print("table %s column %s is nullable  ? %s "% (table_name, col, res[col]))

            assert res[col]

    def table_default(self, table_name, default):

        res = self.conn_str.is_default(table_name, default)

        for (k,v) in default.items():
            print("table %s  column %s has default? %s" % (table_name, k, res[k]))

            assert res[k]