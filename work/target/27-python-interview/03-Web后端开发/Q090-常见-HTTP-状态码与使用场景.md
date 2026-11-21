---
title: [Q090] 常见 HTTP 状态码与使用场景
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q090 · 常见 HTTP 状态码与使用场景

> 难度:★☆☆ | 标签:HTTP, 状态码

**问**:面试中常问的状态码有哪些?分别应该在什么场景返回?

**答**:2xx 成功类:200 OK、201 Created(POST 创建成功)、204 No Content(删除成功无响应体);3xx 重定向:301 永久、302 临时、304 Not Modified(缓存);4xx 客户端错误:400 参数错误、401 未认证、403 已认证但无权限、404 不存在、409 冲突、422 参数校验失败、429 限流;5xx 服务端错误:500 内部错误、502/504 网关错误与超时。准确区分 401/403、400/422 是高频考点。

```python
# file: code/03_Web后端开发/q090_status_codes.py
try:
    from fastapi import FastAPI, HTTPException, status
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
items = {1: 'apple'}

@app.post('/items', status_code=status.HTTP_201_CREATED)
def create_item(name: str):
    new_id = max(items or {0: 0}) + 1
    items[new_id] = name
    return {'id': new_id, 'name': name}

@app.get('/items/{item_id}')
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='item not found')
    return {'id': item_id, 'name': items[item_id]}

@app.delete('/items/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    items.pop(item_id, None)
```

**追问**:
- 401 和 403 的准确边界?——401 未认证(不知道你是谁,应带 WWW-Authenticate),403 已认证但无权限(知道你是谁但不行);混用会让客户端重试逻辑出错。
- 429 响应应该带什么?——`Retry-After` 头告知可重试时间,配合客户端退避;只给状态码不给策略,重试风暴照旧。
- 502 和 504 分别说明什么?——502 上游返回无效响应/进程崩溃,504 上游超时;排查方向不同:502 看进程存活与异常,504 看慢查询与超时配置。
