---
title: [Q7097] 指标基数 cardinality 爆炸容量账
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7097 · 监控指标 cardinality（基数）爆炸容量账

难度：P6 ｜ 标签：可观测性 / Prometheus / 容量规划

**问**：接了 Prometheus 后监控成本每月翻倍，某服务一个 Counter 就贡献了几百万时序。指标基数怎么算容量？"把 user_id 加进 label"这类操作的实际代价是什么？

**答**：
- **结论**：时序数量 = 每个指标 × 所有 label 值组合的笛卡尔积。`http_requests_total{user_id=..., path=..., status=...}` 在百万用户、千路径、5 状态码下是 50 亿组合（实际是已出现过的组合数，但活跃序列数照样爆炸）。每条活跃时序在 Prometheus 里都有内存索引、每 15s 一个样本、在 TSDB 里占存储——基数爆炸的三笔账：内存（活跃序列 × 每序列 ~10KB 索引）、磁盘（序列数 × 样本频率 × 字节数 × 保留期）、查询延迟（聚合扫描的序列数）。规则：label 只放**有限低基数维度**（服务、实例、方法、状态码），用户级/请求级维度用 trace 或结构化日志承载，指标只做聚合面。
- **取舍**：发现基数爆炸后的处置：① 直方图/histogram bucket 数也是乘数（10 个 bucket × 其他维度翻 10 倍），能减就减；② 已泄漏的高基数指标直接下线比"修复"更实际（旧序列在 TSDB 里要活过保留期才消失）；③ 用 `tsdb status`/`top queries`（Prometheus 2.x 的 cardinality 分析 API）找出 top 序列贡献者。防泄漏机制：label 值白名单校验放在埋点 SDK 层，超白名单的值归一化为 `other`——把治理成本从"事后清库"提前到"埋点即约束"。
- **实战**：步骤：① 每服务上线前跑基数预估：`预估时序数 = Σ 每指标各 label 基数乘积`，超阈值（如单服务 50 万活跃序列）需评审；② 监控监控本身：`prometheus_tsdb_head_series`、`scrape_series_added` 设告警；③ 保留期与序列数联合定价：降采样规则（5m/1h 聚合层）让长保留只存聚合序列；④ 复盘项：新指标 PR 模板带"基数估算"字段。

```python
# 指标基数预估计算器（纯标准库）
# 基线：Python 3.9+

def series_estimate(metric: dict) -> int:
    """单指标时序数 = label 基数乘积"""
    est = 1
    for _, n in metric["labels"].items():
        est *= n
    return est


def storage_gb(
    active_series: int, interval_s: int = 15, retention_days: int = 30,
    bytes_per_sample: float = 2.0,
) -> float:
    """TSDB 压缩后磁盘账（近似：每样本 ~2 字节）"""
    samples = active_series * (86400 / interval_s) * retention_days
    return samples * bytes_per_sample / 1024 ** 3


def main() -> None:
    ok_metric = {"labels": {"service": 20, "path": 50, "status": 5}}
    bad_metric = {"labels": {"service": 20, "user_id": 1_000_000,
                             "status": 5}}
    good = series_estimate(ok_metric)
    bad = series_estimate(bad_metric)
    print(f"正常埋点: {good:,} 时序；user_id 入 label: {bad:,} 时序")
    assert good == 5000
    assert bad == 100_000_000
    # 100M 序列的磁盘账：按 15s 采 30 天 ≈ 5.2TB
    gb = storage_gb(100_000_000)
    print(f"爆炸序列磁盘 ≈ {gb:,.0f} GB")
    assert gb > 5000
    print("OK")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么已删除的高基数指标不会立刻释放存储？
→ 一句话提示：删除是墓碑标记，旧序列的数据块要等保留期滚动掉才物理消失；head block 里的索引也要等 compaction——所以治理要看"两周后"的曲线而不是删除即验证。

**追问 2**：trace 和 metric 的分工边界怎么划？
→ 一句话提示：metric 回答"多少、多快、多稳"（预聚合、低基数、可告警），trace 回答"这一次请求经历了什么"（高基数、按需采样）；把"每次请求"塞进 metric 等于用 TSDB 干 trace 的活，成本结构完全错配。

## 背诵要点
- 时序数 = label 基数笛卡尔积；user_id 级维度入 label 是成本事故之首，100M 序列 30 天 ≈ 5TB。
- label 白名单校验放在埋点 SDK 层（超限归一为 other）；基数预估要进上线评审。
- 三笔账：内存索引（活跃序列）、磁盘（序列 × 频率 × 保留期）、查询扫描延迟；处置先看 tsdb cardinality API 找 top 贡献者。

## 复盘追问
- 为什么 histogram 的 bucket 数也是基数乘数？提示：每个 bucket + sum + count 都是一条独立序列，10 bucket 的 histogram 在同一维度下时序数 ×12；桶边界设计要兼顾精度与成本。
- 降采样（5m/1h）为什么能救长保留成本？提示：长保留层只存聚合序列，原始高分辨率序列保留短窗口；代价是长周期查询失去毛刺细节，SLO 计算要确认聚合口径一致。
