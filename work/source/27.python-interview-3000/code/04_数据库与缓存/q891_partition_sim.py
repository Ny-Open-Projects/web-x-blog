"""应用层按月分表模拟分区裁剪与 DROP PARTITION 式过期清理"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        for m in ("202401", "202402", "202403"):
            conn.execute(f"""CREATE TABLE log_{m}
                             (id INTEGER PRIMARY KEY, msg TEXT)""")
            conn.executemany(f"INSERT INTO log_{m} (msg) VALUES (?)",
                             [(f"log-{m}-{i}",) for i in range(3)])

        def query_partition(month):
            # 分区裁剪: 只打开目标分表
            return conn.execute(f"SELECT * FROM log_{month}").fetchall()

        print("查 202402:", query_partition("202402"))

        # 等价于 MySQL 的 DROP PARTITION: 直接删表, 秒级且不产生大事务
        conn.execute("DROP TABLE log_202401")
        tables = [r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
        print("清理后剩余分表:", tables)
