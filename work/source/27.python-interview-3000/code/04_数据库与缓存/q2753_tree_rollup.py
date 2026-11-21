"""树的自底向上聚合: 每行自为根的递归, 一趟算出每个节点的子树总额"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE cat (id INTEGER PRIMARY KEY, parent INTEGER, amt REAL)")
# 1 总类目 <- 2 数码 <- 4 手机 5 电脑;  1 <- 3 服装 <- 6 上衣
c.executemany("INSERT INTO cat VALUES(?,?,?)",
              [(1, None, 0), (2, 1, 0), (3, 1, 0),
               (4, 2, 30), (5, 2, 50), (6, 3, 20)])

sql = """
WITH RECURSIVE down AS (
  SELECT id, id AS root, amt FROM cat
  UNION ALL
  SELECT c.id, d.root, c.amt FROM cat c JOIN down d ON c.parent = d.id
)
SELECT root, COUNT(*) AS nodes, SUM(amt) AS subtree_amt
FROM down GROUP BY root ORDER BY root
"""
for root, nodes, total in c.execute(sql):
    print("节点 %d: 子树 %d 个节点, 子树金额 %.0f" % (root, nodes, total))

expect = {1: 100, 2: 80, 3: 20, 4: 30, 5: 50, 6: 20}
for root, _, total in c.execute(sql):
    assert int(total) == expect[root], "子树聚合结果必须与手算一致"
print("子树总额与手算完全一致, 一次递归替代逐层回填")
