#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controllers import user_obj
from system.views.user_view import User

urls = [
    ("user", User, user_obj),
]

