---
title: [PER-546] 手写一个 CLS 回归测试：自动化模拟关键交互，断言列表、弹层、图片位不产生布局偏移
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-546：手写一个 CLS 回归测试：自动化模拟关键交互，断言列表、弹层、图片位不产生布局偏移

**答**：
- 原理：PerformanceObserver 收集 `layout-shift` entries（过滤 `hadRecentInput`），驱动一组已知会引发偏移的交互（图片懒加载、弹层插入、字体交换），断言累计 CLS 低于阈值。
- 要点：交互之间要等 settle（图片加载完/弹层动画结束）再统计，避免把合法动画计成回归；用 `sources` 字段归因到具体元素定位问题。
- 边界：动画类 transform 位移不算 layout-shift，测试误报通常是断言脚本自己的注入元素没预留占位。
- 评分点：hadRecentInput 过滤与 sources 归因。

```javascript

const puppeteer = require('puppeteer');
async function clsRegression(url) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'networkidle2' });
  // 在页面里安装探针
  const collect = await page.evaluate(() => {
    window.__shifts = [];
    new PerformanceObserver(l => l.getEntries().forEach(e => {
      if (!e.hadRecentInput) window.__shifts.push({   // 用户主动输入引起的偏移不背锅
        value: e.value,
        src: e.sources?.[0]?.node?.className ?? 'unknown', // 归因到元素
      }));
    })).observe({ type: 'layout-shift', buffered: true });
    return true;
  });
  // 驱动关键交互
  await page.click('[data-testid="load-more"]');
  await page.waitForTimeout(1200);                       // 等异步图加载完
  await page.click('[data-testid="open-modal"]');
  await page.waitForTimeout(600);
  const cls = await page.evaluate(() => window.__shifts.reduce((s, e) => s + e.value, 0));
  const top = await page.evaluate(() => window.__shifts.sort((a, b) => b.value - a.value)[0]);
  await browser.close();
  return { cls: +cls.toFixed(4), pass: cls < 0.1, topSource: top?.src }; // 阈值 CWV 0.1
}
clsRegression('https://example.com/list').then(console.log);
```
