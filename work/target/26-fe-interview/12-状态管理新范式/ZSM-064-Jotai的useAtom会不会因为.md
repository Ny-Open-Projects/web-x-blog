---
title: [ZSM-064] Jotai 中两个组件订阅同一 atom，一个写了值，另一个会重渲染吗？依赖链怎么传播？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-064：Jotai 中两个组件订阅同一 atom，一个写了值，另一个会重渲染吗？依赖链怎么传播？
**答**：
- 会：写触发该 atom 通知，所有订阅者（含间接派生依赖者）收到失效信号，重算并按「新值与旧值 Object.is 相等则不渲染」收敛。
- 传播路径：base atom 变 → 直接派生重算 → 派生的派生……每层只通知值真正变化的分支；依赖图保证最小集。
- 写者自身：useSetAtom 的组件不订阅值，不渲染；useAtom 解构了 value 的会渲染。
- 若写的新值 Object.is 相等（如 set 同一引用），整条链静默，这也是不可变更新的意义。

```javascript
const a = atom(1)
const b = atom(g => g(a) * 2)   // 依赖 a
// 组件A: useAtomValue(b)；组件B: useSetAtom(a)
// B 写 a=2 → a 通知 → b 失效重算=4 → A 渲染（值变了）
// B 写 a=1（相同值）→ a 通知但 b 重算结果仍为 2 → b 无渲染通知，A 不动
```
