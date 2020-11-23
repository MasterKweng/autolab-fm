# -*- coding:utf-8 -*-

__author__ = "YukwengRu"

"""
    基类&核心驱动类
"""
# for http
import re
import requests
from requests import Request
from requests.auth import HTTPBasicAuth

# for database
from sqlalchemy import create_engine 
from sqlalchemy.engine import reflection
from sqlalchemy.dialects.mysql import *

class Runner(object):
    def __init__(self, name="Base Runner"):
        self.name = name



class HttpRunner(Runner):
    def __init__(self, base_url="127.0.0.1", verify=False):
        super().__init__(name="Http Runner")
        self.base_url = base_url
        self.http = requests.Session()

        # 在session实例上挂载Adapter实例， 目的：请求异常时，自动重试
        a = requests.adapters.HTTPAdapter(max_retries=3)
        self.http.mount('http://', a)
        self.http.verify = verify
        self.token="" # 登录token

        self.r = None

    def auth(self, uri, user, passwd):
        url = self,base_url + uri

        return self.http.get(url, auth=HTTPBasicAuth(user, passwd))
    
    def request(self, method, uri, **kwargs):
        """
            该函数参数与requests库的request方法
            method： GET、POST、DELETE、PUT HEADER等等
            uri: 目标请求资源
            kwargs: 其他请求参数
            返回requests Response 对象
        """
        url = self,base_url + uri
        try:
            self.r = self.http.request(method=method, url=url, **kwargs)
        except requests.exceptions.ConnecTimeout as e:
            print("HttpRunner Exception: [%s]" % str(e))
        except requests.exceptions.InvalidURL as e:
            print("Http Runner Exception: [%s]" % str(e))
        
        return self.r
    
    @property
    def status_code(self):
        """
            获取http相应状态码
        """

        return self.r.status_code

    @property
    def encoding(self):
        """
            获取http相应内容coding
        """

        return self.r.coding

    def get_headers(self, key=None):
        """
            获取http响应headers, dict类型
        """
        if key is None:
            return self.r.headers
        else:
            return self.r.headers[key]
    
    @property
    def json(self):
        """
            获取json格式的响应内容
        """

        return self.r.json()
    
    @property
    def text(self):
        """
            获取原始响应内容
        """

        return self.r.text
    
    def get_http(self):
        """
            返回requests.session对象，用于直接操作requests
        """

        return self.http
    
    def close(self):
        """
            断开http连接
        """

        self.http.close()    

    

class DBRunner(Runner):
    
    def __init__(self, conn_str="", encoding="utf-8", echo=False):
        print(super)
        print(super())
        super().__init__(name = "DataBase Runner")

        # init engine object
        engine = create_engine(conn_str, encoding=encoding, echo=echo)

        # init inspector object
        self.insp = reflection.Inspector.from_engine(engine)

    def has_tables(self, tables_name=[]):
        res = {}

        tables = self.insp.get_table_names()

        for table in tables_name:
            if table in tables:
                res[table] = True
            else:
                res[table] = False
        
        return res
    
    def has_columns(self, table_name, columns_name=[]):
        res = {}
        for col in columns_name:
            res[col] = self.__find_column(table_name, col) != None
        
        return res
    
    def is_primary_key(self, table_name, columns_name=[]):
        res = {}
        for  col in columns_name:
            res[col] = self.__find_column(table_name, col) !=None
        
        return res
    
    def is_unique(self, table_name, columns_name=[]):
        res = {}

        unique_columns = self.insp.get_unique_constraints(table_name)
        for col in columns_name:
            res[col] = False
            for unique in unique_columns:
                if col == unique["column_names"][0]:
                    res[col] = True
                    break

        return res
    
    def has_index(self, table_name, columns_name = []):
        res = {}

        indexes = self.insp.get_indexes(table_name)
        for col in columns_name:
            res[col] = False
            for index in indexes:
                if col == index["columns_name"][0]:
                    res[col] = True
        
        return res

    def is_nullable(self, table_name, columns_name=[]):
        res = {}
        for col in columns_name:
            res[col] = self.__find_column(table_name, col)["nullable"]
        
        return res
    
    def is_default(self, table_name, columns=[]):
        res = {}
        for col in columns:
            k, v = col.popitem()
            res[k] = v == self.__find_column(table_name, k)["default"]
        
        return res
    
    def __find_column(self, table_name, column_name):
        columns = self.insp.get_columns(table_name)

        for col in columns:
            if column_name == col["name"]:
                return col
        
        return None