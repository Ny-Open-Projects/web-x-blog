---
title: [Q129] DRF ViewSet 与 Router
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q129 · DRF ViewSet 与 Router

> 难度:★★☆ | 标签:DRF, ViewSet

**问**:ViewSet 相比 APIView 的优势是什么?Router 生成了哪些路由?

**答**:`ModelViewSet` 把 list/retrieve/create/update/partial_update/destroy 六个标准动作聚合到一个类,配合 `DefaultRouter` 自动生成 RESTful 路由表,代码量远低于逐个写 APIView;`@action` 装饰器追加自定义端点(如 `ViewSet` 上的 `down()`)。权限/过滤/分页通过类属性 `permission_classes/queryset` 声明,配合 `get_serializer_class()` 按动作切换序列化器。

```python
# file: code/03_Web后端开发/q129_drf_viewset.py
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
```

**追问**:
- ViewSet 和 APIView 怎么选?——标准 CRUD + Router 自动路由用 ViewSet;非标准端点、需要完全控制方法映射用 APIView。
- @action(detail=False) 是什么意思?——作用于集合级(`GET /users/active`),detail=True 作用于单个对象(`POST /users/42/down`)。
- get_serializer_class 的常见用法?——按 self.action 返回不同序列化器:list 用简版、create 用完整版,避免一个 serializer 包打天下。
