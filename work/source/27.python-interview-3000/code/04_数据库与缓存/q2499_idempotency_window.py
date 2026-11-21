"""幂等记录的保留窗口: 防重放与表膨胀的平衡"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE idem (req_key TEXT PRIMARY KEY, result TEXT, created_at INTEGER)")
RETENTION = 100                                      # 幂等记录只保留 100 个时间单位

def process(key, now):
    row = c.execute("SELECT result, created_at FROM idem WHERE req_key=?", (key,)).fetchone()
    if row and now - row[1] <= RETENTION:
        return row[0], "命中幂等记录, 不重复执行"
    if row:                                          # 记录过期: 防重放保护失效!
        return do_work(key, now), "警告: 记录超窗, 请求被当作新请求重放执行"
    return do_work(key, now), "首次执行并登记"

def do_work(key, now):
    result = "result-of-%s@%d" % (key, now)
    c.execute("INSERT OR REPLACE INTO idem VALUES(?,?,?)", (key, result, now))
    return result

print("t=10   首次: %s -> %s" % process("pay:o1", 10))
print("t=50   重放: %s" % process("pay:o1", 50)[1])
print("t=200  窗口已过, 记录仍在: %s" % process("pay:o1", 200)[1])

# 治理侧: 到期记录分批清理, 窗口外请求按新请求处理 (重放风险由业务层承担)
c.execute("DELETE FROM idem WHERE created_at < ?", (300 - RETENTION,))
print("t=300  清理 created_at < 200 的幂等记录, 剩余 %d 行"
      % c.execute("SELECT COUNT(*) FROM idem").fetchone()[0])

# 表膨胀侧: 高峰期每秒 5000 个请求, 保留 24 小时 = 4.3 亿行
qps, hours = 5000, 24
print("若 qps=%d 保留 %d 小时: 幂等表约 %.1f 亿行" % (qps, hours, qps * 3600 * hours / 1e8))
print("结论: 保留窗口 = 防重放的有效时长, 太短挡不住重放 太长表与索引膨胀;")
print("      按业务的重放风险期定窗口 (支付类对齐对账周期), 清理必须走分批删除")
