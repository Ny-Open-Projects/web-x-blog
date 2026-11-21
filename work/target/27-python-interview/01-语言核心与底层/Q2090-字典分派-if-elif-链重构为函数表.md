---
title: [Q2090] 字典分派:if-elif 链重构为函数表
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2090 · 字典分派:if-elif 链重构为函数表

> 难度:★★★☆☆ | 标签:字典分派, 函数表, 重构

**问**:一长串 if action == "..." elif ... 怎么重构?字典分派的边界在哪?

**答**:把每个分支体提炼成同签名函数,装进模块级 HANDLERS 字典,分支逻辑变成一次 O(1) 查表:handler = HANDLERS.get(action),取不到走默认。收益:新增动作只注册一个函数,符合开闭原则;分支与实现一一对应可单测;表本身可导出做能力清单(与 Q2078 的 match 等价实现同源)。两个边界:键必须可哈希,区间、前缀这类范围匹配仍需要 if-elif 或「区间映射到函数」的二级设计;分支间有共享前置逻辑时,要么提升到查表之前统一执行,要么改用类分派。demo 用 assert 保证重构前后行为一致——重构的前提永远是行为等价。

```python
# file: code/01_语言核心与底层/q2090_dict_dispatch.py
"""字典分派:把 if-elif 链重构为函数表。"""


def _approve(amount):
    return f"通过 {amount}"


def _review(amount):
    return f"转人工 {amount}"


def _reject(amount):
    return f"拒绝 {amount}"


def decide_if_chain(action, amount):
    """重构前:分支链每加一个动作就长一节。"""
    if action == "approve":
        return _approve(amount)
    elif action == "review":
        return _review(amount)
    elif action == "reject":
        return _reject(amount)
    return "未知动作"


HANDLERS = {"approve": _approve, "review": _review, "reject": _reject}


def decide_table(action, amount):
    """重构后:查表分派,新增动作只注册函数。"""
    handler = HANDLERS.get(action)
    return handler(amount) if handler else "未知动作"


if __name__ == "__main__":
    for action in ("approve", "review", "reject", "hack"):
        a, b = decide_if_chain(action, 100), decide_table(action, 100)
        assert a == b, action
        print(f"{action:8} -> {b}")
```

**追问**:1) 分支需要共享前置逻辑怎么办?——提升到查表之前统一执行,或让 handler 接收统一上下文对象;范围条件能上字典吗?——键要可哈希,区间匹配用「区间映射到函数」的二级表或保留 if-elif。2) 字典分派的设计要点?——handler 统一签名(接收 ctx);注册式扩展(新类型 register 即插,Q1552 呼应);默认 handler 兜底;漏注册 NotImplementedError(Q2078 哨兵判缺)。3) 与 match 的分工?——分派表运行时可扩展、键是值;match 静态结构、模式是形状;命令路由/事件类型用表,协议解析用 match。4) 生产陷阱?——表定义时 handler 名字拼错(要到运行时才发现,启动期校验表完整性);键冲突静默覆盖;共享前置逻辑在各 handler 重复。
