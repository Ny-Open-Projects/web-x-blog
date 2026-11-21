---
title: [Q1297] 可变对象作 dict key:hash 与内容漂移
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1297 · 可变对象作 dict key:hash 与内容漂移

> 难度:★★☆☆☆ | 标签:hash, dict, 疑难杂症

**问**:自定义类的实例可以当 dict key,那我修改它的属性会发生什么?为什么 list/dict 直接不允许当 key?

**答**:dict 的查找契约是「hash 决定桶,eq 决定命中」,两者都来自 key 对象:自定义类默认 hash 基于 id、永不变,所以实例当 key 「能跑」;但一旦 __hash__ 参与了可变字段(如 self.name),修改字段后 hash 漂移,对象落进错误的桶——`k in cache` 变 False、值取不出来,而条目还占着位置,len 不变,成为幽灵数据。list/dict/set 在语言层禁止(__hash__ 为 None)正是因为它们的 hash 会随内容变化,契约无法维持。纪律:参与 __hash__ 的字段必须不可变(且最好与 __eq__ 严格同源);需要「可变 key」语义时,用稳定标识符(id、主键、frozenset 化的字段)做 key,把可变部分放 value。与 Q535 的哈希随机化呼应:进程内一致是底线,跨进程可复现是额外要求。

```python
# file: code/01_语言核心与底层/q1297_mutable_dict_key.py


class Bucket:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)          # hash 参与了可变字段:埋雷

    def __eq__(self, other):
        return isinstance(other, Bucket) and self.name == other.name


if __name__ == "__main__":
    b = Bucket("cold")
    cache = {b: 100}
    b.name = "hot"                      # 内容漂移
    print("lookup by key:", b in cache)
    try:
        cache[b]                        # hash 已变,桶对不上
    except KeyError:
        print("KeyError -> hash drifted, entry is a ghost")
    print("len still:", len(cache), "| scan finds:",
          sum(1 for k in cache if k is b))
```

**追问**:1) 为什么「len 不变但查不到」最危险?——它破坏的是不变量而非报错,监控与测试都看不到,唯一线索是业务侧「偶尔取不到缓存」;这类事故排查看 Q1296 的方法论。2) 漂移的机制?——哈希在插入时计算并存储;查找时重算哈希+eq 比对;可变 key 内容变了则「存时哈希 ≠ 查时哈希」,桶定位失败但 len 不变。3) 防御姿势?——key 一律不可变(不可变类型或自定义类的字段全不可变);需要 identity 语义就用 id(obj) 或对象默认哈希(不改 __eq__);缓存 key 用显式序列化字符串。4) 生产陷阱?——把可变对象当 key 后修改它;自定义类定义了 __eq__ 但字段可变;「缓存命中率偶发下降」的真相常常就是 key 漂移。
