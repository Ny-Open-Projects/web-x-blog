---
title: [Q2623] functools.cmp_to_key 的复杂排序:比较器思维的正确出口
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2623 · functools.cmp_to_key 的复杂排序:比较器思维的正确出口

> 难度:★★★☆☆ | 标签:排序, cmp_to_key, functools

**问**:key 函数表达不了的排序规则怎么办?cmp_to_key 什么时候用?

**答**:Python 3 删掉了 cmp 参数,`functools.cmp_to_key` 是官方桥:把「返回负数/零/正数」的两两比较器包成可做 key 的对象,`sorted` 内部对每个元素包一层 K 实例,用 `__lt__` 委托回比较器。适用场景是 key 函数无法表达的**非全序或跨字段耦合**规则:比如「部门升序、同部门内工号降序」虽然能用多级 key(取负数)技巧实现,但字符串无法取负,就得用比较器;再如字典序里混着数字需要数值序的场景。注意成本:每对元素一次 Python 层比较器调用,比 C 级 key 快排慢一个量级,数据量大时优先想办法把规则拆成可 key 的元组(借助 `sorted` 的稳定性做多次排序是零成本的替代)。

```python
# file: code/01_语言核心与底层/q2623_cmp_to_key.py
"""cmp_to_key:比较器排序与「多次稳定排序」替代方案的对照。"""
import functools

rows = [("dev", "10"), ("qa", "9"), ("dev", "2"), ("ops", "100")]


def by_dept_then_num(a, b):
    """部门升序;同部门内按数值降序(字符串没法取负,必须比较器)。"""
    if a[0] != b[0]:
        return -1 if a[0] < b[0] else 1
    return int(b[1]) - int(a[1])


if __name__ == "__main__":
    print("cmp_to_key:", sorted(rows, key=functools.cmp_to_key(by_dept_then_num)))

    # 替代方案:利用 sorted 稳定性,从次要键到主要键排两遍
    staged = sorted(rows, key=lambda r: -int(r[1]))
    staged = sorted(staged, key=lambda r: r[0])
    print("稳定排序:", staged)

    # 数值序排字符串,key 一层就够,不必上比较器
    nums = ["10", "9", "2"]
    print("数值序:", sorted(nums, key=int))
```

**追问**:1) cmp_to_key 包装后的对象支持什么比较?——它生成一个实现 `__lt__`/`__gt__` 等全 family 的 K 类,把每个比较都翻译成对原比较器的调用,所以任何依赖比较的函数都能吃它。2) 何时才该用?——比较逻辑无法表达成 key(非对称规则、跨字段复杂裁决)时;能写 key 的一律 key(decorate-sort-undecorate,每元素算一次);cmp 每对比较都调 Python 函数,数量级更贵。3) 与 stability 的关系?——sorted 稳定性在 cmp_to_key 下仍然成立;多级裁决可在比较器内完成;与 itemgetter 组合按需降级(Q2624)。4) 生产陷阱?——能用 key 的用 cmp(性能);比较器不满足全序(NaN/不一致规则)让排序结果不可预测;比较器抛异常中断排序。
