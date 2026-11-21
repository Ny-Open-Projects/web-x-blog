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
from django.db.models import F

class Account(models.Model):
    owner = models.CharField(max_length=32)
    balance = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Account)

Account.objects.create(owner="a", balance=100)
Account.objects.filter(owner="a").update(balance=F("balance") - 30)  # 单条原子 UPDATE
a = Account.objects.get(owner="a")
print(a.balance)

updated = Account.objects.filter(owner="a", balance__gte=200).update(balance=F("balance") - 200)
print("条件扣款成功笔数:", updated)  # 0 表示余额不足, 天然防超扣
