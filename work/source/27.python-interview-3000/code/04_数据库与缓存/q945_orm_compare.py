"""同一查询在两套 ORM 心智模型下的写法对照"""
COMPARISON = """
同一需求: 取每个作者的书籍数, 只要有书的作者

Django ORM:
    Author.objects.annotate(n=Count("book")).filter(n__gt=0)
    # QuerySet 惰性链, 迁移/admin 与模型一体

SQLAlchemy 2.0:
    select(Author, func.count(Book.id)).join(Book) \\
        .group_by(Author).having(func.count(Book.id) > 0)
    # 显式 join/group/having, Session 管理事务与状态

取舍:
  Django: 约定优先 上手快 生态内全链路  复杂 SQL 受限
  SQLAlchemy: 显式优先 控制力强 独立于框架  学习曲线陡
"""
if __name__ == "__main__":
    print(COMPARISON)
