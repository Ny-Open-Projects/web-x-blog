"""连接的归因审计: 借还事件按客户端标签聚合, 找出占坑大户"""
clients = [
    ("api-web",       3000, 0.08),    # (客户端标签, 借出次数, 平均持有秒)
    ("report-job",      60, 15.0),
    ("admin-console",  100, 0.60),
]
POOL_SIZE, WINDOW_S = 20, 60.0
capacity = POOL_SIZE * WINDOW_S
print("池容量 %d 连接 x %.0fs = %.0f 连接秒" % (POOL_SIZE, WINDOW_S, capacity))

usage = []
total_used = 0.0
for name, borrows, hold in clients:
    used = borrows * hold
    usage.append((name, used))
    total_used += used
for name, used in sorted(usage, key=lambda u: -u[1]):
    share = used / capacity * 100
    flag = "  <-- 占坑大户" if share > 50 else ""
    print("%-14s 用掉 %6.0f 连接秒, 占池容量 %5.1f%%%s" % (name, used, share, flag))
print("池整体利用率 %.0f%%; 没有客户端标签就没有归因, unknown 占比必须告警"
      % (total_used / capacity * 100))
