---
title: [PER-539] 手写一个页面变体（A/B 两套实现）的性能对比采样工具：输出带置信度的对比结论
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-539：手写一个页面变体（A/B 两套实现）的性能对比采样工具：输出带置信度的对比结论

**答**：
- 比 512 的回归工具更进一步：两变体同批交叉采样后，给出统计意义上的结论——样本量要足够，用均值差与标准差估算置信区间（简化 t 检验）。
- 要点：变体切换用 query 参数强制命中，两个变体 URL 同批交替跑；结论分级"显著回归/显著改善/无法区分"，无法区分时给出需要继续采样的建议次数。
- 边界：标准差过大时提示先治理环境噪声而不是硬出结论。
- 评分点：简化显著性判断（均值差 > 2 倍合并标准差）与样本量建议。

```javascript

const puppeteer = require('puppeteer');
async function sampleOnce(browser, url) {
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'load', timeout: 30000 });
  const lcp = await page.evaluate(() => new Promise(res => {
    new PerformanceObserver(l => res(l.getEntries().at(-1)?.startTime ?? -1))
      .observe({ type: 'largest-contentful-paint', buffered: true });
    setTimeout(() => res(-1), 12000);
  }));
  await page.close();
  return lcp;
}
function mean(a) { return a.reduce((s, v) => s + v, 0) / a.length; }
function sd(a) { const m = mean(a); return Math.sqrt(a.reduce((s, v) => s + (v - m) ** 2, 0) / (a.length - 1)); }

async function abCompare(urlA, urlB, runs = 20) {
  const browser = await puppeteer.launch();
  const A = [], B = [];
  for (let i = 0; i < runs; i++) {                    // 交替采样消时段效应
    A.push(await sampleOnce(browser, urlA));
    B.push(await sampleOnce(browser, urlB));
  }
  await browser.close();
  const [mA, mB] = [mean(A), mean(B)], se = Math.sqrt(sd(A) ** 2 / A.length + sd(B) ** 2 / B.length);
  const diff = mB - mA, significant = Math.abs(diff) > 2 * se;   // 简化显著性
  const verdict = !significant ? { v: '无法区分', need: Math.ceil(runs * 2) } // 建议加样本
    : diff < 0 ? { v: 'B 显著更快' } : { v: 'B 显著更慢(回归)' };
  return { mA: Math.round(mA), mB: Math.round(mB), diffMs: Math.round(diff), ...verdict };
}
abCompare('https://x.com/?v=a', 'https://x.com/?v=b').then(console.log);
```
