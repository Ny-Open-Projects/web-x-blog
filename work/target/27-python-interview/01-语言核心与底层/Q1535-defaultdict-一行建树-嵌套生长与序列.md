---
title: [Q1535] defaultdict 一行建树:嵌套生长与序列化清洗
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1535 · defaultdict 一行建树:嵌套生长与序列化清洗

> 难度:★★☆☆☆ | 标签:defaultdict, 分组, collections

**问**:defaultdict 除了分组还能干什么?怎么用它一行造出嵌套树?序列化前要做什么?

**答**:defaultdict 的工厂返回容器就能「一行建树」:`tree = lambda: defaultdict(tree)` 让任意深度的缺键访问自动生长,配合 defaultdict(list) 建邻接表、defaultdict(int) 计数,是分组与索引场景的最短路径(Q479 讲默认值模式与读长键副作用,本题聚焦建树与清洗)。两个工程纪律:① 读取副作用——访问不存在的键会真的写入,试探性读取留下幽灵键,遍历/序列化前必须清洗;② 序列化前递归洗回普通 dict(本文 wash),否则 pickle 的 lambda 工厂必炸、类型断言与 JSON 之外的工具链都会踩到实现细节。需要「读不建键」时改用 d.get;需要「读写都显式」用 setdefault。

```python
# file: code/01_语言核心与底层/q1535_defaultdict_tree.py
import json
from collections import defaultdict


def tree():
    return defaultdict(tree)


def wash(node):
    """把嵌套 defaultdict 递归洗回普通 dict,便于 JSON 与断言。"""
    return {key: wash(child) if isinstance(child, dict) else child
            for key, child in node.items()}


if __name__ == "__main__":
    index = tree()
    index["docs"]["q1526"]["title"] = "loop else"    # 任意深度缺键自动生长
    index["docs"]["q1527"]["title"] = "try else"
    index["meta"]["count"] = 45
    print("nested access:", index["docs"]["q1526"]["title"])

    # 分组:邻接表一行建
    edges = [("a", "b"), ("a", "c"), ("b", "d")]
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    print("adjacency:", dict(adj))

    # 计数桶
    counter = defaultdict(int)
    for ch in "mississippi":
        counter[ch] += 1
    print("count:", dict(counter))

    # 反面:读也会长键,ghost 键污染结构
    _ = index["ghost"]["deeper"]
    print("ghost leaked:", "ghost" in index)

    clean = wash(index)
    del clean["ghost"]                                # 洗净前删掉误访问
    print("json roundtrip:",
          json.dumps(clean, ensure_ascii=False, sort_keys=True))
```

**追问**:1) defaultdict 的工厂会被 pickle 吗?——工厂必须是可按名找到的对象,lambda 工厂 pickle 必炸;序列化前 wash 回普通 dict 是最稳的做法。2) 一行建树的机制?——tree = lambda: defaultdict(tree),子节点按需生长;递归工厂引用自身,无限深度——所以「读不存在的路径」会静默长出键,要用 in 探测(Q479)。3) 序列化清洗?——递归把 defaultdict 转普通 dict(工厂自然剥离);json.dumps 对 defaultdict 能工作(dict 子类)但 pickle 会携带工厂;往回读是普通 dict,行为退化。4) 生产陷阱?——探测性访问污染树结构;lambda 工厂进 pickle/multiprocessing 崩;wash 递归爆栈(深树,配合 Q1299 限深)。
