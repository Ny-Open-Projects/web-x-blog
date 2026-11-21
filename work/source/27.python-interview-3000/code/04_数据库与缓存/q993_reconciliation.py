"""订单与支付流水对账: 差异分类 + 自动修复"""
def reconcile(orders, payments):
    diffs = []
    for oid, amount in orders.items():
        if oid not in payments:
            diffs.append((oid, "missing_payment", amount))
        elif payments[oid] != amount:
            diffs.append((oid, "amount_mismatch",
                          (amount, payments[oid])))
    for pid in payments:
        if pid not in orders:
            diffs.append((pid, "orphan_payment", payments[pid]))
    return diffs

def auto_fix(diff, fixers):
    oid, kind, _ = diff
    if kind == "missing_payment" and "re_query_payment" in fixers:
        return f"{oid}: 触发支付结果重查"
    if kind == "amount_mismatch":
        return f"{oid}: 差错转人工"
    if kind == "orphan_payment":
        return f"{oid}: 触发退款/补单流程"
    return f"{oid}: 待处理"

if __name__ == "__main__":
    orders = {"O1": 100, "O2": 200, "O3": 300}
    payments = {"O1": 100, "O2": 150, "P9": 500}
    for d in reconcile(orders, payments):
        print("差异:", d, "->", auto_fix(d, {"re_query_payment"}))
    print("对账目标: 差错表每日清零, 差错率突增触发告警")
