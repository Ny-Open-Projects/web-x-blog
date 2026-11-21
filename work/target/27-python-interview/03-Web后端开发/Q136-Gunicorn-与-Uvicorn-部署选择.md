---
title: [Q136] Gunicorn 与 Uvicorn 部署选择
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q136 · Gunicorn 与 Uvicorn 部署选择

> 难度:★★☆ | 标签:Gunicorn, Uvicorn, 部署

**问**:同步 Django 项目和异步 FastAPI 项目分别怎么选部署组合?worker 类型如何决定?

**答**:WSGI 栈:Gunicorn 管理 worker 进程承载 Flask/Django(同步);ASGI 栈:FastAPI/Django-async 用 Uvicorn 启动,生产建议 `gunicorn -k uvicorn.workers.UvicornWorker`(Gunicorn 做进程管理与崩溃重启,Uvicorn 做协议与事件循环)。worker 类型按应用特征选:IO 密集用 gevent/uvicorn worker,CPU 密集用 sync+多进程;Django 双栈时 ASGI 是未来方向,可用 asgi.py + Uvicorn。

```python
# file: code/03_Web后端开发/q136_gunicorn_conf.py
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
```

**追问**:
- Gunicorn 管理 UvicornWorker 的意义?——Gunicorn 负责 worker 生命周期、优雅重启、超时回收;Uvicorn 只管协议与事件循环,各司其职。
- sync worker 遇到慢客户端会怎样?——worker 被占住等客户端;必须前置 Nginx 做请求缓冲,或改异步 worker。
- 优雅重启怎么实现?——`kill -HUP` 让 Gunicorn 拉起新 worker、旧 worker 处理完存量请求退出;发布不丢在途请求。
