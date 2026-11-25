---
title: [WCN-252] Signals 作为「组件外全局状态」与「组件内局部状态」的边界划分？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-252：Signals 作为「组件外全局状态」与「组件内局部状态」的边界划分？
**答**：
- 全局信号：跨组件共享的真·全局态（购物车/主题/会话）。
- 局部信号：组件实例私有（挂在组件上下文，随组件销毁释放）。
- 误用信号：把「组件局部状态」也全局化 → 内存泄漏 + 命名冲突。
- 规范：信号命名空间 + 所有权声明（谁创建谁销毁）。

```javascript
// 全局（显式命名空间）
export const cartSignals = { items: signal<Item[]>([]), total: computed(...) };
// 局部（组件作用域创建，随组件释放）
function useLocalState(init) {
  const s = signal(init);
  onDispose(() => s.dispose?.());   // 绑定生命周期
  return s;
}
r
```
