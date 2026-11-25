---
title: [WCN-638] Signal 的 effect 如何与 AbortController 配合做取消与清理？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-638：Signal 的 effect 如何与 AbortController 配合做取消与清理？

**答**：
- 结论：effect 每次重跑前应清理上一次的副作用（onCleanup），异步请求用 AbortController 取消，防止过期回调写状态。
- 做法：effect(fn) 支持 fn 返回清理函数；重跑前先执行旧清理；把 controller.abort 放进清理函数。
- 追问钩子：忘记清理会怎样？内存泄漏 + 竞态写入——面试官常追问「你在项目里怎么排查泄漏」，要能答出用 WeakMap 观测 effect 存活。

```javascript
function effect(fn) {
  let cleanup = null;
  const run = () => {
    cleanup?.(); // 重跑前先清理上一次
    cleanup = fn() || null; // fn 可返回新的清理函数
  };
  run();
  return () => { cleanup?.(); }; // 外部可手动 dispose
}
const url = signal('/a');
const stop = effect(() => {
  const ctrl = new AbortController();
  fetch(url.get(), { signal: ctrl.signal }).then(r => r.json());
  return () => ctrl.abort(); // url 变化前取消旧请求
});
url.set('/b'); // 自动 abort /a 请求
// stop(); // 组件卸载时彻底清理
```
