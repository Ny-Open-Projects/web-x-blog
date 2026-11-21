try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django、djangorestframework:pip install django djangorestframework,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=["rest_framework"],
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    USE_TZ=True,
)
django.setup()

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

class EnvelopeRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return super().render(
            {"code": 0, "data": data}, accepted_media_type, renderer_context
        )

class Ping(APIView):
    renderer_classes = [EnvelopeRenderer]

    def get(self, request):
        return Response({"hello": True})

resp = Ping.as_view()(APIRequestFactory().get("/ping"))
resp.render()
print(resp.content.decode())
