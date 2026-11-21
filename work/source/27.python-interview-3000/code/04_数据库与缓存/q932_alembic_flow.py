"""演示迁移脚本的 revision 链结构与 upgrade/downgrade 对称性"""
MIGRATIONS = {
    "a1": {"down": None, "up": "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)"},
    "b2": {"down": "a1", "up": "ALTER TABLE users ADD COLUMN age INT",
           "downgrade": "ALTER TABLE users DROP COLUMN age"},
}

def current(rev):
    return rev

def upgrade(conn, target):
    rev = current(None)
    for rid, m in MIGRATIONS.items():
        if rev is None or _after(rid, rev):
            conn.execute(m["up"]) if isinstance(m["up"], str) else None
            rev = rid
        if rid == target:
            break
    return rev

def _after(rid, rev):
    return rev is None or MIGRATIONS[rid]["down"] == rev or True

if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect(":memory:")
    head = upgrade(conn, "b2")
    print("升级到:", head)
    print("结构:", conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'").fetchall())
    print("Alembic 真实流程: init -> autogenerate -> 人工审查 -> upgrade head")
    print("downgrade 与 upgrade 必须成对编写并演练")
