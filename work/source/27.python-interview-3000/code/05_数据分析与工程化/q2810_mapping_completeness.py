"""映射配置的完备性校验: 上线前把配置错误一次清零"""

SOURCE_SCHEMA = {
    "user_name": "str", "phone": "str", "city": "str",
    "reg_dt": "str", "amt": "float|null", "channel": "str|null",
}
REQUIRED_TARGETS = {"user_id", "phone_tail", "city_std", "reg_date", "amount"}

GOOD = [
    {"target": "user_id", "source": "user_name", "fn": "strip"},
    {"target": "phone_tail", "source": "phone", "fn": "last4"},
    {"target": "city_std", "source": "city", "fn": "alias"},
    {"target": "reg_date", "source": "reg_dt", "fn": "iso_date"},
    {"target": "amount", "source": "amt", "fn": "to_float", "default": 0.0},
]

BAD = [
    {"target": "user_id", "source": "user_name", "fn": "strip"},
    {"target": "city_std", "source": "city", "fn": "alias"},
    {"target": "city_std", "source": "channel", "fn": "alias"},
    {"target": "reg_date", "source": "user_nm", "fn": "iso_date"},
    {"target": "amount", "source": "amt", "fn": "to_float"},
]


def validate_mapping(mapping, schema, required):
    errors = []
    seen = set()
    for rule in mapping:
        target = rule["target"]
        if target in seen:
            errors.append(f"重复目标字段 {target}")
        seen.add(target)
        src = rule["source"]
        if src not in schema:
            errors.append(f"规则 {target}: 源字段 {src} 不在源 schema 中")
        elif "null" in schema[src] and "default" not in rule:
            errors.append(f"规则 {target}: 源字段 {src} 可空但未配置默认值")
    missing = sorted(required - seen)
    for m in missing:
        errors.append(f"必选目标字段 {m} 没有任何规则覆盖")
    return errors


if __name__ == "__main__":
    errs_bad = validate_mapping(BAD, SOURCE_SCHEMA, REQUIRED_TARGETS)
    errs_good = validate_mapping(GOOD, SOURCE_SCHEMA, REQUIRED_TARGETS)
    print("问题配置的错误清单:")
    for e in errs_bad:
        print(f"  - {e}")
    print(f"问题配置错误数 {len(errs_bad)}, 正确配置错误数 {len(errs_good)}")
    assert len(errs_good) == 0, "正确配置应零错误"
    assert len(errs_bad) == 5, "问题配置应有五处错误"
    assert any("phone_tail" in e for e in errs_bad), "漏配的必选目标应被发现"
    assert any("user_nm" in e for e in errs_bad), "未知源字段应被发现"
    assert any("可空" in e for e in errs_bad), "可空源缺默认值应被发现"
    print("要点: 映射配置是代码, 也要有单测与门禁; 完备性校验四查——重复 目标漏配 源不存在 可空无默认")
