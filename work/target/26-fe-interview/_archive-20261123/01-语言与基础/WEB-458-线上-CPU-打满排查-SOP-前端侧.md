---
title: [WEB-458] 线上 CPU 打满的排查 SOP（前端侧）
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-458：线上 CPU 打满的排查 SOP（前端侧）

**答**：
- 先分类：持续满（死循环/泄漏型计算）还是瞬间尖峰（一次性大计算）；用户侧表现为卡死还是风扇狂转
- 定位脚本循环：Performance 面板录一段，看火焰图主线程顶部的函数栈；线上用 Long Task API（`PerformanceObserver` >50ms）聚合上报脚本 URL 与函数位置
- 常见元凶清单：同步 JSON.parse 大字符串、深层递归（树组件）、正则回溯（ReDoS）、高频 resize/scroll 未节流、动画里做布局读取
- 死循环特判：页面完全冻结时用 DevTools 的 Pause（F8）看当前栈，一击必中
- 治理：重计算搬 Worker、分片 requestIdleCallback、输入节流，并给 CPU 高峰加降级开关

```javascript
new PerformanceObserver(list => {
  list.getEntries().forEach(t => {
    report({ dur: t.duration, name: t.name, attr: t.attribution?.[0]?.scriptURL });
  });
}).observe({ entryTypes: ['longtask'] });
```
