# Django + DRF 模块级代码
try:
    from rest_framework import viewsets, routers
    from rest_framework.decorators import action
    from rest_framework.response import Response
except ImportError:
    print("该题演示需要第三方库 djangorestframework:pip install djangorestframework(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

class BookViewSet(viewsets.ModelViewSet):
    queryset = None          # 实际: Book.objects.all()
    serializer_class = None  # 实际: BookSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        # 实际: book = self.get_object(); book.status = 'published'; book.save()
        return Response({'id': pk, 'status': 'published'})

# urls.py:
router = routers.DefaultRouter()
# router.register(r'books', BookViewSet)
# 自动生成:
# GET    /books/        -> list
# POST   /books/        -> create
# GET    /books/{pk}/   -> retrieve
# PUT    /books/{pk}/   -> update
# PATCH  /books/{pk}/   -> partial_update
# DELETE /books/{pk}/   -> destroy
# POST   /books/{pk}/publish/ -> 自定义 action
urlpatterns = router.urls if hasattr(routers, 'DefaultRouter') else []
