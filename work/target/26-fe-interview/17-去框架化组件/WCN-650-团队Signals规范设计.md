---
title: [WCN-650] 从零为团队设计一套 Signals 使用规范，你会定哪些约定？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-650：从零为团队设计一套 Signals 使用规范，你会定哪些约定？

**答**：
- 结论：规范 = 命名（xxx$ 或 xxxSignal）+ 创建位置（集中 store 而非组件内散落）+ 副作用纪律（必须 onCleanup）+ 异步统一用 resource 模式。
- 补充：禁止在 computed 中做副作用；跨组件共享必须经 context；每个 signal 必须有明确 owner 负责 dispose。
- 追问钩子：如何保证规范落地？用 lint 规则 + code review checklist + 模板脚手架——考察「规范→工具→流程」的闭环思维。

```javascript
// 团队规范示例（以命名与生命周期为核心）
const cartCount$ = signal(0);          // 约定：$ 后缀表示 signal
const cartTotal$ = computed(() => cartCount$.get() * 99);

// 纪律 1：副作用在 effect 内，且必须清理
const stop = effect(() => {
  const n = cartCount$.get();
  return () => { /* 清理订阅/定时器 */ };
});

// 纪律 2：异步统一 resource 模式（三态 + epoch）
const user$ = createResource(userId$, fetchUser);

// 纪律 3：跨组件共享经 context
provideScope(appRoot, { cartCount$, user$ });

// 纪律 4：owner 负责在卸载时 dispose
// component.disconnectedCallback -> stop()
```
