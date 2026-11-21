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

class Timestamped(models.Model):           # abstract: 公共字段 Mixin
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True
        app_label = "demo"

class Post(Timestamped):
    title = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

class Draft(Post):                          # proxy: 同表不同行为
    class Meta:
        proxy = True
        app_label = "demo"

    @property
    def label(self):
        return f"草稿:{self.title}"

with connection.schema_editor() as se:
    se.create_model(Post)

p = Post.objects.create(title="hello")
print(Draft.objects.get(pk=p.pk).label)
print("proxy 同表:", Post._meta.db_table == Draft._meta.db_table)
