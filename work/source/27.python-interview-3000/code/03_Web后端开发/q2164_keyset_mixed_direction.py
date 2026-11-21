"""混合方向排序的 keyset 翻页: 每列方向参与比较, tie-breaker 防丢行(纯标准库)。"""


class Desc:
    """包装降序列值, 让统一的元组比较天然生效。"""
    __slots__ = ("v",)

    def __init__(self, v):
        self.v = v

    def __lt__(self, other):
        return other.v < self.v

    def __eq__(self, other):
        return other.v == self.v


def sort_key(row, columns):
    return tuple(Desc(row[f]) if d == "desc" else row[f] for f, d in columns)


def keyset_page(rows, columns, cursor_key, limit):
    """取排序键严格大于游标键的行; 游标为上一页最后一行的排序键。"""
    data = rows
    if cursor_key is not None:
        data = [r for r in rows if sort_key(r, columns) > cursor_key]
    items = data[:limit]
    next_key = sort_key(items[-1], columns) if len(data) > limit else None
    return items, next_key


rows = [{"id": 1, "score": 90}, {"id": 2, "score": 90}, {"id": 3, "score": 80},
        {"id": 4, "score": 80}, {"id": 5, "score": 70}]
columns = [("score", "desc"), ("id", "asc")]
rows.sort(key=lambda r: sort_key(r, columns))
ordered = [r["id"] for r in rows]
print("完整排序:", ordered)

cursor, seen = None, []
while True:
    items, cursor = keyset_page(rows, columns, cursor, 2)
    seen += [r["id"] for r in items]
    if not cursor:
        break
print("keyset 翻页:", seen)
assert seen == ordered and len(set(seen)) == len(seen)

# 反例: 只用非唯一列 score 做游标, 页边界落在同分行时会整行丢失
page1 = rows[:1]
cursor_score = page1[-1]["score"]
rest = [r for r in rows if r["score"] < cursor_score]
naive_seen = [r["id"] for r in page1] + [r["id"] for r in rest[:3]]
print("裸 score 游标:", naive_seen, "-> id=2 的同分行被跳过")
assert 2 not in naive_seen
print("要点: 排序键必须追加唯一 tie-breaker; 混合方向时谓词与排序用同一个键函数, 方向参与每列比较")
