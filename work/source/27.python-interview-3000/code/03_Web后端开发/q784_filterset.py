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
from rest_framework import filters, serializers, viewsets
from rest_framework.test import APIRequestFactory

class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Product)

Product.objects.bulk_create([
    Product(name="手机", price=3000),
    Product(name="耳机", price=300),
    Product(name="充电器", price=99),
])

class ProductS(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price"]

class PriceRange(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        lo = request.query_params.get("min_price")
        hi = request.query_params.get("max_price")
        if lo is not None:
            queryset = queryset.filter(price__gte=int(lo))
        if hi is not None:
            queryset = queryset.filter(price__lte=int(hi))
        return queryset

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductS
    filter_backends = [PriceRange, filters.OrderingFilter]
    ordering_fields = ["price", "name"]
    ordering = ["name"]

req = APIRequestFactory().get("/products", {"min_price": "100", "ordering": "-price"})
resp = ProductViewSet.as_view({"get": "list"})(req)
resp.render()
print(resp.content.decode()[:80])
