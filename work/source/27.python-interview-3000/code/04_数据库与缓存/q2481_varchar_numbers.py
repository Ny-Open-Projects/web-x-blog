"""varchar 存数字: 排序与范围的双陷阱"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE bad (code TEXT NOT NULL)")        # 编号被建成 TEXT
c.executemany("INSERT INTO bad VALUES(?)", [('2',), ('9',), ('10',), ('100',)])

# 陷阱一: 字典序不是数值序, '10' < '2'
got = [r[0] for r in c.execute("SELECT code FROM bad ORDER BY code")]
print("TEXT 排序: %s   <- '10' 排在 '2' 前面" % got)
good = [r[0] for r in c.execute("SELECT code FROM bad ORDER BY CAST(code AS INTEGER)")]
print("CAST 修复: %s   <- 但 CAST 让索引失效, 每行都要转换" % good)

# 陷阱二: 范围条件按字符串比较, 边界错得离谱
in_range = [r[0] for r in c.execute("SELECT code FROM bad WHERE code BETWEEN '3' AND '50'")]
print("TEXT 范围 [3,50]: %s   <- 字典序下 '10' 在界外, '100' 也不在, 全错" % in_range)
in_range2 = [r[0] for r in c.execute(
    "SELECT code FROM bad WHERE CAST(code AS INTEGER) BETWEEN 3 AND 50")]
print("CAST 范围 [3,50]: %s   <- 结果对了, 但全表扫描" % in_range2)

# 正解: 从类型上就别让数字住进字符串, 已有表用表达式索引救急
c.execute("CREATE TABLE good (code INTEGER NOT NULL)")
c.executemany("INSERT INTO good VALUES(?)", [(2,), (9,), (10,), (100,)])
print("INTEGER 列排序:", [r[0] for r in c.execute("SELECT code FROM good ORDER BY code")])
c.execute("CREATE TABLE legacy (code TEXT)")
c.executemany("INSERT INTO legacy VALUES(?)", [('2',), ('9',), ('10',), ('100',)])
c.execute("CREATE INDEX idx_code_num ON legacy(CAST(code AS INTEGER))")
plan = " | ".join(r[3] for r in c.execute(
    "EXPLAIN QUERY PLAN SELECT * FROM legacy WHERE CAST(code AS INTEGER) = 10"))
print("表达式索引兜底的计划: %s" % plan)
print("结论: 排序错与范围错同源——字典序; 修复靠类型, 兜底靠表达式索引, 别靠 CAST 硬扛")
