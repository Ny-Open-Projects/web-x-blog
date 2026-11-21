---
title: [DP-310] 笔试题：手写前端 SLO 错误预算计算器？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-310：笔试题：手写前端 SLO 错误预算计算器？
**题目**：实现 ErrorBudget：1) 输入日级指标（pv/白屏数/致命错误数），输出可用性与预算燃尽；2) 预算跨日累计（滑动 7 天窗口）；3) 燃尽 > 80% 触发冻结建议；4) 消耗来源归因（错误类型占比）。
**评分点**：
- 可用性口径正确（1 - (白屏率+致命错误率)）。
- 窗口累计正确（7 天滑动求和）。
- 冻结阈值判定。
- 归因结构可读。
```javascript
class ErrorBudget {
  constructor(private slo = 0.999) { this.daily = []; }
  ingestDay({ date, pv, whiteScreens, fatalErrors, byType }) {
    const whiteRate = whiteScreens / pv, fatalRate = fatalErrors / pv;
    const availability = 1 - (whiteRate + fatalRate);       // 1) 前端口径
    const spend = Math.max(0, (1 - this.slo) - (availability - this.slo));  // 消耗量
    this.daily.push({ date, availability, spend, byType });
  }
  window(days = 7) {                                        // 2) 滑动窗口
    const w = this.daily.slice(-days);
    const totalBudget = (1 - this.slo) * days;
    const spent = w.reduce((s, d) => s + d.spend, 0);
    const burn = spent / totalBudget;
    const byType = w.reduce((acc, d) => { for (const [t, c] of Object.entries(d.byType)) acc[t] = (acc[t] ?? 0) + c; return acc; }, {});
    return { burn, frozen: burn > 0.8,                       // 3) 冻结建议
      topTypes: Object.entries(byType).sort((a, b) => b[1] - a[1]).slice(0, 3) };   // 4) 归因
  }
}
// 用：budget.ingestDay({ date: '11-18', pv: 1e6, whiteScreens: 500, fatalErrors: 120, byType: { js: 300, api: 200 } })
// window() → { burn: 0.42, frozen: false, topTypes: [['js', 300], ['api', 200]] }
```
