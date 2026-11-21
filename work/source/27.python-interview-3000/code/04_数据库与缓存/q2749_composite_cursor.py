"""复合游标分页: 元组比较命中复合索引, OR 改写是等价退路"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE item (id INTEGER PRIMARY KEY, created INTEGER, score REAL)")
c.executemany("INSERT INTO item VALUES(?,?,?)",
              [(i, 1700000000 + i // 3, (i * 7) % 100) for i in range(1, 40001)])
c.execute("CREATE INDEX idx_page ON item(created, id)")

def page_tuple(cur):
    sql = """SELECT created, id FROM item
             WHERE (created, id) > (?, ?) ORDER BY created, id LIMIT 20"""
    return c.execute(sql, cur).fetchall()

def page_or(cur):
    ct, cid = cur
    sql = """SELECT created, id FROM item
             WHERE created > ? OR (created = ? AND id > ?)
             ORDER BY created, id LIMIT 20"""
    return c.execute(sql, (ct, ct, cid)).fetchall()

cur = (0, 0)
seen = []
for p in range(10):
    a = page_tuple(cur)
    b = page_or(cur)
    assert a == b, "两种写法必须翻出同一页"
    seen.extend(a)
    cur = (a[-1][0], a[-1][1])
ids = [x[1] for x in seen]
assert len(set(ids)) == len(ids), "复合键排序下不丢行不重行"
print("两种游标写法 10 页各 20 行完全一致, 共 %d 行无重无漏" % len(seen))
print("元组版计划:", c.execute(
    "EXPLAIN QUERY PLAN SELECT created, id FROM item WHERE (created, id) > (1700000100, 5) "
    "ORDER BY created, id LIMIT 20").fetchall())
