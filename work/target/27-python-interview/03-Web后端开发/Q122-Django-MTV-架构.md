---
title: [Q122] Django MTV 架构
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q122 · Django MTV 架构

> 难度:★★☆ | 标签:Django, MTV

**问**:解释 Django 的 MTV 模式,它与 MVC 的对应关系是什么?

**答**:Django 的 MTV:Model 负责数据与业务规则(对应 MVC 的 Model)、Template 负责展示层(对应 View)、View 负责接收请求返回响应的业务逻辑(对应 Controller)。请求路径是:URLconf 按 url 匹配到 View,View 调用 Model 读写数据、渲染 Template,返回 HttpResponse。对比 MVC 只是命名侧重不同,Django 把"控制器"职责交给了框架自身的 URL 分发。

```python
# file: code/03_Web后端开发/q122_django_mtv.py
# Django 项目关键文件示意(模块级代码,展示三层协作)
# urls.py  -> path 映射到 views
# views.py -> 业务逻辑
# models.py-> 数据层
# templates/xxx.html -> 展示层

URLS = {  # 模拟 urls.py
    '/books/': 'book_list',
    '/books/<id>/': 'book_detail',
}

def book_list(request):          # views.py
    from myapp.models import Book
    books = Book.objects.all()   # models.py:ORM 查询
    context = {'books': books}   # 传给 templates 渲染
    return {'template': 'book_list.html', 'context': context}

# 流程:请求 -> urls.py 匹配 -> view -> model 读写 -> template 渲染 -> response
print(book_list.__doc__ or 'MTV flow demo')
```

**追问**:
- MTV 里 View 对应 MVC 的什么?——Controller 的职责(接收请求返回响应);MVC 的 View 职责由 Template 承担,差异主要是命名。
- Django 没有显式 Controller 吗?——URLconf 分发 + View 函数共同承担;框架本身把控制器逻辑内置了。
- 为什么这个命名差异是高频考点?——它考察「理解职责而非背名词」:能画出请求路径 URLconf→View→Model→Template 就算答对。
