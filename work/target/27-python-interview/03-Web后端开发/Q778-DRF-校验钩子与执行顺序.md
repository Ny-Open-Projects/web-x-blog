---
title: [Q778] DRF 校验钩子与执行顺序
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q778 · DRF 校验钩子与执行顺序

> 难度:★★★☆ | 标签:DRF, 校验

**问**:validate_<field> 与 validate() 的执行顺序?校验失败怎么映射到响应?

**答**:顺序:**字段级验证器(含 validate_<field>)逐字段执行 → 对象级 validate(attrs)**,任一步失败即停止收集错误。字段级错误映射到字段名,validate() 里抛的 ValidationError 落到 `non_field_errors`(可自定义 NON_FIELD_ERRORS_KEY)。`is_valid(raise_exception=True)` 直接抛被 DRF 异常处理器转成 400;跨字段断言放 validate(),单纯格式放字段级或 validators 列表,层次清晰才能复用。

```python
# file: code/03_Web后端开发/q778_validators.py
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

from rest_framework import serializers

order = []

class Signup(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate_name(self, value):
        order.append("field:name")
        return value.strip()

    def validate(self, attrs):
        order.append("object:validate")
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("两次密码不一致")
        return attrs

s = Signup(data={"name": " alice ", "password": "x", "password2": "x"})
print(s.is_valid(), s.validated_data["name"])
print(order)
```

**追问**:
- 想让所有错误一次性收集完怎么做?——默认会收集字段级错误继续跑对象级,但字段级失败的字段不会进 validated_data。
- 校验器写在哪一层?——格式类放字段 validators,业务类放 validate(),跨模型唯一性用 UniqueTogetherValidator 声明。
