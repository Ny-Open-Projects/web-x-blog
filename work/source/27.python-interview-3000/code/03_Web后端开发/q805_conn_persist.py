try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={"default": {
        "ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:",
        "CONN_MAX_AGE": 60, "CONN_HEALTH_CHECKS": True,
    }},
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.db import connection

with connection.cursor() as cur:
    cur.execute("SELECT 1")
print("连接被保留复用:", connection.connection is not None)
print("CONN_MAX_AGE:", connection.settings_dict["CONN_MAX_AGE"])
