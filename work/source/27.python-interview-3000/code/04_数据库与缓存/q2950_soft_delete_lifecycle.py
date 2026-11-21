"""软删除全链路: 盖时间戳 查询过滤 恢复冲突 到期分批清除"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE doc(id INTEGER PRIMARY KEY, slug TEXT NOT NULL,
                 title TEXT, deleted_at REAL);
CREATE UNIQUE INDEX uq_slug ON doc(slug) WHERE deleted_at IS NULL;
CREATE INDEX idx_doc_del ON doc(deleted_at);
""")


def add(slug, title):
    cur = conn.execute("INSERT INTO doc(slug, title) VALUES(?,?)", (slug, title))
    conn.commit()
    return cur.lastrowid


def get_live(slug):
    row = conn.execute(
        "SELECT id, slug, title FROM doc WHERE slug=? AND deleted_at IS NULL",
        (slug,)).fetchone()
    return dict(zip(("id", "slug", "title"), row)) if row else None


def soft_delete(slug):
    cur = conn.execute(
        "UPDATE doc SET deleted_at=? WHERE slug=? AND deleted_at IS NULL",
        (time.time(), slug))
    conn.commit()
    return cur.rowcount == 1


id1 = add("hello", "第一篇")
print("写入:", get_live("hello"))
print("软删除:", soft_delete("hello"), "-> 查询:", get_live("hello"))

# 部分唯一索引: 删除后 slug 释放, 同名可以再建
id2 = add("hello", "接力篇")
print("同 slug 再建成功, 新 id =", id2,
      "总行数(1 删 1 活):", conn.execute("SELECT COUNT(*) FROM doc").fetchone()[0])

# 直接恢复旧行会撞部分唯一索引(slug 被新行占用) -> 先换名再恢复
try:
    conn.execute("UPDATE doc SET deleted_at=NULL WHERE id=?", (id1,))
    conn.commit()
except sqlite3.IntegrityError as e:
    conn.rollback()
    print("直接恢复被唯一索引拦下:", e)
    conn.execute("UPDATE doc SET slug=?, deleted_at=NULL WHERE id=?",
                 ("hello-v1", id1))
    conn.commit()
    print("换名后恢复成功:", get_live("hello-v1"))

# 到期清理: 把 id1 的删除时间挪到 90 天前, 分批物理清除
conn.execute("UPDATE doc SET deleted_at=? WHERE id=?",
             (time.time() - 90 * 86400, id1))
conn.commit()
while True:
    cur = conn.execute(
        "DELETE FROM doc WHERE id IN "
        "(SELECT id FROM doc WHERE deleted_at IS NOT NULL "
        "AND deleted_at < ? LIMIT 1)",
        (time.time() - 30 * 86400,))
    conn.commit()
    if cur.rowcount == 0:
        break
print("过期清理后总行数:", conn.execute("SELECT COUNT(*) FROM doc").fetchone()[0])
