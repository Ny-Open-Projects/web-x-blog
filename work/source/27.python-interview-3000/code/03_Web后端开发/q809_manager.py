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

class PublishedQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status="p")

    def popular(self, n: int = 3):
        return self.order_by("-views")[:n]

class Post(models.Model):
    title = models.CharField(max_length=64)
    status = models.CharField(max_length=1, default="d")
    views = models.IntegerField(default=0)
    objects = PublishedQuerySet.as_manager()
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Post)

Post.objects.bulk_create([
    Post(title="a", status="p", views=10),
    Post(title="b", status="p", views=30),
    Post(title="c", status="p", views=20),
    Post(title="d", status="d", views=99),
])
print(list(Post.objects.published().popular(2).values_list("title", flat=True)))
