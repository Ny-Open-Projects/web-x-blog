"""Q2591 容量预估联动限流阈值:按等级按比例下调并保底。

降级容量算出来后,限流阈值要机械联动下调,别靠人拍脑袋;
premium 留保底份额,free 先砍到地板,下调后逐级校验单调。
"""

BASE_LIMITS = {"premium": 400, "standard": 100, "free": 20}


def derate(capacity_ratio, base=BASE_LIMITS, floor=1):
    assert 0 < capacity_ratio <= 1, "容量比例必须在 0 到 1 之间"
    return {k: max(floor, int(v * capacity_ratio)) for k, v in base.items()}


def protected_derate(ratio, protect):
    out = derate(ratio)
    out["premium"] = max(out["premium"], protect)
    return out


def main():
    healthy = derate(1.0)
    degraded = derate(0.35)
    assert healthy == BASE_LIMITS
    assert degraded["premium"] == 140 and degraded["standard"] == 35, degraded
    assert degraded["free"] == 7
    assert degraded["premium"] > degraded["standard"] > degraded["free"]  # 单调保持
    worst = protected_derate(0.05, protect=50)
    assert worst["premium"] == 50 and worst["free"] == 1
    print("健康态:", healthy)
    print("降级态 35%:", degraded)
    print("极端降级带保底:", worst, "← premium 至少留 50")


if __name__ == "__main__":
    main()
