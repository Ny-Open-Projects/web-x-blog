---
title: [Q346] Parquet 格式的优势
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q346 · Parquet 格式的优势

> 难度:★★★ | 标签:parquet, 存储

**问**:为什么数仓和分析场景偏爱 Parquet 而不是 CSV?列出关键技术优势。

**答**:Parquet 是列式存储 + 自描述 schema 的二进制格式。优势:①列式读取,查几列只解压几列,配合谓词下推和 row group 统计信息可跳过无关数据块;②内置压缩(通常比 CSV 小 5-10 倍)与编码(RLE/dictionary);③保留类型信息(int64/datetime/decimal),不存在 CSV 的类型解析歧义;④生态通用,Spark/DuckDB/Polars/pandas 直接读写。工程建议:分析型中间数据一律 parquet,CSV 只留给对外交付;大表按分区键(如 date)写分区目录。

```python
# file: code/05_数据分析与工程化/q346_parquet_advantage.py
import json
import os

def write_csv_like(rows, path):
    """模拟 CSV:全文本、无类型。"""
    with open(path, "w") as f:
        for r in rows:
            f.write(",".join(str(v) for v in r.values()) + "\n")

if __name__ == "__main__":
    try:
        import pandas as pd
        df = pd.DataFrame({"id": [1, 2, 3],
                           "ts": pd.to_datetime(["2026-01-01"] * 3),
                           "amt": [1.5, 2.5, 3.5]})
        df.to_parquet("demo.parquet")          # 需 pyarrow
        back = pd.read_parquet("demo.parquet", columns=["id", "amt"])  # 列裁剪
        print(back.dtypes.to_dict(), back.shape)   # 类型无损
        os.remove("demo.parquet")
    except ImportError:
        rows = [{"id": 1, "ts": "2026-01-01", "amt": 1.5}]
        write_csv_like(rows, "demo.csv")
        print("CSV 无类型:读到的都是字符串,需要重新解析")
        print(open("demo.csv").read())
        os.remove("demo.csv")
```

**追问**:
- 谓词下推在 Parquet 里怎么生效?——row group 统计信息(min/max)让引擎跳过整块数据;按 date 分区 + 排序写入能放大这个收益。
- 小文件问题怎么治理?——定时 compaction 合并,写入按分区攒批;小文件会让元数据与调度开销爆炸。
- CSV 转 Parquet 要注意什么?——显式指定 schema(避免类型推断歧义)、处理空值表示、压缩选 snappy(均衡)或 zstd(更小)。

```mermaid
flowchart LR
    A[分析场景存储选型] --> B{需求}
    B -->|分析查询 列裁剪| C[Parquet 列式 压缩 带类型]
    B -->|对外交换 通用性| D[CSV 或 Excel]
    C --> E[分区目录 date 城市]
    E --> F[Pruning 跳过无关分区]
```

---
