---
title: [PER-543] 手写一个多 Tab 内存压力测试脚本：同站开 N 个 Tab，观察总内存增长与跨 Tab 同步延迟
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-543：手写一个多 Tab 内存压力测试脚本：同站开 N 个 Tab，观察总内存增长与跨 Tab 同步延迟

**答**：
- 用 puppeteer 起 N 个 page（同 browserContext 共享存储），每个 Tab 执行同一段业务交互脚本，周期性采集各 Tab 的 `performance.memory.usedJSHeapSize` 与跨 Tab 广播延迟。
- 跨 Tab 同步延迟测法：Tab A 写 localStorage/BroadcastChannel postMessage，Tab B 记录收到时刻，差值即同步延迟。
- 边界：`performance.memory` 仅 Chromium 且有精度限制，标注数据口径；Tab 数超过机器承受时 OS 会交换内存，结果失真，要限 N 并记录环境。
- 评分点：广播延迟测量与内存增长是否回归（增长不回落即泄漏嫌疑）。

```javascript

const puppeteer = require('puppeteer');
async function multiTabStress(n = 8, ticks = 10) {
  const browser = await puppeteer.launch();
  const ctx = await browser.createBrowserContext();
  const pages = await Promise.all(Array.from({ length: n }, () => ctx.newPage()));
  await Promise.all(pages.map(p => p.goto('https://example.com/app', { waitUntil: 'load' })));
  // Tab0 发广播，Tab1 记录接收时刻 -> 测同步延迟
  await pages[0].evaluate(() => new BroadcastChannel('app').postMessage({ t: performance.now() }));
  await pages[1].evaluate(() => new Promise(res => {
    const ch = new BroadcastChannel('app');
    ch.onmessage = ({ data }) => res(performance.now() - data.t);
    setTimeout(() => res(-1), 2000);
  }));
  const snap = [];
  for (let i = 0; i < ticks; i++) {
    await Promise.all(pages.map(p => p.evaluate(() => window.tick?.()))); // 模拟业务交互
    const mems = await Promise.all(pages.map(p => p.evaluate(() =>
      performance.memory ? performance.memory.usedJSHeapSize / 1048576 : -1)));
    snap.push({ tick: i, totalMB: +mems.reduce((s, v) => s + Math.max(0, v), 0).toFixed(1) });
  }
  await browser.close();
  const growth = snap.at(-1).totalMB - snap[0].totalMB;
  return { snap, growthMB: +growth.toFixed(1), leakSuspect: growth > 200 }; // 持续增长不回落
}
multiTabStress().then(console.log);
```
