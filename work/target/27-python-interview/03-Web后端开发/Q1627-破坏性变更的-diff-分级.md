---
title: [Q1627] 破坏性变更的 diff 分级
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1627 · 破坏性变更的 diff 分级

> 难度:★★★★ | 标签:OpenAPI, 接口演进

**问**:schema diff 出来了,怎么机器判定哪些是破坏性变更?

**答**:分级规则可以完全机器化:响应删字段、字段改类型、请求新增必填、删除路径或方法、收窄枚举都是破坏;响应新增可选字段、请求放宽必填、新增路径、扩枚举是兼容。判定方向感来自一个问题:调用方会不会崩——调用方按文档读一个字段你删了就崩,你加了字段它看不见所以没事。把规则写成分类器,CI 输出 breaking 与 compatible 两组列表,破坏项存在就阻断,除非走快照豁免流程。特殊结构单独处理:oneof 变化、默认值变更、nullable 变化都可能破坏,规则表要持续维护。

```python
# file: code/03_Web后端开发/q1627_breaking_diff.py
"""OpenAPI 破坏性变更分级: diff 分类器(纯标准库)。"""

V1 = {
    "required": ["amount"],
    "response_fields": {"id": "str", "status": "str", "amount": "float"},
}
V2 = {
    "required": ["amount", "currency"],        # 新增必填 -> 破坏
    "response_fields": {"id": "str", "status": "str", "amount": "float", "coupon": "str|none"},
}
V3 = {
    "required": ["amount"],                     # 与 V1 相同 -> 不因必填破坏
    "response_fields": {"id": "str", "amount": "decimal"},   # 删字段 + 改类型 -> 破坏
}


def diff_operation(old, new, label):
    findings = []
    removed = sorted(set(old["response_fields"]) - set(new["response_fields"]))
    added = sorted(set(new["response_fields"]) - set(old["response_fields"]))
    for f in removed:
        findings.append(("breaking", f"{label}: 响应删除字段 {f}"))
    for f in added:
        findings.append(("compatible", f"{label}: 响应新增字段 {f}"))
    for f in sorted(set(old["response_fields"]) & set(new["response_fields"])):
        if old["response_fields"][f] != new["response_fields"][f]:
            findings.append(("breaking", f"{label}: 字段 {f} 类型变更"))
    for f in sorted(set(new["required"]) - set(old["required"])):
        findings.append(("breaking", f"{label}: 请求新增必填 {f}"))
    for f in sorted(set(old["required"]) - set(new["required"])):
        findings.append(("compatible", f"{label}: 请求放宽必填 {f}"))
    return findings


def verdict(findings):
    bad = [msg for level, msg in findings if level == "breaking"]
    return "阻断合并" if bad else "放行"


for old, new, label in ((V1, V2, "V1->V2"), (V1, V3, "V1->V3")):
    fs = diff_operation(old, new, label)
    for level, msg in fs:
        print(f"[{level:10}] {msg}")
    print("结论:", verdict(fs))
    print()

print("经验: 新增可选输出、放宽校验是兼容; 删字段、改类型、加必填是破坏")
```

**追问**:
- 改字段描述算破坏吗?——不算,描述只影响人;但改 format 如 date-time 变 date 要按类型变化处理。
- 破坏性变更一定不能上吗?——不是,配合版本化:新路径或新 media type 承载破坏,旧版本走弃用倒计时。
