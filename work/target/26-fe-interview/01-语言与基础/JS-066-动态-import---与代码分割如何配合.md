---
title: [JS-066] 动态 import() 与代码分割如何配合？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-066：动态 import() 与代码分割如何配合？

**答**：
- `import(path)` 返回 Promise，运行时按需加载，可在任何位置调用（含条件与循环内）。
- 打包器据此切分 chunk：路由级懒加载、大依赖（编辑器、图表库）按需加载。
- 配合 webpack 的 magic comment 控制命名与预加载（webpackChunkName / prefetch）。
- 失败可 catch 并降级重试，适合做微前端/插件系统。

```javascript
// 路由懒加载
const routes = [
  { path: '/admin', component: () => import('./views/Admin.vue') },
];

// 交互触发的大依赖
button.addEventListener('click', async () => {
  try {
    const { default: Chart } = await import(
      /* webpackChunkName: "chart" */ './lib/chart.js'
    );
    new Chart(container, data);
  } catch (e) {
    console.error('chunk load failed, retry...');
  }
});

// 条件加载
if (window.matchMedia('(hover: hover)').matches) {
  await import('./hover-effect.js');
}
```

## 十、手写实现
