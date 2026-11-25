---
title: [TST-655] 笔试：实现内存增长趋势分类器（缓存 vs 泄漏）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-655：笔试：实现内存增长趋势分类器（缓存 vs 泄漏）

**题目**：实现 classify(snaps,{minRounds,flatRatio})。snaps=[{afterGC}]。计算相邻斜率；样本不足返回 insufficient；斜率<=0 为 cache，末斜率 < 平均*flatRatio 为 bounded-cache，否则 leak。

**答**：
- 计算相邻轮次 GC 后堆大小的斜率序列。
- 斜率 <=0 判缓存；最后斜率显著小于平均（<30%）判有界缓存；否则判泄漏。
- 样本不足返回 insufficient。

```javascript
function classify(snaps, { minRounds = 3, flatRatio = 0.3 } = {}) {
  if (snaps.length < minRounds)
    return { verdict: 'insufficient' };
  const b = snaps.map(s => s.afterGC || s.heap);
  const slopes = b.slice(1).map((v, i) => v - b[i]);
  const avg = slopes.reduce((a, x) => a + x, 0) / slopes.length;
  const last = slopes[slopes.length - 1];
  const verdict = avg <= 0 ? 'cache'
    : last < avg * flatRatio ? 'bounded-cache' : 'leak';
  return { verdict, avgSlope: +avg.toFixed(1), lastSlope: last };
}
```

**评分点**：
- 斜率序列计算正确
- 三类判定阈值准确
- 样本量保护
- 返回诊断数据便于复盘
