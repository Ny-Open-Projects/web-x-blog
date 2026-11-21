---
title: [ZSM-362] 状态库（store 订阅）与 Signals 的本质差异是什么
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-362：状态库（store 订阅）与 Signals 的本质差异是什么

**答**:
- 粒度模型：store 是「组件级订阅」——变化通知到组件，组件重渲染后靠 selector/比较跳过；Signal 是「值级订阅」——绑定处直接精准更新，跳过组件函数重跑
- 依赖发现：store 靠开发者显式写 selector；Signal 运行时自动收集（读即依赖）
- 更新语义：store + React 不可变模型（新引用触发）；Signal 可变写入 + 自动传播，天然免引用陷阱
- 集成差异：store 接 React 走 useSyncExternalStore（合规并发安全）；Signal 接 React 需桥接且与并发渲染的交互更微妙（写时机限制）
- 面试答法：先讲「订阅粒度」这一根本差异，再谈各自的成本（selector 心智 vs 自动依赖的隐性开销），最后给选型（React 生态 store 成熟；多框架/细粒度更新场景 Signal 有优势）

```javascript
// 同一需求两种模型
// store：显式 selector
const count = useStore((s) => s.count)
// signal：读即依赖
const count = useSignal(counter)     // 只有绑定处更新，组件函数不重跑
```
