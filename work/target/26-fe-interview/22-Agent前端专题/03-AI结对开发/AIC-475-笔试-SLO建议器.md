---
title: [AIC-475] 笔试：从历史数据建议 SLO 目标值。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-475：笔试：从历史数据建议 SLO 目标值。
**答**：输入指标历史 `number[]`（如每日错误率）。建议 SLO = P50 的 1.5 倍（错误率类向上取两位小数），并校验 P99 是否超 SLO 的 3 倍（超则提示「分布长尾需先治理」）。

```javascript
function quantile(sorted, q) {
  if (!sorted.length) return 0;
  const pos = (sorted.length - 1) * q, base = Math.floor(pos);
  const rest = sorted[base + 1] ?? sorted[base];
  return sorted[base] + (rest - sorted[base]) * (pos - base);
}
function suggestSLO(history) {
  const s = [...history].sort((a, b) => a - b);
  const p50 = quantile(s, 0.5), p99 = quantile(s, 0.99);
  const slo = +((p50 * 1.5).toFixed(4));
  return { slo, longTail: p99 > slo * 3,
    note: p99 > slo * 3 ? `P99=${p99} 超目标 3 倍：先治理长尾再定 SLO` : '分布健康' };
}
console.log(suggestSLO([0.01, 0.01, 0.02, 0.02, 0.02, 0.5]));
// P99≈0.354 → longTail true

```

**评分点**：
- 分位数计算正确（排序 + 线性插值或简化取下标）。
- SLO 公式明确且方向对（错误率取上界，可用率取下界——题目只需错误率方向）。
- 长尾提示（P99/目标 > 3）。
- 空数据防御。
