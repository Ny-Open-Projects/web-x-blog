---
title: [TST-748] 性能预算（performance budget）如何借助 AI 做「动态阈值」调整
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-748：性能预算（performance budget）如何借助 AI 做「动态阈值」调整

**答**：
- 结论：固定预算要么过松要么误报，动态预算用历史分布 + 业务上下文自动调阈值，但必须保留「不可突破的硬底线」。
- 模型看趋势（如页面逐渐变大）按时序预测合理阈值，同时识别突变为回归。
- 动态调整要有限幅：单次调整不超过 ±10%，且需人工确认才生效，防止模型漂移放宽标准。
- 追问钩子：AI 把预算越调越松，最后形同虚设，如何防止？

```javascript
// 动态预算：基于历史 P75 加安全边际，限制调整幅度
function adjustBudget(history, hardFloor, maxStep = 0.1) {
  const s = [...history].sort((a, b) => a - b);
  const p75 = s[Math.floor(s.length * 0.75)] || 0;
  const candidate = Math.max(hardFloor, p75 * 1.1);
  const prev = history[history.length - 1] || candidate;
  const lower = prev * (1 - maxStep), upper = prev * (1 + maxStep);
  return +Math.min(upper, Math.max(lower, candidate)).toFixed(1);
}
console.log(adjustBudget([1000, 1100, 1050, 1200], 900));
```
