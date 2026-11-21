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
from rest_framework.test import APIRequestFactory

class Order(models.Model):
    owner = models.CharField(max_length=32)
    amount = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Order)

Order.objects.create(owner="alice", amount=100)
Order.objects.create(owner="bob", amount=200)

class OrderS(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["owner", "amount"]

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderS

    def get_queryset(self):
        qs = Order.objects.all()
        user = self.request.headers.get("X-User", "anon")
        if user != "admin":
            qs = qs.filter(owner=user)   # 数据隔离总闸门
        return qs

factory = APIRequestFactory()
list_view = OrderViewSet.as_view({"get": "list"})
r1 = list_view(factory.get("/orders", HTTP_X_USER="alice"))
r1.render()
print("alice 看到:", r1.content.decode())
r2 = list_view(factory.get("/orders", HTTP_X_USER="admin"))
r2.render()
print("admin 看到条数:", r2.content.decode().count("owner"))
