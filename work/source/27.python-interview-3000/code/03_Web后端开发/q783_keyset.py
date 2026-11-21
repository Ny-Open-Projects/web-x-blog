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

class Item(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Item)

Item.objects.bulk_create([Item(name=f"i{i}") for i in range(20)])

def page(cursor=None, size=5):
    qs = Item.objects.order_by("-id")
    if cursor is not None:
        qs = qs.filter(id__lt=cursor)
    rows = list(qs.values_list("id", flat=True)[:size])
    return rows, rows[-1] if rows else None

page1, cur = page()
page2, _ = page(cur)
print("第一页:", page1)
print("游标后第二页:", page2)
