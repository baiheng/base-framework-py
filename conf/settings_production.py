#!/bin/env python
# -*- coding:utf8 -*-


class BaseConfig(object):
    DEBUG = False
    CREATE_TABLE = False
    LOG_SETTING = "logging_production.ini"

    # 生产新数据库
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "jpush"
    MYSQL_PWD = "jpush"
    MYSQL_DB = "devops"
