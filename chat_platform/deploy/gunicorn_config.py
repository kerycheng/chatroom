# coding=utf-8
bind = '0.0.0.0:8000'
backlog = 2048
workers = 2
worker_class = 'sync'
worker_connection = 1000
timeout = 30
keepalive = 2

daemon = False
raw_env = [
    'DJANGO_SECRET_KEY=something',
]
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None
errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s" "%(a)s'
proc_name = "e_shoes"
