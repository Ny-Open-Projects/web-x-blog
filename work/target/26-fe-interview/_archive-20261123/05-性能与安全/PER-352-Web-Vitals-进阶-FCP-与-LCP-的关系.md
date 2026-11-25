---
title: [PER-352] FCP 与 LCP 差距过大说明什么？"白屏后空白"的中间态如何归因？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-352：FCP 与 LCP 差距过大说明什么？"白屏后空白"的中间态如何归因？

**答**：
- 口径含义：FCP = 首次渲染任何内容（含骨架屏/loader）；LCP = 最大内容元素渲染。gap = LCP - FCP 大（>2s）意味着"用户看到了加载态，但真正的内容迟迟不来"——体验上是"假首屏"，感知比纯白屏更糟（给了希望又拖延）。
- 常见根因：骨架屏渲染快但数据接口慢（CSR 串行：HTML→JS→接口→内容）；SSR 页面的注水慢（HTML 有内容但 JS 没就绪交互失效——这是 TTI/INP 问题不是 LCP）；LCP 图片晚发现（懒加载误用/动态注入）。
- 归因方法：Event 序（FCP→数据接口 responseEnd→LCP）对照：gap ≈ 接口耗时 → 数据链路问题（BFF 聚合/预取）；gap 大但接口早返回 → 渲染链路问题（JS 长任务阻塞/图片优先级）；SSR 场景看 hydration 完成时间与 LCP 的关系。
- 优化方向：缩短 gap 的核心是"让内容元素尽早成为 LCP 候选"——数据预取（接口与 HTML 并行）、SSR 直出内容、骨架屏尺寸贴近真内容（避免 LCP 元素被替换两次）。

```javascript
// gap 归因采集
let fcp = null;
new PerformanceObserver((l) => { for (const e of l.getEntries()) if (e.name === 'first-contentful-paint') fcp = e.startTime; })
  .observe({ type: 'paint', buffered: true });
new PerformanceObserver((l) => {
  const e = l.getEntries().at(-1);
  report({
    type: 'lcp-gap',
    fcp: Math.round(fcp), lcp: Math.round(e.startTime),
    gap: Math.round(e.startTime - fcp),
    lcpIsImg: !!e.url, url: e.url || '',
  });
}).observe({ type: 'largest-contentful-paint', buffered: true });
// 判读：gap > 2000ms && !lcpIsImg → 数据接口等待（查接口耗时）；
// gap > 2000ms && lcpIsImg → 图片发现/加载晚（查懒加载与优先级）
```
