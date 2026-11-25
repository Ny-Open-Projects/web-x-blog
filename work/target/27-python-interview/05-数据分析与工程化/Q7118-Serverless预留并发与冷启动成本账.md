---
title: [Q7118] Serverless 预留并发与冷启动的成本账
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7118 · Serverless 预留并发与冷启动的成本账

难度：P6 ｜ 标签：成本工程 / Serverless / 冷启动

**问**：一个 Python 数据服务（导入-heavy，冷启动 2.5s）迁到 Serverless 后，白天 P99 长尾被冷启动拖到 4s，SLO 告警。开"预留并发"解决冷启动，账单却涨了近一倍。这道账怎么算？冷启动还有哪些不动钱的治理手段？什么信号说明该放弃 Serverless 回常驻？

**答**：
- **结论**：账的结构：① **按量模式**——费用 = 请求数 × (执行时长 × 内存单价)，冷启动实例的首请求慢但只多计一次初始化时长（多数厂商计入）；高峰时段实例频繁新建/销毁，冷启动率 = 新建实例数/请求数，与流量波动率正相关；② **预留并发 N**——为 N 个实例常驻付费（7×24 × N × 内存单价），无论有没有请求；账单涨一倍说明 N 设得接近峰值并发、且峰值时段占比低（常驻费 × 全天 vs 按量费 × 只在峰时发生）——典型的"用全天常驻买 2 小时的长尾"。优化顺序不是二选一：先**压冷启动本身**（便宜且一劳永逸），再**精算预留量**（不是峰值并发而是"覆盖 P95 流量即可，长尾容忍少量冷启动"），最后考虑**混合**（预留小基座 + 按量溢出）。冷启动治理手段：① 减 import——延迟导入重模块（pandas/ML 库按需 import，冷启动最大头是 import 时间，Q7081 CLI import 慢同源）；② 快照/快照池（如 AWS SnapStart 类机制或预初始化镜像）；③ 初始化并发化（模块级并行 init）；④ 缩小部署包（镜像层裁剪）；⑤ 预热请求（定时 ping，注意与计费窗口的关系，可能是自欺）。放弃信号：流量平稳高占用（利用率 >60% 常驻更便宜）、常驻需求大（长连接/状态）、冷启动 SLO 根本不可容忍。
- **取舍**：预留量精算：预留覆盖"P95 并发"而非峰值——让 5% 长尾接受冷启动，常驻费降 30~50%；或"时间表预留"（工作时段高预留、夜间零预留），配合业务流量画像。混合架构的成本拐点：当 24h 平均利用率（请求时长总和/可用实例秒数）>50~60% 时，常驻容器/虚机的单位成本低于按量——按月账单对比即可决策。
- **实战**：落地：① 采集冷启动率与 init 时长分布（平台指标 + 函数内首次请求埋点）；② import 审计（`-X importtime`）排 Top 模块，懒加载改造；③ 预留量按周流量画像回算，月度复查；④ 决策面板放三个数：冷启动率、利用率、单位请求成本，任何一项恶化触发重估。

```python
# Serverless 冷启动与预留并发的成本账
# 基线：Python 3.9+ 标准库；参数以云厂商实价与流量画像校准
from dataclasses import dataclass


@dataclass
class SlsProfile:
    daily_requests: float
    avg_exec_s: float        # 平均执行时长（导入-heavy 服务偏长）
    mem_gb: float
    price_per_gb_s: float    # 按量单价（GB-秒）
    peak_hour_ratio: float   # 峰值时段请求占比


def ondemand_cost(p: SlsProfile) -> float:
    """按量日成本 = 总执行 GB-秒 x 单价。"""
    return p.daily_requests * p.avg_exec_s * p.mem_gb * p.price_per_gb_s


def reserved_cost(p: SlsProfile, instances: int, window_s: float = 86400) -> float:
    """预留日成本 = 实例数 x 常驻秒 x 内存单价（与是否空闲无关）。"""
    return instances * window_s * p.mem_gb * p.price_per_gb_s


def utilization(p: SlsProfile, instances: int, window_s: float = 86400) -> float:
    """利用率 = 执行秒数 / (实例数 x 窗口秒)。"""
    exec_s = p.daily_requests * p.avg_exec_s
    return exec_s / (instances * window_s)


def main() -> None:
    p = SlsProfile(daily_requests=500_000, avg_exec_s=2.0, mem_gb=2.0,
                   price_per_gb_s=1.0, peak_hour_ratio=0.4)
    base = ondemand_cost(p)                       # 200 万 GB-秒/日
    exec_s = p.daily_requests * p.avg_exec_s      # 100 万实例-秒/日

    # 预留峰值并发 20：常驻费比按量涨 73% —— "账单近翻倍"
    full = reserved_cost(p, 20)
    assert 1.5 * base < full < 2 * base, full / base
    assert utilization(p, 20) < 0.6               # 48%: 预留过量的浪费
    print(f"预留20实例日费 {full:.0f} vs 按量 {base:.0f}（{full/base:.2f}x），利用率仅 {utilization(p,20):.0%}")

    # 精算：只覆盖 P95 并发 12，长尾容忍冷启动
    part = reserved_cost(p, 12)
    assert part < full * 0.65
    assert utilization(p, 12) > 0.9               # 96%: 预留吃满
    print(f"P95 预留12实例（降 {1-part/full:.0%}），利用率 {utilization(p,12):.0%}，5% 长尾接受冷启动")

    print("OK: 先压冷启动(懒import/快照)，再精算预留量，利用率>60%评估回常驻")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"预留峰值并发"是最贵的错误？
→ 一句话提示：峰值并发一天只在少数时段出现，为它 7×24 付常驻费等于把按量的"用时付费"优势完全交回去；正确目标是"覆盖 P95 + 长尾容忍"，甚至用时间表预留匹配业务节奏。

**追问 2**：定时预热为什么可能是自欺？
→ 一句话提示：预热只保住"被 ping 的实例"，流量上来时平台仍会新建实例（并发放大），冷启动照样发生；且预热请求本身计费——治理冷启动要靠压 init 时长，而不是靠加热。

## 背诵要点
- 账单结构：按量 = 请求数×时长×内存单价；预留 N 实例 = 7×24 常驻费——"预留峰值并发"用全天常驻买峰时长尾，账单近翻倍。
- 治理顺序：先压冷启动（懒 import、快照池、初始化并发化、缩包）→ 预留只覆盖 P95 并发（常驻费降 30~50%）→ 利用率 >60% 评估回常驻。
- 决策三指标：冷启动率、24h 利用率（拐点 50~60%）、单位请求成本；定时预热可能自欺（并发放大仍会新建实例且预热计费）。

## 复盘追问
- 怎么量化"懒 import 改造"值多少预留费？提示：init 时长下降直接降低单次冷启动成本与首请求延迟，同时按量模式下初始化计费减少——用 `-X importtime` 的 Top 模块改造收益折算成"可减少的预留实例数"。
- 混合架构（预留基座+按量溢出）的坑在哪？提示：两条路径的行为差异（版本、配置、网络）要保证一致，否则"同一请求走不同实例表现不同"；监控要能区分路径归因。
