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
    slug = models.SlugField(default="")
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Author)
Author.objects.create(name="鲁迅")

def gen_slug(apps, schema_editor):       # 与真实迁移文件里的签名一致
    Author = apps.get_model("demo", "Author")
    for a in Author.objects.all().iterator():
        a.slug = f"author-{a.pk}"
        a.save(update_fields=["slug"])

class FakeApps:                          # 单文件演示: 模拟迁移框架注入
    @staticmethod
    def get_model(app, name):
        return Author

gen_slug(FakeApps, connection.schema_editor())
print(list(Author.objects.values("name", "slug")))
