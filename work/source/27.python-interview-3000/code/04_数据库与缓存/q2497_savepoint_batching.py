"""批量导入的保存点分段: 一条脏数据不拖垮整批"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT UNIQUE)")

raw = [("%d@x.com" % i) for i in range(1, 31)]
raw[7] = "1@x.com"      # 与第 1 条撞唯一键
raw[22] = "2@x.com"     # 与第 2 条撞唯一键

CHUNK = 10
imported, bad = 0, []
for start in range(0, len(raw), CHUNK):
    chunk = raw[start:start + CHUNK]
    c.execute("SAVEPOINT sp")
    try:
        c.executemany("INSERT INTO users(email) VALUES(?)",
                      [(e,) for e in chunk])
        c.execute("RELEASE sp")
        imported += len(chunk)
    except sqlite3.IntegrityError:
        c.execute("ROLLBACK TO sp")                   # 整段退回, 但不放弃本段
        for e in chunk:                               # 段内逐条抢救
            try:
                c.execute("INSERT INTO users(email) VALUES(?)", (e,))
                imported += 1
            except sqlite3.IntegrityError as err:
                bad.append((e, str(err).split(":")[0]))
        c.execute("RELEASE sp")

total = c.execute("SELECT COUNT(*) FROM users").fetchone()[0]
print("导入 30 条, 其中 2 条撞唯一键")
print("保存点分段结果: 成功导入 %d 条, 跳过 %d 条 %s" % (imported, len(bad), bad))
print("库里实际行数: %d" % total)
assert total == imported

# 对照组: 不用保存点的整批导入, 一条脏数据全军覆没
try:
    c.execute("BEGIN")
    c.executemany("INSERT INTO users(email) VALUES(?)", [(e,) for e in raw])
except sqlite3.IntegrityError as e:
    print("整批提交对照: %s -> 已入库的整批被回滚, 只能从零再来" % e)
print("结论: 保存点把'整批原子'细化成'分段原子 + 段内自救',")
print("      脏数据的爆炸半径从整批缩小到一个 chunk")
