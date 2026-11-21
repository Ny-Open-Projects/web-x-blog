---
title: [Q1533] frozenset 工程场景:集合作 key、常量集与边界归一
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1533 · frozenset 工程场景:集合作 key、常量集与边界归一

> 难度:★★★☆☆ | 标签:frozenset, 集合, API 设计

**问**:frozenset 除了「不可变的 set」还有什么正经用途?什么时候必须用它而不是 tuple?

**答**:frozenset 的价值在「可哈希的集合」三个场景:① 作 dict key 或集合成员——图的边(端点无序)用 frozenset((a, b)) 归一化,「集合的集合」只有这条路,set 不可哈希直接 TypeError;② 模块级常量注册表——不可变语义杜绝运行期被误改,也向读者声明「这是一组无序成员」;③ API 边界归一化——接受任意可迭代、内部 frozenset 化,天然去重,且调用方后续修改不影响内部状态。与 tuple 的分界:有序用 tuple,需要成员资格测试与 | & - ^ 运算用 frozenset(tuple 成员检测是 O(n))。空集是 frozenset() 而不是 { }(那是 dict);frozenset 相等只看成员,与构造顺序无关。

```python
# file: code/01_语言核心与底层/q1533_frozenset_scenarios.py

READ = frozenset({"doc:read", "doc:list"})
WRITE = frozenset({"doc:read", "doc:list", "doc:write"})
ADMIN = WRITE | frozenset({"user:manage"})     # frozenset 支持集合运算


def can(granted, needed):
    """所需权限是否全部被授予:子集判定。"""
    return frozenset(needed) <= granted


def undirected_edges(pairs):
    """无向边去重:a-b 与 b-a 是同一条边——用 frozenset 作 key。"""
    seen = {}
    for a, b in pairs:
        edge = frozenset((a, b))
        seen[edge] = seen.get(edge, 0) + 1
    return {tuple(sorted(e)): n for e, n in seen.items()}


def normalize_tags(tags):
    """API 边界:接受任意可迭代,归一成不可变集合,防外部漂移。"""
    return frozenset(tags)


if __name__ == "__main__":
    print("can(ADMIN, [doc:write, user:manage]):",
          can(ADMIN, ["doc:write", "user:manage"]))
    print("can(READ, [doc:write]):", can(READ, ["doc:write"]))

    print("edges:", undirected_edges([("a", "b"), ("b", "a"), ("b", "c")]))

    tags = ["db", "cache", "db"]
    frozen = normalize_tags(tags)
    tags.append("evil")                         # 调用方继续改原列表
    print("frozen tags unaffected:", frozen)

    groups = {frozenset((1, 2)): "pair", frozenset((3,)): "single"}
    print("set-as-dict-key:", groups[frozenset((2, 1))])
    try:
        {{1, 2}: "x"}
    except TypeError:
        print("set literal key -> TypeError 不可哈希")
```

**追问**:1) frozenset 能省内存吗?——不,它与 set 结构相同,买的是「可哈希 + 不可变语义」;需要省内存的只读常量才考虑 tuple,代价是成员检测退化为 O(n) 且没有集合运算。2) 什么时候买 frozenset?——作 dict key 或另一个 set 的元素、模块级常量集(语义上不可改)、输入归一(去重+固定);要的是语义收益而非性能。3) 底层细节?——与 set 同构但哈希缓存于对象;没有字面量语法(frozenset([...]) 运行时构建,不参与常量折叠);与 set 的运算仍生成新集合。4) 生产陷阱?——以为 {1,2} 写法能得到 frozenset(那是 set);常量集放函数内每次调用重新构造,应模块级缓存;把 tuple 当「省内存 frozenset」丢掉 O(1) 成员检测。
