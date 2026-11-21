"""回归基准集:固定输入 + 期望输出 + 容忍度,指标逻辑改动先跑基准再上线"""

BENCH = [
    # case_id, 输入(订单额列表), 期望 gmv, 期望订单数
    ("c1_smoke", [100, 200, 300], 600, 3),
    ("c2_zero", [], 0, 0),
    ("c3_refund", [100, -50, 80], 130, 3),
    ("c4_round", [33, 33, 34], 100, 3),
]
TOL = 0.0


def calc_v1(orders):
    """被测口径 v1:GMV 按净额(退款冲减),订单数全量计数"""
    return sum(orders), len(orders)


def calc_v2(orders):
    """被测口径 v2:退款单不计 GMV 也不计订单数 —— 演示口径变更触发基准更新"""
    return sum(x for x in orders if x > 0), len([x for x in orders if x > 0])


def run(bench, calc, tol=TOL):
    passed, failed = 0, []
    for cid, orders, exp_gmv, exp_cnt in bench:
        gmv, cnt = calc(orders)
        if abs(gmv - exp_gmv) <= tol and cnt == exp_cnt:
            passed += 1
        else:
            failed.append((cid, (gmv, cnt), (exp_gmv, exp_cnt)))
    return passed, failed


if __name__ == "__main__":
    passed, failed = run(BENCH, calc_v1)
    print(f"口径 v1 基准回归: {passed}/{len(BENCH)} 通过")
    passed2, failed2 = run(BENCH, calc_v2)
    print(f"口径 v2 基准回归: {passed2}/{len(BENCH)} 通过")
    for cid, got, exp in failed2:
        print(f"  失败 {cid}: 实际 {got} 期望 {exp} -> 属预期口径变更则走'评审-更新基准-记版本',否则修复代码")
    print("要点:基准集=输入+期望+容忍度,进 CI 门禁;更新基准必须留版本与评审记录,不允许悄悄重置")
