---
title: [Q1931] LIKE 逃逸: ESCAPE 子句与用户输入转义
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1931 · LIKE 逃逸: ESCAPE 子句与用户输入转义

> 难度:★★☆☆ | 标签:SQL, LIKE

**问**:用户搜索框里输入了一个下划线或百分号, 拼进 LIKE 之后为什么查出来的东西不对?正确的处理方式是什么?

**答**:LIKE 里 % 匹配任意长度、_ 匹配任意单字符, 用户输入如果原样拼进模式, 这两个字符会被当成通配符解释, 语义被劫持。标准解法是三步:先把用户输入里的转义符本身翻倍,再转义 % 与 _,最后在 SQL 里显式写 ESCAPE 指定转义符。必须强调顺序:转义符要最先替换, 否则会出现二次转义错误。另外注意 LIKE 的匹配是整串匹配, 想要包含语义要自己在两端补 %, 转义只针对用户输入的部分。这是所有模糊搜索接口的必修课, 也是 LIKE 注入式查询错乱的根源。

```python
# file: code/04_数据库与缓存/q1931_like_escape.py
"""LIKE 逃逸: ESCAPE 子句与用户输入的通配符转义"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE files(name TEXT)")
rows = ["report_2026.pdf", "report-2026.pdf", "100%.csv", "a_b_c.txt", "plain.txt"]
conn.executemany("INSERT INTO files VALUES(?)", [(r,) for r in rows])
conn.commit()

# 陷阱: 用户输入直接拼进 LIKE, _ 与 % 会被当成通配符
pattern = "report_2026.pdf"
naive = [r[0] for r in conn.execute("SELECT name FROM files WHERE name LIKE ?", (pattern,))]
print("直接 LIKE report_2026.pdf ->", naive, "(下划线被当成任意单字符)")

# 修复: escape_like 把 \ % _ 全部转义, SQL 里用 ESCAPE 指定转义符
def escape_like(text, esc="\\"):
    return (text.replace(esc, esc + esc)
                .replace("%", esc + "%")
                .replace("_", esc + "_"))

safe = escape_like(pattern)
fixed = [r[0] for r in conn.execute(
    "SELECT name FROM files WHERE name LIKE ? ESCAPE '\\'", (safe,))]
print("转义后 ESCAPE 查询   ->", fixed, "(只命中字面下划线那一行)")

# 转义符本身也要转义: 文件名里带反斜杠时先替换它
tricky = escape_like("a_b\\c%d")
print("含转义符的输入      ->", repr(tricky), "(反斜杠先翻倍 其余再转义)")

# 通配符语义本身仍然可用: 字面量与模式各归各
w1 = [r[0] for r in conn.execute("SELECT name FROM files WHERE name LIKE '100\\%%' ESCAPE '\\'")]
w2 = [r[0] for r in conn.execute("SELECT name FROM files WHERE name LIKE '%pdf'")]
print("字面 100\\%% 加通配  ->", w1)
print("模式 %pdf 结尾匹配  ->", w2)
print("结论: 用户输入进 LIKE 前必须转义 \\ % _ 三个字符, SQL 显式写 ESCAPE, 否则语义被通配符劫持")
```

**追问**:
- 为什么转义符必须最先替换?—— 否则后续加进去的反斜杠会被当成需要转义的内容再次翻倍, 产生错误的模式。
- 参数化查询能防住这个问题吗?—— 不能, 参数化只防 SQL 注入, LIKE 模式里的通配符语义仍然生效, 转义是另一层。

---
