---
title: [Q780] SerializerMethodField 与 source 的边界
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q780 · SerializerMethodField 与 source 的边界

> 难度:★★☆☆ | 标签:DRF, 序列化器

**问**:输出字段与模型字段对不上时,source 和 SerializerMethodField 怎么选?

**答**:`source="profile.bio"` 适合**取值路径**不同但仍是纯取数(支持跨关系点路径);`SerializerMethodField` 适合**需要计算、拼接、条件逻辑**的输出,实现 get_<field>(obj)。两者都是只读字段。注意点:source 跨关系会触发关联加载,注意 N+1;MethodField 里避免做查询,数据该在 view 层 prefetch 好;写路径需要同名输入时必须另建输入模型,读写模型分离是 DRF 的常态。

```python
# file: code/03_Web后端开发/q780_source_method.py
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
from rest_framework import serializers

class Profile(models.Model):
    bio = models.CharField(max_length=64, default="")
    class Meta:
        app_label = "demo"

class User(models.Model):
    name = models.CharField(max_length=32)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Profile)
    se.create_model(User)

u = User.objects.create(name="alice", profile=Profile.objects.create(bio="dev"))

class UserOut(serializers.ModelSerializer):
    bio = serializers.CharField(source="profile.bio", read_only=True)
    upper_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["name", "bio", "upper_name"]

    def get_upper_name(self, obj):
        return obj.name.upper()

print(UserOut(User.objects.select_related("profile").get(pk=u.pk)).data)
```

**追问**:
- source 指向不存在的属性会怎样?——序列化时抛 AttributeError,通常由错误的字段路径或漏 prefetch 引起。
- MethodField 能参与写吗?——不能,只读;写路径请显式声明可写字段或拆输入序列化器。
