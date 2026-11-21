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
