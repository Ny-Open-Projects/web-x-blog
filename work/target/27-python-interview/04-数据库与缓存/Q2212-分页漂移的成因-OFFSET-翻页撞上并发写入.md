---
title: [Q2212] 分页漂移的成因: OFFSET 翻页撞上并发写入
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2212 · 分页漂移的成因: OFFSET 翻页撞上并发写入

> 难度:★★★☆ | 标签:SQL, 分页

**问**:用户翻到第二页看到了第一页的旧数据,或者漏了几行,是怎么回事?

**答**:OFFSET 分页的偏移量是"位置"不是"数据",两页之间的间隙里只要发生插入或删除,所有行的位置整体平移:新插入的行把旧行往后推,后面的页会重复出现已看过的行;删除则让某些行被跳过。这就是分页漂移,导出任务比用户翻页更容易中招,因为导出跨越的时间更长。根治办法是 keyset(游标)分页:每页携带本页最后一行的排序锚点,下一页用 WHERE 锚点比较 + LIMIT,位置与数据绑定,写入不影响已翻过的页。OFFSET 仍适合管理后台这类"可容忍抖动 + 需要跳页"的场景;两者取舍本质是"按位置看"与"按数据看"。

```python
# file: code/04_数据库与缓存/q2212_pagination_drift.py
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
```

**追问**:
- 排序列不唯一时 keyset 还稳吗?—— 不稳,锚点必须带唯一 tie-breaker(如 id),比较写成元组条件,否则同值边界会丢行。
- 深分页下 keyset 还有别的优势吗?—— LIMIT OFFSET 越深扫描越多,keyset 的 WHERE 走索引定位,代价与页深无关。

---
