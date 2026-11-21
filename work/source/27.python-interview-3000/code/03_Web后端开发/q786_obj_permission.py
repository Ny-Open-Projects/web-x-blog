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
from django.test import RequestFactory
from rest_framework import serializers, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.test import APIRequestFactory

class Note(models.Model):
    text = models.CharField(max_length=64)
    owner = models.CharField(max_length=32)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Note)

Note.objects.create(text="mine", owner="alice")
Note.objects.create(text="theirs", owner="bob")

class NoteS(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["text", "owner"]

class NoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteS

    def get_object(self):
        obj = super().get_object()
        if obj.owner != self.request.headers.get("X-User", ""):
            raise PermissionDenied("只能访问自己的笔记")
        return obj

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.headers.get("X-User", "")
        if user:
            qs = qs.filter(owner=user)   # 列表层的数据隔离
        return qs

factory = APIRequestFactory()
view = NoteViewSet.as_view({"get": "retrieve"})
r1 = view(factory.get("/notes/2", HTTP_X_USER="alice"), pk=2)
r1.render()
print("取他人笔记:", r1.status_code)
r2 = view(factory.get("/notes/1", HTTP_X_USER="alice"), pk=1)
r2.render()
print("取自己笔记:", r2.status_code)
