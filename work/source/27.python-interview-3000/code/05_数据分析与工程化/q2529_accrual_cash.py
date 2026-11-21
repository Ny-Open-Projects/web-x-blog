"""收入口径: 应计(权责发生)与实收(现金收付)对照与递延收入滚存"""

MONTHS_Q1 = ["1月", "2月", "3月"]
ANNUAL_PRICE = 1200          # 年费订阅, 1 月 1 日一次性收款
MONTHLY_RECOG = ANNUAL_PRICE / 12


def accrual_view():
    """权责发生制: 服务逐月确认, 每月 100"""
    return {m: MONTHLY_RECOG for m in MONTHS_Q1}


def cash_view():
    """收付实现制: 钱几月到账算几月收入"""
    return {"1月": ANNUAL_PRICE, "2月": 0.0, "3月": 0.0}


def deferred_rollforward(opening, billed, recognized):
    """递延收入(合同负债)滚存: 期初 + 新收款 - 本期确认 = 期末"""
    closing = opening + billed - recognized
    assert abs((closing + recognized) - (opening + billed)) < 1e-9, "滚存必须守恒"
    return closing


if __name__ == "__main__":
    acc, cash = accrual_view(), cash_view()
    print(f"{'月份':<4} 实收口径 应计口径 递延余额")
    deferred = 0.0
    for m in MONTHS_Q1:
        deferred = deferred_rollforward(deferred, cash[m], acc[m])
        print(f"{m:<4} {cash[m]:8.0f} {acc[m]:6.0f} {deferred:8.0f}")
    assert deferred == 900.0, "Q1 末递延收入应为 900"
    # 全年口径守恒: 现金总收入 == 应计总收入, 差的只是时间分布
    total_cash = ANNUAL_PRICE
    total_acc = sum(MONTHLY_RECOG for _ in range(12))
    assert abs(total_cash - total_acc) < 1e-9
    print(f"全年对照: 实收 {total_cash:.0f} == 应计 {total_acc:.0f}, 两口径全年守恒, 差异只在月份分布")
    print("要点: 看现金流用实收, 看经营业绩用应计, 递延余额是两者的桥, 滚存必须逐期守恒")
