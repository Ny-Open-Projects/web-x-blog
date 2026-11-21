try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={
        "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"},
        "replica": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"},
    },
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        return "replica"

    def db_for_write(self, model, **hints):
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, **hints):
        return db == "default"

from django.db import models

class KV(models.Model):
    k = models.CharField(max_length=8)
    class Meta:
        app_label = "demo"

router = PrimaryReplicaRouter()
print("读走:", router.db_for_read(KV))
print("写走:", router.db_for_write(KV))
print("迁移只落主库:", router.allow_migrate("replica", "demo") is False)
