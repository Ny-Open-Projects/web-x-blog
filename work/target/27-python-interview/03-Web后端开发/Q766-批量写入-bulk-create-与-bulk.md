---
title: [Q766] 批量写入 bulk_create 与 bulk_update
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q766 · 批量写入 bulk_create 与 bulk_update

> 难度:★★★☆ | 标签:Django ORM, 性能

**问**:要插入几万行,循环 save 为什么不行?bulk 系列的注意事项?

**答**:循环 save 每行一次 INSERT 加一轮信号和字段准备,几万行就是几万次往返;`bulk_create(objs, batch_size=n)` 合并成批量 INSERT,batch_size 控制单批大小避免 SQL 过长或参数超限。注意事项:bulk_create **不触发 post_save 信号、不调用 save()**;主键回填依赖后端 RETURNING(新 Django + SQLite/PG 支持),`ignore_conflicts=True` 时主键不回填;`bulk_update` 按字段名批量 UPDATE,同样跳过信号。批量导入的信号/业务钩子要在调用处显式补偿。

```python
# file: code/03_Web后端开发/q766_bulk_ops.py
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

class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Product)

Product.objects.bulk_create(
    [Product(name=f"p{i}", price=i) for i in range(5)], batch_size=2
)
products = list(Product.objects.all())
for p in products:
    p.price *= 10
Product.objects.bulk_update(products, ["price"], batch_size=3)
print(list(Product.objects.values_list("name", "price")))
```

**追问**:
- bulk_create 和 update_or_create 混合的幂等导入怎么做?——先 ignore_conflicts 批插,再按唯一键 bulk_update 修正字段。
- 大批量导入还要注意什么?——包一层 transaction.atomic 减少提交次数,导入期间可延后索引与约束校验。
