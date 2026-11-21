---
title: [Q7022] 大表导出的 chunked Parquet 流水线
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7022 · 大表导出内存治理：单文件 DataFrame.to_parquet 为什么会 OOM？

> 难度:★★★★ | 标签:parquet, pandas, 数据导出

**问**：把 3 亿行日志表导出为 Parquet 给数仓，`df.to_parquet("out.parquet")` 在 16G 内存机器上 OOM。怎么设计一条"常量内存"的导出流水线？分片文件和单文件怎么选？

**答**：结论：OOM 根因是"全量读进内存再一次写出"——DataFrame 3 亿行的峰值内存是文件体积的 3-10 倍（列式压缩前要物化 Python 对象）。改造为**游标分块读 → 每块直接写 Parquet 文件（append 模式写 ParquetDataset / row group）→ 目录形态交付**，内存峰值 = 单块行数，与总量无关。2.x 里首选 `pyarrow.dataset.write_dataset` 的 `existing_data_behavior="overwrite_or_ignore"` 或 `ParquetWriter` 逐块写 row group。

取舍与实战：
- 单文件 vs 分片：单文件多 row group 可以（ParquetWriter 持续 append row group），下载友好；分片目录并行消费友好、坏一块不影响整批。数仓（Spark/ClickHouse）通常更爱目录形态 + `_SUCCESS` 完成标记。
- 分块大小：行宽 × 行数控制在 128-256MB 内存水位；块太小文件碎片化 row group 过多反而伤读取性能（每个 row group 至少 ~64MB 落盘）。
- 元数据陷阱：目录形态下每个分片自带 schema，中途 schema 漂移（上游加列）会产生不兼容分片——导出前先做一次 `SELECT ... LIMIT 1` 校验列集合，或写 `_schema.json` 快照；pq 读侧用 `dataset(schema=...)` 强校验。

```python
# 基线:Python 3.9+ / pyarrow 10+ / pandas 2.x ;缺 pyarrow 降级为 CSV 分块流
from dataclasses import dataclass

try:
    import pyarrow as pa
    import pyarrow.parquet as pq
    HAS_PA = True
except ImportError:
    HAS_PA = False


@dataclass
class ExportReport:
    rows: int
    parts: int
    schema_drift: bool = False


def stream_to_parquet(row_chunks, out_dir: str, batch_rows: int = 100_000) -> ExportReport:
    """常量内存导出:每块物化一个分片文件,内存峰值=单块。"""
    import os
    os.makedirs(out_dir, exist_ok=True)
    writer = None
    rows = parts = 0
    base_schema = None
    buf: list = []
    for chunk in row_chunks:
        buf.append(chunk)
        rows += len(chunk)
        if sum(len(c) for c in buf) < batch_rows:
            continue
        tbl = pa.Table.from_pylist([r for c in buf for r in c])
        if base_schema is None:
            base_schema = tbl.schema
        elif tbl.schema != base_schema:
            tbl = tbl.cast(base_schema)          # 漂移即对齐,强 schema
        pq.write_table(tbl, f"{out_dir}/part-{parts:05d}.parquet")
        parts += 1
        buf = []
    if buf:
        tbl = pa.Table.from_pylist([r for c in buf for r in c])
        pq.write_table(tbl, f"{out_dir}/part-{parts:05d}.parquet")
        parts += 1
    return ExportReport(rows=rows, parts=parts)


def demo_csv_fallback() -> None:
    """缺 pyarrow 的降级:CSV 分块流式写,同样常量内存。"""
    import csv
    rows = ({"id": i, "val": i * 2} for i in range(1000))
    n = 0
    with open("/tmp/export_demo.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "val"])
        w.writeheader()
        for r in rows:
            w.writerow(r)
            n += 1
    print("CSV 降级导出行数:", n)


if __name__ == "__main__":
    if HAS_PA:
        chunks = ([{"id": i, "val": str(i)} for i in range(k, k + 50)]
                  for k in range(0, 300, 50))
        rep = stream_to_parquet(chunks, "/tmp/pq_export_demo")
        print("导出报告:", rep)
        ds = pq.read_table("/tmp/pq_export_demo/part-00000.parquet")
        print("回读首分片:", ds.num_rows, "行")
    else:
        demo_csv_fallback()
```

**追问一**：为什么不用 `to_parquet(partition_cols=...)` 一次写完？
答：它内部仍是全量物化 Table；数据在内存放不下时同样 OOM。分块写的前提是"块级物化、写完即释放"，pandas 的 partition 写 API 不满足块级流式语义。

**追问二**：导出中途失败怎么办？
答：分片文件是天然断点——重跑前按文件名序号续传（已有分片跳过），整批完成后写 `_SUCCESS` 标记，下游以 `_SUCCESS` 存在为可读信号。这正是"目录 + 完成标记"比单文件稳的原因：单文件中途坏掉只能整废。

**背诵要点**：
- OOM 根因是全量物化，解法是游标分块 + 块级写 Parquet 分片，内存峰值=单块。
- 分片目录 + `_SUCCESS` 标记：断点续跑、并行消费、坏片不影响整批。
- schema 漂移在导出层强校验（cast 或拒绝），防目录内混入不兼容分片。

**复盘追问**：
- row group 大小对下游 Spark 读取并行度的影响是什么？
- 如何在导出流水线里做行级 checksum 以支撑导出前后对账？

## 背诵要点
- ParquetWriter 逐块 append 与 write_dataset 分片是两条常量内存路径。
- 分块水位 128-256MB，row group 过小伤列存读取性能。
- 完成标记 + 分片序号 = 导出任务的断点续跑协议。

## 复盘追问
- 若下游要求严格单文件，如何用合并步骤在导出后低峰期聚合成单文件？
- 导出 schema 演进（加列）时目录内新旧分片如何兼容读取？
