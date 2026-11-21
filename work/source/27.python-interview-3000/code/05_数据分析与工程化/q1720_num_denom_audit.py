"""分子分母对齐审计:转化率的分子分母必须同时间窗、同人群、同粒度"""

ORDERS = {"d1": 120, "d2": 135}                # 订单表:d3 上游延迟,整日缺数
VISITS = {"d1": 2000, "d2": 2100, "d3": 2250}  # 访问表:d3 正常


def audit(num, den):
    issues = []
    for k in sorted(set(num) | set(den)):
        n, d = num.get(k), den.get(k)
        if d in (None, 0):
            issues.append((k, "denominator_missing", d))
        elif n is None:
            issues.append((k, "numerator_missing", n))
        elif n > d:
            issues.append((k, "num_gt_den", (n, d)))
    return issues


def safe_rate(num, den):
    """分子缺失当日整日剔除而不是按 0 处理,避免转化率被稀释"""
    ok = [k for k in den if den.get(k) and num.get(k) is not None]
    total_n = sum(num[k] for k in ok)
    total_d = sum(den[k] for k in ok)
    return total_n / total_d, ok, len(den) - len(ok)


if __name__ == "__main__":
    for k, kind, detail in audit(ORDERS, VISITS):
        print(f"违规: {k} {kind} {detail}")
    rate, used, dropped = safe_rate(ORDERS, VISITS)
    print(f"剔除异常日后整体转化率: {rate:.2%} (使用 {used}, 剔除 {dropped} 天)")
    dilute = sum(ORDERS.values()) / sum(VISITS.values())
    print(f"若按缺失=0 处理会被稀释成: {dilute:.2%}")
    print("要点:对齐三查——时间窗一致、人群一致(登录/游客)、粒度一致(人/会话);分子缺日整日剔除并标注,绝不按 0 补")
