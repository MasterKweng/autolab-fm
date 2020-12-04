# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

def for_assertTrue(result={}):
    for k in result.keys():
        v = result[k]
        print(" %s assert %s " % (k, v))
        assert v