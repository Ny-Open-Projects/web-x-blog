"""契约核验脚本: 用消费者期望核对 provider 真实响应(纯标准库)。"""

EXPECT = {
    "status": 200,
    "body_has": ["order_id", "total", "state"],
    "body_not_has": ["internal_cost"],
    "types": {"order_id": "str", "total": "number"},
    "enum": {"state": ["created", "paid", "shipped"]},
}
TYPE_CHECKS = {"str": str, "number": (int, float), "bool": bool, "list": list, "obj": dict}


def verify(response, expect):
    """返回违规列表; 只检查期望里记录过的约束。"""
    findings = []
    if response["status"] != expect["status"]:
        findings.append("status {} != 期望 {}".format(response["status"], expect["status"]))
    body = response.get("body") or {}
    for key in expect.get("body_has", []):
        if key not in body:
            findings.append("缺少消费者依赖的字段: " + key)
    for key in expect.get("body_not_has", []):
        if key in body:
            findings.append("泄漏了消费者未依赖的内部字段: " + key)
    for key, want in expect.get("types", {}).items():
        got = body.get(key)
        if got is not None and not isinstance(got, TYPE_CHECKS[want]):
            findings.append("字段 {} 类型 {} 不符合契约 {}".format(
                key, type(got).__name__, want))
    for key, allowed in expect.get("enum", {}).items():
        if body.get(key) not in allowed:
            findings.append("字段 {} 值 {} 超出契约枚举 {}".format(
                key, body.get(key), allowed))
    return findings


good = {"status": 200, "body": {"order_id": "o-1", "total": 99.5, "state": "paid"}}
bad = {"status": 200, "body": {"order_id": 7, "state": "refunded", "internal_cost": 12}}
print("场景一:", verify(good, EXPECT) or "契约核验通过")
for f in verify(bad, EXPECT):
    print("场景二:", f)
assert verify(good, EXPECT) == [] and len(verify(bad, EXPECT)) == 4
print("要点: 核验只看记录过的约束, provider 新增字段不该挂红——这正是消费驱动与快照测试的分界")
