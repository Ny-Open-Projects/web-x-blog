try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

events = []

class FullHooks:
    def __init__(self, get_response):
        self.get_response = get_response
        events.append("init")

    def __call__(self, request):
        events.append("call-in")
        response = self.get_response(request)
        events.append("call-out")
        return response

    def process_view(self, request, view_func, args, kwargs):
        events.append("process_view")
        return None

    def process_exception(self, request, exception):
        events.append("process_exception")
        return None

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=["__main__.FullHooks"],
    ROOT_URLCONF="__main__",
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.http import HttpResponse
from django.urls import path

def boom(request):
    raise ValueError("视图内异常")

urlpatterns = [path("boom", boom)]

from django.test import Client

c = Client()
c.get("/boom", raise_request_exception=False)
print("钩子触发顺序:", events)
