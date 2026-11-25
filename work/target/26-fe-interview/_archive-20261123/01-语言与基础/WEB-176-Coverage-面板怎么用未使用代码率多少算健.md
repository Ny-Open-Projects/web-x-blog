---
title: [WEB-176] Coverage 面板怎么用？未使用代码率多少算健康？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-176：Coverage 面板怎么用？未使用代码率多少算健康？
**答**：
- 命令面板搜 Coverage 录制页面加载与交互，统计 JS/CSS 的字节级使用率：绿色已用、红色未用。
- 两个数字分开看：首屏未用率（影响加载性能）与全程未用率（影响维护成本）；首屏未用率超过一半通常意味着该拆包。
- CLI 化：Puppeteer 的 page.coverage 可进 CI 做未用代码率门禁。
- 行动项：路由级 code splitting、组件库按需引入、检查 tree-shaking 是否被 CJS 依赖破坏。

```javascript
// Puppeteer 在 CI 中量化未使用代码率
const page = await browser.newPage();
await page.coverage.startJSCoverage();
await page.goto('https://app.example.com', { waitUntil: 'networkidle0' });
const js = await page.coverage.stopJSCoverage();
for (const e of js) {
  const total = e.text.length;                                     // 文件总字节
  const used = e.ranges.reduce((s, r) => s + (r.end - r.start), 0); // 执行到的字节
  const ratio = (used / total * 100).toFixed(1);
  if (total > 100000 && used / total < 0.5) console.log('候选拆分:', e.url, `${ratio}%`);
}
```
