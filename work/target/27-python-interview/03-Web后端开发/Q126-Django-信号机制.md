---
title: [Q126] Django 信号机制
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q126 · Django 信号机制

> 难度:★★☆ | 标签:Django, signal

**问**:Django 信号是什么?post_save 和 pre_save 的区别?使用时有什么坑?

**答**:信号是模型生命周期等事件的广播机制:实例在 `save()` 内先触发 `pre_save`(写库前,可修改待存值)再触发 `post_save`(写库后,`created=True` 表示是新建,适合发通知、清缓存);删除对应 pre/post_delete,m2m_changed 监听多对多变化。坑:信号隐式耦合难追踪,建议放 app 的 signals.py 并在 AppConfig.ready() 中注册;批量操作 `bulk_create/update()` 不触发 save 信号;receiver 要保证幂等以防重连重复执行。

```python
# file: code/03_Web后端开发/q126_django_signals.py
# myapp/signals.py (模块级代码)
try:
    from django.db.models.signals import post_save, pre_save
    from django.dispatch import receiver
    from myapp.models import Book
except ImportError:
    print("该题演示需要第三方库 django,且需在含 myapp.models 的 Django 项目上下文中运行:pip install django,原理见正文")
    raise SystemExit(0)

audit_log: list[str] = []

@receiver(pre_save, sender=Book)
def normalize_title(sender, instance, **kwargs):
    instance.title = instance.title.strip()      # 写库前修正数据

@receiver(post_save, sender=Book)
def on_book_saved(sender, instance, created, **kwargs):
    if created:
        audit_log.append(f'book created: {instance.title}')  # 建索引/发通知
    else:
        audit_log.append(f'book updated: {instance.title}')  # 清缓存

# myapp/apps.py 中注册:
# class MyAppConfig(AppConfig):
#     def ready(self):
#         import myapp.signals  # noqa: 导入即注册 receiver
```

**追问**:
- 为什么 bulk_create 不触发 save 信号?——它绕过模型 save() 直接拼批量 SQL;需要信号逻辑时改为循环 save 或在 bulk 后手动补事件。
- 信号放在哪注册?——app 的 signals.py + AppConfig.ready() 导入;否则接收器可能未被加载,静默失效。
- signals 的替代方案?——显式 service 层调用、领域事件入队;隐式魔法多了以后,调用链不可读是主要代价。
