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
from django.test.utils import CaptureQueriesContext

class Book(models.Model):
    title = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

class Author(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        app_label = "demo"

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Author)
    se.create_model(Book)

a = Author.objects.create(name="甲")
Book.objects.bulk_create([Book(title=f"b{i}", author=a) for i in range(3)])

def n_plus_one():
    for b in Book.objects.all():
        _ = b.author.name

def fixed():
    for b in Book.objects.select_related("author"):
        _ = b.author.name

with CaptureQueriesContext(connection) as ctx1:
    n_plus_one()
with CaptureQueriesContext(connection) as ctx2:
    fixed()
print("修复前查询数:", len(ctx1.captured_queries))
print("修复后查询数:", len(ctx2.captured_queries))
