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
