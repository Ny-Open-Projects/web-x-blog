"""流失预警评分:规则引擎版,条件命中加权求和后分层"""

RULES = [
    ("近7天未登录", lambda u: u["days_since_login"] > 7, 30),
    ("近30天订单下降超一半", lambda u: u["orders_30d"] < u["orders_prev_30d"] * 0.5, 25),
    ("客单价持续走低", lambda u: u["aov"] < u["aov_baseline"] * 0.6, 15),
    ("客诉未解决", lambda u: u["open_tickets"] > 0, 15),
    ("优惠券即将过期未用", lambda u: u["expiring_coupon"] is True, 10),
]

USERS = [
    {"uid": "u1", "days_since_login": 12, "orders_30d": 1, "orders_prev_30d": 5,
     "aov": 60, "aov_baseline": 100, "open_tickets": 1, "expiring_coupon": False},
    {"uid": "u2", "days_since_login": 1, "orders_30d": 4, "orders_prev_30d": 5,
     "aov": 95, "aov_baseline": 100, "open_tickets": 0, "expiring_coupon": True},
]


def risk_score(user):
    score, reasons = 0, []
    for name, cond, weight in RULES:
        if cond(user):
            score += weight
            reasons.append(f"{name}(+{weight})")
    return score, reasons


def band(score):
    if score >= 60:
        return "高危"
    if score >= 30:
        return "关注"
    return "健康"


if __name__ == "__main__":
    for u in USERS:
        score, reasons = risk_score(u)
        print(f"{u['uid']} 得分 {score} [{band(score)}] 命中: {'; '.join(reasons) or '无'}")
    print("规则分的好处是可解释、可快速上线;量大后再换模型分并保留规则分做兜底")
