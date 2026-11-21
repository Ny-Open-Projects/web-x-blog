"""密钥轮换台账: 到期分级预警与轮换留痕"""

from datetime import date

TODAY = date(2026, 3, 15)
SECRETS = [
    # 名称, 到期日, 最近轮换记录
    ("支付网关 API key", date(2026, 3, 10), "2026-02-20 轮换过"),
    ("对象存储 AK", date(2026, 3, 19), "未轮换"),
    ("数据库密码", date(2026, 4, 25), "2026-01-15 轮换过"),
    ("内部 JWT 签名密钥", date(2026, 12, 31), "未轮换"),
]


def level(days_left):
    if days_left < 0:
        return "已过期: 立即轮换并审计泄露"
    if days_left <= 7:
        return "CRITICAL: 7 天内必须轮换"
    if days_left <= 30:
        return "WARN: 排入本周计划"
    return "OK"


if __name__ == "__main__":
    for name, expire, last in sorted(SECRETS, key=lambda s: s[1]):
        d = (expire - TODAY).days
        print(f"{name:<14} 到期 {expire} 剩 {d:>4} 天 [{level(d)}] 记录: {last}")
    print("要点: 台账只记元数据不存密钥值; 过期即事故; 轮换必须带联调验证才算闭环; 新增密钥强制登记")
