---
title: [R19-139] useDeferredValue 与 useTransition 怎么选？各自的适用边界在哪？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-139：useDeferredValue 与 useTransition 怎么选？各自的适用边界在哪？
**答**：
- 本质区别：useTransition 是"我拥有这次更新的触发点"（在事件里主动降级）；useDeferredValue 是"值是别人传来的"（组件内部对 prop/state 做延迟镜像）。
- 受控输入自己 onChange 的场景用 useTransition；封装好的输入组件（如设计库 Input）改不了 onChange，用 useDeferredValue 包 query。
- useDeferredValue 不需要 isPending 额外导出，它返回旧值让旧 UI 留存，配合 key+memo 也能做骨架。
- 两者都依赖可中断渲染才有效；组件树里有同步且不可中断的工作时都会失效。

```jsx
// DeferredVsTransition.jsx —— 同一个搜索列表的两种写法
import { useDeferredValue, useState, useMemo, memo } from 'react';

function filterItems(items, keyword) {
  return items.filter(i => i.name.toLowerCase().includes(keyword.toLowerCase()));
}

// 写法 A：useDeferredValue —— 组件只拿到 query，触发点不在自己手里
export function SearchWithDeferred({ query, items }) {
  const deferredQuery = useDeferredValue(query); // 延迟镜像：新值先不用于重活
  const isStale = query !== deferredQuery;       // 新旧不一致 = 正在追赶

  const filtered = useMemo(
    () => filterItems(items, deferredQuery),
    [items, deferredQuery],
  );

  return (
    <div style={{ opacity: isStale ? 0.6 : 1 }}>
      {filtered.map(item => <li key={item.id}>{item.name}</li>)}
    </div>
  );
}

// 写法 B：useTransition —— 输入事件在自己的组件里，可主动分流
export function SearchWithTransition({ items }) {
  const [input, setInput] = useState('');
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();

  const filtered = useMemo(() => filterItems(items, query), [items, query]);

  return (
    <>
      <input
        value={input}
        onChange={e => {
          setInput(e.target.value);
          startTransition(() => setQuery(e.target.value));
        }}
      />
      {isPending && <span>筛选中...</span>}
      <ul>{filtered.map(item => <li key={item.id}>{item.name}</li>)}</ul>
    </>
  );
}

// 选型口诀：触发点在手 -> useTransition；触发点在父级/受控库 -> useDeferredValue
// 封装通用列表时推荐 A：调用方无需理解 transition 也能获得性能收益
```

## 追问（补充）

**追问**：

1. useDeferredValue 的第二个参数 initialValue 解决什么问题？ → React 19 新增。首帧直接用它而不是"先真值后降级"，避免初始就渲染一万行重活；可传一个轻量占位渲染，让第一次 paint 直接轻装上阵。
2. 为什么说有不可中断的同步工作时两者都会失效？ → 可中断只作用于 render 阶段。如果重活落在 useLayoutEffect 或同步的第三方绘制里，会占住主线程，旧 UI 无法保持响应，降级也就没有意义。
3. 它和 debounce 的本质区别是什么？ → debounce 按时间窗口丢弃事件、延迟固定；deferred 按渲染优先级让新值尽快追上，输入即刻上屏、重活可被打断，没有固定延迟，但慢设备上结果仍可能落后于输入。
