---
title: [Q480] 字典合并语义:| 与 update 与展开
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q480 · 字典合并语义:| 与 update 与展开

> 难度:★★☆☆ | 标签:字典, PEP 584

**问**:d1 | d2、{**d1, **d2}、d1.update(d2) 三种合并,冲突键谁赢、顺序怎么算、是否原地?

**答**:冲突一律右侧赢(后写覆盖),但顺序语义有细节:结果键序是「左侧键按原顺序,右侧新增键追加在后」,冲突键保持左侧首次出现的位置。| 与 {**} 都生成新字典,区别是 {**} 可以一次摊平多个字典且值里的可变对象是浅拷贝引用;update 是原地修改、返回 None,这是它常被当表达式用而踩坑的原因。性能上 update 稍快(免建临时),| 最易读;需要「视图式合并、底层改动实时可见」时用 collections.ChainMap。

```python
# file: code/01_语言核心与底层/q480_dict_merge.py
base = {"a": 1, "b": 2, "c": 3}
override = {"b": 20, "d": 4}

if __name__ == "__main__":
    print(base | override)                # 右侧赢,新字典
    print({**base, **override})           # 等价,可混入更多字典
    print(override | base)                # 方向反了结果不同

    m = base.copy()
    result = m.update(override)           # 原地:返回 None
    print(result, m)
    print("base unchanged:", base)

    print(list((base | override).keys())) # 冲突键保持 base 的位置
    print(list((override | base).keys()))
```

**追问**:1) ChainMap 与 | 合并的本质区别?——ChainMap 是多层视图不拷贝数据,底层字典修改实时可见且查找从前往后;| 是一次性的快照拷贝,之后互不影响。2) 三个操作的冲突与顺序语义?——冲突一律右侧赢;结果键序是左侧原序+右侧新增追加,冲突键保留左侧首次位置;update 原地返回 None。方向写反(优先级高的放左边)会让默认值覆盖用户配置。3) | 的操作数限制?——PEP 584 要求两侧都是 dict 实例(子类可以);接受任意 Mapping 用 d |= mapping;ChainMap 写路径永远落在第一层映射。4) 生产陷阱?——`m = base.update(override)` 把 None 赋给 m 是经典笔误;多层合并链太长难调试,配置合并建议显式分层(默认→环境→实例)并留变更日志。
