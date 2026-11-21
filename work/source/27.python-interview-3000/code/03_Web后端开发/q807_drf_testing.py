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

from django.db import connection, models
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.test import APIRequestFactory, force_authenticate

class Note(models.Model):
    text = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Note)
Note.objects.create(text="n1")

class NoteS(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteS
    permission_classes = [IsAuthenticated]

class FakeUser:
    is_authenticated = True
    username = "alice"

factory = APIRequestFactory()
view = NoteViewSet.as_view({"get": "list"})

req = factory.get("/notes")
force_authenticate(req, user=FakeUser())
r1 = view(req)
r1.render()
print("已认证:", r1.status_code)

r2 = view(factory.get("/notes"))
r2.render()
print("未认证:", r2.status_code)
