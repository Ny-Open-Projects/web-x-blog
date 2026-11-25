---
title: [WCN-795] 大型平台中「编译响应式 + Signals + WC」混合架构的边界与取舍是什么？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-795：大型平台中「编译响应式 + Signals + WC」混合架构的边界与取舍是什么？

**答**：
- 结论：三者解决不同问题且可互补——编译响应式优化「模板渲染性能」，Signals 管「细粒度状态」，WC 提供「跨框架封装与隔离」；关键是明确每层职责与数据流向，避免能力重叠。
- 典型组合：编译框架生成渲染代码、内部用 signals 驱动更新、对外输出 WC 供其他框架消费；边界上要防止「同一个状态被两套响应式系统管理」导致双重更新。
- 追问钩子：如何在团队中落地这种混合架构而不失控？考察「分层规范 + 单一数据源 + 边界测试」的治理手段。

```javascript
// 混合架构数据流：token -> signal(state) -> 编译渲染 -> WC 对外
const state = signal({ qty: 1 });
const derived = computed(() => state.value.qty * 2);   // Signals 派生
function render() { return `<ds-badge>${derived.value}</ds-badge>`; } // 编译产物
// WC 对外隔离，内部不重复持有同一状态
class DsBadge extends HTMLElement { connectedCallback() { this.attachShadow({ mode:'open' }); } }
console.log('单一数据源，避免双重响应式管理');
```
