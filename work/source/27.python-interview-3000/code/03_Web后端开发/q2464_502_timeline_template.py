"""502 的因果链复盘模板: 时间线重建与报告生成(纯标准库)。"""

TEMPLATE = [
    ("现象", None),
    ("直接原因", None),
    ("根因", None),
    ("修复动作", None),
    ("验证方法", None),
]


def rebuild_timeline(events):
    """events: (时刻秒, 层, 事件)。排序后相邻层构成因果链的骨架。"""
    return sorted(events, key=lambda e: e[0])


def causal_chain(events):
    """按 请求路径 的层顺序串出因果链: client -> gateway -> upstream -> 回程。"""
    order = ["client", "gateway", "upstream"]
    chain = []
    for _, layer, text in rebuild_timeline(events):
        if layer not in order:
            order.append(layer)
        chain.append("[{}] {}".format(layer, text))
    return chain


def render_report(incident_id, events, findings):
    lines = ["== 复盘报告 {} ==".format(incident_id)]
    lines.append("时间线:")
    base = events[0][0]
    for ts, layer, text in rebuild_timeline(events):
        lines.append("  +{:6.2f}s [{:8s}] {}".format(ts - base, layer, text))
    lines.append("因果链: " + " -> ".join(causal_chain(events)))
    for key, value in findings:
        lines.append("{}: {}".format(key, value))
    return "\n".join(lines)


events = [
    (0.00, "client", "客户端发起 POST /checkout"),
    (0.02, "gateway", "网关收到请求, 转发到 upstream:8000"),
    (0.03, "upstream", "上游 worker 池已满, 请求进入积压队列"),
    (14.98, "upstream", "队列超时, 请求未被处理即丢弃"),
    (15.00, "gateway", "网关读上游响应超时, 判定 upstream 无效"),
    (15.01, "gateway", "网关生成 502 返回客户端"),
    (15.02, "client", "客户端收到 502"),
]

findings = [
    ("直接原因", "网关等不到上游响应, 502 由网关侧产生"),
    ("根因", "上游慢查询拖住全部 worker, 池满后新请求排队超时"),
    ("修复动作", "给上游调用加 3 秒超时与连接池上限, 慢查询加索引"),
    ("验证方法", "压测注入 5 秒慢请求, 断言 502 率为零且网关 3 秒熔断"),
    ("现象", "峰值时段 /checkout 大面积 502, 持续 4 分钟"),
]

print(render_report("INC-1105-01", events, findings))
chain = causal_chain(events)
assert len(chain) == 7
assert chain[0].startswith("[client]") and chain[-1].startswith("[client]")
report = render_report("INC-1105-01", events, findings)
for key, _ in TEMPLATE:
    assert any(line.startswith(key) for line in report.splitlines()), key
print("要点: 复盘模板的骨架是 时间线 因果链 五要素, "
      "时间线用相对秒对齐各层日志, 因果链按 client gateway upstream 的路径回放")
