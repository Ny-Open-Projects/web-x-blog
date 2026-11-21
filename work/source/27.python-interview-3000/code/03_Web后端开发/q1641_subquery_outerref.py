"""相关子查询取每行最新关联值: Subquery/OuterRef 的 SQL 本质(标准库 sqlite3)。"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE books (id INTEGER PRIMARY KEY, author_id INT, title TEXT, created_at TEXT);
INSERT INTO authors VALUES (1, '王工'), (2, '李工');
INSERT INTO books VALUES (11, 1, '书一', '2026-01-01'), (12, 1, '书二', '2026-03-01'),
                         (13, 2, '书三', '2026-02-01');
""")

# 相关子查询: 内层用外层行的 author_id 过滤, 排序取第一条, 这就是 OuterRef 的本质
rows = conn.execute(
    "SELECT a.name, "
    "  (SELECT b.title FROM books b WHERE b.author_id = a.id "
    "   ORDER BY b.created_at DESC LIMIT 1) AS latest, "
    "  (SELECT COUNT(*) FROM books b WHERE b.author_id = a.id) AS total "
    "FROM authors a ORDER BY a.id").fetchall()
for r in rows:
    print(r)

# 反例: 先 GROUP BY 求最大时间再 join 回原表, created_at 撞车时一行会变多行
conn.execute("INSERT INTO books VALUES (14, 2, '书三修订', '2026-02-01')")
tie = conn.execute(
    "SELECT a.name, b.title FROM authors a "
    "JOIN (SELECT author_id, MAX(created_at) AS m FROM books GROUP BY author_id) t "
    "  ON t.author_id = a.id "
    "JOIN books b ON b.author_id = a.id AND b.created_at = t.m").fetchall()
print("MAX 回连在时间撞车时多行:", tie)
print("Django 写法: Subquery(Book.objects.filter(author=OuterRef('pk'))"
      ".order_by('-created_at').values('title')[:1])")
