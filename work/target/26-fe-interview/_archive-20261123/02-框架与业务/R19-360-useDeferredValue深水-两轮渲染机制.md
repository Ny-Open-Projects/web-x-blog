---
title: [R19-360] useDeferredValue 深水：两轮渲染与重用机制
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## R19-360：useDeferredValue 深水：两轮渲染与重用机制

**答**：
- 机制：deferredValue = useDeferredValue(value)——value 变化时 React 先用「旧 deferred 值」渲染一遍（立即 commit，UI 不卡），再用新值后台重渲染（可打断）
- 与 useTransition 的分工：Transition 包「更新动作」（setState 侧），DeferredValue 包「值消费」（渲染侧）——数据来自 props/外部时用 DeferredValue（无法包裹 setState）
- 两轮渲染的成本：每个 value 变化至少两次渲染（旧值提交 + 新值计算）——大计算场景值得，小组件反成浪费
- React 19 优化： initialValue 参数——SSR/hydration 时用初始值，避免水合期两轮渲染
- 嵌套与组合：DeferredValue 派生值（deferred(query) → useMemo(filter)）——filter 的重算发生在「第二轮」（低优先级），主线程输入不再被 filter 卡住

```jsx
function SearchList({ query }) {
  const deferredQuery = useDeferredValue(query);
  const results = useMemo(() => filterHugeList(deferredQuery), [deferredQuery]);
  // 第一轮: 旧 deferredQuery → 旧 results 立即提交(输入流畅)
  // 第二轮: 新 deferredQuery → 新 results (可打断后台渲染)
  const stale = query !== deferredQuery;
  return <List results={results} stale={stale} />;
}
```
