---
title: [TST-607] 测试平台对业务的 SLA 应该怎么定、怎么度量？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-607：测试平台对业务的 SLA 应该怎么定、怎么度量？

**答**：
- 结论：SLA 分三层——可用性（如 99.9%）、反馈时长（P95）、结果准确性（误报率），缺一不可。
- 度量必须用真实请求日志，不用内部埋点；违约要自动告警并降级为异步排队。
- 严格区分「平台故障」和「业务用例本身失败」，后者不算平台违约。
- 追问钩子：SLA 99.9% 但业务体感依然差，缺失的是哪个维度？

```javascript
function slaReport(logs, windows) {
  const inWindow = logs.filter(l => l.ts >= windows.from && l.ts < windows.to);
  const total = inWindow.length || 1;
  const ok = inWindow.filter(l => !l.platformFault).length;
  const lat = inWindow.map(l => l.ms).sort((a, b) => a - b);
  return {
    availability: +(ok / total * 100).toFixed(3),
    p95: lat[Math.floor(lat.length * 0.95)] || 0,
    breach: ok / total < 0.999,
  };
}
console.log(slaReport([{ ts: 1, platformFault: false, ms: 120 }],
  { from: 0, to: 10 }).availability);
```
