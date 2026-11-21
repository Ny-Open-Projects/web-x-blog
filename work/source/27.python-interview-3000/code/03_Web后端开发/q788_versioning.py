try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django、djangorestframework:pip install django djangorestframework,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=["rest_framework"],
    REST_FRAMEWORK={
        "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.HeaderVersioning",
        "DEFAULT_VERSION": "v1",
        "ALLOWED_VERSIONS": ["v1", "v2"],
    },
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    USE_TZ=True,
)
django.setup()

from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

class Echo(APIView):
    def get(self, request):
        return Response({"version": request.version})

factory = APIRequestFactory()
r1 = Echo.as_view()(factory.get("/echo", HTTP_ACCEPT="application/json; version=v2"))
print(r1.data)
r2 = Echo.as_view()(factory.get("/echo"))
print(r2.data)
