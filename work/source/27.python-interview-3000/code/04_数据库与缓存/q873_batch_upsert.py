"""sqlite3 演示批量 upsert: executemany + ON CONFLICT DO UPDATE"""
import sqlite3

UPSERT = """
INSERT INTO stock (sku, qty) VALUES (?, ?)
ON CONFLICT (sku) DO UPDATE SET qty = qty + excluded.qty
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE stock (sku TEXT PRIMARY KEY, qty INT)")
        batches = [
            [("A1", 10), ("A2", 5)],
            [("A1", 3), ("A3", 8)],   # A1 冲突, 应累加而非报错
        ]
        for batch in batches:
            with conn:
                conn.executemany(UPSERT, batch)

        for sku, qty in conn.execute("SELECT sku, qty FROM stock ORDER BY sku"):
            print(sku, qty)
