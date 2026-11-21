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

from django.db import connection, models, transaction

class Ledger(models.Model):
    owner = models.CharField(max_length=32)
    amount = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Ledger)

try:
    with transaction.atomic():
        Ledger.objects.create(owner="a", amount=100)
        try:
            with transaction.atomic():          # 内层变成 SAVEPOINT
                Ledger.objects.create(owner="b", amount=-1)
                raise ValueError("内层失败")
        except ValueError:
            pass                                 # 只回滚内层
        Ledger.objects.create(owner="c", amount=50)
except ValueError:
    pass

print(list(Ledger.objects.values_list("owner", "amount")))
