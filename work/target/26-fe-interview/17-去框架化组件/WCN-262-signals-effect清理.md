---
title: [WCN-262] effect 的清理（dispose）与重新运行（cleanup 函数）语义？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-262：effect 的清理（dispose）与重新运行（cleanup 函数）语义？
**答**：
- 每次 effect 重跑前执行上次的 cleanup（清理订阅/DOM/定时器）——与 React useEffect 语义对齐。
- dispose（永久销毁）：从依赖图移除节点，断开订阅链——必须显式调用（组件卸载时）。
- 清理注册：effect(fn) 内 onCleanup(cb) 捕获当前 effect 上下文。
- 泄漏审计：开发工具列出「无宿主的存活 effect」（已脱离组件但未销毁）。

```javascript
effect(() => {
  const sub = store.subscribe(render);
  onCleanup(() => sub.unsubscribe());   // 每次重跑前清理上次订阅
});
// 组件卸载：dispose(effectNode) → 从图中摘除
r
```
