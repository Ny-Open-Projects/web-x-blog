---
title: [CSS-181] 如何用 CSS 变量做 JS 与 CSS 的通信接口？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-181：如何用 CSS 变量做 JS 与 CSS 的通信接口？

**答**：
- 变量是天然的双向总线：JS → CSS 下发配置（主题/密度/尺寸），CSS → JS 回读当前值（JS 逻辑与 CSS 布局用同一 token）。
- 变量有继承：设在父组件实例上的变量只影响子树，天然支持“组件级配置”而无需 prop 钻透到 CSS。
- 配合 @property 注册类型后，变量本身可 transition，主题切换能带动画。
- 相比 JS 直改 style 属性：变量不破坏组件封装、SSR 安全、可被 DevTools 检视。

```javascript
// JS → CSS：配置下发
function applyConfig({ primary, radius, density }) {
  const s = document.documentElement.style;
  s.setProperty('--brand', primary);
  s.setProperty('--radius', radius + 'px');
  s.dataset.density = density;          // 非数值配置走 data 属性
}

// 组件实例级下发：变量继承，只影响子树
card.style.setProperty('--elevation', '3');

// CSS → JS：回读同一 token，JS 动画与 CSS 布局共用一套尺寸
const gap = parseFloat(
  getComputedStyle(document.body).getPropertyValue('--gap')
);
drawer.style.transform = `translateX(-${gap * 2}px)`;

// 响应式读取：ResizeObserver + 变量，让 JS 行为跟随 CSS 布局
const ro = new ResizeObserver(entries => {
  const w = entries[0].contentRect.width;
  list.classList.toggle('is-compact', w < parseFloat(
    getComputedStyle(list).getPropertyValue('--compact-at') || 320
  ));
});
ro.observe(list);
```
