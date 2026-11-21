---
title: [R19-199] 如何理解并发时代 React 的心智模型（从同步到可中断）？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-199：如何理解并发时代 React 的心智模型（从同步到可中断）？
**答**：
- 旧模型：render 是同步函数，setState 即"排队一次完整重渲染"，UI 只能在两次渲染间变化，长渲染直接卡死输入。
- 并发模型：render 可以**暂停-让位-重启-丢弃**；更新分优先级（用户输入 > transition），低优渲染被高优打断后**整体重来**，不存在渲染一半的中间态。
- 由此推导出的 API 语义：transition 是"这个更新可以被丢弃重排"的声明；Suspense 是"这块数据没好就先展示外壳"；useOptimistic 是"先展示叠加值，结束自动结算"。
- 写代码的新纪律：渲染保持纯净（可重入）、副作用全部进 effect/事件、不要依赖"渲染恰好执行一次"的假设（StrictMode 双跑即训练）。

```jsx
// concurrency-model.jsx —— 心智模型对照示例
import { useState, useTransition, useOptimistic, Suspense } from 'react';

// 旧心智：setState = 立即改变屏幕（同步、一次到位）
// 新心智：setState = 描述"下一个屏幕长什么样"（声明），渲染时机由调度器决定

function ModelDemo({ items }) {
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();

  // 心智要点 1：高优先级输入先"到达"，低优先级结果可以"迟到"
  // 心智要点 2：被打断的 transition 整体作废，不留半成品
  // 心智要点 3：isPending 是调度器给你的进度信号，UI 必须消费它
  return (
    <>
      <input
        value={query}
        onChange={e => {
          setQuery(e.target.value);                  // 优先级高：立刻重渲染输入框
          startTransition(() => {/* 重列表更新 */ }); // 优先级低：可被打断
        }}
      />
      {isPending && <Spinner />}

      {/* 心智要点 4：Suspense 边界 = "这里的 UI 可以先欠着" */}
      <Suspense fallback={<Skeleton />}>
        <HeavyResult query={query} items={items} />
      </Suspense>
    </>
  );
}

// 心智要点 5：乐观更新 = "先给结果，失败自动回收"
function Like({ count, onLike }) {
  const [likes, addLike] = useOptimistic(count, (c, d) => c + d);
  return (
    <button onClick={() => addLike(1)}>{likes} 赞</button>
  );
}
// 一次 onClick 里可能发生：乐观渲染 -> 中断 -> 回滚 -> 真实渲染
// 唯一安全的写法：渲染函数纯净、变更走 startTransition、UI 消费 isPending

// 一句话总结：
// 同步时代的 React："调用 setState -> 屏幕变了"
// 并发时代的 React："调用 setState -> 描述了新屏幕 -> 调度器决定何时/是否真的画出来"
```
