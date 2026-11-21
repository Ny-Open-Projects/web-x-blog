---
title: [FRP-036] useTransition 与 useDeferredValue 的原理是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-036：useTransition 与 useDeferredValue 的原理是什么？

**答**：
- 两者都基于 lane 优先级：`useTransition` 把更新标记为 **TransitionLane**（可中断、可被紧急更新插队），`isPending` 在过渡期间为 true。
- `startTransition(fn)` 执行期间的所有 setState 都以 TransitionLane 调度：紧急更新（输入）先渲染，过渡内容被切片渲染；被打断的过渡 render 可整体丢弃重放。
- `useDeferredValue(value)` 返回一个"延迟副本"：紧急渲染先用旧值，空闲后用新值再渲染一次——本质是"两次渲染、旧值先行"，不新增调度 API。
- 典型分工：输入框直接绑定原始值（跟手），昂贵的列表绑定 deferredValue。

```jsx
// 一一对应：useTransition 与 useDeferredValue 的原理性用法
import { useTransition, useDeferredValue, useState, useMemo } from 'react';

function SearchWithTransition({ items }) {
  // 双 state：输入值紧急更新，查询值走过渡更新
  const [inputValue, setInputValue] = useState('');
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();

  return (
    <>
      {/* 输入用同步 setState：紧急更新，保证跟手 */}
      <input value={inputValue} onChange={(e) => {
        setInputValue(e.target.value);            // SyncLane 立即渲染输入框
        startTransition(() => {
          setQuery(e.target.value);               // TransitionLane：结果列表低优渲染
        });
      }} />
      {isPending && <span>更新中...</span>}
      <BigList filter={query} items={items} />    {/* 被切片渲染，不阻塞输入 */}
    </>
  );
}

function SearchWithDeferred({ items }) {
  const [query, setQuery] = useState('');
  // 延迟副本：先以旧 query 渲染列表（快），空闲后以新 query 重渲染
  const deferredQuery = useDeferredValue(query);

  const list = useMemo(
    () => items.filter((it) => it.name.includes(deferredQuery)),
    [items, deferredQuery]
  );

  return (
    <>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <BigList list={list} stale={deferredQuery !== query} />
    </>
  );
}
```

## 六、React 更新、事件与异常处理
