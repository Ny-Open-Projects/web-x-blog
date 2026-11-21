---
title: [Q322] 大文件分块读取 chunksize
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q322 · 大文件分块读取 chunksize

> 难度:★★★ | 标签:pandas, 大文件

**问**:CSV 有 20GB 读不进内存怎么办?说明 chunksize 分块处理的模式。

**答**:用 `pd.read_csv(..., chunksize=n)` 返回迭代器,每个 chunk 是独立 DataFrame,循环中做"过滤 + 聚合"再合并部分结果,这是典型的 map-reduce 单机模式;配合 usecols 只读必要列、dtype 显式指定可进一步压内存。注意:跨 chunk 的去重、排序、join 不能简单分块,需要全局键或改用数据库/Polars/DuckDB。分块读取还应记录已处理的行号,便于失败重跑。

```python
# file: code/05_数据分析与工程化/q322_chunk_read.py
import csv
import os

def write_demo_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["city", "amt"])
        for city, amt in rows:
            w.writerow([city, amt])

def process_chunks(path, chunk_size=3):
    """map-reduce:逐块过滤聚合,最后合并部分结果。生产上用
    pd.read_csv(path, chunksize=chunk_size) 得到同样语义的迭代器。"""
    partial = {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                merge_partial(partial, chunk)
                chunk = []
        if chunk:
            merge_partial(partial, chunk)
    return partial

def merge_partial(partial, chunk):
    for r in chunk:
        partial[r["city"]] = partial.get(r["city"], 0) + float(r["amt"])

if __name__ == "__main__":
    try:
        import pandas as pd
        path = "demo_chunk.csv"
        write_demo_csv(path, [("BJ", 10), ("SH", 20), ("BJ", 5), ("SZ", 8)])
        total = {}
        for chunk in pd.read_csv(path, chunksize=2):   # 生产写法
            g = chunk.groupby("city")["amt"].sum()
            total = total.add(g, fill_value=0)
        print(total.to_dict())
        os.remove(path)
    except ImportError:
        path = "demo_chunk.csv"
        write_demo_csv(path, [("BJ", 10), ("SH", 20), ("BJ", 5), ("SZ", 8)])
        print(process_chunks(path))
        os.remove(path)
```

**追问**:
- 跨 chunk 去重怎么做?——维护全局已见键集合(或 Bloom/写临时表),chunk 内先去重再对全局集合过滤;纯分块无法全局去重。
- chunksize 取多大?——以单 chunk 内存 100-500MB 为限,先看列数与平均行长;过小则调度开销占比高。
- 分块算 mean 能直接平均各 chunk 均值吗?——不能,要按 sum/count 加权合并;分位数、去重计数这类非可加指标必须保留原始数据或换 HyperLogLog。

---
