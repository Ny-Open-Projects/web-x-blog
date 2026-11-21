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
