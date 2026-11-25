---
title: [Q7122] ETL worker 数与上游限流的容量匹配账
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7122 · ETL worker 数与上游限流的容量匹配账

难度：P6 ｜ 标签：容量规划 / ETL / 限流

**问**：ETL 从外部 API 拉数（上游限流 100 req/s），当前 8 个 worker 串行拉取，单请求 300ms，全量拉取要 6 小时，经常赶不上下游窗口。扩 worker 能提速到哪？什么瓶颈会先出现？"加机器"和"申请配额"哪边先做？

**答**：
- **结论**：先算上限：上游限流 100 req/s 是**硬天花板**——当前吞吐 = worker 数 / 单请求时延 = 8/0.3 ≈ 27 req/s，远低于天花板；理论上扩到 30 worker 贴满配额（约 1.7h 跑完），工程上按配额 0.8 留余量（24 worker，约 2.1h）。但“加 worker”之前要过三道检查：① **限流余量归属**——100 req/s 是全租户共享还是本任务独享？共享的话你打满会挤压同租户其他业务，必须先申请专属配额而不是抢；② **瓶颈次序**——worker 加到贴限后，下一瓶颈常是：下游 DB 写入吞吐（Q6519 批量写）、本机出口带宽/连接数（Q6536 短连接爆炸同源）、上游分页的扫描效率（拉了不用或重复拉）；③ **429 处理**——贴限运行必然触发限流响应，退避策略必须存在且尊重 Retry-After，否则重试流量让有效吞吐更低（Q7541 重试风暴同源）。容量账公式化：目标时间 T → 需要吞吐 = 数据量/T；瓶颈 = min(配额, worker数/时延, 写入吞吐)；扩容对象 = 当前最小的那一项。
- **取舍**：先申请配额还是先加 worker？判断标准：当前吞吐是否已接近配额——27/100 说明离配额远，**先加 worker**（零谈判成本、当天见效）；加到接近配额还有缺口才谈配额（商务/审计周期长）。如果配额是共享的，加 worker 前先做"租户内配额隔离"评估，或主动降速到安全水位并接受追赶窗口拉长（Q7096 ETL 积压账同源）。另一个不花钱的优化次序：先降单请求时延（并发连接、批量端点、字段裁剪）与减少无效拉取（增量水位），常常等效于"白捡一半 worker"。
- **实战**：落地：① 拉取层统一限流器（令牌桶按配额 0.8 运行），worker 数只是消费者——限流是全局的而不是每 worker 限流（8 worker 各自限流 = 实际 8 倍配额，必被打）；② 监控三指标：有效吞吐（成功 req/s）、429 率、瓶颈归因（拉取 vs 写入时间占比）；③ 改造验证用影子拉取对比新旧吞吐；④ 与上游约定配额变更流程与监控页面，避免"抢配额"式共享。

```python
# ETL 容量匹配账: 瓶颈 = min(配额, worker/时延, 下游写入), 全局限流器
# 基线: Python 3.9+ 标准库; 真实场景配令牌桶 + 429 退避
from dataclasses import dataclass


@dataclass
class EtlBudget:
    total_requests: int
    quota_rps: float          # 上游配额(全任务共享)
    workers: int
    latency_s: float
    downstream_rps: float     # 下游写入吞吐


def throughput(b: EtlBudget) -> float:
    return min(b.quota_rps, b.workers / b.latency_s, b.downstream_rps)


def finish_hours(b: EtlBudget) -> float:
    return b.total_requests / throughput(b) / 3600


def suggested_workers(b: EtlBudget, safety: float = 0.8) -> int:
    """贴配额 x safety 所需 worker 数。"""
    return int(b.quota_rps * safety * b.latency_s)


def main() -> None:
    b = EtlBudget(total_requests=600_000, quota_rps=100,
                  workers=8, latency_s=0.3, downstream_rps=500)
    assert abs(throughput(b) - 8 / 0.3) < 1e-9   # 26.7 rps, worker 是瓶颈
    assert 6 < finish_hours(b) < 7               # 6e5/26.7 ≈ 6.25h, 赶不上窗口
    w = suggested_workers(b)
    assert w == 24                                # 100*0.8*0.3
    b2 = EtlBudget(**{**b.__dict__, "workers": w})
    assert abs(throughput(b2) - 80) < 1e-9        # 贴 0.8x 配额
    assert 2 < finish_hours(b2) < 3               # ≈2.1h
    print(f"8w: {throughput(b):.0f}rps {finish_hours(b):.1f}h -> {w}w: "
          f"{throughput(b2):.0f}rps {finish_hours(b2):.1f}h (瓶颈转到配额)")

    # 全局限流器: 每 worker 各自限流 = 实际 x8 配额, 必被打
    assert 8 * 100 > b.quota_rps
    print("OK: 限流必须全局按配额0.8运行; 扩容对象=当前最小瓶颈项")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么限流器必须全局而不是每 worker 一个？
→ 一句话提示：每 worker 各按配额限流，N 个 worker 合成 N 倍配额打向上游，429 风暴反而拉低有效吞吐；令牌桶要放在共享层（进程内聚合或 Redis 分布式令牌桶），worker 只是消费者。

**追问 2**：贴限运行时 429 退避怎么做才不拖垮吞吐？
→ 一句话提示：尊重 Retry-After、退避做全局抖动（避免同步重试齐步走）、把 429 率当反馈信号动态降速率（AIMD），而不是把 429 当普通失败重试——重试流量本身计入配额会进一步恶化。

## 背诵要点
- 容量账：吞吐 = min(配额, worker数/时延, 下游写入)；扩容对象 = 当前最小项——27/100 rps 时先加 worker（零谈判成本），贴近配额才申请扩配额。
- 限流器全局化（配额 × 0.8 运行），worker 只是消费者；每 worker 各自限流 = 实际 N 倍配额，必然 429 风暴。
- 贴限运行必配：尊重 Retry-After 的全局抖动退避 + 429 率反馈调速；降时延/增量水位等"白捡吞吐"优化排在加机器之前。

## 复盘追问
- 为什么"先降单请求时延"常比加 worker 更划算？提示：吞吐 = worker/时延，时延减半等效 worker 翻倍，但不用加机器、不占配额余量；批量端点、连接复用、字段裁剪都是时延侧杠杆。
- 下游写入成为瓶颈时怎么判断？提示：监控拉取与写入时间占比——拉取快了但总时长没降就是写入侧满载，解法在批量写/并行写（Q6519）而不是继续加拉取 worker。
