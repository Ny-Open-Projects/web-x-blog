"""GROUP BY 与 DISTINCT 的隐式排序神话: 输出顺序是计划的副产品"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, cat TEXT)")
c.executemany("INSERT INTO t VALUES(?,?)",
              [(i, "cat%d" % (i % 7)) for i in range(1, 20001)])

# 场景一: ASC 索引在手, 优化器走索引扫描, 输出'恰好'有序
c.execute("CREATE INDEX idx_cat_asc ON t(cat)")
plan = [r[3] for r in c.execute("EXPLAIN QUERY PLAN SELECT DISTINCT cat FROM t")]
out = [r[0] for r in c.execute("SELECT DISTINCT cat FROM t")]
print("ASC 索引: %s" % out)
print("  计划: %s" % plan[0])

# 场景二: 同一条查询, 重建一个 DESC 索引, 输出顺序整个翻转
c.execute("DROP INDEX idx_cat_asc")
c.execute("CREATE INDEX idx_cat_desc ON t(cat DESC)")
plan = [r[3] for r in c.execute("EXPLAIN QUERY PLAN SELECT DISTINCT cat FROM t")]
out = [r[0] for r in c.execute("SELECT DISTINCT cat FROM t")]
print("DESC 索引: %s" % out)
print("  计划: %s" % plan[0])
plan = [r[3] for r in c.execute("EXPLAIN QUERY PLAN SELECT cat, COUNT(*) FROM t GROUP BY cat")]
out = [r[0] for r in c.execute("SELECT cat, COUNT(*) FROM t GROUP BY cat")]
print("GROUP BY 同样跟着索引方向走: %s" % out)

# 没有任何契约说它必须有序; 今天靠计划白捡的顺序, 明天一次 ANALYZE 就能收走
c.execute("DROP INDEX idx_cat_desc")
plan = [r[3] for r in c.execute("EXPLAIN QUERY PLAN SELECT DISTINCT cat FROM t")]
out = [r[0] for r in c.execute("SELECT DISTINCT cat FROM t")]
print("无索引回退临时结构: %s | 计划: %s" % (out, plan[0]))
print("结论: 输出顺序取决于优化器选了哪条路, 面向人或喂给 INSERT SELECT 的结果必须显式 ORDER BY")
