---
title: [Q2362] walrus 的循环用法:边读边判
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2362 · walrus 的循环用法:边读边判

> 难度:★★★☆☆ | 标签:walrus, 循环, 3.8 新特性

**问**:=: 在循环里最值得用的三个场景是什么?

**答**:walrus 的价值是把「计算一次、使用两处」压进表达式,循环里有三个高频场景。一是读-判循环:`while (chunk := read()) is not None:` 把赋值和判空合并,消灭「先读一次、循环尾再读一次」的重复代码;二是推导式过滤:`[t for v in data if (t := f(v)) > 0]`,f(v) 只算一次,旧写法要么算两遍要么套两层循环;三是分支预计算:`if (m := pattern.match(s)) is not None:` 直接拿匹配对象,省掉 match 与 group 之间的中转变量。边界也要清楚:walrus 让代码变密,一行塞太多赋值会伤可读性,团队规范常限制每行至多一个 :=;它绑定到最近的作用域,推导式里用要意识到变量会「漏」到外层函数作用域,别与循环变量重名。

```python
# file: code/01_语言核心与底层/q2362_walrus_loop.py
"""walrus 的循环用法:边读边判,避免重复计算。"""
import random


def fetch_chunk():
    """模拟流式读取:None 表示流结束。"""
    return random.choice([None, "", "data-1", "data-2"])


if __name__ == "__main__":
    random.seed(42)

    chunks = []
    while (chunk := fetch_chunk()) is not None:
        chunks.append(chunk)
    print("读到的块:", chunks)

    values = [3, -1, 7, 0, -5, 8]
    big = [trimmed for v in values if (trimmed := abs(v)) > 4]
    print("推导式内 walrus:", big)
    print("旧写法等价(abs 算两遍):", [abs(v) for v in values if abs(v) > 4])

    buckets = {}
    for v in values:
        k = "正" if v > 0 else "非正"
        buckets.setdefault(k, []).append(v)
    print("分组:", buckets)
```

**追问**:1) while (chunk := read()) 为什么必须 is not None 而不是真值判断?——空串、0、空列表都是合法数据但为假,真值判断会提前断流;哨兵语义的比较必须用 is/is not None。2) walrus 的循环模式?——读-判一体:while (chunk := f.read(size)):、first = (m := re.search(p, s)) and m.group();表达式赋值减少重复调用。3) 与 for 的分工?——for 管「已知集合」,walrus while 管「读到哨兵/条件」;readline 循环、socket recv 都是 walrus 主场。4) 生产陷阱?——真值判断吃掉合法 falsy 数据(本题核心);walrus 嵌套过深可读性;海象变量泄漏到外层作用域(它就是普通局部名)。
