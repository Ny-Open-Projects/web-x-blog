---
title: [WCN-416] 笔试：实现 WC 元素与信号的双向绑定器（bind(el, signal)）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-416：笔试：实现 WC 元素与信号的双向绑定器（bind(el, signal)）。
**题目**：双向：signal→el.value（effect，值比对防回环）；el input/change 事件→signal。返回 dispose（断 effect + 移除监听）。

```javascript
function bind(el, sig, { event = 'input' } = {}) {
  const stop = effect(() => { if (el.value !== sig.get()) el.value = sig.get(); });
  const h = () => sig.set(el.value);
  el.addEventListener(event, h);
  return () => { stop(); el.removeEventListener(event, h); };
}
// WC: <ds-input> → bind(el, nameSignal, { event: 'change' })

```

**评分点**：
- 回环防护：effect 写前比对（el.value !== sig.value）。
- 事件监听 {el, 'input'} → sig.set。
- dispose 完整（effect + listener）。
- 自定义事件名可配（change/checked 等）。
