"""对账系统完整实现: 拉取 比对 分类修复 复核 报告 闭环"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE pay(order_no TEXT PRIMARY KEY, amount INTEGER, state TEXT);
INSERT INTO pay VALUES
 ('P1',100,'ok'),('P2',200,'ok'),('P3',50,'ok'),
 ('P4',300,'ok'),('P5',80,'ok'),('P6',20,'ok');
""")


def pull_remote():
    """拉取渠道账单: 现实里是分页拉文件或接口, 这里给固定样本"""
    return {"P1": 100, "P2": 199, "P4": 300, "P5": 80, "P6": 20, "P9": 66}


def compare(local, remote):
    d = {"amount_mismatch": [], "missing_local": [], "only_local": []}
    for no, amt in remote.items():
        mine = local.get(no)
        if mine is None:
            d["missing_local"].append((no, amt))          # 渠道有本地无: 漏单
        elif mine != amt:
            d["amount_mismatch"].append((no, mine, amt))  # 金额差错
    for no, amt in local.items():
        if no not in remote:
            d["only_local"].append((no, amt))             # 本地有渠道无: 挂人工
    return d


def repair(diffs):
    fixed = []
    for no, amt in diffs["missing_local"]:                # 漏单补录
        conn.execute("INSERT INTO pay VALUES(?,?,?)", (no, amt, "recovered"))
        fixed.append(("补录", no))
    for no, mine, theirs in diffs["amount_mismatch"]:     # 金额差错以渠道为准
        conn.execute("UPDATE pay SET amount=? WHERE order_no=?", (theirs, no))
        fixed.append(("补差", no))
    conn.commit()
    return fixed


local = {r[0]: r[1] for r in
         conn.execute("SELECT order_no, amount FROM pay WHERE state='ok'")}
diffs = compare(local, pull_remote())
print("比对结果:", diffs)
fixed = repair(diffs)
print("修复动作:", fixed)

print("---- 对账报告 ----")
total = conn.execute("SELECT COUNT(*) FROM pay").fetchone()[0]
print("本地笔数 %d | 金额差错 %d | 漏单 %d | 本地单出 %d | 已修复 %d"
      % (total, len(diffs["amount_mismatch"]), len(diffs["missing_local"]),
         len(diffs["only_local"]), len(fixed)))
print("人工待办:", diffs["only_local"])

# 复核: 修复后再比一轮, 可修复类必须清零
local2 = {r[0]: r[1] for r in conn.execute(
    "SELECT order_no, amount FROM pay WHERE state IN ('ok','recovered')")}
diffs2 = compare(local2, pull_remote())
assert not diffs2["amount_mismatch"] and not diffs2["missing_local"]
print("复核通过: 差错与漏单清零, 剩余差异仅剩人工项")
