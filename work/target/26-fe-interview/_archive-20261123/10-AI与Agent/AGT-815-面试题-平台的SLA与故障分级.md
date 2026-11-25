---
title: [AGT-815] 企业客户 SLA（可用性/响应指标）与故障分级响应怎么定？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-815：企业客户 SLA（可用性/响应指标）与故障分级响应怎么定

**答**：
- SLA 拆解到可承诺维度：平台可用性 99.9%（网关+运行时）、任务完成率 95%（含模型供应商因素需注明依赖）、P95 首响 <3s；模型供应商故障的豁免条款写清（降级到备用模型期间仍算达标）。
- 故障分级：P0（平台不可用，15min 响应 1h 恢复目标）、P1（核心功能降级，30min 响应）、P2（非核心/单租户，工作时段）；每级带赔付条款（SLA credit）。
- 租户视角状态页：每租户可看自己的SLA达成度与历史故障赔付，透明化减少纠纷。

```javascript
const SLA = {
  availability: { target: 0.999, credit: '10%/month below' },
  taskDone: { target: 0.95, exempt: 'vendor-down-with-failover' },
  ttftP95: { target: 3 },
};
const SEVERITY = {
  P0: { response: '15m', restore: '1h', notify: 'status-page+phone' },
  P1: { response: '30m', restore: '4h' },
  P2: { response: 'workhours' },
};
```

