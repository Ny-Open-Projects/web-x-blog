---
title: [R19-098] 如何定位并修复 Context 风暴？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-098：如何定位并修复 Context 风暴？
**答**：
- 定位：React DevTools Profiler 录制一次交互，看到大量组件的 render reason 是 "Context change"，即 Provider 的 value 变化引起。
- 常见根因：value 是每次 render 新建的对象字面量；或把高频变化的状态（实时行情）与低频状态（用户信息）塞进同一个 Context。
- 修复三板斧：拆分 Context、value 用 useMemo 稳定、dispatch 单独成 Context。
- 进一步用 use-context-selector 按字段订阅；why-did-you-render 可以在开发期直接打印"哪个 props/context 变了"。

```jsx
// StoreProvider.tsx —— Context 风暴修复示例
import { createContext, useMemo, useState } from 'react';
import { useContextSelector } from 'use-context-selector';

// 1. 拆分：高频变化的与低频的分离
const UserContext = createContext(null);      // 低频：登录信息
const RealtimeContext = createContext(null);  // 高频：实时数据

// 2. Provider value 用 useMemo 稳定，杜绝每次渲染新对象
function StoreProvider({ children }) {
  const [user, setUser] = useState(null);
  const [metrics, setMetrics] = useState({});
  const userValue = useMemo(() => ({ user, setUser }), [user]);
  const metricsValue = useMemo(() => ({ metrics, setMetrics }), [metrics]);
  return (
    <RealtimeContext.Provider value={metricsValue}>
      <UserContext.Provider value={userValue}>{children}</UserContext.Provider>
    </RealtimeContext.Provider>
  );
}

// 3. 消费端只挑需要的字段
function Header() {
  const userName = useContextSelector(UserContext, s => s.user?.name);   // 只订阅 name
  return <span>{userName}</span>;
}
// 排查辅助：给可疑组件接 why-did-you-render，日志会指明是哪种 props/context 变化
```
