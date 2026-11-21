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

class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Product)

Product.objects.bulk_create(
    [Product(name=f"p{i}", price=i) for i in range(5)], batch_size=2
)
products = list(Product.objects.all())
for p in products:
    p.price *= 10
Product.objects.bulk_update(products, ["price"], batch_size=3)
print(list(Product.objects.values_list("name", "price")))
