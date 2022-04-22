"""Gunicorn settings"""

bind = '0.0.0.0:8000'
chdir = 'proxy_server'
reload = True
workers = 1
