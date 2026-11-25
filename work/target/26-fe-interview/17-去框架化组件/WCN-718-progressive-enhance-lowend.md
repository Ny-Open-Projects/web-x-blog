---
title: [WCN-718] WC 组件在弱网/低端机上如何做渐进增强与加载优先级？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-718：WC 组件在弱网/低端机上如何做渐进增强与加载优先级？

**答**：
- 结论：核心功能用轻量 HTML/CSS 打底，WC 脚本异步加载并 `customElements.whenDefined` 后增强；非首屏组件用 IntersectionObserver 懒加载。
- 用 `loading=lazy`、resource hints（preconnect/prefetch）控制优先级；低端机通过 `navigator.hardwareConcurrency`/`deviceMemory` 降级动画与虚拟列表规模。
- 追问钩子：脚本还没加载完时用户点击了按钮怎么办？考察「占位态 + 事件缓冲 + 升级后重放」

```javascript
// 渐进增强：先显示静态骨架，定义后增强
function enhance(root) {
  const btn = root.querySelector('ds-button');
  if (customElements.get('ds-button')) return;
  const placeholder = document.createElement('button');
  placeholder.textContent = btn?.textContent || '加载中';
  btn?.replaceWith(placeholder);
  customElements.whenDefined('ds-button').then(() => {
    const real = document.createElement('ds-button');
    real.textContent = placeholder.textContent;
    placeholder.replaceWith(real);
  });
}
const lowEnd = (navigator.hardwareConcurrency || 4) <= 2;
console.log('低端机降级动画:', lowEnd);
```
