---
title: [TST-761] AI 如何辅助设计混沌实验的「稳态假设」
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-761：AI 如何辅助设计混沌实验的「稳态假设」

**答**：
- 结论：稳态假设要「可观测、可证伪、有边界」，AI 可从监控指标与历史事故中候选生成假设，但必须由人确认指标阈值与观测窗口。
- AI 适合：从 SLO 文档/指标中提炼候选稳态指标、发现指标间的相关性；不适合：定义业务可接受的退化程度。
- 生成的假设要结构化（指标 + 阈值 + 窗口 + 注入点），直接可注入实验平台执行。
- 追问钩子：AI 提出的稳态指标很漂亮但业务方不认，如何处理？

```javascript
// 稳态假设结构：指标 + 阈值 + 窗口
function buildHypothesis({ metric, threshold, windowMs, injectPoint }) {
  return {
    steady: `${metric} 在 ${windowMs}ms 内保持在 ${threshold}`,
    verify: (samples) => samples.every(s => s <= threshold),
    injectPoint,
  };
}
const h = buildHypothesis({ metric: 'errorRate', threshold: 0.01, windowMs: 60000, injectPoint: 'api' });
console.log(h.steady);
console.log(h.verify([0.005, 0.008, 0.012])); // false，超出阈值
```
