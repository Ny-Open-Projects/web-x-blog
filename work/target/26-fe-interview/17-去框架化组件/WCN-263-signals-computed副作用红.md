---
title: [WCN-263] 为什么 computed 必须无副作用？违规的实际后果？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-263：为什么 computed 必须无副作用？违规的实际后果？
**答**：
- computed 可能被惰性跳过（无订阅者不算）——副作用执行次数不确定，逻辑崩坏。
- 并发/批处理下 computed 可能重算多次——副作用重复执行。
- 正确做法：副作用进 effect（有明确执行次数语义）；computed 只做纯派生。
- lint 层面：编译器检测 computed 内的写操作/DOM 访问并告警。

```javascript
// 反例：computed 里发请求（次数不可控）
const total = computed(() => { fetch('/log'); return a() + b(); });   // ✗
// 正例：computed 纯派生 + effect 副作用
const total = computed(() => a() + b());
effect(() => { report(total.value); });                                // ✓ 次数确定
r
```
