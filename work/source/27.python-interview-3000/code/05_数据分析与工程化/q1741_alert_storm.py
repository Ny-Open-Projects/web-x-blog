"""告警风暴聚合:同指纹窗口内折叠计数,恢复发一条汇总,避免刷屏"""

RAW_ALERTS = [
    # 时间偏移秒, 服务, 告警名, 状态
    (0, "api", "HighLatency", "firing"),
    (5, "api", "HighLatency", "firing"),
    (9, "api", "HighLatency", "firing"),
    (12, "db", "ConnPoolFull", "firing"),
    (20, "api", "HighLatency", "resolved"),
    (25, "api", "HighLatency", "firing"),
    (40, "db", "ConnPoolFull", "resolved"),
]


def aggregate(alerts):
    """按 (服务, 告警名) 指纹聚合:firing 折叠计数,首条发出,恢复发汇总"""
    groups, out = {}, []
    for t, svc, name, state in alerts:
        key = (svc, name)
        g = groups.setdefault(key, {"firing": 0, "open": False})
        if state == "firing":
            g["firing"] += 1
            if not g["open"]:
                g["open"] = True
                out.append((t, key, "首条告警"))
        elif g["open"]:
            g["open"] = False
            out.append((t, key, f"恢复:共触发 {g['firing']} 次,折叠为 1 条通知"))
            g["firing"] = 0
    return out


if __name__ == "__main__":
    for t, key, msg in aggregate(RAW_ALERTS):
        print(f"[t+{t:>2}s] {key[0]}/{key[1]}: {msg}")
    print("要点:聚合键=指纹(服务+告警名+维度值),窗口内折叠计数只发首条;再叠加静默期与分级,风暴时低级别告警只进看板不进 IM")
