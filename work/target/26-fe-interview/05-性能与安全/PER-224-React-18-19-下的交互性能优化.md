---
title: [PER-224] React 18/19 下的交互性能（INP）怎么优化？transition 与 useDeferredValue 各适合什么场景？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-224：React 18/19 下的交互性能（INP）怎么优化？transition 与 useDeferredValue 各适合什么场景？

**答**：
- 优先级分级：React 18 的并发特性让"输入响应"与"重渲染"分离。`startTransition` / `useTransition` 把不紧急的状态更新标记为可中断的低优先级，输入仍然即时响应——适合 tab 切换、搜索结果列表这种"输入快、结果可慢"的场景。
- `useDeferredValue`：给"派生值"降级——输入框 state 立即更新，用 deferred 值驱动昂贵渲染，自动延后一帧。适合大列表过滤、图表重算等"昂贵派生渲染"。
- 渲染成本本身也要治：长列表用虚拟化；`memo`/`useMemo` 挡住无关重渲染；避免在 render 中做重计算（挪 useMemo/Worker）。优先级手段只是"让卡顿不挡输入"，不减少总工作量。
- 边界：transition 不能包裹同步 IO 与事件 handler 里的同步重计算（那还是主线程长任务）；别滥用——所有更新都 transition 会导致 UI 永远"慢半拍"。

```jsx
import { useDeferredValue, memo } from 'react';

function SearchPage({ query }) {
  const deferredQuery = useDeferredValue(query);   // 输入即时，列表延后
  const isStale = query !== deferredQuery;         // 可用于展示过渡态
  return (
    <>
      <input value={query} onChange={/* ... */} />           {/* 紧急：INP 友好 */}
      <div style={{ opacity: isStale ? 0.6 : 1 }}>
        <BigList keyword={deferredQuery} />                   {/* 昂贵：延迟渲染 */}
      </div>
    </>
  );
}
const BigList = memo(({ keyword }) => {
  // 虚拟列表 + 按 keyword 过滤；memo 挡住 query 其他字段变化导致的重渲染
  return filterRows(keyword).map(renderRow);
});
```
