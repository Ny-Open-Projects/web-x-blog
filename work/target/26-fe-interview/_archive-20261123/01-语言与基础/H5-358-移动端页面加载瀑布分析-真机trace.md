---
title: [H5-358] 移动端页面加载瀑布分析与真机 trace
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## H5-358：移动端页面加载瀑布分析与真机 trace

**答**：
- 瀑布三段式：网络段（DNS/TCP/TLS/请求排队）、解析段（HTML/JS/CSS 解析执行）、渲染段（layout/paint/composite）——移动端网络段与 JS 执行都显著慢于桌面
- 排队瓶颈：h1 下同域 6 连接排队、关键资源被非关键资源占道——用 resource timing 的 initiatorType/startTime/queueing 分析，CSS 预加载、JS defer、预连接提示
- JS 执行瓶颈：移动端 JS 执行耗时是桌面 2~5 倍，大 bundle 的 eval 与框架 hydration 是重头——bundle 分析 + 分包 + 按需执行
- 真机 trace 工具：chrome://inspect → Performance 录制（低端安卓首选）、iOS Safari 远程调试；App 内 WebView 部分版本可用 remote debugging
- 优化验证纪律：每项优化跑 AB（或前后同口径对比），指标必须闭环到秒开率/INP，不做「感觉快了」的优化

```javascript
// 排队与执行段自动分析
const rs = performance.getEntriesByType('resource');
const queueSum = rs.reduce((s, e) => s + Math.max(0, e.startTime - (e.requestStart || e.startTime)), 0);
const execSum = rs.filter(e => e.initiatorType === 'script').reduce((s, e) => s + (e.responseEnd - e.responseStart), 0);
beacon({ queueSum, execSum, count: rs.length, slow: rs.filter(e => e.duration > 1000).map(e => e.name) });
```
