"""字段映射配置化: 声明式规则驱动清洗, 转换逻辑与业务代码解耦"""
from datetime import datetime

ALIAS = {"魔都": "上海", "帝都": "北京"}

MAPPING = [
    {"target": "user_id", "source": "user_name", "fn": "strip"},
    {"target": "phone_tail", "source": "phone", "fn": "last4"},
    {"target": "city_std", "source": "city", "fn": "alias"},
    {"target": "reg_date", "source": "reg_dt", "fn": "iso_date"},
    {"target": "amount", "source": "amt", "fn": "to_float", "default": 0.0},
]

RAW_ROWS = [
    {"user_name": " 张三 ", "phone": "13812345678", "city": "魔都",
     "reg_dt": "2026-01-15", "amt": "129.9"},
    {"user_name": "李四", "phone": "18987654321", "city": "深圳",
     "reg_dt": "2026-02-30", "amt": None},
    {"user_name": "王五", "phone": "17700001111", "city": "北京",
     "reg_dt": "2026-03-08", "amt": "88"},
]


def t_strip(v):
    return v.strip()


def t_last4(v):
    return v[-4:] if len(v) >= 4 else v


def t_alias(v):
    return ALIAS.get(v, v)


def t_iso_date(v):
    try:
        return datetime.strptime(v, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        return None


def t_to_float(v, default=None):
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


TRANSFORMS = {"strip": t_strip, "last4": t_last4,
              "alias": t_alias, "iso_date": t_iso_date, "to_float": t_to_float}


def apply_mapping(rows, mapping):
    out = []
    for row in rows:
        rec, issues = {}, []
        for rule in mapping:
            fn = TRANSFORMS[rule["fn"]]
            val = fn(row.get(rule["source"]))
            if val is None and "default" in rule:
                val = rule["default"]
            if val is None:
                issues.append(rule["target"])
            rec[rule["target"]] = val
        rec["_issues"] = issues
        out.append(rec)
    return out


if __name__ == "__main__":
    for rec in apply_mapping(RAW_ROWS, MAPPING):
        print(rec)
    clean = apply_mapping(RAW_ROWS, MAPPING)
    assert clean[0]["user_id"] == "张三" and clean[0]["city_std"] == "上海"
    assert clean[0]["phone_tail"] == "5678" and clean[0]["amount"] == 129.9
    assert clean[1]["amount"] == 0.0, "amt 缺失应落到配置的默认值"
    assert clean[1]["reg_date"] is None and clean[1]["_issues"] == ["reg_date"], "非法日期应进问题清单"
    assert clean[2]["amount"] == 88.0
    print("要点: 新增字段或换清洗规则只改配置不改代码, 问题值进 _issues 而不是让整批任务失败")
