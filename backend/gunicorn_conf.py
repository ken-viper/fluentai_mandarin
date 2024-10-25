#from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/home/ubuntu/fluentai-be/gunicorn.sock'

# Worker Options
#workers = cpu_count() + 1
workers = 4
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/ubuntu/fluentai-be/access_log'
errorlog =  '/home/ubuntu/fluentai-be/error_log'
