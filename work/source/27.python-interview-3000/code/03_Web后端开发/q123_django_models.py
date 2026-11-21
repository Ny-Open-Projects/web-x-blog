# file: myapp/models.py  (Django 模块级代码)
try:
    from django.db import models
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='books')       # 一对多
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = models.ManyToManyField('Tag', blank=True)        # 多对多
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

# author.books.all()        反向查询
# book.tags.all()           多对多查询
# Book.objects.filter(author__name='alice')   跨表双下划线
