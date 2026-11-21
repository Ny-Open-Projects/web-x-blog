---
title: [Q2960] 数据校验器:schema 约束 + 业务规则 + 结构化报告
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2960 · 数据校验器:schema 约束 + 业务规则 + 结构化报告

> 难度:★★★★ | 标签:数据质量, 校验器

**问**:面试官:给你一份入库前的用户表,你怎么把校验做成工程,而不是一堆散落的 if?

**答**:三段式:schema 管字段级约束(类型、必填、范围、正则、长度),业务规则管 schema 表达不了的跨字段逻辑(例如未成年人需监护人标记),报告层同时输出行级明细与按字段聚合。实测 6 行样例:通过率 16.67%,按字段聚合 email 2 处、user_id 3 处,按错误码聚合 MISSING 2、RANGE 2、TYPE 1——明细给修复的人,聚合给定优先级的人。一个容易踩的坑是 bool 冒充 int:isinstance(True, int) 为真,类型检查必须显式排除 bool,样例里 user_id=True 就是这样被拦下的。schema 与规则的分工让新增约束不改引擎,新增规则不改 schema。

```python
# file: code/05_数据分析与工程化/q2960_schema_validator.py
"""完整的数据校验器: schema 字段约束 + 跨字段业务规则 + 结构化报告"""
import json
import re

# schema: 每个字段的类型、必填性与约束
SCHEMA = {
    "user_id": {"type": "int", "required": True, "min": 1},
    "name":    {"type": "str", "required": True, "max_len": 20},
    "age":     {"type": "int", "required": False, "min": 0, "max": 150},
    "email":   {"type": "str", "required": True,
                "pattern": re.compile(r"^[\w.]+@[\w.]+\.\w+$")},
}

# 业务规则: schema 表达不了的跨字段检查, 返回错误消息或 None
RULES = {
    "adult_user": lambda row: None if row.get("age", 18) >= 18 else "age<18 需监护人标记",
}

TYPE_CHECK = {
    "int": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "str": lambda v: isinstance(v, str),
}


def check_row(row):
    """返回该行错误列表: (字段, 错误码, 消息)"""
    errs = []
    for field, spec in SCHEMA.items():
        v = row.get(field)
        if v is None:
            if spec.get("required"):
                errs.append((field, "MISSING", "必填字段缺失"))
            continue
        if not TYPE_CHECK[spec["type"]](v):
            errs.append((field, "TYPE", "期望 %s 实得 %s" % (spec["type"], type(v).__name__)))
            continue
        lo, hi = spec.get("min"), spec.get("max")
        if (lo is not None and v < lo) or (hi is not None and v > hi):
            errs.append((field, "RANGE", "超出 [%s, %s]" % (lo if lo is not None else "-inf",
                                                            hi if hi is not None else "inf")))
        pattern = spec.get("pattern")
        if pattern is not None and not pattern.match(v):
            errs.append((field, "PATTERN", "不满足正则 " + pattern.pattern))
        max_len = spec.get("max_len")
        if max_len is not None and len(v) > max_len:
            errs.append((field, "LEN", "长度超过 %d" % max_len))
    for name, rule in RULES.items():
        msg = rule(row)
        if msg:
            errs.append(("*", "RULE:" + name, msg))
    return errs


def validate(rows):
    """校验全部行, 输出明细与按字段聚合的报告"""
    report = {"total": len(rows), "passed": 0, "rejected": 0,
              "errors": [], "by_field": {}, "by_code": {}}
    for i, row in enumerate(rows):
        errs = check_row(row)
        if not errs:
            report["passed"] += 1
        else:
            report["rejected"] += 1
        for f, code, msg in errs:
            report["errors"].append({"row": i, "field": f, "code": code, "msg": msg})
            report["by_field"][f] = report["by_field"].get(f, 0) + 1
            report["by_code"][code.split(":")[0]] = report["by_code"].get(code.split(":")[0], 0) + 1
    report["pass_rate"] = round(report["passed"] / report["total"], 4) if report["total"] else 1.0
    return report


ROWS = [
    {"user_id": 1, "name": "alice", "age": 30, "email": "a@x.com"},
    {"user_id": 2, "name": "bob", "email": "bad-mail"},             # 邮箱不合规
    {"user_id": -3, "name": "c" * 25, "age": 200},                  # 三处越界
    {"name": "dave", "email": "d@x.com"},                           # 缺 user_id
    {"user_id": 5, "name": "erin", "age": 15, "email": "e@x.com"},  # 命中业务规则
    {"user_id": True, "name": "frank", "email": "f@x.com"},         # bool 冒充 int
]

if __name__ == "__main__":
    rep = validate(ROWS)
    print("总体: 总数=%d 通过=%d 拒收=%d 通过率=%.2f%%"
          % (rep["total"], rep["passed"], rep["rejected"], rep["pass_rate"] * 100))
    print("按字段:", json.dumps(rep["by_field"], ensure_ascii=False))
    print("按错误码:", json.dumps(rep["by_code"], ensure_ascii=False))
    for e in rep["errors"]:
        print("  行%d 字段[%s] %s: %s" % (e["row"], e["field"], e["code"], e["msg"]))
    print("要点: schema 管字段级约束, 规则管跨字段逻辑, 报告同时给明细与聚合, 便于定位和派单")
```

**追问**:
- 追问 1:校验失败的数据一定不能入库吗?—— 不是,按错误码分级:MISSING 与 TYPE 直接拒收,RANGE 进隔离区人工修,RULE 类可标记后放行。
- 追问 2:schema 怎么和上游约定联动?—— 用 JSON Schema 或 OpenAPI 表达同一份约束并生成校验代码,避免文档与代码两张皮。
