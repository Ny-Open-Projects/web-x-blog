---
title: [MFW-789] Web Vitals 的 attribution 归因
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-789：Web Vitals attribution 归因

**答**:
- Web Vitals 的归因维度（web-vitals 库的 attribution: true）：1) **LCP attribution**（element：LCP 元素 / url：资源 URL / timeOrigin：导航开始——LCP 的构成分解（TTFB + 资源加载 + 渲染）；2) **INP attribution**（interactionTarget：交互元素 / interactionTime：交互时刻 / nextPaintTime：绘制时刻——INP 的延迟来源（输入延迟 + 处理时间 + 呈现延迟）；3) **CLS attribution**（sources：偏移元素列表——最大的偏移源 RBL-670）；4) **TTFB attribution**（waitingDuration：DNS/TCP/TLS 时间——网络 vs 服务器时间）。
- RSC 架构的归因解读：LCP 的 url = RSC payload 的 HTML 块（server 渲染）；INP 的 interactionTarget = client 组件（RSC 树中的 client 岛）；「Web Vitals 归因 → RSC 架构的映射」（LCP 慢 → server 渲染慢（fetch）/ client 渲染慢（水合）——归因数据决定优化方向 RBL-940）。
- 追问钩子：为什么「attribution 数据」比「指标值」更能指导优化？——指标值（LCP 3000ms）告诉你「慢」；attribution 告诉你「为什么慢」（element=heroImage + url=/api/hero → server fetch 慢；interactionTarget=SearchBox → 水合慢）；「归因 → 优化决策」：attribution 的 element/url/interactionTarget 直接映射到代码位置（优化靶点）；没有 attribution 的指标优化 = 瞎猜——有 attribution 的优化 = 精确打击。

```typescript
// web-vitals 的 attribution 采集
import { onLCP, onINP, onCLS, onTTFB } from 'web-vitals/attribution';
onLCP((metric) => {
  report('lcp', { value: metric.value,
    attribution: {
      element: metric.attribution?.element,           // LCP 元素
      url: metric.attribution?.url,                    // 资源 URL
      timeToFirstByte: metric.attribution?.timeToFirstByte,   // TTFB 占比
      resourceLoadDelay: metric.attribution?.resourceLoadDelay,  // 资源加载延迟
      resourceLoadTime: metric.attribution?.resourceLoadTime,    // 资源加载时间
      elementRenderDelay: metric.attribution?.elementRenderDelay, // 渲染延迟
    }, buildId: window.__BUILD_ID });
});
// LCP 的四段分解（Google LCP phases）
// TTFB → resource load delay → resource load time → element render delay
// 每段的优化：TTFB → SSR/CDN；load delay → preload；load time → 压缩；render → 代码
```
