"""索引体积估算: 对照实测 page_count 之差"""
import os
import sqlite3

def build(path, with_index):
    if os.path.exists(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("PRAGMA page_size=4096")
    c.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    c.executemany("INSERT INTO users VALUES(?,?,?)",
                  [(i, "user%d" % i, "user%d@example.com" % i) for i in range(1, 50001)])
    if with_index:
        c.execute("CREATE INDEX idx_email ON users(email)")
    conn.commit()
    pages = c.execute("PRAGMA page_count").fetchone()[0]
    conn.close()
    return pages * 4096

base = build("/tmp/q2241_a.db", with_index=False)
plus = build("/tmp/q2241_b.db", with_index=True)
idx_bytes = plus - base
n = 50000
key = len("user49999@example.com".encode())
print("5 万行 无索引库 %.2f MB, 带索引库 %.2f MB" % (base / 1048576.0, plus / 1048576.0))
print("索引实占 %.2f MB, 每行摊 %.0f B; 理论键宽 %d B + rowid 4 B + 页开销, 再按填充率放大"
      % (idx_bytes / 1048576.0, idx_bytes / n, key))
print("先问选择性再背成本: 低选择性宽键索引是常驻负担")
