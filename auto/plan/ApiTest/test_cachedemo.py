# -*- coding:utf8 -*-

__author__ = "YuKwengRu"

import pytest

from auto.conftest import http_connector

from auto.rescources.ApiTest.conf import assign,create_task_help

@pytest.fixture
def test_a(http_connector, cache):

    hr,b = http_connector()
    
    help_id = cache.get("help_id", 0)
    if help_id == 0:
        # print("no cahce")
        res = hr.request(create_task_help["method"], create_task_help["uri"], params = create_task_help["params"])
        # print(res.json())
        rj = res.json()
        assert rj["code"] == 1
        cache.set("help_id", rj["data"]["id"])
        help_id = cache.get("help_id", 0)
    return help_id

