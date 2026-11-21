---
title: [Q777] DRF 序列化器上下文 context 传递
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q777 · DRF 序列化器上下文 context 传递

> 难度:★★★☆ | 标签:DRF, 序列化器

**问**:SerializerMethodField 里要用当前用户做判断,context 怎么传进来?视图到序列化器的默认上下文有什么?

**答**:实例化时传 `Serializer(data, context={"request": request})`,序列化器内部用 `self.context` 读取;DRF 视图的 `get_serializer` 默认注入 **view 与 request** 两个键,所以 `self.context["request"].user` 是惯用法。context 让"同一个序列化器,不同视角输出不同"(管理员多字段、本人可见标记)。注意 context 是**弱契约**:团队要约定键名,或封装 get_serializer_context 统一供数。

```python
# file: code/03_Web后端开发/q777_serializer_context.py
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

class CommentIn(serializers.Serializer):
    body = serializers.CharField()

    def validate_body(self, value):
        for w in self.context.get("banned_words", set()):
            if w.lower() in value.lower():
                raise serializers.ValidationError(f"包含敏感词 {w}")
        return value

class CommentOut(serializers.Serializer):
    body = serializers.CharField()
    mine = serializers.SerializerMethodField()

    def get_mine(self, obj):
        return obj.get("owner") == self.context.get("viewer")

bad = CommentIn(data={"body": "剧透:主角死了"}, context={"banned_words": {"剧透"}})
print(bad.is_valid(), bad.errors)
out = CommentOut({"body": "很好看", "owner": "alice"}, context={"viewer": "alice"})
print(out.data)
```

**追问**:
- 序列化器嵌套时 context 会传给子序列化器吗?——会,context 沿嵌套传递,深度依赖 context 是可读性坏味道,及时收敛。
- to_representation 里怎么拿请求用户?——`self.context["request"].user`,但注意测试直调序列化器时必须手动给 context。
