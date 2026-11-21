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
from django.db.models import Count, OuterRef, Subquery

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

a1, a2 = Author.objects.create(name="甲"), Author.objects.create(name="乙")
Book.objects.create(title="甲一", author=a1)
Book.objects.create(title="甲二", author=a1)
Book.objects.create(title="乙一", author=a2)

latest = Book.objects.filter(author=OuterRef("pk")).order_by("-id").values("title")[:1]
qs = Author.objects.annotate(book_count=Count("book"), latest_title=Subquery(latest))
print(list(qs.values("name", "book_count", "latest_title")))
