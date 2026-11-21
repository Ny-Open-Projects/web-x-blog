try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django、djangorestframework:pip install django djangorestframework,原理见正文")
    raise SystemExit(0)

def envelope_handler(exc, context):
    from rest_framework.views import exception_handler as default_handler
    resp = default_handler(exc, context)
    if resp is None:
        return resp
    detail = resp.data.get("detail") if isinstance(resp.data, dict) else None
    resp.data = {
        "code": resp.status_code,
        "message": str(detail) if detail else "request failed",
        "errors": None if detail else resp.data,
    }
    return resp

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=["rest_framework"],
    REST_FRAMEWORK={"EXCEPTION_HANDLER": "__main__.envelope_handler"},
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    USE_TZ=True,
)
django.setup()

from rest_framework.exceptions import NotFound
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

class Boom(APIView):
    def get(self, request):
        raise NotFound("资源不存在")

resp = Boom.as_view()(APIRequestFactory().get("/boom"))
resp.render()
print(resp.status_code, resp.content.decode())
