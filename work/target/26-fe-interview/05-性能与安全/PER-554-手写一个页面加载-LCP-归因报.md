---
title: [PER-554] 手写一个页面加载 LCP 归因报告生成器：跑分后自动输出 LCP 元素、耗时分解与优化建议
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-554：手写一个页面加载 LCP 归因报告生成器：跑分后自动输出 LCP 元素、耗时分解与优化建议

**答**：
- LCP 归因四段：TTFB（等待文档）、加载延迟（资源开始加载前的浪费）、加载时长（资源下载）、渲染延迟（下载完到渲染的浪费，主线程被占）；用 `largest-contentful-paint` + PerformanceObserver 的属性 + `PerformanceServerTiming` 拼出分解。
- 生成器结构：采集（puppeteer + 注入探针）-> 归因（四段占比 + 元素信息）-> 建议（规则映射：图片类大 -> 建议预加载/格式优化；渲染延迟大 -> 建议查长任务）。
- 边界：LCP 候选变化要取最终候选（停止观察后）；跨域资源无 TAO 时加载段拿不到细分，标注降级。
- 评分点：四段分解计算与规则化建议映射。

```javascript

const puppeteer = require('puppeteer');
async function lcpAttribution(url) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.emulateNetworkConditions({ /* fast3g */ latency: 150, downloadThroughput: 1.6e6 / 8, uploadThroughput: 750e3 / 8, offline: false });
  await page.goto(url, { waitUntil: 'load' });
  const r = await page.evaluate(() => new Promise(res => {
    new PerformanceObserver(list => {
      const e = list.getEntries().at(-1);
      res({
        startTime: e.startTime, url: e.url, tag: e.element?.tagName,
        size: e.size, id: e.id,
        ttfb: performance.getEntriesByType('navigation')[0].responseStart,
      });
    }).observe({ type: 'largest-contentful-paint', buffered: true });
    setTimeout(() => res(null), 10000);
  }));
  await browser.close();
  if (!r) return { pass: false };
  const adv = r.url
    ? ['LCP 是图片：建议 preload + AVIF + 合适尺寸']
    : ['LCP 是文本：字体 swap + 关键 CSS 内联'];
  return {
    element: `${r.tag}#${r.id || ''} size=${Math.round(r.size / 1024)}KB`,
    lcpMs: Math.round(r.startTime),
    ttfbMs: Math.round(r.ttfb),
    loadPhaseMs: Math.round(r.startTime - r.ttfb),       // 含加载+渲染两段
    advice: r.loadPhaseMs > 1500 ? adv : ['当前 LCP 达标'],
  };
}
lcpAttribution('https://example.com').then(console.log);
```
