---
title: [Q142] API 版本管理策略
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q142 · API 版本管理策略

> 难度:★★☆ | 标签:API 设计, 版本

**问**:API 为什么要版本化?URL 版本和 Header 版本各有什么优劣?

**答**:版本化让破坏性变更(改字段语义、删字段)在不中断老客户端的前提下演进。主流方案:URL 版本 `https://api.example.com/v1/users` 直观、易路由、可缓存,最常用;Header 版本 `Accept: application/vnd.myapp.v2+json` 保持 URL 稳定但调试不直观。原则:非破坏性变更(加可选字段)不升版本,破坏性变更才升;同一版本内只做向后兼容演进;FastAPI 用 APIRouter 按 prefix 拆分版本目录,老版本设废弃期并返回 Sunset 头。

```python
# file: code/03_Web后端开发/q142_api_version.py
try:
    from fastapi import FastAPI, APIRouter, Request
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI(title='versioned api')

v1 = APIRouter(prefix='/v1', deprecated=True)   # 标记废弃
v2 = APIRouter(prefix='/v2')

@v1.get('/users/{uid}')
def get_user_v1(uid: int):
    return {'id': uid, 'name': 'alice', 'email': 'a@x.com'}

@v2.get('/users/{uid}')
def get_user_v2(uid: int, request: Request):
    # v2 只加字段不改语义:向后兼容,不破坏 v1 客户端
    return {'id': uid, 'name': 'alice',
            'profile': {'email': 'a@x.com'}}

app.include_router(v1)
app.include_router(v2)
```

**追问**:
- URL 版本和 Header 版本怎么选?——优先 URL 版本:可缓存、可路由、调试直观;Header 版本只在网关能力成熟时用。
- 同一版本内怎么兼容演进?——只加可选字段、不改字段语义、新增端点;删字段/改类型必须升版本并给 Sunset 头过渡期。
- 废弃的旧版本怎么下线?——监控旧版本流量→公告 Sunset→返回弃用头→流量归零后下线;直接关停等于制造事故。
