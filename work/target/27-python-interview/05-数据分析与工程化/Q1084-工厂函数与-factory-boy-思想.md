---
title: [Q1084] 工厂函数与 factory_boy 思想
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1084 · 工厂函数与 factory_boy 思想

> 难度:★★★☆ | 标签:测试数据, factory

**问**:批量造 100 条有关联关系的订单数据,factory_boy 的哪些思想值得手写复刻?

**答**:三个核心思想:序列(每个实例唯一 id/邮箱)、子工厂(订单自动带出用户,关联数据一键生成)、覆盖参数(`make_order(user=xxx)` 局部替换)。手写版就是一个模块级工厂函数加计数器:默认值函数化(`f"user{n}@t.io"`)实现序列,工厂内调用另一工厂实现子工厂,`**overrides` 实现覆盖。相比静态 JSON 夹具,factory 让数据意图清晰("这个测试只关心金额")且能跟随 schema 演进。

```python
# file: code/05_数据分析与工程化/q1084_factory_function.py

_counter = {"n": 0}

def make_user(**overrides):
    _counter["n"] += 1
    n = _counter["n"]
    user = {"id": n, "email": f"user{n}@t.io", "role": "member"}
    user.update(overrides)
    return user

def make_order(**overrides):
    order = {
        "id": len(overrides) + 1000,
        "user": overrides.pop("user", None) or make_user(),
        "amount": 9.9,
        "status": "paid",
    }
    order.update(overrides)
    return order

if __name__ == "__main__":
    orders = [make_order(amount=i) for i in range(1, 4)]
    for o in orders:
        print(o["id"], o["user"]["email"], o["amount"], o["status"])
    assert orders[0]["user"]["email"] != orders[1]["user"]["email"], "序列保证唯一"
    print("子工厂自动造用户,覆盖参数只写关心的字段")
```

**追问**:
- 追问 1:factory 的计数器要在测试间重置吗?—— 要,fixture setup 里 reset,否则跨测试累加造成 id 断言耦合。
- 追问 2:子工厂会不会失控造太多数据?—— 控制默认关联深度(默认一层),深层关联由测试显式声明。
