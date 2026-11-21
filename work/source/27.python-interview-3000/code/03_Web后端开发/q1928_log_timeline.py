"""跨组件日志关联: 按 trace id 还原请求时间线(纯标准库)。"""
from datetime import datetime

# 三个组件的日志流, 时间戳统一 UTC
LOGS = [
    ("gateway", "2026-11-05T03:14:15.100Z", "req-42", "POST /checkout 202"),
    ("order-api", "2026-11-05T03:14:15.180Z", "req-42", "auth ok user=u1"),
    ("order-api", "2026-11-05T03:14:15.240Z", "req-42", "create order o-9"),
    ("inventory", "2026-11-05T03:14:15.260Z", "req-42", "reserve sku=99 x2"),
    ("payment", "2026-11-05T03:14:16.950Z", "req-42", "charge 120.00 ok"),
    ("order-api", "2026-11-05T03:14:17.010Z", "req-42", "order o-9 confirmed"),
    ("gateway", "2026-11-05T03:14:17.050Z", "req-42", "respond 200 1946ms"),
    ("gateway", "2026-11-05T03:14:15.300Z", "req-43", "GET /items 200"),
]


def fmt_ts(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ").timestamp()


def build_timeline(logs, trace_id):
    """抽同一 trace id 的事件按时间排序, 输出相对偏移与段间隔。"""
    events = [(fmt_ts(ts), comp, msg)
              for comp, ts, tid, msg in logs if tid == trace_id]
    events.sort()
    t0 = events[0][0]
    lines, prev = [], None
    for ts, comp, msg in events:
        gap = "" if prev is None else "  (delta {:+.0f}ms)".format((ts - prev) * 1000)
        lines.append("{:+7.0f}ms {:<10s} {}{}".format((ts - t0) * 1000, comp, msg, gap))
        prev = ts
    return lines, (events[-1][0] - events[0][0]) * 1000


lines, total = build_timeline(LOGS, "req-42")
print("trace req-42 的时间线(总时长 %.0fms):" % total)
for line in lines:
    print(" ", line)

# 段间隔分析: 找出慢在哪个组件之间
gaps = []
prev = None
for comp, ts, tid, msg in LOGS:
    if tid != "req-42":
        continue
    if prev is not None:
        gaps.append(((fmt_ts(ts) - fmt_ts(prev[1])) * 1000, prev[0], comp))
    prev = (comp, ts)
worst = max(gaps)
print("最大间隔: {} -> {} 差 {:.0f}ms".format(worst[1], worst[2], worst[0]))
assert worst[1] == "inventory" and worst[2] == "payment" and worst[0] > 1000

missing = [tid for tid in ("req-42", "req-44") if not any(l[2] == tid for l in LOGS)]
print("无法关联的请求:", missing, "(需要提示: 中间组件可能没透传 id)")
print("要点: 时间线还原靠统一时钟与 trace id 全链路透传, 最大间隔一眼定位瓶颈段")
