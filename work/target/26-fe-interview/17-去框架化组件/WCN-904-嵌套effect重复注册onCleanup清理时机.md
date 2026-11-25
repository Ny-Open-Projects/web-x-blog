---
title: [WCN-904] effect 里再创建 effect，依赖变化时怎么避免重复注册（onCleanup 时机深水）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-904：effect 里再创建 effect，依赖变化时怎么避免重复注册（onCleanup 时机深水）

**答**：
- 结论先行：嵌套 effect 的清理函数是「下一次 effect 重新执行前」调用，利用这个时机先 dispose 旧的子 effect，就不会累积重复注册。
- 常见坑：在 effect 回调里直接 `effect(() => ...)`，父依赖每次变化都会新建子 effect，旧的子 effect 仍在订阅 → 内存泄漏 + 回调重复执行。
- 正确写法：用 `onCleanup(() => childDispose())`（Solid）或返回清理函数，确保重建前先释放；动态 key 列表用 Map 缓存子 effect，key 消失时清理。
- WC 组件里尤其关键：connectedCallback 创建 effect、disconnectedCallback 释放；属性 signal 变化触发重建时，务必先清理上一批监听，避免 reattach 后重复绑定事件（微前端多实例场景）。
- 追问钩子：追问「清理里又写 signal 会怎样」——答：清理阶段写可能触发新的调度，通常应只做释放；确需复位用 queueMicrotask 延后，避免同步重入。

```javascript
// Solid 风格：onCleanup 释放嵌套 effect
import { createSignal, createEffect, onCleanup, createRoot } from 'solid-js';
const [userId, setUserId] = createSignal(1);

createEffect(() => {
  const id = userId(); // 父依赖
  const dispose = createRoot(dispose => {
    createEffect(() => {
      const data = fetchUser(id); // 子 effect 依赖 id
      const timer = setInterval(() => refresh(data), 1000);
      onCleanup(() => clearInterval(timer)); // id 变化时先清 timer
    });
    return dispose;
  });
  onCleanup(() => dispose()); // 父重建前先释放整个子 root
});
setUserId(2); // 旧Interval 被清，不泄漏
```
