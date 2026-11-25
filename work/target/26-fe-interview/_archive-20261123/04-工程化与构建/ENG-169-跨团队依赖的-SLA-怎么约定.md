---
title: [ENG-169] 跨团队依赖的 SLA 怎么约定？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-169：跨团队依赖的 SLA 怎么约定？
**答**：
- 把跨团队接口当供应商协议：明确交付物、时间点、质量标准、故障响应时效（SLA）。
- 典型条款：契约冻结日、联调就绪日、性能基线（QPS/P99）、P1 响应与恢复时限、破坏性变更提前通知天数。
- 落地形式：依赖登记表（who/what/when/SLA）+ 迭代会逐条过状态，违约升级到两级主管。
- 技术兜底：SLA 约束不了的地方用降级设计（超时 缓存兜底 mock 桩），不把业务可用性押在别人的承诺上。

```yaml
# team-contracts/depend-on-order-team.yaml —— 跨团队依赖登记
dependency:
  consumer: team-mall-frontend
  provider: team-trade
  deliverable: 订单详情聚合接口 /api/v2/orders/{id}
  milestones:
    contractFreeze: 2026-11-05    # 契约冻结日
    integrationReady: 2026-11-12  # 联调就绪
    perfBaseline: QPS 2000 P99 低于 200ms
  sla:
    p1Response: 15m
    p1Recovery: 2h
    changeNotice: 14d             # 破坏性变更提前 14 天通知
  fallback:                       # SLA 失效时的技术兜底
    timeout: 3s
    staleCache: 5m
    degradedUI: 展示缓存数据并提示可能延迟
```

## 第三十三章 安全工程化（ENG-170 ~ ENG-174）
