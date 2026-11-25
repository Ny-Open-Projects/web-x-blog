---
title: [PER-053] LCP 的候选元素规则和失效规则是什么？为什么 LCP 可能越优化越差？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-053：LCP 的候选元素规则和失效规则是什么？为什么 LCP 可能越优化越差？

**答**：
- LCP 候选仅限 `<img>`、`<image>`（SVG 内）、`<video>` 的封面帧、带背景图的元素、**包含文本节点的块级元素**；先渲染较小候选，后续更大的元素出现时会**更新候选**。
- 失效/停止规则：候选元素从 DOM 移除、变成 `visibility: hidden`、或用户发生**第一次真实交互**（点击/按键）后 LCP 定格，此后新内容不再参与。
- “越优化越差”的经典坑：把首屏大图改成懒加载后，浏览器选中了下方一段**长文本块**当候选，文本又依赖字体和 JS 渲染，LCP 反而变慢。
- 结论：LCP 优化要盯“浏览器最终会选谁”，用 `PerformanceObserver` 观察候选变化再决定 preload 什么。

```javascript
// 观察 LCP 候选元素的变化，弄清浏览器到底在等谁
new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const latest = entries[entries.length - 1];
  console.log('当前 LCP 候选：', latest.element, '时间：', latest.startTime);
  console.log('加载相关耗时：', {
    ttfb: latest.responseStart - latest.startTime,      // 图片从发起请求到响应头
    loadDelay: latest.loadTime - latest.startTime,       // 资源加载耗时
    renderDelay: latest.renderTime - latest.loadTime,    // 加载完成到上屏
  });
  // 若 element 是一段文本而非图片，说明大图被跳过或未被视为候选
}).observe({ type: 'largest-contentful-paint', buffered: true });

// 用户第一次点击后 LCP 定格 —— 交互不能是首屏渲染路径的一部分
window.addEventListener('pointerdown', () => console.log('LCP 从此定格'), { once: true });
```
