---
title: [WCN-507] 元素库接入统一埋点 SDK：如何在不侵入业务代码前提下自动采集元素曝光/点击？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-507：元素库接入统一埋点 SDK：如何在不侵入业务代码前提下自动采集元素曝光/点击？

**答**：
- 结论：用全局事件委托 + MutationObserver 自动识别带 data-track 的元素，业务零改动。
- 曝光用单例 IntersectionObserver，threshold 分级（0 / 0.5 / 1），进入视口上报一次。
- 点击走 composedPath 穿透 Shadow DOM 归因到宿主元素，取 data-track-id 作为事件标识。
- 追问：动态插入的元素如何自动接管？（答：MutationObserver 监听 subtree 新增节点并注册观察）

```javascript
const io = new IntersectionObserver(entries => {
  for (const e of entries) if (e.isIntersecting) {
    track('exposure', e.target.dataset.trackId); io.unobserve(e.target);
  }
}, { threshold: [0, 0.5, 1] });
function observe(root = document) {
  root.querySelectorAll('[data-track-id]').forEach(el => io.observe(el));
}
document.addEventListener('click', e => {
  const el = e.composedPath().find(n => n.dataset?.trackId);
  if (el) track('click', el.dataset.trackId);
}, true);
new MutationObserver(() => observe()).observe(document.body, { childList: true, subtree: true });
```
