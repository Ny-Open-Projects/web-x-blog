---
title: [Q7106] Parquet 行组大小与内存吞吐的容量账
date: 2026-11-21
categories: [Python数据分析与工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7106 · Parquet 行组（row group）大小与内存/吞吐的容量账

难度：P6 ｜ 标签：Parquet / 容量规划 / 存储格式

**问**：数据组把导出 Parquet 的行组从默认改成 1000 行"为了小批次流式读"，结果查询平台的扫描 P99 从 800ms 恶化到 12s，对象存储请求费也翻了几倍。行组大小到底怎么定？这笔容量账怎么算？

**答**：
- **结论**：行组（row group）是 Parquet 的**并行与 IO 调度单元**：读端一次至少读一个行组的 column chunk，谓词下推/统计裁剪也以行组为单位。行组过小（几千行）导致：① 元数据占比暴涨（每个行组每列都存 min/max 统计与页头），文件里"说明书比数据厚"；② 对象存储的 GET 请求数暴涨（按请求计费）且每个请求都要 TLS/重试开销；③ 下游引擎并行度失控（每个行组一个 task，调度开销淹没计算）。行组过大（如 1 亿行）则单行组内存装不下、流式读失去意义、写端缓冲占用大。主流实践：**行组 128MB-1GB（约 10 万-100 万行，视列宽），Parquet 页 1MB 左右**，配合 HDFS block/对象存储聚合上传对齐。
- **取舍**：三个参数联动：① 行组大小决定内存与 IO 粒度——写端 `row_group_size`（行数）或按字节估算 `row_group_size ≈ 目标行组字节 / 每行均宽`；② 每行组压缩后 ~128MB 在大多数查询引擎（DuckDB/Spark/Polars）的甜点区；③ 小行组并非全错——极宽表（几千列）或流式逐批消费场景可以到 1 万-10 万行，但必须重新算"元数据占比"账：`元数据占比 = 每行组开销 × 行组数 / 文件总字节`，超过 5% 就是过量。对象存储场景还要算请求费账：`GET 请求数 = 文件数 × 每文件 column chunk 数`。
- **实战**：容量账四步：① 采样算每行压缩后均宽（各列 `column_statistics` + 压缩比）；② 定行组字节目标（128MB）反推行数；③ 回算三个账：元数据占比、GET 请求费、写端内存峰值（`行组字节 × 并发写线程`）；④ 用查询平台对三种配置做基准（扫描 P99 + 裁剪率），选"裁剪率不降、P99 最优"的组合。注意 `pyarrow.parquet.ParquetWriter` 是按 `write_table` 调用边界切行组，流式写入时要攒批再写，别每批一个小行组。

```python
# Parquet 行组容量账：均宽采样 → 行组行数 → 元数据/请求费/写内存三账（标准库模拟）
# 基线：Python 3.9+；真实测量用 pyarrow 14+ 读 ParquetMetadata

from dataclasses import dataclass


@dataclass
class ParquetPlan:
    rows_total: int
    avg_row_compressed_bytes: float   # 每行压缩后均宽（实测采样）
    target_rg_mb: float = 128.0       # 行组字节目标
    rg_overhead_bytes: float = 64_000 # 每行组元数据开销（统计/页头，实测估）

    def row_group_rows(self) -> int:
        return int(self.target_rg_mb * 1024**2 / self.avg_row_compressed_bytes)

    def accounts(self) -> dict[str, float]:
        rg_rows = self.row_group_rows()
        n_rg = -(-self.rows_total // rg_rows)
        total_bytes = self.rows_total * self.avg_row_compressed_bytes
        meta_ratio = (self.rg_overhead_bytes * n_rg) / total_bytes
        # DuckDB/对象存储按 column chunk GET：假设 10 列
        get_reqs = n_rg * 10
        write_mem_mb = self.target_rg_mb * 4   # 4 并发写线程
        return {"rg_rows": rg_rows, "n_rg": n_rg, "meta_pct": meta_ratio * 100,
                "get_reqs_per_file_scan": get_reqs, "write_mem_mb": write_mem_mb}


def main() -> None:
    # 正常配置：均宽 130B，1 亿行
    plan = ParquetPlan(rows_total=100_000_000, avg_row_compressed_bytes=130)
    acc = plan.accounts()
    assert 600_000 < acc["rg_rows"] < 1_200_000
    assert acc["meta_pct"] < 5, f"元数据占比 {acc['meta_pct']:.2f}% 应达标"
    print(f"行组 {acc['rg_rows']} 行（≈{plan.target_rg_mb}MB），文件 {acc['n_rg']} 个行组")

    # 事故配置：1000 行行组 → 元数据暴涨百倍、GET 请求暴涨
    rg_rows_bad = 1000
    n_rg_bad = 100_000_000 // rg_rows_bad
    meta_pct_bad = 64_000 * n_rg_bad / (100_000_000 * 130) * 100
    get_reqs_bad = n_rg_bad * 10
    assert meta_pct_bad > 5 and meta_pct_bad > acc["meta_pct"] * 100, \
        f"小行组元数据占比 {meta_pct_bad:.1f}% vs 正常 {acc['meta_pct']:.3f}%"
    print(f"事故配置：行组 1000 行 → 元数据占比 {meta_pct_bad:.1f}%（正常配置的 "
          f"{meta_pct_bad / acc['meta_pct']:.0f} 倍），单次扫描 GET {get_reqs_bad:,} 次")
    print("OK: 行组账三指标——元数据占比 / GET 请求数 / 写端内存峰值")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"小行组利于谓词下推"是误解？
→ 一句话提示：下推粒度变细听起来更精准，但每个行组的统计都是元数据要读，行组太碎时读元数据的开销与 GET 次数吞掉了裁剪收益；真实收益靠把数据按查询维度**排序/聚簇**（配合 ZSTD + min/max 跳跃）而非切碎行组。

**追问 2**：流式写入 Parquet 怎么避免"每批一个行组"？
→ 一句话提示：用 ParquetWriter 攒批——内存里凑满目标行组行数再 `write_table`；凑不满时用 `writer.close()` 收尾小行组；或干脆改走"按小时分区 + 定期 compaction 小文件合并"（见 Q7089 小文件治理）。

## 背诵要点
- 行组是并行/IO/下推的调度单元：目标 128MB-1GB（约十万到百万行），页 ~1MB；过小则元数据占比与 GET 请求暴涨，过大则内存与流式失效。
- 账目三指标：元数据占比 <5%、单扫描 GET 请求数、写端内存峰值 = 行组字节 × 并发线程。
- pyarrow 按调用边界切行组：流式写要攒批；下推收益靠排序聚簇，不靠切碎行组。

## 复盘追问
- 怎么实测每行压缩后均宽？提示：写一个 1 万行样本文件，读 `parquet_file.metadata.row_group(0).total_byte_size` 除以行数，再按分区/时间抽样复核；样本要覆盖宽行（长字符串列）的分布。
- 查询平台的"裁剪率"指标怎么定义？提示：被 min/max/分区统计裁剪掉的行组占比 = (1 - 扫描行组/总行组)，是验证聚簇与行组配置有效性的核心指标。
