#!/bin/env python
# -*- coding:utf8 -*-

from settings_production import BaseConfig


class LocalConfig(BaseConfig):
    DEBUG = True
    CREATE_TABLE = True
    LOG_SETTING = "logging.ini"

    # 生产新数据库
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "jpush"
    MYSQL_PWD = "jpush"
    MYSQL_DB = "devops"
