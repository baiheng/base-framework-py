#!/bin/env python
# -*- coding:utf8 -*-

from sqlalchemy import Column, String, Integer, DateTime, text, LargeBinary

from common.sqlalchemy_ctl import Base
from common.utility import create_table

from conf import settings


class User(Base):
    __tablename__ = 'system_user'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    # 父项目
    parent_id = Column(Integer(), nullable=False, server_default='0')
    # 名称
    name = Column(String(256), nullable=False, server_default='')
    # 类型，内网还是外网
    web_type = Column(String(256), nullable=False, server_default='')
    # 更新时间
    update_time = Column(DateTime(), nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    # 负责人1
    principal1 = Column(Integer(), nullable=False, server_default='0')
    # 负责人2
    principal2 = Column(Integer(), nullable=False, server_default='0')
    # 备注
    remark = Column(String(256), nullable=False, server_default='')


if settings.CREATE_TABLE:
    create_table("system_user")
