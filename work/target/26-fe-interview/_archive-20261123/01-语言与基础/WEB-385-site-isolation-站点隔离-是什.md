---
title: [WEB-385] site isolation（站点隔离）是什么？解决了什么安全问题？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-385：site isolation（站点隔离）是什么？解决了什么安全问题？
**答**：
- Chrome 67+ 把不同站点（same-site 粒度）分到不同渲染进程，防止恶意站点进程内读取其他站点数据（如 Spectre 类侧信道）。
- 粒度是 site 而非 origin：bank.com 与 evil.com 不同进程，a.bank.com 与 b.bank.com 可能同进程（配 Origin Isolation 可再细）。
- 代价：进程数暴涨内存开销大；对前端的含义：iframe 跨站点是进程级隔离，通信成本（序列化）更高。

```javascript
// 进程分配（示意）
const processOf = (url) => siteOf(url);  // https://a.bank.com → site bank.com
console.log(processOf('https://evil.com') !== processOf('https://bank.com'));
// 跨进程 iframe → postMessage 走进程间序列化，高频通信要节流
```
