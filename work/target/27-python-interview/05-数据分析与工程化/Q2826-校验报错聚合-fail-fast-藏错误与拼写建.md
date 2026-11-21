---
title: [Q2826] 校验报错聚合:fail-fast 藏错误与拼写建议
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2826 · 校验报错聚合:fail-fast 藏错误与拼写建议

> 难度:★★★☆ | 标签:配置校验, 错误聚合

**问**:面试官:校验器报了第一个错,用户改完再跑又撞第二个,五轮才改完,怎么破?

**答**:聚合模式,fail-fast 是反模式。同一份问题配置:fail-fast 只报第一个错($.name 长度 0),聚合模式一次列全 5 处——$.name、$.workers 类型、$.mode 枚举、$.retry.max_tries 缺失、$.scheduel 未知字段。对未知字段再加 difflib 最近匹配:scheduel 提示"你是不是想写 schedule?",一个建议省一次来回。经验法则:CI 门禁里的校验器永远聚合,交互式 CLI 可以 fail-fast 但要支持 --all。报错信息本身是 API,报错质量决定用户修复速度,值得像代码一样设计与测试。

```python
# file: code/05_数据分析与工程化/q2826_validate_aggregate.py
"""校验报错聚合: fail-fast 藏错误, 聚合模式一次列全, 再送一个拼写建议"""
import difflib

SCHEMA = {
    "type": "object", "closed": True,
    "required": ["name", "workers", "mode", "retry"],
    "fields": {
        "name": {"type": "str", "min_len": 1},
        "workers": {"type": "int", "min": 1, "max": 64},
        "mode": {"type": "str", "enum": ["full", "incremental"]},
        "schedule": {"type": "str", "min_len": 5},
        "retry": {"type": "object", "required": ["max_tries"],
                  "fields": {"max_tries": {"type": "int", "min": 1}}},
    },
}

BAD_CONFIG = {"name": "", "workers": "8", "mode": "delta", "retry": {},
              "scheduel": "0 3 * * *"}


def check_one(key, value, rule, path):
    errors = []
    t = rule["type"]
    type_ok = {"str": isinstance(value, str),
               "int": isinstance(value, int) and not isinstance(value, bool)
               }.get(t, True)
    if not type_ok:
        return [(path, f"应为 {t}, 实际 {type(value).__name__}")]
    if "min_len" in rule and len(value) < rule["min_len"]:
        errors.append((path, f"长度 {len(value)} 低于下限 {rule['min_len']}"))
    if "min" in rule and value < rule["min"]:
        errors.append((path, f"{value} 低于下限 {rule['min']}"))
    if "max" in rule and value > rule["max"]:
        errors.append((path, f"{value} 超出上限 {rule['max']}"))
    if "enum" in rule and value not in rule["enum"]:
        errors.append((path, f"{value!r} 不在枚举 {rule['enum']} 中"))
    return errors


def validate_all(config, schema, path="$", errors=None):
    if errors is None:
        errors = []
    for req in schema.get("required", []):
        if req not in config:
            errors.append((f"{path}.{req}", "必填字段缺失"))
    for key, rule in schema.get("fields", {}).items():
        if key not in config:
            continue
        child_path = f"{path}.{key}"
        if rule["type"] == "object":
            validate_all(config[key], rule, child_path, errors)
        else:
            errors.extend(check_one(key, config[key], rule, child_path))
    if schema.get("closed"):
        for key in config:
            if key not in schema["fields"]:
                errors.append((f"{path}.{key}", f"未知字段, 不在 schema 中"))
    return errors


def validate_fail_fast(config, schema, path="$"):
    for req in schema.get("required", []):
        if req not in config:
            return [(f"{path}.{req}", "必填字段缺失")]
    for key, rule in schema.get("fields", {}).items():
        if key not in config:
            continue
        child_path = f"{path}.{key}"
        if rule["type"] == "object":
            errs = validate_fail_fast(config[key], rule, child_path)
            if errs:
                return errs
        else:
            errs = check_one(key, config[key], rule, child_path)
            if errs:
                return errs[:1]
    for key in config:
        if schema.get("closed") and key not in schema["fields"]:
            return [(f"{path}.{key}", "未知字段, 不在 schema 中")]
    return []


def suggest(unknown, schema):
    return difflib.get_close_matches(unknown, schema["fields"], n=1)


if __name__ == "__main__":
    ff = validate_fail_fast(BAD_CONFIG, SCHEMA)
    all_errs = validate_all(BAD_CONFIG, SCHEMA)
    print(f"fail-fast 只报第一个错: {ff}")
    print("聚合模式一次列全:")
    for path, msg in all_errs:
        print(f"  {path}: {msg}")
    fix_hint = suggest("scheduel", SCHEMA)
    print(f"拼写建议: scheduel -> 你是不是想写 {fix_hint}?")
    assert len(ff) == 1, "fail-fast 应只报第一个错"
    assert len(all_errs) == 5, "聚合模式应列全五处错误"
    assert fix_hint == ["schedule"], "编辑距离应找回 schedule"
    print("要点: CI 里永远用聚合模式, 否则用户要改一轮跑五轮; 未知字段给最近拼写, 报错本身就是文档")
```

**追问**:
- 追问 1:错误之间有依赖怎么排序?—— 按字段路径字典序或按"修复后可能消失"的关系拓扑排序,根因放前面。
- 追问 2:聚合报错会不会淹没重点?—— 分级输出:错误 error、疑似警告 warn、建议 hint 三层,CI 只对 error 拦截。
