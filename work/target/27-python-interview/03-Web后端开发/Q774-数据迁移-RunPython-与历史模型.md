---
title: [Q774] 数据迁移 RunPython 与历史模型
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q774 · 数据迁移 RunPython 与历史模型

> 难度:★★★★ | 标签:Django, 迁移

**问**:写 data migration 为什么必须用 apps.get_model 而不是直接 import 模型?

**答**:迁移要在**任意历史时点可重放**,直接 import 拿到的是"当前代码"的模型,字段可能与该迁移时点的 schema 不一致,导致隐蔽数据错误;`apps.get_model(app_label, model_name)` 迁移框架提供的**历史模型快照**才与当时的迁移状态匹配。规范写法:函数签名 `(apps, schema_editor)`,配 `reverse_code` 保证可回滚;大表迁移分批 iteration 防止长事务;新加字段带 default 的迁移策略见在线 DDL 题。

```python
# file: code/03_Web后端开发/q774_data_migration.py
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

from django.db import connection, models

class Author(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(default="")
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Author)
Author.objects.create(name="鲁迅")

def gen_slug(apps, schema_editor):       # 与真实迁移文件里的签名一致
    Author = apps.get_model("demo", "Author")
    for a in Author.objects.all().iterator():
        a.slug = f"author-{a.pk}"
        a.save(update_fields=["slug"])

class FakeApps:                          # 单文件演示: 模拟迁移框架注入
    @staticmethod
    def get_model(app, name):
        return Author

gen_slug(FakeApps, connection.schema_editor())
print(list(Author.objects.values("name", "slug")))
```

**追问**:
- reverse_code 不写会怎样?——默认不可逆,回滚该迁移会报错,数据迁移应显式给 noop 或反向逻辑。
- 大表数据迁移怎么避免锁库?——按主键分批 update 循环提交,或改造为读旧写新的应用层策略。
