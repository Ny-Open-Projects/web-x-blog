---
title: [Q2170] 契约核验脚本:provider 端的核对
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2170 · 契约核验脚本:provider 端的核对

> 难度:★★★★ | 标签:契约测试, 演进

**问**:拿到所有消费者的期望文件后,provider 侧的核验脚本要做哪些检查?输出什么?

**答**:核验脚本把每个期望文件的 interaction 重放到 provider 的沙箱环境,对真实响应做四类断言:status 是否一致;body_has 的字段是否存在(消费者会崩的改动);body_not_has 是否泄漏(内部字段出现在响应里也是破坏,因为消费者可能开始依赖它);types 与 enum 的类型与取值是否满足。输出是逐条 findings 列表,每条带期望文件、交互描述与违规内容,CI 里 findings 非空即失败,把"provider 改坏消费者"从线上事故前移到合并门禁。与快照测试的分界要守住:核验只看记录过的约束,provider 新增字段绝不该挂红,否则就退化为快照。

```python
# file: code/03_Web后端开发/q2170_contract_verify.py
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
```

**追问**:
- 核验在什么环境跑?——provider 的沙箱或本地启动实例加种子数据,重放必须可复现,禁止直连生产。
- 多个消费者的期望冲突怎么办?——说明契约本身有分叉,要把公共部分抽成 provider 的正式契约,各消费者期望只做增量。
