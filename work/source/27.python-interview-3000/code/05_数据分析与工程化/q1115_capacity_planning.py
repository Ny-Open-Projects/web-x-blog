
DAU = 1_000_000          # 假设 1:日活
REQ_PER_USER = 20        # 假设 2:人均请求数,来自埋点
PEAK_FACTOR = 5          # 假设 3:峰值系数,来自历史曲线
INSTANCE_QPS = 300       # 假设 4:单实例压测容量
REPLICA = 2              # 冗余:高可用最少两副本
PAYLOAD_KB = 2
LOG_KB_PER_REQ = 0.5

daily_req = DAU * REQ_PER_USER
peak_qps = daily_req * PEAK_FACTOR / 86400
instances = -(-int(peak_qps) // INSTANCE_QPS) * REPLICA   # 向上取整再乘冗余
bandwidth_gbps = peak_qps * PAYLOAD_KB * 8 / 1e6
log_gb = daily_req * LOG_KB_PER_REQ / 1e6

print(f"日请求 {daily_req:,}")
print(f"峰值 QPS {peak_qps:,.0f} -> 实例 {instances} 个")
print(f"入口带宽 {bandwidth_gbps:.2f} Gbps,日志 {log_gb:.1f} GB/日")
print("每条假设标注出处,输出 假设-推导-余量 三段式")
