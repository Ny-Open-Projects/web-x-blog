---
title: [MFW-790] 笔试：手写 LCP 归因分析器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-790：笔试：手写 LCP 归因分析

**答**：实现 `lcpAttribution(attr, { ttfbBudget, loadBudget, renderBudget })`。attr: `{ timeToFirstByte, resourceLoadDelay, resourceLoadTime, elementRenderDelay, element, url }`。规则：1) 四段分解：ttfb / loadDelay / loadTime / renderDelay——各段的占比；2) **瓶颈识别**：最大段的优化建议映射：TTFB → SSR/CDN/缓存；loadDelay → preload/priority hint；loadTime → 压缩/CDN；renderDelay → JS 阻塞/水合；3) **超标判断**：各段超过 budget → 超标段列表；4) 返回 `{ breakdown: Record<segment, ms>, percentages: Record<segment, string>, bottleneck: { segment, suggestion }, overBudget: string[] }`。边界：attr 空（no-data）；全段 0（立即渲染——不现实但处理）；单段占比 >50% → bottleneck 确定明确。

```javascript
function lcpAttribution(attr = {}, budgets = { ttfbBudget: 200, loadBudget: 500, renderBudget: 1000 }) {
  if (!attr.timeToFirstByte && !attr.elementRenderDelay)
    return { noData: true, breakdown: {}, percentages: {}, bottleneck: null, overBudget: [] };
  const segments = {
    ttfb: attr.timeToFirstByte ?? 0,
    loadDelay: attr.resourceLoadDelay ?? 0,
    loadTime: attr.resourceLoadTime ?? 0,
    renderDelay: attr.elementRenderDelay ?? 0,
  };
  const total = Object.values(segments).reduce((s, v) => s + v, 0) || 1;
  const percentages = Object.fromEntries(
    Object.entries(segments).map(([k, v]) => [k, `${Math.round(v / total * 100)}%`]));
  const budgetMap = {
    ttfb: budgets.ttfbBudget, loadDelay: budgets.loadBudget,
    loadTime: budgets.loadBudget, renderDelay: budgets.renderBudget,
  };
  const overBudget = Object.entries(segments)
    .filter(([k, v]) => v > budgetMap[k])
    .map(([k]) => k);
  const bottleneck = Object.entries(segments).sort((a, b) => b[1] - a[1])[0];
  const SUGGESTIONS = {
    ttfb: 'SSR 缓存/Edge 部署/preconnect',
    loadDelay: 'preload/priority hint/modulepreload',
    loadTime: '压缩/CDN/格式优化（webp/avif）',
    renderDelay: '减少 JS 阻塞/水合优先级/islands',
  };
  return {
    breakdown: segments, percentages,
    bottleneck: { segment: bottleneck[0], ms: bottleneck[1],
      suggestion: SUGGESTIONS[bottleneck[0]] },
    overBudget,
  };
}

// 自测
// TTFB 主导
let r = lcpAttribution({ timeToFirstByte: 2000, resourceLoadDelay: 50,
  resourceLoadTime: 200, elementRenderDelay: 100 });
console.log(r.bottleneck.segment === 'ttfb');
console.log(r.percentages.ttfb === '85%');
console.log(r.overBudget.includes('ttfb'));
console.log(r.bottleneck.suggestion.includes('SSR'));

// render delay 主导
r = lcpAttribution({ timeToFirstByte: 100, resourceLoadDelay: 50,
  resourceLoadTime: 100, elementRenderDelay: 2000 });
console.log(r.bottleneck.segment === 'renderDelay');
console.log(r.bottleneck.suggestion.includes('水合'));

// 全达标
r = lcpAttribution({ timeToFirstByte: 100, resourceLoadDelay: 50,
  resourceLoadTime: 200, elementRenderDelay: 300 },
  { ttfbBudget: 200, loadBudget: 500, renderBudget: 1000 });
console.log(r.overBudget.length === 0);

// 空
console.log(lcpAttribution({}).noData === true);
```

**评分点**：
- 四段分解（TTFB/loadDelay/loadTime/renderDelay——Google LCP phases）；百分比计算
- 瓶颈识别（最大段 → 优化建议映射——精确打击）；超标段列表（各段 budget 独立判断）
- 边界（空 no-data/单段主导）；overBudget 与 bottleneck 的区别（单个超标 vs 最大占比）
- 能说清「LCP attribution 的四段分解映射到不同优化方向：TTFB→缓存、loadDelay→preload、render→水合」属于加分
