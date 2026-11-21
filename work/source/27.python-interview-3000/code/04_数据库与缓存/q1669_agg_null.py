"""聚合与 NULL: COUNT 三种口径 与 AVG/SUM 的隐性偏差"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE score(student TEXT, subject TEXT, val REAL)")
conn.executemany("INSERT INTO score VALUES(?,?,?)",
                 [("a", "math", 80), ("a", "eng", None), ("a", "phys", 90),
                  ("b", "math", None), ("b", "eng", None), ("b", "phys", None),
                  ("c", "math", 70), ("c", "eng", 60), ("c", "phys", 50)])
conn.commit()

def one(sql):
    return conn.execute(sql).fetchone()[0]

print("COUNT(*) =", one("SELECT COUNT(*) FROM score"), "     数行, 含 NULL")
print("COUNT(val) =", one("SELECT COUNT(val) FROM score"), "    只数非 NULL")
print("COUNT(DISTINCT val) =", one("SELECT COUNT(DISTINCT val) FROM score"))

# AVG 只对非 NULL 求均值: a 是 80 与 90 两门 -> 85, 不是 (80+90)/3 也不是 170/3 的误解
for stu in ("a", "b", "c"):
    avg = one("SELECT AVG(val) FROM score WHERE student='" + stu + "'")
    print(f"{stu}: AVG={avg}  (b 全 NULL -> AVG 是 NULL 而不是 0)")

print("空集 SUM:", one("SELECT SUM(val) FROM score WHERE student='zz'"),
      "-> 是 NULL 不是 0, 报表必须 COALESCE")
print("COALESCE 修正:", one("SELECT COALESCE(SUM(val), 0) FROM score WHERE student='zz'"))
print("结论: 每个统计先明确口径, 是数行还是数值, 空集想显示 0 还是不显示, 再写 SQL")
