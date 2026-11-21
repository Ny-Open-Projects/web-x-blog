---
title: [Q779] ModelSerializer 嵌套写入 create/update
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q779 · ModelSerializer 嵌套写入 create/update

> 难度:★★★★ | 标签:DRF, 序列化器

**问**:ModelSerializer 的可嵌套关系字段默认只读,要支持嵌套创建(订单带明细),怎么写?

**答**:嵌套 writable 关系必须**自己实现 create/update**:从 validated_data 弹出子列表,先建主对象再批量建子对象;更新语义要明确——整体替换(删旧建新)还是 diff 更新,两者一致性问题不同。要点:主子对象在**一个事务**里创建;批量插子行用 bulk_create;验证子行的业务约束(如明细不为空)放在 validate()。DRF 不替你做这些,是因为"正确的嵌套写语义"本来就是业务决策。

```python
# file: code/03_Web后端开发/q779_nested_write.py
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

from django.db import connection, models, transaction
from rest_framework import serializers

class Poll(models.Model):
    question = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Poll)
    se.create_model(Choice)

class ChoiceS(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["text"]

class PollS(serializers.ModelSerializer):
    choices = ChoiceS(many=True)
    class Meta:
        model = Poll
        fields = ["id", "question", "choices"]

    def create(self, validated_data):
        choices = validated_data.pop("choices")
        with transaction.atomic():
            poll = Poll.objects.create(**validated_data)
            Choice.objects.bulk_create([Choice(poll=poll, **c) for c in choices])
        return poll

data = {"question": "选谁", "choices": [{"text": "A"}, {"text": "B"}]}
s = PollS(data=data)
print(s.is_valid(raise_exception=False))
poll = s.save()
print(poll.question, poll.choices.count())
```

**追问**:
- 嵌套更新的删除语义怎么定?——整体替换最简单但会重建主键;要保 ID 就按 ID diff 增删改,建议在文档里写死。
- validated_data 里的嵌套结构长什么样?——关系键变成字典/列表的普通 Python 结构,pop 出来即用。
