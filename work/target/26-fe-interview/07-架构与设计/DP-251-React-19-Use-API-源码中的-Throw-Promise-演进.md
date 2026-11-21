---
title: [DP-251] 源码识别：React 19 use() 源码中的信号与缓存？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-251：源码识别：React 19 use() 源码中的信号与缓存？
**答**:
- use(promise) 是 DP-213 throw promise 机制的正式 API 化：promise throw 给 Suspense 捕获、resolve 后继续渲染——"信号控制流"从约定变成一等公民。
- 条件调用能力：use 可以在 if/循环里用（不像 hooks 顺序约束）——因为它不是状态槽而是"读取信号"。
- 备忘录（缓存层）：use 消费的 promise 必须来自缓存（server component 传下 / client cache），每次 render 新建 promise = 无限挂起。
- 识别要点：能对比 use(promise) vs use(Context)——use 统一了"读取外部值"两种形态（异步信号与同步上下文）。

```tsx
// use() 心智模型
function Profile({ userId }) {
  const user = use(fetchUser(userId));        // 未 resolve → throw 给 Suspense；resolve → 渲染
  return <h1>{user.name}</h1>;
}
// 缓存前提（错误示范 vs 正确）：
function Bad({ id }) { return use(fetch(`...${id}`).then(r => r.json())); }   // 每次 render 新 promise → 永挂起
const cache = new Map();
function fetchUser(id) {
  if (!cache.has(id)) cache.set(id, fetch(`...${id}`).then(r => r.json()));   // 稳定 promise
  return cache.get(id);
}
// use(Context)：const theme = use(ThemeContext) —— 与 useContext 等价但可在条件分支用
```
