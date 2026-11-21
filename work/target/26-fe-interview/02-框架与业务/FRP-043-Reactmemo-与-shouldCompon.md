---
title: [FRP-043] React.memo 与 shouldComponentUpdate 的原理是什么？浅比较的坑在哪？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-043：React.memo 与 shouldComponentUpdate 的原理是什么？浅比较的坑在哪？

**答**：
- 更新传播默认是"父更新则子全更新"；`React.memo`（函数组件）与 `shouldComponentUpdate/PureComponent`（类组件）提供一道**手动逃生门**：props 浅比较相同则跳过整个子树的 render（bailout）。
- memo 第二个参数可自定义比较函数（返回 true 表示相等、跳过渲染），语义与 SCU 相反，容易写反。
- 浅比较的坑：**每次渲染新建的 props 引用必然不等**——`onClick={() => ...}`、`style={{...}}`、数组字面量都会让 memo 失效，需要 useCallback/useMemo/stable 库配合。
- bailout 只是跳过**本组件的 render**：若子孙组件消费了 context 或自身有 state 更新，仍会更新。

```jsx
// 一一对应：memo 失效与修复
import { memo, useState, useCallback, useMemo } from 'react';

// 浅比较实现（源码 shallowEqual 的核心逻辑）
function shallowEqual(objA, objB) {
  if (Object.is(objA, objB)) return true;
  const keysA = Object.keys(objA), keysB = Object.keys(objB);
  if (keysA.length !== keysB.length) return false;
  return keysA.every((k) => Object.prototype.hasOwnProperty.call(objB, k) && Object.is(objA[k], objB[k]));
}

const Row = memo(({ item, onSelect }) => {
  console.log('render row', item.id);
  return <li onClick={() => onSelect(item.id)}>{item.name}</li>;
});

export default function List() {
  const [keyword, setKeyword] = useState('');

  // 坑：内联函数每次渲染都是新引用，memo 完全失效，列表全量重渲
  // <Row item={item} onSelect={(id) => console.log(id)} />

  // 修复 1：useCallback 稳定函数引用
  const onSelect = useCallback((id) => console.log('select', id), []);

  return (
    <ul>
      <input value={keyword} onChange={(e) => setKeyword(e.target.value)} />
      {items.map((item) => (
        <Row key={item.id} item={item} onSelect={onSelect} />
        // keyword 变化时 List 重渲，但 item/onSelect 引用不变 -> Row 被 bailout
      ))}
    </ul>
  );
}

const items = [
  { id: 1, name: 'a' },
  { id: 2, name: 'b' },
];
```
