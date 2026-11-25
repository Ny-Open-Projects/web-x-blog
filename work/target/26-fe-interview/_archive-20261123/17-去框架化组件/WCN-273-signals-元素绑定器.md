---
title: [WCN-273] WC 场景的信号↔元素绑定器（bind(el, signal) 双向工具）实现？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-273：WC 场景的信号↔元素绑定器（bind(el, signal) 双向工具）实现？
**答**：
- 单向：effect(() => el.value = sig.value)（值比对防回环）。
- 反向：监听元素 input/change → sig.value = el.value。
- 双向回环防护：写前比对 + 写期间静默标志。
- 销毁：返回 dispose（effect dispose + 移除监听）。

```javascript
function bind(el, sig) {
  const stop = effect(() => { if (el.value !== sig.value) el.value = sig.value; });
  const h = () => { sig.value = el.value; };
  el.addEventListener('input', h);
  return () => { stop(); el.removeEventListener('input', h); };
}
r
```
