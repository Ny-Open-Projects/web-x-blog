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
    body = models.TextField(default="")
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Article)

Article.objects.bulk_create([Article(title=f"t{i}", body="x" * 100) for i in range(3)])

connection.queries_log.clear()
articles = list(Article.objects.only("id", "title"))
print("SQL 里取了 body 吗:", "body" in connection.queries[0]["sql"].split())
articles[0].body  # 访问未加载字段触发第二次查询
print("当前总查询数:", len(connection.queries))
