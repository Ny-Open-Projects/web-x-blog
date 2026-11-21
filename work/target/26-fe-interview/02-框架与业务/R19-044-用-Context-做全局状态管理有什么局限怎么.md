---
title: [R19-044] 用 Context 做全局状态管理有什么局限？怎么缓解？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-044：用 Context 做全局状态管理有什么局限？怎么缓解？
**答**：
- 核心局限：Provider 的 value 引用变化时，所有消费组件整体重渲染，无法细粒度订阅。
- value 字面量导致每次渲染都产生新引用，必须 useMemo 或把 state 拆到更小粒度的 Provider。
- 多层级 Context 更新可能引发大范围渲染，性能敏感的高频状态不适合 Context。
- 缓解手段：拆分 Provider、value 用 useMemo、配合 memo 隔离子树；仍不够就换 Zustand 等外部 store。

```jsx
import { createContext, useContext, useMemo, useState } from 'react';

const UserContext = createContext(null);
const ThemeContext = createContext(null);

export default function App() {
  const [user, setUser] = useState({ name: 'Wang' });
  const [theme, setTheme] = useState('dark');

  // 分别 memo 两个 value，且拆成两个 Provider，主题切换不影响用户订阅者
  const userValue = useMemo(() => ({ user, setUser }), [user]);
  const themeValue = useMemo(() => ({ theme, setTheme }), [theme]);

  return (
    <UserContext.Provider value={userValue}>
      <ThemeContext.Provider value={themeValue}>
        <Header />
      </ThemeContext.Provider>
    </UserContext.Provider>
  );
}

export function useUser() {
  const ctx = useContext(UserContext);
  if (!ctx) throw new Error('useUser 必须在 Provider 内使用');
  return ctx;
}
```
