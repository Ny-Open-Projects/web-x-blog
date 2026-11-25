---
title: [WCN-279] 信号图的内存泄漏审计工具实现要点？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-279：信号图的内存泄漏审计工具实现要点？
**答**：
- 注册表记录所有 effect（创建栈/宿主组件标签/dispose 状态）。
- 审计：无宿主组件引用且未 dispose 的 effect → 泄漏嫌疑；断开组件后信号仍被持有 → 引用链报告。
- 集成：开发面板实时图（订阅数/泄漏数），CI 里内存回归测试（场景循环后审计计数不增）。
- heapdump 对照：leaked effect 与 detached DOM 关联定位。

```javascript
function auditLeaks() {
  return registry.effects.filter(e => !e.disposed && !e.ownerComponent)
    .map(e => ({ name: e.debugName, stack: e.createdStack.slice(0, 3) }));
}
r
```
