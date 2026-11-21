"""对账差异修复闭环: 比对 分类 修复 复核 直到零差异"""
import sqlite3

src = sqlite3.connect(":memory:")
dst = sqlite3.connect(":memory:")
for db in (src, dst):
    db.execute("CREATE TABLE acct(id INTEGER PRIMARY KEY, balance INTEGER)")
src.executemany("INSERT INTO acct VALUES(?,?)", [(1, 100), (2, 200), (3, 300), (4, 400)])
# 目标库故意漂移: 2 少记 5, 3 余额错, 9 是多出来的, 4 缺失
dst.executemany("INSERT INTO acct VALUES(?,?)", [(1, 100), (2, 195), (3, 999), (9, 777)])

def diff_once():
    s = dict(src.execute("SELECT id, balance FROM acct"))
    d = dict(dst.execute("SELECT id, balance FROM acct"))
    out = []
    for k in sorted(set(s) | set(d)):
        if k not in d:
            out.append(("missing", k, s[k]))
        elif k not in s:
            out.append(("extra", k, d[k]))
        elif s[k] != d[k]:
            out.append(("mismatch", k, s[k], d[k]))
    return out

def repair(item):
    """修复动作全部用 upsert 或 delete 表达, 天然幂等可重跑"""
    kind = item[0]
    if kind == "missing" or kind == "mismatch":
        dst.execute("INSERT OR REPLACE INTO acct VALUES(?,?)", (item[1], item[2]))
    elif kind == "extra":
        dst.execute("DELETE FROM acct WHERE id=?", (item[1],))

for round_no in range(1, 4):
    diffs = diff_once()
    print(f"第 {round_no} 轮差异 {len(diffs)} 条:", diffs)
    if not diffs:
        print("闭环完成: 零差异")
        break
    for item in diffs:
        repair(item)
    dst.commit()

print("最终复核零差异:", diff_once() == [])
print("要点: 修复以源为准; 每个动作幂等可重跑; 循环上限防死循环; 差异明细要落表留痕供审计")
