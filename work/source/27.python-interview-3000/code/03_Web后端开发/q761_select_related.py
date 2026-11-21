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

class Author(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        app_label = "demo"

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Author)
    se.create_model(Book)

a = Author.objects.create(name="鲁迅")
Book.objects.bulk_create([Book(title=f"书{i}", author=a) for i in range(3)])

connection.queries_log.clear()
for b in Book.objects.select_related("author"):
    _ = b.author.name
print("select_related 查询数:", len(connection.queries))

connection.queries_log.clear()
for b in Book.objects.prefetch_related("author"):
    _ = b.author.name
print("prefetch_related 查询数:", len(connection.queries))
