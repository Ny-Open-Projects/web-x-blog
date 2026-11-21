"""批量 upsert 冲突分支: DO NOTHING 与 DO UPDATE 的拆分与条件"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE sku_price(sku TEXT PRIMARY KEY, price REAL, source TEXT)")
conn.executemany("INSERT INTO sku_price VALUES(?,?,?)",
                 [("A", 10.0, "erp"), ("B", 20.0, "erp"), ("C", 30.0, "erp")])
conn.commit()

feed = [("A", 11.0, "feed"), ("B", 19.0, "feed"), ("D", 5.0, "feed")]
conn.execute("CREATE TEMP TABLE feed(sku TEXT PRIMARY KEY, price REAL, source TEXT)")
conn.executemany("INSERT INTO feed VALUES(?,?,?)", feed)

# 分支一: 只新增不覆盖 -> DO NOTHING
n_ins = conn.execute("""
  INSERT INTO sku_price(sku, price, source)
  SELECT sku, price, source FROM feed WHERE true
  ON CONFLICT(sku) DO NOTHING""").rowcount
print("DO NOTHING 实际插入:", n_ins, "行 (只有 D; 注意 INSERT 源是 SELECT 时必须写 WHERE true)")

# 分支二: 只覆盖降价 -> DO UPDATE 带条件
n_upd = conn.execute("""
  INSERT INTO sku_price(sku, price, source)
  SELECT sku, price, source FROM feed WHERE true
  ON CONFLICT(sku) DO UPDATE SET price = excluded.price, source = excluded.source
  WHERE excluded.price < sku_price.price""").rowcount
print("条件 DO UPDATE 生效:", n_upd, "行 (B 降价被更新, A 涨价被 WHERE 挡住)")
print("最终:", conn.execute("SELECT * FROM sku_price ORDER BY sku").fetchall())
print("要点: 一条 INSERT 只能挂一个冲突动作, 新增与更新分支要拆成两条语句;")
print("      rowcount 只统计实际变更行, 幂等重跑时天然为 0")
