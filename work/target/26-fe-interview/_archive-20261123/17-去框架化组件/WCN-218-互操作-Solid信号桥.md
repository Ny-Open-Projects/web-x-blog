---
title: [WCN-218] Solid 的信号（Signals）与自定义元素的双向绑定桥接实现？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-218：Solid 的信号（Signals）与自定义元素的双向绑定桥接实现？
**答**：
- 元素 property 变化 → 元素派发 input/change 事件 → Solid createEffect 更新信号。
- 信号 → 元素：createEffect 里写 property。
- 桥接组件封装双向（避免循环触发：写 property 前比对值）。
- 通用化：抽「signalBridge(el, propsMap)」工具函数，所有元素复用。

```javascript
function signalBridge(el: any, get: () => any, set: (v: any) => void) {
  createEffect(() => { const v = get(); if (el.value !== v) el.value = v; });  // 防回环
  const h = () => set(el.value);
  el.addEventListener('input', h);
  onCleanup(() => el.removeEventListener('input', h));
}
r
```
