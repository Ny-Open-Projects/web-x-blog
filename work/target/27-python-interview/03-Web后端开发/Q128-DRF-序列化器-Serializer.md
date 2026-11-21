---
title: [Q128] DRF 序列化器 Serializer
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q128 · DRF 序列化器 Serializer

> 难度:★★☆ | 标签:DRF, Serializer

**问**:DRF Serializer 如何做序列化与反序列化校验?ModelSerializer 省了什么?

**答**:Serializer 是"双向适配器":`.data` 把 ORM 对象转 dict(JSON),`is_valid()` 校验外部输入后 `.validated_data` 供业务使用、`.save()` 创建/更新实例;校验层次为字段级 `validate_<field>` → 对象级 `validate` → 自定义 validators。`ModelSerializer` 依据模型自动生成字段与 validators,`PrimaryKeyRelatedField` 处理关联,`read_only/write_only` 控制方向;只读敏感字段务必显式声明,防止批量赋值漏洞。

```python
# file: code/03_Web后端开发/q128_drf_serializer.py
# Django + DRF 模块级代码(需 INSTALLED_APPS 含 rest_framework)
try:
    from rest_framework import serializers
except ImportError:
    print("该题演示需要第三方库 djangorestframework:pip install djangorestframework(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def validate_name(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError('name 不能为空')
        return value.strip()

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)

    class Meta:
        model_name = 'Book'   # 实际代码写 model = Book
        fields = ['id', 'title', 'price', 'author', 'author_id']
        read_only_fields = ['id']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('price 必须大于 0')
        return value

    def create(self, validated_data):
        validated_data.pop('author_id', None)
        # 实际: return Book.objects.create(**validated_data)
        return validated_data
```

**追问**:
- is_valid() 通过后 save() 必须调吗?——只读接口只要 validated_data;写操作 save() 才落库,两者职责不同。
- ModelSerializer 怎么控制暴露字段?——fields 元组白名单、read_only_fields、自定义 SerializerMethodField;全量暴露 model 字段是越权泄漏来源。
- 字段级与对象级校验的执行顺序?——先 validate_<field> 再对象级 validate;跨字段逻辑放 validate(),字段格式放字段级。
