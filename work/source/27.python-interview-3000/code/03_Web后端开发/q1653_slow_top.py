"""慢接口 top 统计: 聚合访问日志找 P95 最差的路由(纯标准库)。"""
import statistics

LOG = [
    "GET /v1/orders 412 200", "GET /v1/orders 388 200", "GET /v1/orders 980 200",
    "GET /v1/orders 1030 200", "GET /v1/orders 455 200", "GET /v1/orders 301 200",
    "GET /v1/orders 150 200", "GET /v1/orders 220 200",
    "POST /v1/pay 2100 200", "POST /v1/pay 2600 500", "POST /v1/pay 1900 200",
    "GET /v1/health 3 200", "GET /v1/health 2 200", "GET /v1/health 4 200",
]


def parse(lines):
    rows = []
    for line in lines:
        method, route, dur, status = line.split()
        rows.append({"route": f"{method} {route}", "ms": int(dur), "status": int(status)})
    return rows


def top_slow(rows, n=3):
    by = {}
    for r in rows:
        by.setdefault(r["route"], []).append(r)
    stats = []
    for route, items in by.items():
        ms = sorted(i["ms"] for i in items)
        p95 = ms[min(int(len(ms) * 0.95), len(ms) - 1)]
        err = sum(1 for i in items if i["status"] >= 500) / len(items)
        stats.append({"route": route, "p95_ms": p95, "avg_ms": int(statistics.mean(ms)),
                      "n": len(items), "err": err})
    return sorted(stats, key=lambda s: s["p95_ms"], reverse=True)[:n]


for s in top_slow(parse(LOG)):
    print(f'{s["route"]:16} p95={s["p95_ms"]}ms avg={s["avg_ms"]}ms '
          f'n={s["n"]} err={s["err"]:.0%}')
print("要点: 用 P95 而不是平均值排序, 长尾才是用户体感; err 列帮助区分慢和坏")
