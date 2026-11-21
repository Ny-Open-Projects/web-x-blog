---
title: [TST-433] 笔试：水合耗时的打点采集与预算断言。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-433：笔试：水合耗时的打点采集与预算断言。
**题目**：在 HTML 注入标记脚本（首字节/水合开始/水合完成三点）。实现 `hydrationTiming(marks)` 计算各段耗时，断言水合总时长 < 预算；缺失 mark 报错（埋点丢失检测）。

```javascript
function hydrationTiming(marks, { budgetMs = 2000 } = {}) {
  const need = ['ttfb', 'hydrate-start', 'hydrate-done'];
  const missing = need.filter(k => marks[k] === undefined);
  if (missing.length) throw new Error(`埋点缺失: ${missing}`);
  const segs = { ttfbToStart: marks['hydrate-start'] - marks.ttfb,
                 hydrating: marks['hydrate-done'] - marks['hydrate-start'] };
  const total = marks['hydrate-done'] - marks.ttfb;
  return { ...segs, total, withinBudget: total <= budgetMs,
    bottleneck: segs.hydrating > segs.ttfbToStart ? 'hydrate' : 'ttfb' };
}

```

**评分点**：
- 三段时差计算（首字节→开始→完成）。
- mark 缺失显式报错（埋点完整性）。
- 预算断言与分段时间分布（哪段慢）。
- 输出可入库（趋势）。
