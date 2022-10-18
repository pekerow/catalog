import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/www/catalog/venv/lib/python3.10/site-packages')
sys.path.insert(0, '/var/www/')

from catalog import app as application
application.secret_key = 'super_secret_key'
