---
title: [NODE-505] Node 服务的接口依赖声明（BFF 声明依赖哪些下游）如何治理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-505：接口依赖声明治理
**答**:
- 声明制：每个 BFF 接口声明下游依赖（调用了谁/关键还是非关键/超时预算/降级策略——NODE-490 降级声明的上游版），依赖清单进服务注册表（NODE-427 依赖图的声明式补充——运行时 trace 是事实，声明是意图）。
- 治理价值：影响面评审（改下游接口 → 反查哪些 BFF 接口声明了依赖 → 自动通知 NODE-447/428）、容量协商（新接口声明高 QPS 依赖 → 下游容量对齐 NODE-405）、依赖健康基线（声明的预算 vs 实际 trace 数据对比——偏差告警）。
- 演进控制：新增依赖走轻量评审（新依赖 = 新故障面——影响分析必须过）、僵尸依赖清理（声明了但 trace 显示 90 天零调用 → 清理提醒）。
- 与代码同步：声明与实现一致性校验（CI：代码里调了未声明的下游 → 阻断——防"偷偷依赖"）。
- 例外机制：紧急依赖（事故中临时加依赖）→ 事后补声明（豁免留痕 ARC-435）。
```yaml
# 接口依赖声明
- route: /api/home
  deps:
    - { svc: goods-svc, critical: true, timeout: 800ms, fallback: cache }
    - { svc: recommend-svc, critical: false, timeout: 200ms, fallback: static }
  ci_check: code-callers ⊆ declared   # 未声明调用阻断
```
