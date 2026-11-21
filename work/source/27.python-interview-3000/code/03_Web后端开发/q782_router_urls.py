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

from rest_framework import routers, serializers, viewsets

class NoteS(serializers.Serializer):
    text = serializers.CharField()

class NoteViewSet(viewsets.ModelViewSet):
    queryset = []
    serializer_class = NoteS

    from rest_framework.decorators import action

    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        pass

router = routers.SimpleRouter()
router.register(r"notes", NoteViewSet)
for url in router.urls:
    print(str(url.pattern), url.name)
