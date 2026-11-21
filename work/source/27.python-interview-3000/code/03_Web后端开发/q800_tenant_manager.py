import contextvars
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

CURRENT_TENANT: contextvars.ContextVar = contextvars.ContextVar("tenant", default="public")

class TenantManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tenant=CURRENT_TENANT.get())

class Invoice(models.Model):
    tenant = models.CharField(max_length=32)
    amount = models.IntegerField(default=0)
    objects = TenantManager()      # 默认隔离
    all_objects = models.Manager() # 显式逃生口
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Invoice)

with connection.schema_editor() as se:
    pass
Invoice.all_objects.bulk_create([
    Invoice(tenant="acme", amount=100),
    Invoice(tenant="globex", amount=200),
])

token = CURRENT_TENANT.set("acme")
print("租户内可见:", Invoice.objects.count())
CURRENT_TENANT.reset(token)
print("逃生口全量:", Invoice.all_objects.count())
