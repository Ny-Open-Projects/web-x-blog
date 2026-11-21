---
title: [Q118] Flask 上下文机制:application context 与 request context
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q118 · Flask 上下文机制:application context 与 request context

> 难度:★★★ | 标签:Flask, 上下文

**问**:Flask 的 current_app、request、g 为什么能在"全局"使用却互不串扰?

**答**:Flask 把"应用对象"和"请求对象"分别封装进 Application Context 与 Request Context 两个栈(LocalProxy),通过 werkzeug 的 thread-local(协程隔离)实现:每个线程/协程只能看到自己的栈,所以多并发下 `request` 指向各自请求而互不干扰。`current_app` 代理栈顶 app,离开应用上下文访问会抛 `RuntimeError`——这正是离线脚本要 `with app.app_context()` 的原因;`g` 是挂在应用上下文上的请求级共享命名空间。

```python
# file: code/03_Web后端开发/q118_flask_context.py
try:
    from flask import Flask, current_app, g, request
except ImportError:
    print("该题演示需要第三方库 flask:pip install flask,原理见正文")
    raise SystemExit(0)

app = Flask(__name__)
app.config['DB'] = 'sqlite:///:memory:'

def get_db():
    if 'db' not in g:                      # g 生命周期:一个请求
        g.db = current_app.config['DB']    # 请求内缓存连接
    return g.db

@app.get('/who')
def who():
    return {'db': get_db(), 'path': request.path}

# 离线/测试脚本中必须手动推上下文
with app.app_context():
    print(current_app.config['DB'])

with app.test_request_context('/who'):
    print(get_db(), request.path)
```

**追问**:
- app context 和 request context 谁包含谁?——push request context 时会自动 push 一个 app context;请求结束按相反顺序弹出。
- 离线脚本为什么报 RuntimeError: Working outside of application context?——current_app/g 依赖上下文栈;脚本要 `with app.app_context():` 手动压栈。
- Flask 的 LocalProxy 怎么实现并发隔离?——werkzeug Local 基于线程/协程 id 的字典,每个执行流看到自己的栈顶。
- g 对象和全局变量差在哪?——g 按请求/上下文隔离且请求结束自动清空;模块级全局在多并发下共享且要自己管生命周期。
