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
