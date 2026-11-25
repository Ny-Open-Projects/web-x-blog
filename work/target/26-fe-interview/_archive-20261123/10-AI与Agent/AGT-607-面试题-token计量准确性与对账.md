---
title: [AGT-607] 前端显示的 token 用量与服务端账单对不上，如何建立计量对账机制？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-607：前端显示的 token 用量与服务端账单对不上，如何建立计量对账机制

**答**：
- 计量三源头：模型返回的 usage（权威）、服务端日志累计（对账用）、前端展示（体验用）。前端只展示不参与计费，计费以服务端聚合为准。
- 对账任务：日级对账「服务端聚合 vs 模型账单」，偏差 >1% 告警（常见原因：重试未去重、流式 usage 补发丢失、缓存命中计量口径不一）。
- 前端体验口径要注明是估算还是实测（实测=服务端回传 usage，估算=本地 tokenizer 预估），避免"看到 100 结果账单 120"的投诉。

```javascript
// 日级对账
async function reconcile(day) {
  const internal = await aggInternal(day);       // 服务端累计
  const vendor = await fetchVendorBill(day);     // 模型账单
  const drift = Math.abs(internal.total - vendor.total) / vendor.total;
  if (drift > 0.01) alert({ type: 'usage_drift', day, drift,
    suspects: ['retry_dup', 'stream_usage_missed', 'cache_accounting'] });
}
```

