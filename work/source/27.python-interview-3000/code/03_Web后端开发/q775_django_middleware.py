try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

def request_log(get_response):
    def middleware(request):
        request.META["X-Tenant"] = request.META.get("HTTP_X_TENANT", "public")
        response = get_response(request)
        response["X-Process-Flag"] = "ok"
        return response
    return middleware

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=["__main__.request_log", "django.middleware.common.CommonMiddleware"],
    ROOT_URLCONF="__main__",
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.http import HttpResponse
from django.urls import path

def index(request):
    return HttpResponse(f"tenant={request.META['X-Tenant']}")

urlpatterns = [path("", index)]

from django.test import Client

c = Client()
r = c.get("/", HTTP_X_TENANT="acme")
print(r.status_code, r.content.decode(), r["X-Process-Flag"])
