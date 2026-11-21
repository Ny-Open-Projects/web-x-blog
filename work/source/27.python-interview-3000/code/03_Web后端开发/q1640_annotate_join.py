"""annotate 聚合的 join 放大: 两个反关系计数互相污染(标准库 sqlite3)。"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE books (id INTEGER PRIMARY KEY, author_id INT, title TEXT);
CREATE TABLE awards (id INTEGER PRIMARY KEY, book_id INT, name TEXT);
INSERT INTO authors VALUES (1, '王工');
INSERT INTO books VALUES (11, 1, '书一'), (12, 1, '书二');
INSERT INTO awards VALUES (91, 11, '奖一'), (92, 12, '奖A'), (93, 12, '奖B');
""")

one_join = conn.execute(
    "SELECT a.name, COUNT(b.id) FROM authors a "
    "LEFT JOIN books b ON b.author_id = a.id GROUP BY a.id").fetchall()
print("只 join books:", one_join)                       # 2 正确

two_joins = conn.execute(
    "SELECT a.name, COUNT(b.id), COUNT(w.id) FROM authors a "
    "LEFT JOIN books b ON b.author_id = a.id "
    "LEFT JOIN awards w ON w.book_id = b.id GROUP BY a.id").fetchall()
print("同时 join books+awards:", two_joins)              # 行数相乘, 计数互相污染

distinct = conn.execute(
    "SELECT a.name, COUNT(DISTINCT b.id), COUNT(DISTINCT w.id) FROM authors a "
    "LEFT JOIN books b ON b.author_id = a.id "
    "LEFT JOIN awards w ON w.book_id = b.id GROUP BY a.id").fetchall()
print("DISTINCT 修正:", distinct)
print("Django 对应: Count('books') 与 Count('books__awards') 同 annotate 必须都加 distinct=True")
