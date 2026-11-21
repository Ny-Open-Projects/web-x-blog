"""values_list 的 named、链式覆盖与外键语义(纯标准库模拟)。"""
from collections import namedtuple

ROWS = [{"id": 1, "title": "a", "author_id": 9, "views": 100},
        {"id": 2, "title": "b", "author_id": 9, "views": 200}]


def values_list(*fields, flat=False, named=False):
    if named:
        nt = namedtuple("Row", fields)
        return [nt(*(r[f] for f in fields)) for r in ROWS]
    if flat:
        return [r[fields[0]] for r in ROWS]
    return [tuple(r[f] for f in fields) for r in ROWS]


def chain_values(*stages):
    """模拟 QuerySet 链式: 每个 values 阶段整体替换投影, 只有最后一个生效。"""
    return [{f: r[f] for f in stages[-1]} for r in ROWS]


row = values_list("id", "views", named=True)[0]
print("named 按名访问:", row.id, row.views, "| 列名固定, 不随元组顺序漂移")
print("外键列拿到的是主键:", values_list("author_id")[0], "不是作者对象")
print("链式覆盖 values(id,title).values(id,views) ->", chain_values(("id", "title"), ("id", "views")))
print("CSV 导出用 named 最稳: 表头与取值一一对应")
