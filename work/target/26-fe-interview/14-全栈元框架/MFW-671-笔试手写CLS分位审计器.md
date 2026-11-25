---
title: [MFW-671] 笔试：手写 CLS 分位审计器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-671：笔试：手写 CLS 分位审计器

**答**：实现 `clsAudit(entries, { budget, percentile })`。entries: `{ cls, route, source }[]`（RUM 采集）。规则：1) 全局 P{percentile} CLS（75 分位默认）vs budget（0.1）——超 → verdict 'fail'；2) **路由分桶**：每路由的 P75（哪个路由的 CLS 最差——归因）；3) 来源聚合：source 元素的出现频次（图片/字体/动态内容——修复优先级）；4) 按交互排除：hadRecentInput 已在采集层排除——审计层不重复；5) 返回 `{ globalP75, verdict, worstRoutes: top3, sourceFreq: Record<source, count> }`。边界：entries 空（no-data）；单条目（P75 = 该值）；percentile 0~100 输入校验。

```javascript
function clsAudit(entries = [], { budget = 0.1, percentile = 75 } = {}) {
  if (percentile <= 0 || percentile > 100) throw new Error('percentile 非法');
  if (!entries.length)
    return { noData: true, globalP75: 0, verdict: 'no-data', worstRoutes: [], sourceFreq: {} };
  const sorted = entries.map(e => e.cls).sort((a, b) => a - b);
  const idx = Math.floor((percentile / 100) * sorted.length);
  const globalP75 = +(sorted[Math.min(sorted.length - 1, idx)] ?? 0).toFixed(4);
  // 路由分桶
  const byRoute = new Map();
  for (const e of entries) {
    (byRoute.get(e.route) || byRoute.set(e.route, []).get(e.route)).push(e.cls);
  }
  const worstRoutes = [...byRoute.entries()]
    .map(([route, cls]) => ({ route, p75: cls.sort((a, b) => a - b)[Math.floor(cls.length * percentile / 100)] }))
    .sort((a, b) => b.p75 - a.p75).slice(0, 3);
  // 来源聚合
  const sourceFreq = {};
  for (const e of entries) sourceFreq[e.source] = (sourceFreq[e.source] || 0) + 1;
  return {
    globalP75,
    verdict: globalP75 > budget ? 'fail' : 'pass',
    worstRoutes, sourceFreq,
  };
}

// 自测
const entries = [
  ...Array.from({ length: 70 }, () => ({ cls: 0.02, route: '/home', source: 'image' })),
  ...Array.from({ length: 25 }, () => ({ cls: 0.3, route: '/search', source: 'font' })),
  ...Array.from({ length: 5 }, () => ({ cls: 0.5, route: '/search', source: 'dynamic' })),
];
let r = clsAudit(entries);
// 排序后：70×0.02 + 25×0.3 + 5×0.5 → P75 位置 = 75 → 0.3
console.log(r.globalP75 === 0.3);
console.log(r.verdict === 'fail');                       // 0.3 > 0.1
console.log(r.worstRoutes[0].route === '/search');       // P75 0.5 最高
console.log(r.sourceFreq.image === 70);                  // 图片是最高频源

// 低 CLS
r = clsAudit(entries.filter(e => e.cls <= 0.05));
console.log(r.verdict === 'pass' && r.globalP75 <= 0.05);

// 空
r = clsAudit([]);
console.log(r.noData === true);
// percentile 校验
e = null; try { clsAudit(entries, { percentile: 150 }); } catch (x) { e = x; }
console.log(/非法/.test(e.message));
```

**评分点**：
- P75 计算正确（排序索引——Google Core Web Vitals 规范）；预算判定
- 路由分桶归因（worstRoutes 修复优先级）；来源聚合（sourceFreq——修复靶点）
- 边界（空 no-data/percentile 校验）；hadRecentInput 在采集层排除的分工
- 能说清「CLS 的 P75 优于均值：均值被多数好页面稀释、P75 反映真实用户痛点」属于加分
