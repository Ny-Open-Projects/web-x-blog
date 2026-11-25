---
title: [WCN-408] 笔试：实现 effect 的 onCleanup（重跑前清理）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-408：笔试：实现 effect 的 onCleanup（重跑前清理）。
**答**：effect(fn) 内可调用 onCleanup(cb)：下次重跑前执行 cb；effect dispose 时也执行。

```javascript
let currentEffect = null;
const cleanups = new WeakMap();
export function effect(fn) {
  const node = makeEffectNode();
  node.run = () => {
    (cleanups.get(node) || []).forEach(cb => cb());   // 先清上次
    cleanups.set(node, []);
    currentEffect = node;
    try { fn(); } finally { currentEffect = null; node.dirty = false; }
  };
  node.dispose = () => { (cleanups.get(node) || []).forEach(cb => cb()); detach(node); };
  node.run();
  return node.dispose;
}
export function onCleanup(cb) {
  if (currentEffect) cleanups.get(currentEffect).push(cb);
  else console.warn('onCleanup 必须在 effect 同步体内调用');
}

```

**评分点**：
- cleanup 挂当前 effect 上下文（栈顶）。
- 重跑顺序：cleanup → 新 fn。
- dispose：cleanup + 断依赖。
- 栈式嵌套 cleanup 顺序（后进先出）。
