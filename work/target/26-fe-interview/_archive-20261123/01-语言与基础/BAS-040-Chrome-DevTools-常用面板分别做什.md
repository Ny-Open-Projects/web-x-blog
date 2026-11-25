---
title: [BAS-040] Chrome DevTools 常用面板分别做什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-040：Chrome DevTools 常用面板分别做什么？
**答**：
- Elements：审查 DOM 与样式；Console：执行脚本、看日志报错。
- Sources：断点调试；Network：请求瀑布、耗时、载荷、过滤。
- Performance：火焰图定位卡顿；Memory：堆快照查泄漏；Application：Storage、Service Worker、Cookie；Lighthouse：性能评分。

```javascript
// Network 面板过滤框支持的常用语法（直接输入）：
// is:running        只看进行中的请求
// larger-than:50K   响应大于 50KB 的请求
// method:POST       按请求方法过滤
// status-code:4xx   按状态码过滤
console.log('以上关键字直接输入 Network 过滤框即可');
```
