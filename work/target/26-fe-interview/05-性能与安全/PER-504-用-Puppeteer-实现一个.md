---
title: [PER-504] 用 Puppeteer 实现一个性能门禁脚本：跑 Lighthouse、注入 CPU 节流并对指标做阈值裁决
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-504：用 Puppeteer 实现一个性能门禁脚本：跑 Lighthouse、注入 CPU 节流并对指标做阈值裁决

**答**：
- 面试官想看的不是 API 背诵，而是**测试流水线的骨架**：启动受控浏览器 → 节流 → 采样多次 → 聚合 → 与阈值比较 → 非零退出码阻断合并。
- 关键点：`lighthouse` 以编程方式调用而不是 CLI，才能拿到结构化结果并自定义断言；多次采样取中位数防抖动。
- 边界处理：页面加载失败要重试并最终 fail；指标缺失（如 LCP 未产生）要视为不通过而不是 0 分通过。
- 评分点看是否处理了"退出码"——门禁的价值就在 CI 红灯。

```javascript

const puppeteer = require('puppeteer');
const { launch: launchChrome } = require('chrome-launcher');
const lighthouse = require('lighthouse');

const BUDGET = { lcp: 2500, tbt: 300, cls: 0.1 };

async function audit(url, { runs = 3 } = {}) {
  const chrome = await launchChrome({ chromeFlags: ['--headless'] });
  const results = [];
  for (let i = 0; i < runs; i++) {
    const { lhr } = await lighthouse(url, {
      port: chrome.port,
      emulatedFormFactor: 'mobile',
      throttling: { cpuSlowdownMultiplier: 4, requestLatencyMs: 150 }, // 受控节流
    });
    const a = lhr.audits;
    results.push({
      lcp: a['largest-contentful-paint']?.numericValue ?? Infinity, // 缺失视为不通过
      tbt: a['total-blocking-time']?.numericValue ?? Infinity,
      cls: a['cumulative-layout-shift']?.numericValue ?? 1,
    });
  }
  await chrome.kill();
  const med = (arr) => arr.sort((x, y) => x - y)[Math.floor(arr.length / 2)];
  return {
    lcp: med(results.map(r => r.lcp)),
    tbt: med(results.map(r => r.tbt)),
    cls: med(results.map(r => r.cls)),
  };
}

(async () => {
  const m = await audit('https://example.com');
  const fails = Object.entries(BUDGET).filter(([k, v]) => m[k] > v);
  console.table(m);
  if (fails.length) { console.error('性能门禁未通过:', fails); process.exit(1); } // CI 红灯
})();
```
