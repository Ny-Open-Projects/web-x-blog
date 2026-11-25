---
title: [WCN-079] Signals 常见的坑有哪些？丢失依赖、内存泄漏、无限循环怎么排查？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-079：Signals 常见的坑有哪些？丢失依赖、内存泄漏、无限循环怎么排查？

**答**：
- 丢失依赖：① 在 effect 外解构读取（`const v = sig.value` 后只用了局部变量）不追踪；② 条件分支首次未执行则该分支内 signal 不在依赖里（这是特性，但容易当成 bug）；③ 异步回调（setTimeout 内）读取 signal 时 activeSub 已恢复为 null，不建立依赖。
- 内存泄漏：effect 未 dispose——元素销毁后仍订阅全局 signal；排查用 devtools Memory 快照查 detached 节点的 retainer，或给 signal 加 subscriber 计数日志。
- 无限循环：effect 内写入自己依赖的 signal（无相等短路时）；或 computed A 依赖 B、B 反向写 A。排查：给 effect 打序号日志看重复执行模式。
- 调试工具：`Signal.debug(sig)`（部分库提供）打印订阅链；自实现里可加 `onSubscribe/onUnsubscribe` 钩子。
- 预防约定：effect 只做"同步状态→视图"，业务副作用（请求/路由）放事件回调或 resource；写入尽量在用户意图处（事件）而非 effect。

```javascript
const count = signal(0);

// 坑 1：异步回调丢失依赖
effect(() => {
  setTimeout(() => {            // activeSub 已为 null
    console.log(count.value);   // 读到了值，但 count 不再是依赖！
  }, 0);
});

// 正确：同步读出再异步使用
effect(() => {
  const v = count.value;        // 同步读取，建立依赖
  setTimeout(() => console.log('stable:', v), 0);
});
```
