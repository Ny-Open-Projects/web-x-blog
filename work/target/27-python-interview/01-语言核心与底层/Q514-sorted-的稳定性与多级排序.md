---
title: [Q514] sorted 的稳定性与多级排序
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q514 · sorted 的稳定性与多级排序

> 难度:★★☆☆ | 标签:排序, 算法

**问**:Python 排序是稳定的,这在多级排序里怎么利用?负号 key 与 reverse 的差别?

**答**:sorted/list.sort 用 Timsort,相等元素保持原始相对顺序——多级排序的经典手法就是「从次级到主级连续排两次」:先按分数排,再按部门排,部门相同时分数序自动保留,而且比构造复合 key 更灵活(不同字段方向不同时尤其有用)。一次排序则用元组 key:(dept, -score);对不可取负的字符串做「同字段反向」用 reverse=True 但那会影响整级,跨字段混合方向时可用 functools.cmp_to_key 或先升后降两次排序。性能提示:key 函数每元素调一次,复杂 key 先算好存起来(装饰-排序-去装饰模式)。

```python
# file: code/01_语言核心与底层/q514_sorted_stability.py
rows = [
    {"dept": "sales", "name": "Carol", "score": 88},
    {"dept": "dev", "name": "Alice", "score": 92},
    {"dept": "dev", "name": "Bob", "score": 88},
    {"dept": "sales", "name": "Dave", "score": 92},
]

if __name__ == "__main__":
    # 多级排序:先按分数,再按部门(稳定性保留分数序)
    by_score = sorted(rows, key=lambda r: -r["score"])
    result = sorted(by_score, key=lambda r: r["dept"])
    for r in result:
        print(r)

    print("---")
    # 等价的单次复合 key
    result2 = sorted(rows, key=lambda r: (r["dept"], -r["score"]))
    print("two-pass equals composite key:", result == result2)
```

**追问**:1) list.sort 与 sorted 的内存差异?——sort 原地、临时空间 O(n)(Timsort 合并缓冲)且不分配新列表;sorted 对任意可迭代先物化一份,多一次列表拷贝。2) 稳定性怎么用于多级排序?——Timsort 稳定:相等元素保持原序;多键可从次要键到主要键分轮排序,或单轮 key 返回元组;reverse=True 同样保持稳定(不是先排后倒)。3) Timsort 的底层机制?——run 检测(升/降段)+ 归并,最好 O(n) 最坏 O(n log n);key 每元素只算一次(decorate-sort-undecorate),这是「key 预处理」优化的根据。4) 生产陷阱?——混类型排序 TypeError(3.x 不做跨类型比较);key 返回 None 或不可比字段;多级排序方向写错——应先按次要键升序排,再按主要键 reverse 排,而不是先主后次。
