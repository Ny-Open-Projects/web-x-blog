"""三种批量更新路径的耗时对比"""
import sqlite3
import time

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE goods (id INTEGER PRIMARY KEY, price REAL)")
    N = 5000
    conn.executemany("INSERT INTO goods (price) VALUES (?)",
                     [(i * 1.0,) for i in range(N)])

    def bench(label, fn):
        t0 = time.perf_counter()
        fn()
        print(f"{label}: {(time.perf_counter() - t0) * 1000:.0f} ms")

    def per_row():
        c = sqlite3.connect(":memory:")
        c.execute("CREATE TABLE goods (id INTEGER PRIMARY KEY, price REAL)")
        c.executemany("INSERT INTO goods (price) VALUES (?)",
                      [(i * 1.0,) for i in range(N)])
        for i in range(1, N + 1):
            c.execute("UPDATE goods SET price = price * 2 WHERE id = ?", (i,))
        c.commit()

    def executemany_style():
        data = [(i * 3.0, i) for i in range(1, N + 1)]
        conn.executemany("UPDATE goods SET price = ? WHERE id = ?", data)
        conn.commit()

    def case_when():
        ids = list(range(1, 101))               # 小批量示例
        whens = " ".join(f"WHEN {i} THEN {i * 9.0}" for i in ids)
        conn.execute(f"UPDATE goods SET price = CASE id {whens} END "
                     f"WHERE id IN ({','.join(map(str, ids))})")
        conn.commit()

    bench("逐条 UPDATE 含建库", per_row)
    bench("executemany 5000 行", executemany_style)
    bench("CASE WHEN 100 行", case_when)
