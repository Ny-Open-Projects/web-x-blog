---
title: [R19-080] Context 性能差在哪？怎么优化？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-080：Context 性能差在哪？怎么优化？
**答**：
- 病根：Context 的 value 一变，所有消费组件整体重渲染，无论它用到 value 的哪个字段；且 value 通常是 render 时新建的对象字面量。
- 优化一：拆分 Context，高频变化的（实时数据）与低频的（用户信息）分开 Provider。
- 优化二：value 用 useMemo 稳定；dispatch/setState 这类天然稳定的引用单独放一个 Context，订阅它的组件永不重渲染。
- 优化三：use-context-selector 的 useContextSelector 让组件只订阅选中的那一片，是官方方向的社区实现。

```jsx
// 拆分读写 Context：value 变化只有真正的消费者重渲染
import { createContext, useContext, useMemo, useState } from 'react';

const StateContext = createContext(null);      // 低频数据
const DispatchContext = createContext(null);   // 稳定引用

function Provider({ children }) {
  const [user, setUser] = useState(null);
  return (
    <DispatchContext.Provider value={setUser}>       {/* setUser 引用稳定，永不触发订阅者更新 */}
      <StateContext.Provider value={useMemo(() => user, [user])}>
        {children}
      </StateContext.Provider>
    </DispatchContext.Provider>
  );
}

// selector 思想（use-context-selector 库）：只订阅选中的那一小片
import { useContextSelector } from 'use-context-selector';

function UserName() {
  // 只订阅 user.name，user 其他字段变化不会让本组件重渲染
  const name = useContextSelector(StateContext, s => s?.name);
  return <span>{name}</span>;
}
```
