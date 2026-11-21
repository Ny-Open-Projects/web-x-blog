---
title: [OPT-037] React 大列表与搜索场景的性能专项怎么优化？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-037：React 大列表与搜索场景的性能专项怎么优化？

**答**：
- 行组件 `memo` 化 + 保证 props 引用稳定（数据不可变更新、回调 useCallback），避免一处 setState 全列表重渲。
- 搜索输入用 `useDeferredValue`：输入框保持紧急更新（跟手），列表用延迟值低优先级重渲，输入不再被大列表卡住。
- **状态下放**：把频繁变化的 state（如某行的 hover/选中）下放到最小的组件里，缩小重渲范围。
- Context 改用 selector 订阅（zustand / useSyncExternalStore），只订阅用到的切片，而不是整个 context value 变化就全树更新。

```jsx
// 一一对应：大列表 + 搜索的组合优化
import { memo, useDeferredValue, useState, useCallback } from 'react';
import { useStore } from './store'; // zustand

// 1. 行组件 memo 化，props 不变就不重渲
const Row = memo(function Row({ item, onSelect }) {
  return <li onClick={() => onSelect(item.id)}>{item.name}</li>;
});

export default function BigList({ items }) {
  const [query, setQuery] = useState('');
  // 2. 输入紧急，列表延迟：输入框跟手，列表低优先级重算
  const deferredQuery = useDeferredValue(query);

  // 3. useCallback 稳定回调引用，配合 memo 才有效
  const onSelect = useCallback((id) => console.log('select', id), []);

  // 4. selector 订阅：只订阅 theme 切片，其它状态变化不会引起本组件更新
  const theme = useStore((s) => s.theme);

  const filtered = items.filter((it) => it.name.includes(deferredQuery));

  return (
    <div data-theme={theme}>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <ul>
        {filtered.map((item) => (
          <Row key={item.id} item={item} onSelect={onSelect} />
        ))}
      </ul>
    </div>
  );
}
```
