import asyncio
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=["*"],
    INSTALLED_APPS=[],
    ROOT_URLCONF="__main__",
    USE_TZ=True,
)
django.setup()

from django.http import HttpResponse

async def hello(request):
    return HttpResponse("async ok")

from django.urls import path

urlpatterns = [path("async-hello", hello)]

from django.core.asgi import get_asgi_application

application = get_asgi_application()   # 真实部署交给 uvicorn/daphne

async def call_once():
    async def receive():
        return {"type": "http.request", "body": b""}

    sent: list = []

    async def send(msg):
        sent.append(msg)

    scope = {
        "type": "http", "method": "GET", "path": "/async-hello",
        "headers": [], "query_string": b"",
    }
    await application(scope, receive, send)
    return sent

sent = asyncio.run(call_once())
print("ASGI 响应状态:", sent[0]["status"])
