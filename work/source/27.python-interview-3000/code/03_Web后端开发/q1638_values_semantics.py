"""values/values_list 的语义: dict、tuple、flat 各拿到什么(纯标准库模拟)。"""
try:
    import django
    HAS_DJANGO = True
except ImportError:
    HAS_DJANGO = False
    print("[降级] 未安装 django, 以下用内存数据模拟 QuerySet 的三种取值形态")

ROWS = [
    {"id": 1, "title": "a", "author_id": 9},
    {"id": 2, "title": "b", "author_id": 9},
]


def values(*fields):
    return [{f: r[f] for f in fields} for r in ROWS]


def values_list(*fields, flat=False, named=False):
    if flat:
        if len(fields) != 1:
            raise TypeError("flat 只能取一列")             # 由调用处捕获
        return [r[fields[0]] for r in ROWS]
    if named:
        from collections import namedtuple
        nt = namedtuple("Row", fields)
        return [nt(*(r[f] for f in fields)) for r in ROWS]
    return [tuple(r[f] for f in fields) for r in ROWS]


print("values      ->", values("id", "title"))
print("values_list ->", values_list("id", "title"))
print("flat        ->", values_list("title", flat=True))
print("named       ->", values_list("id", "title", named=True)[0].id)
try:
    values_list("id", "title", flat=True)
except TypeError as e:
    print("多列 flat:", e)
print("注意: 两种形态都不实例化模型, 实例方法与属性不可用; 外键列拿到的是主键值")
