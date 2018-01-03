# -*-coding:utf-8-*-

import os

FLASK_ENV = os.environ.get('FLASK_ENV', '')

if FLASK_ENV == "PRODUCTION":
    import settings_production
    settings = settings_production.BaseConfig()
else:
    import settings_local
    settings = settings_local.LocalConfig()
