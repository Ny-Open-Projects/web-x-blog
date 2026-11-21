---
title: [HW-201] 手写 Vital 归因统一采集器——四指标归因字段（element/invoke/phase）映射到统一 schema
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：四指标归因统一：LCP（element/url + 四段）、INP（target/三段 + LoAF invoker）、CLS（sources 矩形）、TTFB（导航分段）——映射到统一 schema {metric, value, attribution:{cause, suspect, phase}}，看板一套查询查所有归因。

```javascript
function unifiedAttribution(metric, raw) {
  switch (metric) {
    case 'LCP': return { cause: raw.loadDelay > 500 ? 'resource-load' : 'render',
      suspect: raw.url ?? raw.element, phase: { ttfb: raw.ttfb, load: raw.loadDuration, render: raw.renderDelay } };
    case 'INP': { const worst = ['input', 'processing', 'presentation']
      .reduce((a, b) => raw.phases[a] > raw.phases[b] ? a : b);
      return { cause: worst === 'input' ? 'main-thread-busy' : worst === 'processing' ? 'handler-heavy' : 'render-heavy',
        suspect: raw.target ?? raw.loafInvoker, phase: raw.phases }; }
    case 'CLS': return { cause: 'layout-shift', suspect: raw.sources[0]?.el, phase: raw.rects };
    case 'TTFB': return { cause: 'server', suspect: raw.serverTimingTop, phase: raw.nav };
  }
}
// 统一 schema：{ metric, value, attribution: { cause(枚举), suspect(元素/脚本/接口), phase(分段) } }
// 看板价值：cause 维度跨指标聚合 —— "render-heavy 类问题占比 40%"跨 LCP/INP 汇总（单指标看不到）
// suspect 统一为字符串语义标识（元素 tag/data-test-id/脚本 URL/接口路径）—— 可 JOIN 工单系统
// cause 枚举固定集合：resource-load/render/main-thread-busy/handler-heavy/render-heavy/layout-shift/server
```

**评分点**：
- 四指标归因字段的统一 schema（cause 枚举/suspect 语义标识/phase 分段）——本题核心。
- INP 三段取最差定 cause 的判定逻辑。
- suspect 统一为语义字符串（跨指标聚合、与工单系统 JOIN）。
- cause 跨指标聚合的看板价值。
