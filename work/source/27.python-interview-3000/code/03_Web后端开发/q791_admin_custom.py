try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=[
        "django.contrib.admin", "django.contrib.auth",
        "django.contrib.contenttypes", "django.contrib.sessions",
        "django.contrib.messages",
    ],
    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [], "APP_DIRS": True, "OPTIONS": {},
    }],
    USE_TZ=True,
)
django.setup()

from django.contrib import admin
from django.db import connection, models

class Book(models.Model):
    title = models.CharField(max_length=64)
    price = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Book)
Book.objects.create(title="Python cookbook", price=99)

site = admin.AdminSite(name="demo")

@admin.action(description="全部设为免费")
def make_free(modeladmin, request, queryset):
    queryset.update(price=0)

@admin.register(Book, site=site)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]
    search_fields = ["title"]
    actions = [make_free]

ma = BookAdmin(Book, site)
make_free(ma, None, Book.objects.filter(title="Python cookbook"))
print("action 生效:", Book.objects.get().price == 0)
print("列表列:", BookAdmin.list_display)
