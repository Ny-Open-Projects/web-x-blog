"""NULL 三值逻辑陷阱: NOT IN 遇上 NULL 与比较的第三种结果"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE vip(user_id INTEGER PRIMARY KEY);
CREATE TABLE logs(id INTEGER PRIMARY KEY, user_id INTEGER);
INSERT INTO vip VALUES(1), (2), (3);
INSERT INTO logs VALUES(1, 1), (2, 2), (3, NULL);
""")

def rows(sql):
    return [r[0] for r in conn.execute(sql)]

# 陷阱一: NOT IN 的子查询含 NULL 时, 整个外层查询返回空集
bad = rows("SELECT user_id FROM vip WHERE user_id NOT IN (SELECT user_id FROM logs)")
good = rows("SELECT user_id FROM vip v WHERE NOT EXISTS "
            "(SELECT 1 FROM logs l WHERE l.user_id = v.user_id)")
print("NOT IN 含 NULL 的子查询 ->", bad, "(全空: x 不等于 NULL 结果是 UNKNOWN, 整体永假)")
print("NOT EXISTS 同语义查询  ->", good)

# 陷阱二: WHERE col != 1 不会返回 NULL 行, NULL 参与任何比较都是 UNKNOWN
print("COUNT(*) =", rows("SELECT COUNT(*) FROM logs")[0],
      "  COUNT(user_id) =", rows("SELECT COUNT(user_id) FROM logs")[0])
print("user_id != 1 的行 ->", rows("SELECT id FROM logs WHERE user_id != 1"),
      "NULL 行被静默过滤")

# 陷阱三: NULL 与 NULL 不相等, 判等必须用 IS
print("NULL = NULL  ->", rows("SELECT NULL = NULL")[0], " (NULL)")
print("NULL IS NULL ->", rows("SELECT NULL IS NULL")[0], " (1)")
print("结论: 外层否定查询一律用 NOT EXISTS; 统计口径区分 COUNT(*) 与 COUNT(col); 判等用 IS")
