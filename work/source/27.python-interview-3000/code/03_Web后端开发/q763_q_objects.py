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
from django.db.models import Q

class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Product)

Product.objects.bulk_create([
    Product(name="手机", price=3000),
    Product(name="耳机", price=300),
    Product(name="书", price=30, active=False),
])

filters = Q(active=True)                       # 基线条件
filters &= Q(name__contains="机") | Q(price__gte=300)  # 用户勾选的组合
print(list(Product.objects.filter(filters).values_list("name", flat=True)))
print(Product.objects.filter(~Q(name="书")).count())
