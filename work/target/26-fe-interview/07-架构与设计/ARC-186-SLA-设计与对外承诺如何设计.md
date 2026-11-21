---
title: [ARC-186] SLA 设计与对外承诺如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-186：SLA 设计与对外承诺如何设计？
**答**：
- SLA 三要素：指标定义（可用性 = 成功请求/总请求，时延分位 P95/P99——分位数口径必须写死，否则扯皮）、测量方式（哪个探针/监控口径）、违约与补偿（对内是事故定级依据，对外是赔付条款）。
- 内外分层：对外 SLA 保守（承诺的必须稳），对内 SLO 更严格（给错误预算留余量）——对外 99.9% 对内做 99.95%。
- 错误预算机制：月度错误预算（如 43 分钟不可用/月）耗尽即冻结功能发布、只做稳定性修复——SLA 不是墙上的数字，是发布节奏的调节器。
- 前端专项 SLA：首屏时延 P75（比平均分位更贴近体验）、JS 错误率、白屏率；与性能预算体系（ARC-101）联动。

```yaml
# SLA 配置实例
sla:
  external_commitment:            # 对外承诺（保守）
    availability:
      metric: 非 5xx 且响应 < 5s 的请求占比
      target: 99.9%               # 月度不可用预算 ≈ 43.2 min
      measurement: 网关探针 + 三方拨测（双口径取严）
    page_latency:
      metric: 首屏 LCP P75
      target: "< 3s"
  internal_slo:                   # 对内目标（更严，留余量）
    availability: 99.95%          # 错误预算 ≈ 21.6 min
    lcp_p75: "< 2.5s"
    js_error_rate: "< 0.1% per-1k-pv"
    blank_screen_rate: "< 0.05%"
  error_budget_policy:            # 错误预算机制
    - 月度预算耗尽 → 冻结功能发布，仅允许稳定性修复
    - 预算剩余 < 20% → 变更评审升级（tech lead 审批）
  breach_flow:
    - 违约自动告警 → 事故定级 → 复盘报告 48h 内 → 改进项进跟踪清单
  review: SLA 每半年校准（目标应随能力演进收紧，而不是恒定）
```
