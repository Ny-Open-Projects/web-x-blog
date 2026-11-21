"""综合演练:慢接口事故的定位与处置建议(纯标准库)。"""
import statistics

REQUESTS = [
    {"route": "/orders", "status": 200, "db": 0.9, "call": 0.1, "render": 0.05},
    {"route": "/orders", "status": 200, "db": 1.2, "call": 0.1, "render": 0.04},
    {"route": "/orders", "status": 200, "db": 2.5, "call": 0.2, "render": 0.05},
    {"route": "/orders", "status": 500, "db": 3.0, "call": 0.1, "render": 0.0},
    {"route": "/health", "status": 200, "db": 0.01, "call": 0.0, "render": 0.01},
]


def summarize(reqs):
    by_route = {}
    for r in reqs:
        by_route.setdefault(r["route"], []).append(r)
    report = {}
    for route, rows in by_route.items():
        totals = sorted(r["db"] + r["call"] + r["render"] for r in rows)
        p95 = totals[min(int(len(totals) * 0.95), len(totals) - 1)]
        err = sum(1 for r in rows if r["status"] >= 500) / len(rows)
        avg_stage = {s: statistics.mean(r[s] for r in rows) for s in ("db", "call", "render")}
        slowest = max(avg_stage, key=avg_stage.get)
        action = "回滚最近发布或治理慢查询" if (p95 > 1.0 or err > 0) else "观察"
        report[route] = {"p95_s": round(p95, 2), "error_rate": err,
                         "slowest_stage": slowest, "action": action}
    return report


for route, info in summarize(REQUESTS).items():
    print(route, info)
print("闭环:错误日志已全采 -> 指纹聚合 -> 定位 db 阶段 -> 可逆处置 -> 复盘进矩阵")
