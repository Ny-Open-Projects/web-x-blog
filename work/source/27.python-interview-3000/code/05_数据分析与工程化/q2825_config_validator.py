"""配置的 schema 校验器: 迷你 DSL 覆盖类型 必填 枚举 区间与嵌套"""

SCHEMA = {
    "type": "object",
    "required": ["name", "workers", "mode", "retry"],
    "fields": {
        "name": {"type": "str", "min_len": 1},
        "workers": {"type": "int", "min": 1, "max": 64},
        "mode": {"type": "str", "enum": ["full", "incremental"]},
        "retry": {"type": "object", "required": ["max_tries"],
                  "fields": {"max_tries": {"type": "int", "min": 1}}},
    },
}

BAD_CONFIG = {"name": "", "workers": "8", "mode": "delta", "retry": {}}
GOOD_CONFIG = {"name": "trade_etl", "workers": 8, "mode": "full",
               "retry": {"max_tries": 3}}


def check_scalar(value, rule, path, errors):
    t = rule["type"]
    type_ok = {
        "str": isinstance(value, str),
        "int": isinstance(value, int) and not isinstance(value, bool),
        "float": isinstance(value, (int, float)) and not isinstance(value, bool),
    }.get(t, True)
    if not type_ok:
        errors.append((path, f"应为 {t}, 实际 {type(value).__name__}"))
        return
    if "min_len" in rule and len(value) < rule["min_len"]:
        errors.append((path, f"长度 {len(value)} 低于下限 {rule['min_len']}"))
    if "min" in rule and value < rule["min"]:
        errors.append((path, f"{value} 低于下限 {rule['min']}"))
    if "max" in rule and value > rule["max"]:
        errors.append((path, f"{value} 超出上限 {rule['max']}"))
    if "enum" in rule and value not in rule["enum"]:
        errors.append((path, f"{value!r} 不在枚举 {rule['enum']} 中"))


def validate(config, schema, path="$", errors=None):
    if errors is None:
        errors = []
    if schema["type"] == "object":
        if not isinstance(config, dict):
            errors.append((path, "应为 object"))
            return errors
        for req in schema.get("required", []):
            if req not in config:
                errors.append((f"{path}.{req}", "必填字段缺失"))
        for key, rule in schema.get("fields", {}).items():
            if key not in config:
                continue
            child = config[key]
            child_path = f"{path}.{key}"
            if rule["type"] == "object":
                validate(child, rule, child_path, errors)
            elif rule["type"] == "list":
                if not isinstance(child, list):
                    errors.append((child_path, "应为 list"))
                    continue
                item_rule = rule.get("item")
                if item_rule:
                    for i, v in enumerate(child):
                        if item_rule["type"] in ("object", "list"):
                            validate(v, item_rule, f"{child_path}[{i}]", errors)
                        else:
                            check_scalar(v, item_rule, f"{child_path}[{i}]", errors)
            else:
                check_scalar(child, rule, child_path, errors)
    return errors


if __name__ == "__main__":
    errs_bad = validate(BAD_CONFIG, SCHEMA)
    errs_good = validate(GOOD_CONFIG, SCHEMA)
    print("问题配置的报错:")
    for path, msg in errs_bad:
        print(f"  {path}: {msg}")
    print(f"问题配置 {len(errs_bad)} 处错误, 正确配置 {len(errs_good)} 处错误")
    assert errs_good == [], "正确配置应零报错"
    assert len(errs_bad) == 4, "问题配置应有四处错误"
    paths = [p for p, _ in errs_bad]
    assert "$.workers" in paths and "$.mode" in paths and "$.retry.max_tries" in paths
    print("要点: 校验器把'配置写错了'从运行时炸变成上线前拦, 嵌套 path 精确定位, 一眼知道改哪")
