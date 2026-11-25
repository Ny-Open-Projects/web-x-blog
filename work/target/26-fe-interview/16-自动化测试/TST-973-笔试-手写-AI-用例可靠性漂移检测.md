---
title: [TST-973] 笔试：手写「AI 用例可靠性漂移检测器」，基于时间序列判定恶化趋势
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-973：笔试：手写「AI 用例可靠性漂移检测器」，基于时间序列判定恶化趋势
**答**：
- 需求：实现 driftDetect(snapshots, cfg)，snapshots = [{ date, flakeRate, survival, detectRate }]，cfg 含阈值与连续周数。
- 规则：任意指标连续 cfg.weeks 周恶化且累计变化超 cfg.threshold 判为 drift；输出 { drifted, metrics, firstBadDate }。
- 边界：数据不足 cfg.weeks 条返回 not-enough；某周缺失指标跳过该指标判定。

```javascript
function driftDetect(snapshots, cfg = { weeks: 2, threshold: 0.05 }) {
  if (snapshots.length < cfg.weeks) return { drifted: false, reason: 'not-enough' };
  const metrics = ['flakeRate', 'survival', 'detectRate'];
  const bad = [];
  for (const m of metrics) {
    const valid = snapshots.filter(s => typeof s[m] === 'number');
    if (valid.length < cfg.weeks) continue;
    const window = valid.slice(-cfg.weeks);
    const first = window[0][m], last = window[window.length - 1][m];
    const worsening = m === 'flakeRate' ? last > first : last < first;
    const delta = Math.abs(last - first);
    if (worsening && delta > cfg.threshold)
      bad.push({ metric: m, delta: +delta.toFixed(2) });
  }
  return {
    drifted: bad.length > 0, metrics: bad,
    firstBadDate: bad.length ? snapshots[snapshots.length - cfg.weeks].date : null,
  };
}
console.log(driftDetect([
  { date: 'W1', flakeRate: 0.02, survival: 0.95, detectRate: 0.8 },
  { date: 'W2', flakeRate: 0.09, survival: 0.95, detectRate: 0.8 },
]).drifted); // true（flakeRate 连续恶化 0.07 > 0.05）
```
**评分点**：
- 按周窗口判定连续 cfg.weeks 周恶化且超阈值。
- flakeRate 上升算恶化，survival/detectRate 下降算恶化，方向正确。
- 数据不足返回 not-enough，缺失指标跳过，边界完整。
- 输出 firstBadDate 便于回溯何时开始劣化。
