"""分页漂移: OFFSET 翻页遇到并发写入会重复与漏行"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE msgs(id INTEGER PRIMARY KEY AUTOINCREMENT, body TEXT)")
for i in range(1, 11):
    c.execute("INSERT INTO msgs(body) VALUES(?)", ("m%d" % i,))
conn.commit()

def page_offset(page, size=3):
    return [r[0] for r in c.execute(
        "SELECT id FROM msgs ORDER BY id DESC LIMIT ? OFFSET ?", (size, page * size))]

p1 = page_offset(0)
c.execute("INSERT INTO msgs(body) VALUES(?)", ("m11",))
c.execute("INSERT INTO msgs(body) VALUES(?)", ("m12",))
conn.commit()
p2 = page_offset(1)
print("OFFSET 第一页:", p1)
print("OFFSET 第二页:", p2, " <- 新消息把旧行往后推")
dup = sorted(set(p1) & set(p2), reverse=True)
print("两页重复的行:", dup, " 其余行被挤到第三页, 漂移实锤")

last = p1[-1]
p2k = [r[0] for r in c.execute(
    "SELECT id FROM msgs WHERE id < ? ORDER BY id DESC LIMIT 3", (last,))]
print("keyset 第一页:", p1, "锚点 last =", last)
print("keyset 第二页:", p2k, " WHERE id < 锚点, 不受新写入影响")
