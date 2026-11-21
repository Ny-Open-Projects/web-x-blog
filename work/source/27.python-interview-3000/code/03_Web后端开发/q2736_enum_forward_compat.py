"""枚举值的向前兼容: 未知值不炸, 降级映射并保留原文(纯标准库)。"""

STATUS = {"active", "frozen", "closed"}
LEGACY_MAP = {"pending_review": "active", "banned": "closed"}  # 新枚举 -> 旧客户端可懂的值


def read_status(raw, strict=False, known=STATUS):
    """读方向: 认识的原样给; 不认识的查降级映射; 还不行给默认值并保留原文。

    strict 只在网关已知所有消费者都升级后才打开, 否则新服务发新值旧服务直接崩。
    """
    if raw in known:
        return {"value": raw, "raw": raw, "known": True}
    mapped = LEGACY_MAP.get(raw)
    if mapped is not None:
        return {"value": mapped, "raw": raw, "known": False}
    if strict:
        raise ValueError("未知枚举: %r" % raw)
    return {"value": "active", "raw": raw, "known": False}


def write_status(value, allowed=STATUS):
    """写方向: 只出白名单内的值; 新值上线走配置开关灰度, 不做运行时硬编码。"""
    if value not in allowed:
        raise ValueError("禁止输出未注册枚举")
    return value


r1 = read_status("active")
assert r1 == {"value": "active", "raw": "active", "known": True}
r2 = read_status("pending_review")
assert r2 == {"value": "active", "raw": "pending_review", "known": False}, "新值降级为旧语义"
r3 = read_status("brand_new")
assert r3["value"] == "active" and r3["raw"] == "brand_new", "完全未知给默认并保留原文"
try:
    read_status("brand_new", strict=True)
except ValueError as e:
    print("strict 模式拒收:", e)
assert write_status("frozen") == "frozen"
try:
    write_status("draft")
except ValueError as e:
    print("写方向白名单:", e)
print("读: known 原样 / 降级映射 / 默认加原文; 写: 只出注册值, 新值靠灰度开关")
