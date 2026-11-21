try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django、djangorestframework:pip install django djangorestframework,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=["rest_framework"],
    REST_FRAMEWORK={"DEFAULT_THROTTLE_RATES": {"anon": "3/m"}},
    CACHES={"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}},
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    USE_TZ=True,
)
django.setup()

from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

class Ping(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        return Response({"ok": True})

factory = APIRequestFactory()
view = Ping.as_view()
codes = [view(factory.get("/ping")).status_code for _ in range(4)]
print(codes)  # 第 4 次被 429
