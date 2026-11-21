"""演示唯一约束兜底重复写入, 说明唯一索引的业务价值"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE signup (id INTEGER PRIMARY KEY, phone TEXT)")
        conn.execute("CREATE UNIQUE INDEX idx_phone ON signup (phone)")

        def signup(phone):
            try:
                conn.execute("INSERT INTO signup (phone) VALUES (?)", (phone,))
                conn.commit()
                return "ok"
            except sqlite3.IntegrityError:
                return "duplicate"

        print(signup("13800000001"))
        print(signup("13800000001"))   # 并发双击提交, 数据库层兜底
        print("说明: 应用层判重有竞态, 唯一索引是最终防线, 代价是失去 change buffer 加速")
