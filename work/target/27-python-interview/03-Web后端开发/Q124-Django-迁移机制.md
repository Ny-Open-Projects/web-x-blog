---
title: [Q124] Django 迁移机制
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q124 · Django 迁移机制

> 难度:★★☆ | 标签:Django, migration

**问**:`makemigrations` 和 `migrate` 的区别是什么?迁移冲突怎么处理?

**答**:`makemigrations` 把 models.py 的变更生成为迁移文件(版本化的 schema diff,存于 app/migrations/),`migrate` 把未应用的迁移按依赖顺序写入数据库并记录在 django_migrations 表;`sqlmigrate` 可预览 SQL,`showmigrations` 查看状态。多人协作产生的分支迁移冲突,用 `makemigrations --merge` 合并或 rebase 后重新生成;危险操作(删列)应先确认无引用,`--fake` 只改记录不动表,慎用。

```python
# file: code/03_Web后端开发/q124_django_migration.py
# 常用迁移命令(在项目根目录执行,注释形式自洽说明)
# python manage.py makemigrations          # models 变更 -> migrations/*.py
# python manage.py migrate                 # 应用迁移到数据库
# python manage.py showmigrations          # 查看迁移应用状态
# python manage.py sqlmigrate app 0002     # 预览某迁移的 SQL
# python manage.py migrate app 0001        # 回滚到指定迁移

# migrations/0002_add_price.py 生成内容示意
try:
    from django.db import migrations, models
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

class Migration(migrations.Migration):
    dependencies = [('myapp', '0001_initial')]   # 依赖链保证顺序

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(default=0, max_digits=8,
                                      decimal_places=2),
        ),
    ]
```

**追问**:
- 加了非空字段没有默认值会怎样?——makemigrations 会交互式询问一次性默认值或允许先置空,避免对存量数据报错。
- --fake 什么时候用?——手工已执行同等 DDL 或历史库补记录;乱用会造成 schema 与迁移记录不一致,后续迁移连环失败。
- 迁移冲突怎么产生与解决?——两个分支各生成同号迁移;`makemigrations --merge` 合并依赖,或 rebase 后重生成。
- 删列前要确认什么?——老版本代码是否还在读该列、是否有索引/视图依赖;先停写→灰度→删列是安全顺序。
