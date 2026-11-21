---
title: [OPT-194] LCP 达标专项如何从"图片/字体/TTFB"三管齐下？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-194：LCP 达标专项如何从"图片/字体/TTFB"三管齐下？

**答**：
- 先确认 LCP 元素与四段子时长：TTFB → 元素延迟（发现晚）→ 加载时长（下载慢）→ 渲染延迟（解码/排队）。三管对应：TTFB 管（OPT-121/123）、图片管（preload+priority+格式）、字体管（font-display+preload，字体阻塞的是 FCP 也会拖 LCP）。
- 图片三件套：LCP 图 `preload + fetchpriority=high`、AVIF/WebP、明确尺寸；动态 HTML 下发的 hero 图 URL 要能被 preload（SSR 时把 URL 写进 head）。
- 字体策略：`font-display: swap/optional` + 关键字体子集化 preload；`optional` 可彻底消除布局抖动但可能首访不显示字体。
- 元素延迟常被忽略：LCP 元素在轮播第 3 帧/依赖接口数据 → 把首帧 hero 改为静态直出，是最大单项收益。

```html
<!-- 一一对应：LCP 三管齐下的 head 配置模板 -->
<head>
  <!-- 管1 TTFB：103 Early Hints / SSR 缓存（见 OPT-123/179），此处配 preconnect -->
  <link rel="preconnect" href="https://img.example.com" crossorigin>
  <!-- 管2 图片：SSR 把 LCP 图 URL 注入 preload，高优先级 -->
  <link rel="preload" as="image" href="https://img.example.com/hero.avif" fetchpriority="high">
  <!-- 管3 字体：关键子集 preload + swap，防文字被字体拖住 -->
  <link rel="preload" as="font" type="font/woff2"
        href="/fonts/subset-latin-zh-400.woff2" crossorigin>
  <style>
    @font-face {
      font-family: 'Main';
      src: url('/fonts/subset-latin-zh-400.woff2') format('woff2');
      font-display: swap;      /* 先用回退字体渲染，字体到了再换 */
      unicode-range: U+4E00-9FFF, U+0000-00FF;  /* 子集：只覆盖常用区 */
    }
    /* LCP 图明确尺寸：加载期不产生布局位移 */
    .hero img { width: 100%; height: auto; aspect-ratio: 16/7; }
  </style>
</head>
<body>
  <!-- 元素延迟治理：hero 首帧静态直出（不依赖接口），数据驱动的内容放第二屏 -->
  <section class="hero">
    <img src="/hero.avif" width="1280" height="560" alt="" fetchpriority="high" decoding="async">
  </section>
  <script>
    // 验证：上报 LCP 元素与四段子时长，确认当前瓶颈
    new PerformanceObserver(l => {
      const e = l.getEntries().pop();
      navigator.sendBeacon('/api/perf/lcp-seg', JSON.stringify({
        element: e.element?.tagName, url: e.url,
        ttfb: e.startTime, loadDur: e.loadTime, renderDelay: e.renderTime - e.loadTime,
      }));
    }).observe({ type: 'largest-contentful-paint', buffered: true });
  </script>
</body>
```
