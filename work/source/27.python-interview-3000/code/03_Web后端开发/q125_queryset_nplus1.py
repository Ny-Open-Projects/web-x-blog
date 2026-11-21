# 自包含演示:用内存对象 + SQL 计数器模拟 QuerySet,对比 N+1 与两种预取策略
class QueryStats:
    """模拟 django.db.connection.queries:记录"数据库"被查询的次数"""
    count = 0

    @classmethod
    def hit(cls, sql):
        cls.count += 1

class Author:
    def __init__(self, name):
        self.name = name

class Tag:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author, tags):
        self.title = title
        self._author = author
        self._tags = list(tags)
        self._author_loaded = False   # False 时访问 author/tags 属性会"再查一次库"
        self._tags_loaded = False

    @property
    def author(self):
        if not self._author_loaded:   # N+1 的 N:每本书触发一次额外查询
            QueryStats.hit(f"SELECT * FROM author WHERE id = {id(self._author) % 100}")
            self._author_loaded = True
        return self._author

    @property
    def tags(self):
        if not self._tags_loaded:
            QueryStats.hit(f"SELECT * FROM tag WHERE book_id = '{self.title}'")
            self._tags_loaded = True
        return self._tags

BOOKS = [
    Book("三体", Author("刘慈欣"), [Tag("科幻"), Tag("小说")]),
    Book("呐喊", Author("鲁迅"), [Tag("文学")]),
    Book("朝花夕拾", Author("鲁迅"), [Tag("文学")]),
]

def bad_nplus1():
    QueryStats.count = 0
    QueryStats.hit("SELECT * FROM book")        # 迭代求值:第 1 条
    return [f'{b.title} by {b.author.name}' for b in BOOKS]
    # 每本书额外查询一次 author -> 1 + N 条 SQL(N=3 时共 4 条)

def good_select_related():
    # 模拟 select_related('author'):JOIN 一次取回,关联对象迭代前已装填
    QueryStats.count = 0
    for b in BOOKS:
        b._author_loaded = True
    QueryStats.hit("SELECT ... JOIN author ON author.id = book.author_id")
    return [f'{b.title} by {b.author.name}' for b in BOOKS]

def good_prefetch_related():
    # 模拟 prefetch_related('tags'):书 1 条 + 标签 1 条,共 2 条 SQL
    QueryStats.count = 0
    for b in BOOKS:
        b._tags_loaded = True
    QueryStats.hit("SELECT * FROM book")
    QueryStats.hit("SELECT * FROM tag WHERE book_id IN (...)")
    return [{b.title: [t.name for t in b.tags]} for b in BOOKS]
    # 注意:先 prefetch 再 all(),不要再写 b.tags.filter(...) 产生新查询

print(bad_nplus1(), "SQL 条数:", QueryStats.count)             # 4 条(1+N,N=3)
print(good_select_related(), "SQL 条数:", QueryStats.count)    # 1 条
print(good_prefetch_related(), "SQL 条数:", QueryStats.count)  # 2 条
