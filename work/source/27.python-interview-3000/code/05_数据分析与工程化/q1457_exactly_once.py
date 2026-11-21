"""at-least-once 到 exactly-once:去重表与数据写入同一事务"""

import sqlite3

DDL = """
CREATE TABLE ingest_rows (
    row_id TEXT PRIMARY KEY,
    batch_id TEXT NOT NULL,
    payload TEXT NOT NULL
);
CREATE TABLE seen_batches (
    batch_id TEXT PRIMARY KEY
);
"""


def consume_batch(conn, batch_id, rows):
    """整批写入与'批次登记'放在同一事务:任何一步失败整体回滚"""
    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    try:
        cur.execute("INSERT INTO seen_batches (batch_id) VALUES (?)", (batch_id,))
        cur.executemany(
            "INSERT INTO ingest_rows (row_id, batch_id, payload) VALUES (?, ?, ?)",
            [(r[0], batch_id, r[1]) for r in rows])
        conn.commit()
        return "committed"
    except sqlite3.IntegrityError:
        conn.rollback()
        return "duplicate batch skipped"


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.executescript(DDL)
    batch = [("r1", "order o1"), ("r2", "order o2")]

    print("第一次消费 batch-1:", consume_batch(conn, "batch-1", batch))
    # at-least-once 语义下,生产端一定会重放
    print("重放 batch-1   :", consume_batch(conn, "batch-1", batch))
    print("消费 batch-2   :", consume_batch(conn, "batch-2", [("r3", "order o3")]))

    n = conn.execute("SELECT COUNT(*) FROM ingest_rows").fetchone()[0]
    b = conn.execute("SELECT COUNT(*) FROM seen_batches").fetchone()[0]
    print(f"最终行数 {n}(期望 3),已登记批次 {b}(期望 2)")
    print("要点:去重登记与业务写入必须同事务,分开写就退化成 at-least-once")
