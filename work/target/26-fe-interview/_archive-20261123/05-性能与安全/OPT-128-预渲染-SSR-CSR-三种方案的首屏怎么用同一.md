---
title: [OPT-128] 预渲染、SSR、CSR 三种方案的首屏怎么用同一套方法实测对比？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-128：预渲染、SSR、CSR 三种方案的首屏怎么用同一套方法实测对比？

**答**：
- 公平对比原则：同一机器（禁缓存）、同一网络节流（Fast 3G / 4G）、同一指标口径（LCP/FCP/TTI/INP），每方案跑 ≥ 5 次取中位数。
- 三方案用同一份页面代码：CSR 直接发；SSR 用框架同构渲染；预渲染用构建期 `renderPreset` 输出静态 HTML。数据接口 mock 成相同延迟，隔离后端变量。
- 对比维度不只首屏：还要看交互可用时间（hydration 完成时间）、TTFB、以及真实弱网下的表现。
- 结论通常是分层的：营销页用预渲染、动态首页用 SSR、登录后应用用 CSR+预取，按页面类型选方案而不是全局一刀切。

```javascript
// 一一对应：Puppeteer 三方案首屏实测对比脚本
const puppeteer = require('puppeteer');

async function bench(url, runs = 5) {
  const browser = await puppeteer.launch();
  const results = [];
  for (let i = 0; i < runs; i++) {
    const page = await browser.newPage();
    await page.setCacheEnabled(false);                    // 禁缓存保证公平
    const client = await page.target().createCDPSession();
    await client.send('Network.emulateNetworkConditions', {
      offline: false, latency: 100,
      downloadThroughput: (1.6 * 1024 * 1024) / 8,        // Fast 3G
      uploadThroughput: (750 * 1024) / 8,
    });
    await page.tracing.start({ categories: ['loading'] });
    await page.goto(url, { waitUntil: 'load' });
    const metrics = await page.evaluate(() => new Promise(resolve => {
      new PerformanceObserver(l => {
        const e = l.getEntries();
        resolve({ lcp: e[e.length - 1].startTime });
      }).observe({ type: 'largest-contentful-paint', buffered: true });
      setTimeout(() => resolve({ lcp: -1 }), 5000);
    }));
    results.push(metrics);
    await page.close();
  }
  await browser.close();
  const sorted = results.map(r => r.lcp).sort((a, b) => a - b);
  return { url, lcp_p50: sorted[Math.floor(runs / 2)], lcp_min: sorted[0], lcp_max: sorted[runs - 1] };
}

(async () => {
  const rows = await Promise.all([           // 串行跑更稳，并发仅示例
    bench('https://staging.example.com/csr/'),
    bench('https://staging.example.com/ssr/'),
    bench('https://staging.example.com/prerender/'),
  ]);
  console.table(rows);
})();
```

## 二十、交互与流畅度
