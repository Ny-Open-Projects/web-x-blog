---
title: [Q7558] Agent trace 的存储成本治理：采样与分级保留
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7558 · Agent trace 的存储成本治理：采样与分级保留

难度：P6 | 标签：可观测性、trace 采样、成本工程、分级保留

**问**：Agent 平台每百万任务/月，全量 trace 存储要 50GB 且 90% 从来没人查过。trace 该不该全量存？head 采样和 tail 采样的区别是什么？分级保留怎么把成本压到 15% 而不丢 badcase？

**答**：
- **结论**：全量存 trace 是"用存储费买安全感"——查得着的才有价值。正确姿势是 tail-based 采样：失败请求与慢请求（P99 之上）100% 保留（badcase 复现能力是 trace 的核心价值），成功请求按 head 比例采样（本例 10%）——保留比例 15%，存储从 50GB/月降到 7.3GB/月。分级保留再砍一刀：热存储 7 天（全字段可查询，复盘高频期）、温存储 30 天（压缩、按需加载）、冷归档 180 天（合规审计）。组合后月成本降到全量热存的 15%。
- **取舍**：tail 采样的实现代价是"延迟决定"：一条 trace 要等任务结束才能判定去留（需要缓冲），不像 head 采样在入口就决定。牺牲品是"成功请求的 debug 覆盖"——偶发的、只在成功请求里出现的问题（如静默数据错误）可能没被采到，缓解手段是把"用户负反馈的任务"（点踩）从冷归档捞回，负反馈是比"慢/错"更全的坏样本信号。
- **实战**：落地清单：① 采样策略配置化（错误/慢/点踩三类 tail 规则 + head 比例）；② trace 记录保留策略版本，防止"归档里的数据不知道按什么规则删过"；③ 月度复盘"存储成本 vs badcase 复现率"——采样策略调参的依据是复现率不掉。

```python
"""Agent trace 的存储成本治理：tail-based 采样与分级保留。"""
from dataclasses import dataclass

@dataclass
class TracePolicy:
    head_sample: float = 0.1             # head 采样：普通请求只留 10%
    keep_latency_p99_s: float = 30.0     # tail 规则：慢请求全留
    keep_errors: bool = True             # 失败请求全留
    hot_days: int = 7                    # 热存储：全字段可查询
    warm_days: int = 30                  # 温存储：压缩、按需加载
    archive_days: int = 180              # 冷归档：审计留存

policy = TracePolicy()

TASKS_PER_MONTH = 1_000_000
KB_PER_TRACE = 50
full_gb = TASKS_PER_MONTH * KB_PER_TRACE / 1e6

# tail-based 采样：错误与慢请求全保，其余按 head 比例
error_rate, slow_rate = 0.03, 0.02
kept_ratio = error_rate + slow_rate + (1 - error_rate - slow_rate) * policy.head_sample
kept_gb = full_gb * kept_ratio
print(f"全量 trace {full_gb:.0f} GB/月 -> tail 采样后 {kept_gb:.1f} GB/月"
      f"（保留比例 {kept_ratio:.0%}：错误与慢请求 100%，其余 {policy.head_sample:.0%}）")

# 分级保留的价格账（热/温/冷典型比价 1 : 0.4 : 0.1）
hot_gb = kept_gb * policy.hot_days / 30
warm_gb = kept_gb * (policy.warm_days - policy.hot_days) / 30
cold_gb = kept_gb * (policy.archive_days - policy.warm_days) / 30
cost = hot_gb * 0.023 + warm_gb * 0.0092 + cold_gb * 0.0023
print(f"分级保留月成本 ≈ ${cost:.2f}（全量热存同周期 ≈ ${full_gb * 0.023:.2f}，"
      f"降为 {cost / (full_gb * 0.023):.0%}）")
print("关键取舍：tail 规则保住了 badcase 复现能力（错误/慢请求从不丢）；"
      "head 采样只牺牲'成功请求的 debug 覆盖'——这是查询覆盖率与存储成本的核心权衡")
```

**追问链**：
1. 追问一层：为什么"失败与慢请求全保"是采样策略的底线？——trace 的第一价值是复现问题；问题样本（错误/慢/被用户点踩）在总量里占比小（本例 5%）但信息密度极高，砍它们省的钱少、丢的复盘能力大。head 采样砍的是低密度的大多数（成功请求），成本收益比完全不同。
2. 追问二层：分级保留的"热 7 天"边界怎么定？——复盘窗口决定：绝大多数 badcase 在发生后一周内被排查（工单时效），7 天外的查询需求稀疏到可以接受"分钟级加载"（温存储）。边界看本团队的平均排查时长分布（P90 排查耗时），而不是拍一个通用数字。

**背诵要点**：
1. trace 的价值在查得着：tail 采样保错误/慢请求 100%，成功请求 head 采样，保留比例可到 15%。
2. 分级保留：热 7 天全字段可查、温 30 天压缩、冷 180 天审计，月成本降到全量热存的 15%。
3. 用户点踩是 tail 规则的补充信号——成功但错的请求靠它捞回。

**复盘追问**：
1. 有个 badcase 是"成功返回但内容错了"，trace 里查不到，为什么？（head 采样把它丢了；补救靠用户负反馈通道把该任务从冷归档/供应商日志捞回，并把"点踩必留"加进采样策略）
2. 为什么采样策略要配置化并记录版本？（排障时必须知道"这条 trace 为什么在/不在"——策略变更后历史数据的覆盖含义不同；没有版本记录，采样本身的变更会成为排查的迷雾）
