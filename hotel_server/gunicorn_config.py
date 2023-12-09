command = '/home/hotel_server/env/bin/gunicorn'
pythonpath = '/home/hotel_server'
bind = '127.0.0.1:8001'
workers = 3
user = 'root'
limit_request_fileds = 32000
limi_request_filed_size = 0
raw_enc = 'DJANGO_SETTINGS_MODULE=hotel_server.settings.prod'
