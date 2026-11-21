"""索引使用率监控: 计数器模型与候选删除流程"""
idx_scan = {
    "idx_orders_user_status": 0,
    "idx_orders_status": 0,
    "idx_orders_created": 0,
    "idx_orders_amount": 0,
    "idx_orders_city": 0,
}
queries = [
    ("WHERE user_id=? AND status=?", ["idx_orders_user_status"]),
    ("WHERE user_id=? AND status=?", ["idx_orders_user_status"]),
    ("WHERE status=?", ["idx_orders_status"]),
    ("WHERE created>=?", ["idx_orders_created"]),
    ("WHERE user_id=? AND status=?", ["idx_orders_user_status"]),
]
for sql, used in queries:
    for name in used:
        idx_scan[name] += 1

for name, n in sorted(idx_scan.items(), key=lambda x: x[1]):
    tag = "  <- 观察期内零使用" if n == 0 else ""
    print(f"{name}: idx_scan={n}{tag}")
print("处置: 零使用索引先改 INVISIBLE 观察 2-4 周, 仍无流量再 DROP")
print("注意: 唯一约束与外键仍可能需要它们, 删除前核对依赖")
