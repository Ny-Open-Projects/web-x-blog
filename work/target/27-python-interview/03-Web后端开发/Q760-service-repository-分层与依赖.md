---
title: [Q760] service/repository 分层与依赖倒置
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q760 · service/repository 分层与依赖倒置

> 难度:★★★☆ | 标签:FastAPI, 架构

**问**:项目大了之后 handler 直接写 SQL 有什么问题?分层在 FastAPI 里怎么落地?

**答**:三层职责:路由层只做**参数解析与编排**;service 层承载业务规则与事务边界;repository 层只管数据存取,暴露领域语义的方法。FastAPI 的依赖注入是天然的**组合根**:`get_service()` 依赖里组装 repository,测试时用 dependency_overrides 换假实现,各层可独立替换。判断标准:handler 里出现 SQL 或第三方 SDK 就是越层信号;小项目可退化为两层,但路由不摸存储这条底线要守住。

```python
# file: code/03_Web后端开发/q760_layered.py
from dataclasses import dataclass
try:
    from fastapi import Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

@dataclass
class UserRepo:                     # 只管存取
    storage: dict

    def get(self, uid: int):
        return self.storage.get(uid)

@dataclass
class UserService:                  # 只管业务
    repo: UserRepo

    def profile(self, uid: int) -> dict:
        user = self.repo.get(uid)
        if not user:
            return {"id": uid, "name": "guest"}
        return {"id": uid, "name": user["name"]}

_storage = {1: {"name": "alice"}}

def get_service() -> UserService:   # 组合根
    return UserService(repo=UserRepo(storage=_storage))

app = FastAPI()

@app.get("/users/{uid}")
def get_user(uid: int, svc: UserService = Depends(get_service)):
    return svc.profile(uid)

client = TestClient(app)
print(client.get("/users/1").json())
print(client.get("/users/2").json())
```

**追问**:
- service 之间能互相依赖吗?——可以但要防止环,复杂业务用事件或拆分领域服务,组合根负责装配。
- repository 返回 ORM 对象还是 DTO?——向 service 返回 ORM 对象可接受,跨层到路由用响应模型转换,别把 ORM 对象直接塞进缓存。
