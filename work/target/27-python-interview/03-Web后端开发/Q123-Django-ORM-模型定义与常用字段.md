---
title: [Q123] Django ORM 模型定义与常用字段
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q123 · Django ORM 模型定义与常用字段

> 难度:★★☆ | 标签:Django, ORM

**问**:如何定义 Django Model?一对一、一对多、多对多关系分别用什么字段?

**答**:模型继承 `models.Model`,每个字段映射数据库列,关系字段:外键 `ForeignKey`(一对多,多的那方持有)、`OneToOneField`(一对一)、`ManyToManyField`(多对多,Django 自动建中间表);都要写 `on_delete` 策略(CASCADE/SET_NULL/PROTECT)。常用 `Meta` 控制 ordering 和表名,`__str__` 提供可读表示,`related_name` 定义反向查询名。

```python
# file: code/03_Web后端开发/q123_django_models.py
# file: myapp/models.py  (Django 模块级代码)
try:
    from django.db import models
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='books')       # 一对多
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = models.ManyToManyField('Tag', blank=True)        # 多对多
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

# author.books.all()        反向查询
# book.tags.all()           多对多查询
# Book.objects.filter(author__name='alice')   跨表双下划线
```

**追问**:
- on_delete=PROTECT 什么时候用?——业务上不允许删除被引用对象(如财务记录);CASCADE 会连带删除,SET_NULL 要允许空值,选错就是数据事故。
- ManyToManyField 的 through 什么时候需要?——关系本身带属性(订单-商品的数量、加入时间)时自定义中间表;纯关联用默认表。
- related_name 不写会怎样?——默认 `<model>_set`,可读性差且重构易碎;显式命名是团队规范项。
