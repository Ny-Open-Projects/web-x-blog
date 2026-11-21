---
title: [Q130] DRF 分页配置与游标分页
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q130 · DRF 分页配置与游标分页

> 难度:★★☆ | 标签:DRF, 分页

**问**:DRF 有哪几种分页方式?深度分页问题怎么解决?

**答**:内置三种:`PageNumberPagination`(`?page=2&size=10`,实现简单但大偏移量查询慢)、`LimitOffsetPagination`(`?limit=&offset=`,灵活但同样受深分页拖累)、`CursorPagination`(基于游标如 created_at+id,只能顺序翻页但性能稳定,适合信息流)。全局用 `DEFAULT_PAGINATION_CLASS`,也可自定义分页类调整 page_size_query_param、max_page_size 防止拉全量。深分页本质靠"游标 + 索引"或限制最大页码解决。

```python
# file: code/03_Web后端开发/q130_drf_pagination.py
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
```

**追问**:
- 为什么 CursorPagination 性能稳定?——基于有序唯一游标(如 created_at+id)做范围查询,翻页不随 offset 增长变慢;代价是只能顺序翻、不能跳页。
- 怎么防止 page_size 拉全量?——分页类里设 max_page_size,超限强制截断;漏配的接口会被一次循环翻页拖垮。
- 深分页的数据库侧解法?——延迟关联/游标(见 Q184),`LIMIT 100000,20` 之前必须先想到游标化改造。
