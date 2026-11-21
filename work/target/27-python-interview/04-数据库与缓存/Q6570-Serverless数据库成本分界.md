---
title: "[Q6570] Serverless 数据库与传统实例的成本分界"
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6570 · Serverless 数据库与传统实例的成本分界

难度：P6 ｜ 标签：成本工程 / Serverless / Aurora / 容量规划

**问**：一条低峰-峰值差 20 倍的数据库业务（夜间几乎无流量、白天高峰），被建议迁到 Serverless 数据库（Aurora Serverless v2 / 按请求计费的 PG）。怎么算清楚什么时候真省钱、什么时候反被收割？

**答**：

**结论**：Serverless 的账是"单价溢价 × 负载方差"的博弈：按 ACU/请求计费的单价通常比同性能包年实例贵 30%-100%，但只对实际用量付费。分界可以用负载方差系数算：`Serverless成本/预留成本 ≈ (平均负载/峰值负载) × 溢价系数`。当"平均/峰值"低于溢价系数的倒数（如溢价 1.5 倍 → 平均负载低于峰值的 2/3）时 Serverless 才划算。题目场景峰值差 20 倍、夜间近零，表面上很匹配——但有三个隐藏账：① 突发扩容的抖动延迟（ACU 扩容不是瞬时的，高峰突发可能先慢后贵）；② 每请求计费模型的连接/查询模式惩罚（高频小查询被计费粒度放大）；③ 无法用预留实例/包年折扣，大稳态流量下预留反而更省。

**取舍**：混合策略常是最优解：核心常驻负载用预留实例扛住基线，Serverless 承接突发与夜间长尾——但双栈的运维复杂度（连接串路由、两套监控）要进账。另一个方向：不迁 Serverless，而是用"缩容夜间实例规格 + 定时伸缩"吃掉大部分方差，成本节约可达 Serverless 的 70%，且无单价溢价。

**实战**：先量出三组数：24h 负载曲线（平均/峰值比）、查询模式（QPS 分布、单查询 ACU 消耗）、当前预留成本（含 IOPS/存储）。Python 脚本代入曲线模拟两种计费；再对 Serverless 加惩罚项（突发预热延迟、按请求粒度放大）做敏感性分析。落库决策要写"成本临界点"文档：负载涨到 X QPS 或降到 Y QPS 时重新评审。

```python
# Serverless vs 预留实例成本分界模拟
# 仅标准库，Python 3.9+
from __future__ import annotations


def hourly_load(base_qps: float, peak_qps: float) -> list[float]:
    """24h 负载曲线：夜间近零、日间双峰。"""
    hours = []
    for h in range(24):
        if 2 <= h < 8:
            hours.append(base_qps * 0.05)   # 夜间 5%
        elif h in (10, 11, 15, 16, 20):
            hours.append(peak_qps)
        else:
            hours.append(peak_qps * 0.4)
    return hours


def cost_serverless(hours: list[float], unit_cost_per_kqps_h: float,
                    burst_penalty: float = 1.1) -> float:
    return sum(q * unit_cost_per_kqps_h / 1000 * burst_penalty for q in hours)


def cost_reserved(peak_qps: float, reserved_cost_per_day: float) -> float:
    # 预留实例必须按峰值（或定时伸缩后的最大规格）买
    return reserved_cost_per_day


def main() -> None:
    base, peak = 500, 10_000  # QPS，20 倍方差
    hours = hourly_load(base, peak)
    avg = sum(hours) / len(hours)
    print(f"平均 {avg:.0f} QPS / 峰值 {peak}，均值/峰值 = {avg/peak:.2f}")

    # Serverless 单价溢价 1.1x；预留实例按峰值规格
    SL_UNIT = 0.55  # $/千QPS·h（含溢价）
    RS_DAY = 40     # 预留 $/天
    sl = cost_serverless(hours, SL_UNIT)
    rs = cost_reserved(peak, RS_DAY)
    print(f"Serverless ${sl:.0f}/天 vs 预留 ${rs}/天 → {'SL赢' if sl < rs else '预留赢'}")
    assert rs < sl, "高溢价下预留应更省（峰值时段占比高）"

    # 反例：夜间/周末大空置的业务（峰值仅工作日 8h 出现）
    hours2 = [peak if 10 <= h < 18 else base * 0.02 for h in range(24)]
    # 只算工作日 5/7 天
    sl2 = cost_serverless(hours2, SL_UNIT) * 5 / 7
    rs2 = RS_DAY  # 预留 7 天都在付费
    print(f"大空置场景: SL ${sl2:.0f}/天 vs 预留 ${rs2}/天 → {'SL赢' if sl2 < rs2 else '预留赢'}")
    assert sl2 < rs2, "空置大时 Serverless 应更省"


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么"每请求计费"对高频小查询不友好？——计费粒度（请求/行/ACU 秒）有下限，一次 1ms 的点查可能按最小计费单元收费；QPS 高、单查询轻的负载下，实际单价是标价的数倍。这类负载应该算"每百万查询成本"而不是"每 ACU 小时成本"。
- 追问 1.1：ACU 扩容抖动对 SLO 什么影响？——负载从 2 ACU 突增到 8 ACU 时，扩容有秒到分钟级滞后，期间连接排队、延迟抬升；Serverless 不能承诺"突发也保持原延迟"，SLO 要么放宽要么预热+预留混合。
- 追问 2：定时伸缩预留实例方案的上限在哪？——能吃掉"可预测"的方差（昼夜、工作日），吃不掉突发流量与不可预测增长；且最小规格变更粒度、变更耗时（重启连接）限制伸缩频率，通常小时级一档。

**背诵要点**：

1. 分界公式：Serverless 划算 ⇔ 平均负载/峰值负载 < 1/溢价系数；溢价 1.5-2x 下大多数 7x24 业务预留更省。
2. Serverless 三隐藏账：扩容抖动延迟、按请求计费对高频轻查询的粒度惩罚、无预留折扣。
3. 混合策略（预留扛基线 + Serverless 扛突发）或定时伸缩吃掉可预测方差，后者可省 Serverless 方案 70% 且无溢价。

**复盘追问**：

1. 如果业务量月增 30%，"成本临界点"文档里的重评触发条件应该怎么设计？
2. Serverless 迁移后某天账单暴涨 5 倍，你的归因排查顺序？
