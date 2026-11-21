---
title: [FRP-162] TanStack Query 的乐观更新与回滚是怎么实现的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-162：TanStack Query 的乐观更新与回滚是怎么实现的？

**答**：
- mutation 的三个钩子构成闭环：`onMutate`（乐观写缓存）→ `onError`（用快照回滚）→ `onSettled`（invalidate 让服务端真值回流）。
- onMutate 的三步：**取消进行中的同类请求**（防旧响应覆盖乐观值）、**保存缓存快照**（回滚凭据）、**setQueryData 写入乐观值**。
- 回滚就是把快照原样 setQueryData 回去；onSettled 无条件 `invalidateQueries`——乐观值最终被服务端数据校正。
- 并发防护：取消 in-flight 请求 + 快照机制，本质是"单写者原则"——同一时刻只有一个来源在改缓存。

```javascript
// 简化实现，帮助理解乐观更新闭环
async function optimisticToggle(todo) {
  // 1. 乐观写入（onMutate）
  const prev = cache.get(todoKey);                 // 快照
  await cancelQueries(todoKey);                    // 取消 in-flight：防旧响应覆盖
  cache.set(todoKey, { ...prev, data: prev.data.map(t =>
    t.id === todo.id ? { ...t, done: !t.done } : t
  )});

  try {
    await mutateApi(todo);                         // 真实请求
  } catch (e) {
    // 2. 回滚（onError）：快照原样写回
    cache.set(todoKey, prev);
    toast.error('操作失败，已还原');
  } finally {
    // 3. 校正（onSettled）：让服务端真值回流
    invalidateQueries(todoKey);                    // 标记过期 -> 触发重新 fetch
  }
}

// invalidateQueries 的简化语义：
function invalidateQueries(key) {
  const query = cache.get(hash(key));
  query.isStale = true;                            // 标记过期
  if (query.observers > 0) query.fetch();          // 活跃观察者：立即后台重取
  // 无观察者：只标记，等下次挂载时再取（配合 GC）
}

// 为什么必须取消 in-flight：
// 时序反例：乐观写缓存 -> 旧请求（5s 前发出）返回旧列表 -> 覆盖乐观值 -> UI 回跳
// cancelQueries 让旧 promise reject（不再 notify），乐观值存活到真实响应到达
```
