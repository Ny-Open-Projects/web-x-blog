---
title: [Q7084] Polars 流式引擎的内存预算容量账
date: 2026-11-20
categories: [Python数据分析与工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7084 · Polars 流式引擎的内存预算容量账

难度：P6/P7 ｜ 标签：Polars / 内存容量 / 数据处理

**问**：pandas 处理 50GB 日志表会 OOM，团队想换 Polars。Polars 就不会 OOM 吗？做内存预算时要怎么算？

**答**：
- **结论**：Polars（基线 1.x）的 Rust 引擎按列存 chunk 处理，同样的 join/聚合比 pandas 省内存 3-10 倍，但它默认仍是"内存内"执行——50GB 表全量 load 后做无界 join 照样 OOM。真正的解法是流式/惰性执行：`scan_parquet` + `LazyFrame` + `streaming=True`（旧）或新版 streaming engine，让引擎按批流动数据、谓词下推（只读需要的列与行组），峰值内存取决于"批大小 × 并行度 × 状态大小"，而不是整表大小。
- **取舍**：换 Polars 不是免费午餐：① API 与 pandas 不同，团队迁移有学习成本（expression 语法、无 SettingWithCopy 类问题）；② 生态兼容缺口（某些 sklearn 上下游工具链仍要 pandas 转换，转换本身是内存峰值点）；③ 流式引擎对某些操作（全局 sort、无界 join）仍需物化，预算要按这些算子单列。
- **实战**：预算公式：`峰值内存 ≈ Σ(流式批内存) + 物化算子输入/输出 + 线程并行度放大`。工程守门：① 先 `scan_parquet(...).select_schema()`/`collect_schema()` 与谓词投影，只读必要列；② join 前对大表做 key 分桶；③ 容器内存限制按峰值 1.5 倍留 headroom，并用 `POLARS_MAX_THREADS` 控并行（每线程一个批的内存）。写个守门脚本在 CI 用 1% 采样数据估峰值，超出配额直接拒绝合并。

```python
# 用 1% 采样外推内存预算的守门模拟（纯标准库）
# 基线：Python 3.9+
# 说明：Polars 未安装也可运行；实际项目用 df.estimated_size() 获取列存字节

ROW_BYTES = {"user_id": 8, "ts": 8, "event": 20, "payload": 60}


def projected_bytes(schema: dict[str, int], columns: list[str], rows: int) -> int:
    return rows * sum(schema[c] for c in columns)


def peak_budget(total_rows: int, columns: list[str], batch_ratio: float = 0.02,
                threads: int = 8, headroom: float = 1.5) -> int:
    streaming = projected_bytes(ROW_BYTES, columns, int(total_rows * batch_ratio)) * threads
    return int(streaming * headroom)


def main() -> None:
    total = 500_000_000
    need = ["user_id", "ts", "event"]
    full = projected_bytes(ROW_BYTES, ["user_id", "ts", "event", "payload"], total)
    est = peak_budget(total, need)
    print(f"全列物化≈{full/2**30:.0f}GB, 流式峰值预算≈{est/2**30:.1f}GB")
    assert est < full / 10  # 投影+流式预算应远小于全量
    # CI 守门：容器限额 16GB
    limit = 16 * 2**30
    print("限额内?" , est < limit)
    assert est < limit


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"谓词下推 + 列投影"对流式执行如此关键？
→ 一句话提示：Parquet 行组级统计让引擎跳过整块数据、只读需要的列，I/O 与内存同时下降一个量级，是流式预算成立的前提。

**追问 2**：全局 sort 在流式引擎下会怎样？
→ 一句话提示：排序需要看到全部数据，无法真正流式，引擎会物化（外排或全内存），预算按整表投影大小算，或改用分桶+桶内排序绕开。

## 背诵要点
- Polars 默认也是内存内执行；流式（LazyFrame + streaming engine）峰值 = 批 × 并行度 × 状态，与整表无关。
- 预算三因子：列投影裁剪、流式批大小、线程并行度（POLARS_MAX_THREADS），容器限额按峰值 1.5 倍。
- 物化算子（全局 sort/无界 join）单列预算，或分桶改造绕开。

## 复盘追问
- 为什么 pandas→Polars 迁移时"中间转 pandas"环节容易重新 OOM？提示：to_pandas 是全量物化，峰值等于整表，应在边界处保持 Arrow/Polars 格式。
- 如何用 CI 防止以后任务悄悄超内存配额？提示：1% 采样估峰值 + 限额断言进单测，超配额拒绝合并。
