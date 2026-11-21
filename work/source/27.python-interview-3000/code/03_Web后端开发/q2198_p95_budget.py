"""响应时间 P95 目标拆解: 总预算到分层的分配与核算(纯标准库)。"""

BUDGET_MS = 300.0
LAYERS = [("网关与网络", 30), ("应用计算", 120), ("数据库", 90), ("下游调用", 30)]
measured = [25, 180, 70, 40]                        # tracing 取到的各层 P95


def check_budget(budget, layers, measured_vals):
    rows, total, worst = [], 0.0, None
    for (name, allow), actual in zip(layers, measured_vals):
        ratio = actual / allow
        total += actual
        if worst is None or ratio > worst[1]:
            worst = (name, ratio)
        rows.append((name, allow, actual, ratio))
    return rows, total, worst, total <= budget


rows, total, worst, ok = check_budget(BUDGET_MS, LAYERS, measured)
for name, allow, actual, ratio in rows:
    print("{:8s} 预算 {:3d}ms 实测 {:3d}ms 占用 {:4.0f}% {}".format(
        name, allow, actual, ratio * 100, "超支" if ratio > 1 else "ok"))
print("合计 {:.0f}ms / 预算 {:.0f}ms -> {}".format(total, BUDGET_MS, "达标" if ok else "超标"))
print("最该治理的一层: {} 占预算 {:.0f}%".format(worst[0], worst[1] * 100))
assert not ok and worst[0] == "应用计算"
print("要点: P95 目标逐层拆预算, 实测逐层核算, 按超支占比排序治理; 分位数不能跨层相加当总 P95")
