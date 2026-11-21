"""演示 emoji 存储与内置 collation 对排序比较的影响"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (name TEXT)")
        conn.executemany("INSERT INTO t VALUES (?)",
                         [("apple",), ("Banana",), ("apple",), ("über",)])
        # 默认 BINARY: 大小写敏感
        print("BINARY 排序:", [r[0] for r in conn.execute("SELECT name FROM t ORDER BY name")])
        # NOCASE collation: 大小写不敏感比较
        print("NOCASE 排序:", [r[0] for r in conn.execute(
            "SELECT name FROM t ORDER BY name COLLATE NOCASE")])
        print("emoji 存储:", conn.execute(
            "SELECT length(?)", ("ok😀",)).fetchone()[0], "个字符(UTF-8 正常)")
        print("MySQL 对照: utf8 存 emoji 报错, 应统一 utf8mb4 + 0900_ai_ci")
