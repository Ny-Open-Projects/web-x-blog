# gunicorn_conf.py —— Gunicorn 的 Python 配置文件,可直接被 -c 引用
import multiprocessing

bind = '127.0.0.1:8000'
workers = multiprocessing.cpu_count() * 2 + 1   # 经验公式
worker_class = 'uvicorn.workers.UvicornWorker'  # ASGI 应用用这个
# worker_class = 'sync'                          # 纯同步 WSGI 用这个
timeout = 30                # worker 超时被杀
graceful_timeout = 20
keepalive = 5
accesslog = '-'
errorlog = '-'
preload_app = True          # 主进程预加载,省内存但注意 fork 安全

# 启动示例:
# 同步 Flask:   gunicorn -c gunicorn_conf.py myapp.wsgi:application
# 异步 FastAPI: gunicorn -c gunicorn_conf.py myapp.asgi:app
