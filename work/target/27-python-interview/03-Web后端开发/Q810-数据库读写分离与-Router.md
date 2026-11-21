---
title: [Q810] 数据库读写分离与 Router
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q810 · 数据库读写分离与 Router

> 难度:★★★★ | 标签:Django, 读写分离

**问**:读写分离的 Router 怎么写?主从延迟带来的读己之写问题怎么解决?

**答**:实现 `database_routers.Router`:db_for_read 返回副本、db_for_write 返回主库、allow_relation 与 allow_migrate 控制关系与迁移(迁移只落主库),配置到 `DATABASE_ROUTERS`。主从延迟的坑:写后立刻读(注册后登录态)读到旧副本。对策:写后一段时间**粘住主库**(session 标记或缓存时间窗)、关键读显式走主库(using("default"))、或副本按需降级。事务必须整体在主库,Router 里把事务内读也导回主库。

```python
# file: code/03_Web后端开发/q810_db_router.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={
        "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"},
        "replica": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"},
    },
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        return "replica"

    def db_for_write(self, model, **hints):
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, **hints):
        return db == "default"

from django.db import models

class KV(models.Model):
    k = models.CharField(max_length=8)
    class Meta:
        app_label = "demo"

router = PrimaryReplicaRouter()
print("读走:", router.db_for_read(KV))
print("写走:", router.db_for_write(KV))
print("迁移只落主库:", router.allow_migrate("replica", "demo") is False)
```

**追问**:
- 刚写入的数据要立刻展示怎么办?——写操作后把用户粘主库几十秒,或该接口显式 using 主库读。
- 跨库事务怎么办?——Router 方案下没有跨库事务,跨库一致性要靠异步任务与对账,别指望 ORM 帮你。
