---
title: [TS-140] 事件处理器类型怎么写？如何把 DOM 事件泛型化成业务值？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-140：事件处理器类型怎么写？如何把 DOM 事件泛型化成业务值？
**答**：
- 原生事件按目标元素泛型化：`React.ChangeEvent<HTMLInputElement>`，target 类型随之精确。
- 业务组件不应向外抛 DOM 事件，而是把"值"泛型化：`onChange: (value: V) => void`。
- 内部转换用窄断言收敛（`e.target.value as V`），边界只留一处。

```tsx
// 原生事件：按目标元素选择泛型
const onNameChange = (e: React.ChangeEvent<HTMLInputElement>) => e.target.value; // string
const onSelect = (e: React.ChangeEvent<HTMLSelectElement>) => e.target.value;    // string

// 业务组件：把"值"泛型化，不泄漏 event 对象
function TextField<V extends string | number>(props: {
  value: V;
  onChange: (value: V) => void;
}) {
  return (
    <input
      value={props.value}
      onChange={(e) => props.onChange(e.target.value as V)}
    />
  );
}
// <TextField<string> value={name} onChange={(v) => setSearch(v)} />
// v 是 string；若把 ChangeEvent 抛出去，调用方被迫关心 DOM 细节
```
