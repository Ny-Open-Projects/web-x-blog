---
title: [FRP-165] @preact/signals 是怎么把 signals 接入 vdom 框架的（绕过组件重渲）？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-165：@preact/signals 是怎么把 signals 接入 vdom 框架的（绕过组件重渲）？

**答**：
- 关键机制：Preact 的 diff 时检测到 vnode 属性/文本位置的值是 **signal 实例**，就把该 DOM 位置**直接订阅**到 signal——signal 变化时直接更新对应 textContent/属性，**完全不经过组件重渲与 diff**。
- 因此更新粒度是"绑定级"的：一个 signal 变化只改它绑定的那几个 DOM 节点，组件函数都不执行。
- signal 的引用稳定性带来第二个收益：把 signal 当 prop 传递**不会破坏 memo**（引用永不变，比较恒等）。
- React 版本的折中：React 没有渲染器的"绑定"入口，只能用 useSyncExternalStore 桥接——订阅在组件级，粒度退回到"读到该 signal 的组件重渲"。

```javascript
// 简化实现，帮助理解 signal 绑定到 vnode 的原理
const count = signal(0);   // signal(1): { value getter/setter + subs }

// —— 渲染器侧：diff 时识别 signal 并建立"绑定" ——
function diffProps(dom, newProps, oldProps) {
  for (const key in newProps) {
    const v = newProps[key];
    if (isSignal(v)) {
      // 不把 signal.value 写死，而是订阅：signal 变化直接操作这个 DOM 节点
      subscribeSignal(v, () => {
        if (key === 'children') dom.textContent = v.value;       // 文本绑定
        else if (key.startsWith('on')) { /* 事件重新挂接 */ }
        else dom.setAttribute(key, v.value);                     // 属性绑定
      });
      // 立即初始化一次
      if (key === 'children') dom.textContent = v.value;
    } else if (v !== oldProps?.[key]) {
      dom.setAttribute(key, v);   // 普通值：走正常 diff
    }
  }
}

function subscribeSignal(sig, updateFn) {
  sig.subs.add(updateFn);
}
// signal 的 set：只通知订阅者（都是"直接改 DOM"的函数），没有组件级重渲
function setSignal(sig, v) {
  if (sig._v === v) return;
  sig._v = v;
  sig.subs.forEach(fn => fn());
}

// —— 组件层：signal 组件只在首次渲染执行一次 ——
function Counter() {
  // 组件函数读取 count 的位置是 jsx 表达式 —— 不是组件体内读取，
  // 所以组件不订阅 count；订阅发生在渲染器的 props diff 里
  return <div>Count is {count}</div>;
}
// count.value++ 时：跳过 Counter、跳过 diff，直接 dom.textContent = 新值
// 对比 React：setCount -> 整个 Counter 重渲 -> reconciliation -> 才改到文本

// —— React 版本的妥协 ——
function useSignal(sig) {
  return useSyncExternalStore(
    cb => sig.subs.add(cb),      // 订阅
    () => sig.value              // 快照
  );  // 粒度是"调用 useSignal 的组件"，因为 React 渲染器没有绑定入口
}
```
