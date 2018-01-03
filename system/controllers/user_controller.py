#!/bin/env python
# -*-coding:utf-8-*-

from common.base_controller import BaseController
from system.models import User


class UserController(BaseController):
    pass


user_obj = UserController(User)
