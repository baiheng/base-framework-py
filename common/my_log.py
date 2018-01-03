#!/bin/env python
# -*-coding:utf-8-*- 

import logging
import logging.config
import os
from conf import settings


log_path = "%s/conf/%s" % (os.path.abspath('.'), settings.LOG_SETTING)
logging.config.fileConfig(log_path)
logger = logging.getLogger("root")
