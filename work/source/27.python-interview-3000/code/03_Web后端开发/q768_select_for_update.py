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

from django.db import NotSupportedError, connection, models, transaction

class Account(models.Model):
    owner = models.CharField(max_length=32)
    balance = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Account)

Account.objects.create(owner="a", balance=100)

try:
    with transaction.atomic():
        for acc in Account.objects.select_for_update().filter(owner="a"):
            acc.balance -= 10
            acc.save()
    print("行锁扣减后余额:", Account.objects.get(owner="a").balance)
except NotSupportedError:
    print("SQLite 不支持 FOR UPDATE, 生产用 PostgreSQL/MySQL")
