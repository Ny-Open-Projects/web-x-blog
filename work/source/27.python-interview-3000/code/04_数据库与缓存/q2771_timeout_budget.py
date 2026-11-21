"""读路径的超时预算: 每层配额独立, 谁超配额就跳过谁"""
BUDGET_MS = 200.0

def read_path(layers):
    """layers: [(层名, 配额ms, 是否命中, 实际ms)]; 剩余预算逐层递减"""
    remaining = BUDGET_MS
    trail = []
    for name, quota, hit, actual in layers:
        cost = min(actual, quota)
        remaining -= cost
        if hit and actual <= quota:
            trail.append("%s 命中 耗 %.0fms" % (name, actual))
            return trail, "于 %s 返回, 剩余预算 %.0fms" % (name, remaining)
        trail.append("%s 未命中或超时 耗 %.0fms" % (name, cost))
        if remaining <= 0:
            return trail, "预算耗尽"
    return trail, "全部 miss, 降级返回默认值"

scenarios = [
    ("全链路健康", [("L1", 1, False, 0.2), ("L2", 20, True, 8.0), ("DB", 150, True, 40.0)]),
    ("L2 卡死",    [("L1", 1, False, 0.2), ("L2", 20, False, 5000.0), ("DB", 150, True, 40.0)]),
    ("DB 也慢",    [("L1", 1, False, 0.2), ("L2", 20, False, 5000.0), ("DB", 150, False, 400.0)]),
]
for label, layers in scenarios:
    trail, verdict = read_path(layers)
    print("%s: %s -> %s" % (label, " | ".join(trail), verdict))
