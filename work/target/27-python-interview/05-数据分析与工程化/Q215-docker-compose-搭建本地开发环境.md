---
title: [Q215] docker-compose 搭建本地开发环境
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q215 · docker-compose 搭建本地开发环境

> 难度:★★☆ | 标签:docker-compose, 本地环境

**问**:本地开发为什么要用 docker-compose?怎么让服务起来就绪后才跑应用?

**答**:compose 用一个 YAML 声明**整套依赖服务**(Postgres、Redis、消息队列),`docker compose up` 一键起齐,新人零配置搭环境,还能给集成测试提供隔离的临时数据库。关键问题:**依赖启动不等于就绪**——`depends_on` 只管启动顺序,Postgres 容器活着不代表能接受连接,要用 `healthcheck` + `depends_on.condition: service_healthy`,或应用侧重试。开发体验技巧:代码目录 volume 挂载实现热更新、固定容器名与端口、数据卷持久化数据库文件。

```yaml
# docker-compose.yml:非 python 文件
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: dev
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      retries: 5
    volumes:
      - pgdata:/var/lib/postgresql/data
  app:
    build: .
    depends_on:
      db:
        condition: service_healthy
    environment:
      DB_URL: postgres://postgres:dev@db:5432/postgres
    ports:
      - "8000:8000"
volumes:
  pgdata:
```

```python
# file: code/05_数据分析与工程化/q215_wait_for.py
import time


def wait_until(check, timeout: float = 5.0, interval: float = 0.5) -> bool:
    # 应用侧就绪等待:比 depends_on 更可靠的服务依赖处理
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if check():
            return True
        time.sleep(interval)
    return False


def test_wait_until_ready():
    attempts = {"n": 0}

    def ready():
        attempts["n"] += 1
        return attempts["n"] >= 3

    assert wait_until(ready, timeout=2) is True
```

**追问**:
- depends_on 和 service_healthy 的区别?——前者只保证启动顺序,后者等 healthcheck 通过才启动依赖方;数据库场景必须用后者。
- volume 挂载热更新注意什么?——代码挂载生效,但装在镜像里的依赖变化要重建;uvicorn --reload 只适合开发环境。
- compose 环境和生产的差异风险?——compose 是单机、明文配置;不要因为本地能跑就假设生产健康,集成测试要在类生产环境再过一遍。
