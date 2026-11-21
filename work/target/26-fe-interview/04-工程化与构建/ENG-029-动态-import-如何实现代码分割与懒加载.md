---
title: [ENG-029] 动态 import 如何实现代码分割与懒加载？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-029：动态 import 如何实现代码分割与懒加载？
**答**：
- `import()` 返回 Promise，构建工具据此生成独立 chunk，运行到该行才发起加载。
- 与 React.lazy、路由懒加载是同一机制的上层封装。
- 魔法注释可自定义 chunk 名（webpackChunkName）或预取（webpackPrefetch/preload）。
- 分割策略：按路由拆页面，按交互时机拆重组件，按访问概率决定 prefetch。

```javascript
// 点击时才加载图表库及其依赖 chunk
document.getElementById('load-chart')?.addEventListener('click', async () => {
  const { renderChart } = await import('./chart');
  renderChart();
});

// 魔法注释：自定义 chunk 名，构建产物可读性更好
const analytics = await import(
  /* webpackChunkName: "analytics" */ './analytics'
);
```
