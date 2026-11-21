import datetime
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    USE_TZ=True,
    TIME_ZONE="Asia/Shanghai",
    INSTALLED_APPS=[],
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
)
django.setup()

from django.utils import timezone

naive = datetime.datetime(2026, 1, 1, 8, 0)
aware = timezone.make_aware(naive)
print("aware:", aware.isoformat())
print("转本地时区:", timezone.localtime(aware))
print("now 是 aware:", timezone.now().utcoffset() is not None)
try:
    naive < timezone.now()
except TypeError as e:
    print("混比崩溃:", type(e).__name__)
