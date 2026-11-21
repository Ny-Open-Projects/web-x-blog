---
title: [Q1801] slice 对象一等公民:复用、等价与 indices 求界
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1801 · slice 对象一等公民:复用、等价与 indices 求界

> 难度:★★★☆☆ | 标签:切片, 序列, API 设计

**问**:slice 不只是语法糖,作为对象它有哪些独立用法?

**答**:`obj[a:b:c]` 的真相是构造 slice(a, b, c) 传给 __getitem__,slice 因此是一等公民:① 具名切片让长表达式的切片语义集中定义——LAST_THREE = slice(-3, None) 可复用、可测试、可写进配置;② slice.indices(len) 把 None 与越界负号折算成合法的 start/stop/step,是手写分块、分页逻辑的官方工具,不必自己实现负索引规则;③ slice 可哈希、可进集合,operator.itemgetter(slice(1, 3)) 直接生成切片取值器,配合 map/sorted 很顺手(Q041 讲切片语法,本题讲对象形态)。等价性可验证:seq[2:8:2] 与 seq[slice(2, 8, 2)] 永远一致,框架层做「切片参数化」时靠这一等价性透传用户意图。

```python
# file: code/01_语言核心与底层/q1801_slice_object.py
"""slice 对象是一等公民:复用、等价与 indices 求界。"""
import operator


LAST_THREE = slice(-3, None)     # 具名切片:一处定义,处处复用


def apply_slice(seq, sl):
    return seq[sl]               # 等价于 seq[sl.start:sl.stop:sl.step]


def indices_bounding():
    # slice.indices(len) 把 None 与越界折算成合法的 start/stop/step
    return slice(2, 99).indices(5), slice(-2, None).indices(5)


def equivalence_check():
    seq = list(range(10))
    manual = seq[2:8:2]
    via_obj = seq[slice(2, 8, 2)]
    return manual, via_obj, manual == via_obj


def itemgetter_family():
    seq = [10, 20, 30, 40]
    return operator.itemgetter(slice(1, 3))(seq)   # 切片也能进 itemgetter


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    print("具名切片取最后三个:", apply_slice(data, LAST_THREE))
    print("indices 求界:", indices_bounding())
    print("手工切片与 slice 对象等价:", equivalence_check())
    print("itemgetter + slice:", itemgetter_family())
    print("slice 自身字段:", LAST_THREE.start, LAST_THREE.stop, LAST_THREE.step)
```

**追问**:1) slice(2, 99).indices(5) 返回什么?——(2, 5, 1),stop 99 被截到 5;slice(-2, None).indices(5) 得 (3, 5, 1),负号已折算。2) slice 一等公民的价值?——slice 对象可存、可复用、可比较;自定义容器的 __getitem__ 接 slice 参数时,indices(len) 是规范化边界的官方工具,免手写负号/越界逻辑。3) 等价与复用语义?——slice 对象支持 ==(逐字段)但不可哈希(含 None);预先定义的命名切片(STEP = slice(0, None, 2))提升可读性。4) 生产陷阱?——手写「if step < 0 ...」的边界推导(容易漏负 step);把 slice 当 dict key(不可哈希);对长度 0 的容器 indices 结果没做防御。
