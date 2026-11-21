"""NULL 与空串: 语义混用的检测与归一"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, phone TEXT)")
conn.executemany("INSERT INTO users VALUES(?,?)",
                 [(1, '138'), (2, ''), (3, None), (4, '139')])
print("NULL 计数:", conn.execute("SELECT COUNT(*) FROM users WHERE phone IS NULL").fetchone()[0],
      "空串计数:", conn.execute("SELECT COUNT(*) FROM users WHERE phone=''").fetchone()[0])
print("phone = NULL 永远不成立: 判空必须 IS NULL 或 COALESCE")
conn.execute("UPDATE users SET phone=NULL WHERE phone=''")   # 归一: 空串视同未填
print("归一后 NULL:", conn.execute("SELECT COUNT(*) FROM users WHERE phone IS NULL").fetchone()[0])
