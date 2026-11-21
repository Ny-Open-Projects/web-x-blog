"""用户合并的规则引擎: 证据分层裁决, 规则可注册不可改核"""


def norm_phone(p):
    return "".join(ch for ch in (p or "") if ch.isdigit()) or None


def norm_email(e):
    return (e or "").strip().lower() or None


RULES = [
    {"name": "同手机号", "tier": "AUTO_MERGE",
     "test": lambda a, b: norm_phone(a["phone"]) and norm_phone(a["phone"]) == norm_phone(b["phone"])},
    {"name": "同邮箱", "tier": "AUTO_MERGE",
     "test": lambda a, b: norm_email(a["email"]) and norm_email(a["email"]) == norm_email(b["email"])},
    {"name": "同名同市缺手机", "tier": "REVIEW",
     "test": lambda a, b: a["name"] == b["name"] and a["city"] == b["city"]
                          and (not norm_phone(a["phone"]) or not norm_phone(b["phone"]))},
]


def decide(ra, rb):
    """规则按注册顺序即证据强度裁决, 命中即返回"""
    for rule in RULES:
        if rule["test"](ra, rb):
            return rule["tier"], rule["name"]
    return "KEEP", None


A1 = {"id": "a1", "phone": "13800001111", "email": "a@x.com", "name": "张三", "city": "北京", "device": None}
A2 = {"id": "a2", "phone": "138-0000-1111", "email": " A@X.com ", "name": "张三", "city": "北京", "device": None}
A3 = {"id": "a3", "phone": None, "email": "zhangsan@x.com", "name": "张三", "city": "北京", "device": "d9"}
A4 = {"id": "a4", "phone": "13911112222", "email": "l@x.com", "name": "李四", "city": "上海", "device": None}
A5 = {"id": "a5", "phone": "13600009999", "email": "w@x.com", "name": "王五", "city": "广州", "device": "d1"}
A1["device"] = "d1"


if __name__ == "__main__":
    for ra, rb in [(A1, A2), (A1, A3), (A1, A4)]:
        tier, rule = decide(ra, rb)
        print(f"{ra['id']} vs {rb['id']}: {tier}" + (f" 证据={rule}" if rule else ""))
    assert decide(A1, A2)[0] == "AUTO_MERGE"
    assert decide(A1, A3)[0] == "REVIEW"
    assert decide(A1, A4)[0] == "KEEP"
    # 动态注册新证据: 同设备号视为强证据, 只追加不改核
    RULES.insert(0, {"name": "同设备号", "tier": "AUTO_MERGE",
                     "test": lambda a, b: a["device"] and a["device"] == b["device"]})
    tier, rule = decide(A1, A5)
    print(f"注册'同设备号'规则后 {A1['id']} vs {A5['id']}: {tier} 证据={rule}")
    assert tier == "AUTO_MERGE" and rule == "同设备号"
    print("要点: 强证据自动合并, 弱证据进人工复核队列, 新证据规则只追加进注册表")
