# -*- coding:utf-8 -*-

"""
    初步封装，减少重复代码
"""
__author__ = "YuKwengRu"

from auto.conftest import database_connector

class DBTestFunc(object):

    def __init__(self, conn_str, table_name):

        self.conn_str = conn_str

        self.table_name = table_name

    

    def table_columns_exist(self, columns):

        res = self.conn_str.has_columns(self.table_name, columns)
    
        for col in columns:
            print("table %s has columns %s ? %s" % (self.table_name, col, res[col]))

            assert res[col]

    def table_primary_key(self, primary_key):

        res = self.conn_str.is_primary_key(self.table_name, primary_key)

        for col in primary_key:
            print("table %s primary key is %s ? %s "% (self.table_name, col, res[col]))

            assert res[col]

    def table_nullable(self, nullable):

        res = self.conn_str.is_nullable(self.table_name, nullable)

        for col in nullable:
            print("table %s column %s is nullable  ? %s "% (self.table_name, col, res[col]))

            assert res[col]

    def table_default(self, default):

        res = self.conn_str.is_default(self.table_name, default)

        for (k,v) in default.items():
            print("table %s  column %s has default? %s" % (self.table_name, k, res[k]))

            assert res[k]