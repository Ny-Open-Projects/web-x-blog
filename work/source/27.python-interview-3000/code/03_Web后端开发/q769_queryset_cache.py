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

class Article(models.Model):
    title = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Article)

Article.objects.bulk_create([Article(title=f"t{i}") for i in range(3)])

connection.queries_log.clear()
qs = Article.objects.all()
print("count 触发查询:", len(connection.queries) == 1)
list(qs)
print("迭代触发查询:", len(connection.queries) == 2)
list(qs)
print("二次迭代走缓存:", len(connection.queries) == 2)
list(qs.order_by("-id"))
print("链式后重新查询:", len(connection.queries) == 3)
