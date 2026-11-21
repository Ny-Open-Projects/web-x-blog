---
title: [Q805] 数据库连接管理与 CONN_MAX_AGE
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q805 · 数据库连接管理与 CONN_MAX_AGE

> 难度:★★★☆ | 标签:Django, 数据库

**问**:Django 默认每个请求新建数据库连接,CONN_MAX_AGE 是怎么优化的?边界在哪?

**答**:默认 `CONN_MAX_AGE=0`:每请求建连、结束关闭,PG 建连开销(认证、fork)在高 QPS 下很可观。设 `CONN_MAX_AGE=60` 开启持久连接,连接保留复用;`CONN_HEALTH_CHECKS=True` 在复用前 ping,剔除被服务端踢掉的死连。边界:持久连接是**每进程一份**,worker 多时总连接数 = 进程数,要 ≤ DB max_connections 的预算;PG 更彻底的池化用 pgbouncer(transaction 模式),此时要禁用服务端会话特性。

```python
# file: code/03_Web后端开发/q805_conn_persist.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={"default": {
        "ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:",
        "CONN_MAX_AGE": 60, "CONN_HEALTH_CHECKS": True,
    }},
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.db import connection

with connection.cursor() as cur:
    cur.execute("SELECT 1")
print("连接被保留复用:", connection.connection is not None)
print("CONN_MAX_AGE:", connection.settings_dict["CONN_MAX_AGE"])
```

**追问**:
- 长连接遇到 MySQL wait_timeout 断连怎么办?——开 CONN_HEALTH_CHECKS 并把 CONN_MAX_AGE 设小于 wait_timeout,或用 pgbouncer。
- 总连接数怎么算?——gunicorn worker × 线程/协程数 × 每连接池大小,再与 DB max_connections 对账,留管理连接余量。
