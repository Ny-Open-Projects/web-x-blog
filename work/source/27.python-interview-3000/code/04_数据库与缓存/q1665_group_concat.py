"""字符串聚合: group_concat 的分隔符 顺序 与 去重三件套"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE emp(dept TEXT, name TEXT, age INTEGER);
INSERT INTO emp VALUES
 ('dev',  'zhang', 30), ('dev',  'wang',  28), ('dev',  'li',    28),
 ('ops',  'zhao',  35), ('ops',  'qian',  31), ('test', 'sun',   26);
""")

# 默认分隔符是逗号, 且元素顺序不保证 -- 文档明确说 arbitrary
print("默认:", conn.execute(
    "SELECT dept, group_concat(name) FROM emp GROUP BY dept ORDER BY dept").fetchall())

# 第二个参数指定分隔符
print("分号:", conn.execute(
    "SELECT dept, group_concat(name, '; ') FROM emp GROUP BY dept ORDER BY dept").fetchall())

# 想要有序拼接: 在子查询里先排序, 再交给聚合(实现上按子查询序, 语义上无保证)
sql = """
SELECT dept, group_concat(name, ' / ') FROM (
  SELECT dept, name FROM emp ORDER BY dept, name
) GROUP BY dept ORDER BY dept
"""
print("有序:", conn.execute(sql).fetchall())

# 想要去重: DISTINCT 只能与单参数形式连用, 带分隔符的先在子查询去重
print("DISTINCT 年龄:", conn.execute("SELECT group_concat(DISTINCT age) FROM emp").fetchone()[0])
sql2 = """
SELECT group_concat(age, ',') FROM (SELECT DISTINCT age FROM emp ORDER BY age)
"""
print("去重加分隔:", conn.execute(sql2).fetchone()[0])
print("要点: MySQL 的同名函数受 group_concat_max_len 默认 1024 截断; SQLite 无此参数;")
print("      超长或顺序敏感的拼接建议放应用层, SQL 里的拼接适合调试与轻量报表")
