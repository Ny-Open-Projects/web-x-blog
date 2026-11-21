---
title: [Q119] Flask 请求钩子 before/after_request
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q119 · Flask 请求钩子 before/after_request

> 难度:★★☆ | 标签:Flask, 钩子

**问**:Flask 的四个请求钩子分别在什么时机执行?有什么典型用途?

**答**:`before_request` 在视图前执行(认证、记录开始时间);`after_request` 在视图正常返回后执行且必须接收并返回 response(加响应头、耗时统计);`teardown_request` 在异常时也执行(清理资源);`teardown_appcontext` 在应用上下文弹出时执行(关闭 DB 连接)。`after_request` 收到异常响应对象可统一加工;before_request 返回非 None 值会短路,直接作为响应。

```python
# file: code/03_Web后端开发/q119_flask_hooks.py
import time
try:
    from flask import Flask, g, request
except ImportError:
    print("该题演示需要第三方库 flask:pip install flask,原理见正文")
    raise SystemExit(0)

app = Flask(__name__)
logs: list[str] = []

@app.before_request
def start_timer():
    g.start = time.perf_counter()
    logs.append(f'start {request.path}')

@app.after_request
def add_header(response):
    cost = round((time.perf_counter() - g.start) * 1000, 2)
    response.headers['X-Cost-Ms'] = str(cost)
    logs.append(f'end {request.path}')
    return response

@app.teardown_appcontext
def close_db(exc):
    logs.append('teardown app context')   # 关闭 g 中缓存连接的典型位置

@app.get('/')
def index():
    return {'ok': True}

if __name__ == '__main__':
    app.run(port=5000)
```

**追问**:
- before_request 返回非 None 会怎样?——短路:该返回值直接作为响应,后续 before_request 与视图不执行;可用于维护窗口拦截。
- after_request 在视图抛异常时还执行吗?——不执行(走异常路径),teardown_request 才执行;要处理异常响应要用 errorhandler。
- 数据库会话的清理放哪个钩子?——teardown_appcontext,它在应用上下文弹出时必定执行,无论成功异常;放 after_request 会漏异常路径。
