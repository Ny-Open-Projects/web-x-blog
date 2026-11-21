---
title: [Q768] select_for_update 行锁与死锁预防
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q768 · select_for_update 行锁与死锁预防

> 难度:★★★★ | 标签:Django ORM, 并发控制

**问**:并发扣库存除了 F 表达式,行锁怎么用?注意什么?

**答**:`select_for_update()` 在事务内对选中行加排他锁,直到事务结束,其他事务的同类读取会等待。铁律:**必须在 atomic 块内**,否则 Django 抛 TransactionManagementError;锁定要**按固定顺序**访问资源,多行锁定统一排序,防死锁。SQLite 不支持 FOR UPDATE(引擎级并发模型不同),PostgreSQL/MySQL 才有完整语义;还可配 `nowait=True`/`skip_locked=True` 做抢占式任务队列。锁内只做短操作,慢 IO 会放大锁等待。

```python
# file: code/03_Web后端开发/q768_select_for_update.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.db import NotSupportedError, connection, models, transaction

class Account(models.Model):
    owner = models.CharField(max_length=32)
    balance = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Account)

Account.objects.create(owner="a", balance=100)

try:
    with transaction.atomic():
        for acc in Account.objects.select_for_update().filter(owner="a"):
            acc.balance -= 10
            acc.save()
    print("行锁扣减后余额:", Account.objects.get(owner="a").balance)
except NotSupportedError:
    print("SQLite 不支持 FOR UPDATE, 生产用 PostgreSQL/MySQL")
```

**追问**:
- skip_locked 的典型场景?——多个 worker 用 SELECT FOR UPDATE SKIP LOCKED 抢任务行,天然实现工作队列。
- F 表达式和行锁怎么选?——单字段原子运算用 F 足够;要先读后判断多字段业务规则再写,用行锁包住读改写。
