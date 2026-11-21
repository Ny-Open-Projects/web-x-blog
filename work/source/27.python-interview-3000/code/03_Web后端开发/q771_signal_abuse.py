try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.db import connection, models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Order(models.Model):
    no = models.CharField(max_length=32)
    class Meta:
        app_label = "demo"

audit = []

@receiver(post_save, sender=Order)
def sync_audit(sender, instance, created, **kwargs):
    audit.append(f"审计:{instance.no}")

with connection.schema_editor() as se:
    se.create_model(Order)

Order.objects.create(no="A1")                    # 触发信号
Order.objects.bulk_create([Order(no="A2")])      # bulk 不触发
Order.objects.filter(no="A1").update(no="A1b")   # update 不触发
print(audit)
