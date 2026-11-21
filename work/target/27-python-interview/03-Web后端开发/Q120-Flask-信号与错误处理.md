---
title: [Q120] Flask 信号与错误处理
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q120 · Flask 信号与错误处理

> 难度:★★☆ | 标签:Flask, signals

**问**:Flask 信号 signals 和钩子的区别是什么?如何统一处理错误返回 JSON?

**答**:信号是基于 blinker 的观察者机制:`request_started`、`request_finished`、`got_request_exception` 等由框架广播,任意多处的订阅者收到通知但不改变流程;钩子则参与请求处理链并可修改响应。信号适合日志、埋点、解耦的监控。错误统一处理用 `@app.errorhandler(HTTPException)` 或自定义异常类,注册处理器后视图直接 raise 即可。

```python
# file: code/03_Web后端开发/q120_flask_signal_error.py
try:
    from flask import Flask, jsonify, request
    from flask.signals import request_finished
except ImportError:
    print("该题演示需要第三方库 flask:pip install flask,原理见正文")
    raise SystemExit(0)

app = Flask(__name__)

@request_finished.connect_via(app)
def audit(sender, response, **extra):
    print(f'audit: {request.path} -> {response.status_code}')

class APIError(Exception):
    def __init__(self, message: str, status: int = 400):
        super().__init__(message)
        self.message = message
        self.status = status

@app.errorhandler(APIError)
def handle_api_error(e: APIError):
    return jsonify({'error': e.message}), e.status

@app.get('/items/<int:item_id>')
def get_item(item_id: int):
    if item_id > 100:
        raise APIError('item not found', 404)
    return jsonify({'id': item_id})

if __name__ == '__main__':
    app.run(port=5000)
```

**追问**:
- 信号和钩子怎么选?——需要修改流程/响应用钩子;只做旁路观察(埋点、审计)用信号,解耦且不侵入请求链。
- got_request_exception 典型用途?——统一异常上报与指标计数;注意它不能改变响应,改响应要 errorhandler。
- 自定义信号怎么发?——`signal.send(app)` 用 blinker 声明 Namespace 信号,订阅者按需连接;避免在热路径高频发送。
