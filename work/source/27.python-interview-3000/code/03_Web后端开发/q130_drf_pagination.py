# Django + DRF 模块级代码
try:
    from rest_framework.pagination import (
        PageNumberPagination, CursorPagination,
    )
    from rest_framework.response import Response
except ImportError:
    print("该题演示需要第三方库 djangorestframework:pip install djangorestframework(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'      # ?size=20 动态页大小
    max_page_size = 100                 # 上限防滥用

class FeedCursorPagination(CursorPagination):
    page_size = 20
    ordering = '-created_at'            # 游标基于该排序键

class BookListAPI:
    pagination_class = StandardPagination

    def paginate(self, queryset, request):
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        return paginator.get_paginated_response(page)
        # 响应: {"count": 123, "next": "...?page=2", "previous": null, "results": [...]}

print(StandardPagination().page_size)   # 10
