---
title: [Q790] get_queryset 数据隔离与按角色过滤
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q790 · get_queryset 数据隔离与按角色过滤

> 难度:★★★★ | 标签:DRF, 数据隔离

**问**:普通用户只能看自己的数据,管理员能看全部,这套逻辑写在哪才是对的?

**答**:统一收敛在 `get_queryset`:从 request 解析身份,基线 QuerySet 上叠加隔离条件,ViewSet 的 list/retrieve/get_object 全部走它,一处生效。反面教材:在 URL 传 user_id 参数决定范围(可伪造)、在每个 action 里复制粘贴 filter(漏一处就泄)。管理员旁路用集中判断;更复杂的可见性规则(部门、分享)下沉为 queryset 方法或专门的可视性模块。**get_queryset 是数据安全的总闸门**,代码评审重点看它。

```python
# file: code/03_Web后端开发/q790_queryset_isolation.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django、djangorestframework:pip install django djangorestframework,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=["rest_framework"],
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    USE_TZ=True,
)
django.setup()

from django.db import connection, models
from rest_framework import serializers, viewsets
from rest_framework.test import APIRequestFactory

class Order(models.Model):
    owner = models.CharField(max_length=32)
    amount = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Order)

Order.objects.create(owner="alice", amount=100)
Order.objects.create(owner="bob", amount=200)

class OrderS(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["owner", "amount"]

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderS

    def get_queryset(self):
        qs = Order.objects.all()
        user = self.request.headers.get("X-User", "anon")
        if user != "admin":
            qs = qs.filter(owner=user)   # 数据隔离总闸门
        return qs

factory = APIRequestFactory()
list_view = OrderViewSet.as_view({"get": "list"})
r1 = list_view(factory.get("/orders", HTTP_X_USER="alice"))
r1.render()
print("alice 看到:", r1.content.decode())
r2 = list_view(factory.get("/orders", HTTP_X_USER="admin"))
r2.render()
print("admin 看到条数:", r2.content.decode().count("owner"))
```

**追问**:
- retrieve 越权会怎样?——get_object 基于隔离后的 queryset,查不到返回 404,与显式 403 的取舍要统一(建议 404 不暴露存在性)。
- 隔离字段加索引吗?——必须,租户/owner 列是所有查询的前导过滤列,复合索引以它开头。
