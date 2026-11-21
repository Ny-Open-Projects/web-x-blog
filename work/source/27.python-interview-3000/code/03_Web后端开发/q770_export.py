import csv
import io
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

Article.objects.bulk_create([Article(title=f"t{i}") for i in range(5)])

buf = io.StringIO()
writer = csv.writer(buf)
writer.writerow(["id", "title"])
rows = Article.objects.values_list("id", "title").iterator(chunk_size=100)
for row in rows:
    writer.writerow(row)
print("导出行数:", len(buf.getvalue().strip().splitlines()))
