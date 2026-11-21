---
title: [Q086] WSGI 是什么,接口规范长什么样
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q086 · WSGI 是什么,接口规范长什么样

> 难度:★★☆ | 标签:WSGI, HTTP

**问**:请解释 WSGI 协议的作用,并手写一个最小 WSGI application。

**答**:WSGI 是 Python Web 服务器与应用之间的同步调用规范(PEP 3333),它把 HTTP 请求抽象成一个可调用对象:服务器传入 `environ` 字典和 `start_response` 回调,应用返回可迭代字节响应。它的价值在于应用与服务器解耦,Flask/Django 早期都构建在 WSGI 之上。缺点是同步阻塞模型,一个请求占用一个线程,不适合长连接和高并发 IO 场景。

```python
# file: code/03_Web后端开发/q086_wsgi_app.py
def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    path = environ.get('PATH_INFO', '/')
    body = f'hello, path={path}'.encode('utf-8')
    return [body]

if __name__ == '__main__':
    import threading
    import urllib.request
    from wsgiref.simple_server import make_server

    server = make_server('127.0.0.1', 0, application)   # 端口 0:随机空闲端口,防冲突
    port = server.server_port
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        # 本机若设了 http_proxy,urllib 会把回环请求交给代理,必须用空 ProxyHandler 直连
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(f'http://127.0.0.1:{port}/books/42', timeout=5) as resp:
            print(resp.status, resp.read().decode('utf-8'))
    finally:
        server.shutdown()       # 收尾:退出 serve_forever 循环,进程正常结束
        thread.join(timeout=5)
```

**追问**:
- WSGI 规范里 `environ` 包含什么?——CGI 风格的请求元数据,如 `REQUEST_METHOD`、`PATH_INFO`、`QUERY_STRING`、`wsgi.input` 请求体流等。
- 为什么 WSGI 返回的是可迭代对象而不是字符串?——支持流式响应,避免大响应体一次性占用内存。
