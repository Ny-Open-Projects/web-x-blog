---
title: [Q1265] dict 视图对象:keys/values/items 是动态窗口
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1265 · dict 视图对象:keys/values/items 是动态窗口

> 难度:★★☆☆☆ | 标签:dict, 视图

**问**:`d.keys()` 返回的是列表吗?持有它,原字典后来加了键,视图会变吗?

**答**:keys/values/items 返回的是视图对象(view),不是快照:它动态反映字典当前状态,后续增删改立即可见,len 与 in 都是 O(1)。keys 视图实现集合协议,可以直接做 `&`、`|`、`-` 运算,这也是「求两个字典公共键」的地道写法;items 视图支持按 `(key, value)` 元组迭代,是同步遍历键值的标准姿势。反过来,视图是原字典的从属物:字典在视图存活期间被修改,正在进行的迭代会抛 RuntimeError(和直接迭代字典一样);需要与修改隔离时,用 `list(d.items())` 显式拷贝快照。

```python
# file: code/01_语言核心与底层/q1265_dict_views.py
if __name__ == "__main__":
    d = {"a": 1, "b": 2}
    keys, items = d.keys(), d.items()
    print("len before:", len(keys))
    d["c"] = 3                        # 视图动态跟随
    print("len after :", len(keys), "| 'c' in keys:", "c" in keys)
    print("set op keys & {a,z}:", keys & {"a", "z"})
    d["b"] = 20
    print("items reflect updates:", sorted(items))
    snapshot = list(items)            # 需要隔离时才拷贝
    d["d"] = 4
    print("snapshot stays:", len(snapshot), "| live now:", len(items))
```

**追问**:1) 为什么 values 视图不支持集合运算?——它没有键可判等,两个 value 相同无法定义集合语义,所以 Python 只给 keys 与 items(键唯一可作集合)实现了 Set 协议。2) 视图的动态性意味着什么?——视图是底层 dict 的实时窗口,dict 修改视图立即反映;遍历视图时修改 dict 抛 RuntimeError(size changed),需要快照就先 list(view)。3) 底层协议?——KeysView/ItemsView 注册为 collections.abc.Set(动态集合,支持 & | -),ValuesView 只是 Collection;视图轻量不拷贝数据。4) 生产陷阱?——把 items 视图当持久集合缓存(dict 变了它跟着变);遍历中增删键;「快照遍历」与「动态遍历」语义混用出隐蔽 bug。
