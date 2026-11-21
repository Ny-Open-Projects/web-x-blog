---
title: [Q2265] schema 版本协商:生产者声明与消费者适配
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2265 · schema 版本协商:生产者声明与消费者适配

> 难度:★★★★ | 标签:schema, 版本管理

**问**:上游数据格式要升级,几十个下游不可能同步改,版本协商机制怎么设计?

**答**:把兼容规则做成机器可执行的协商协议。生产者在数据里声明 schema 版本,注册中心维护版本树;消费者声明自己支持的版本集合。协商规则三条:命中支持集合直接读;同主版本内更高小版本走适配读——次版本只允许加可选字段,老消费者按旧版本解析、新字段走默认值,实测生产者 1.2 对只认 1.1 的消费者走适配读;跨主版本直接拒绝——主版本意味着语义破坏(如金额从分改元),必须走双写迁移期,消费者升级完成前生产者不能切。协商逻辑写死在公共库,禁止每个下游自行判断;拒绝事件要计数告警,它暴露的是"有人发了下游接不住的版本"。这套协议的本质是把"版本兼容"从口头约定变成握手行为,破坏性变更在握手处被拦截而不是在生产数据里被发现。

```python
# file: code/05_数据分析与工程化/q2265_schema_negotiation.py
"""schema 版本协商: 生产者声明, 消费者适配或拒绝"""

REGISTRY = {
    "1.0": {"order_id": "str", "amount_cents": "int", "status": "str"},
    "1.1": {"order_id": "str", "amount_cents": "int", "status": "str", "channel": "str?"},
    "1.2": {"order_id": "str", "amount_cents": "int", "status": "str", "channel": "str?", "memo": "str?"},
    "2.0": {"order_id": "str", "amount_yuan": "float", "status": "str"},   # 语义破坏: 分改元
}
CONSUMER_SUPPORTS = {"1.0", "1.1"}   # 消费者已适配的版本


def negotiate(producer_version, consumer_supports):
    if producer_version in consumer_supports:
        return "直接读", producer_version
    major, minor = producer_version.split(".")
    same_major = sorted(
        (v for v in consumer_supports if v.split(".")[0] == major),
        key=lambda v: int(v.split(".")[1]),
        reverse=True,
    )
    if same_major and int(minor) >= int(same_major[0].split(".")[1]):
        return "适配读", same_major[0]   # 新增可选字段对老读者透明
    return "拒绝", None                   # 主版本变更, 必须升级消费端


if __name__ == "__main__":
    for pv in ["1.0", "1.1", "1.2", "2.0"]:
        mode, read_as = negotiate(pv, CONSUMER_SUPPORTS)
        if mode == "适配读":
            detail = f"按 {read_as} 解析, 新增字段走默认值"
        elif mode == "直接读":
            detail = ""
        else:
            detail = "主版本语义变更, 消费端升级前生产者保持双写"
        print(f"生产者 {pv} -> {mode} {detail}")
    print("要点: 次版本只加可选字段, 主版本必须双写迁移; 协商逻辑进公共库, 拒绝事件计数告警")
```

**追问**:
- 追问 1:适配读时新字段默认值给什么?—— 显式 NULL 加缺失标记,不用猜测性默认值,统计口径里把缺失单独计数。
- 追问 2:怎么防止"次版本"夹带语义变化?—— 注册中心做变更类型 lint,类型改动或含义变更必须升主版本,评审加自动化双重把关。
