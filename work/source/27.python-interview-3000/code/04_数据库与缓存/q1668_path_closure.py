"""层级查询实现二: 路径枚举与闭包表, 读多写少的两种物化方案"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE node(id INTEGER PRIMARY KEY, name TEXT, parent_id INTEGER, path TEXT);
CREATE TABLE closure(ancestor INTEGER, descendant INTEGER, depth INTEGER,
  PRIMARY KEY(ancestor, descendant));
INSERT INTO node VALUES
 (1, 'root', NULL, '1'),
 (2, 'a',    1,    '1/2'),
 (3, 'b',    1,    '1/3'),
 (4, 'a1',   2,    '1/2/4'),
 (5, 'b1',   3,    '1/3/5');
""")
# 闭包表: 预先展开全部祖先-后代对, 之后子树与祖先查询都是等值 JOIN
nodes = conn.execute("SELECT id, parent_id FROM node").fetchall()
by_id = dict(nodes)
pairs = []
for nid, _ in nodes:
    d, cur = 0, nid
    while cur is not None:
        pairs.append((cur, nid, d))
        d += 1
        cur = by_id.get(cur)
conn.executemany("INSERT OR REPLACE INTO closure VALUES(?,?,?)", pairs)
conn.commit()

print("闭包表查 1 的整棵子树:")
for r in conn.execute("""
  SELECT n.id, n.name, c.depth FROM closure c
  JOIN node n ON n.id = c.descendant
  WHERE c.ancestor = 1 ORDER BY c.depth"""):
    print("  ", r)

print("路径枚举查 1 的整棵子树:")
for r in conn.execute("SELECT id, name, path FROM node WHERE id = 1 OR path LIKE '1/%'"):
    print("  ", r)

print("闭包表反查 5 的全部祖先:")
for r in conn.execute("""
  SELECT n.id, n.name, c.depth FROM closure c
  JOIN node n ON n.id = c.ancestor
  WHERE c.descendant = 5 ORDER BY c.depth"""):
    print("  ", r)

print("对比: 闭包表读快但空间 O(n*深度) 且写重; 路径枚举存储小, 子树靠 LIKE 前缀;")
print("      LIKE 走不了理想索引, 且节点改名要重写整棵子树的路径, 移动子树两者都贵")
