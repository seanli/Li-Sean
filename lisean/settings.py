import os
import socket

PROD_HOSTS = (
    'web330.webfaction.com',
)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

HOST_NAME = socket.gethostname()

if HOST_NAME in PROD_HOSTS:
    from settings_prod import *
else:
    from settings_dev import *

# You can add a settings_extra.py file for additional personal configurations
if os.path.isfile(os.path.join(PROJECT_ROOT, 'settings_extra.py')):
    from settings_extra import *
