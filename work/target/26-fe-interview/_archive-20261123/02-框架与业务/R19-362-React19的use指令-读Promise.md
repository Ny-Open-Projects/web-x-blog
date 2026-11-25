---
title: [R19-362] React19 的 use 指令：读 Promise 与 Context 的统一入口
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 数据流]
type: 面试题
---

## R19-362：React19 的 use 指令：读 Promise 与 Context 的统一入口

**答**：
- use(promise)：读取 Promise 值——组件 throw promise 由 Suspense 捕获；resolve 后组件重渲染拿到值——「在渲染函数里直接 await」的语义化
- 使用约束：只能在渲染函数内调用（Hook 规则之外的新规则——可条件调用！）；promise 必须是稳定的（缓存），每次渲染新建 Promise 会无限循环——配合 fetch cache
- use(context)：替代 useContext——可以条件分支调用（这是与 Hook 规则的最大差异，因为 use 不是 Hook 而是「运行时指令」）
- 与 React Query 的关系：use(promise) 是最底层的原语（缓存/去重/失效自己搭）；React Query 等库在其上封装——「库 vs 原语」的分层认知
- 缓存要求：Promise 状态机要求 stable identity——React 19 的 cache() API（RSC 环境）或组件外 Map 缓存实现稳定引用

```jsx
function Detail({ id }) {
  if (id === 'special') {
    const data = use(fetchSpecial(id));    // 可条件调用!
    return <Special data={data} />;
  }
  const data = use(fetchCached(id));       // promise 必须缓存稳定
  return <Detail data={data} />;
}
```
