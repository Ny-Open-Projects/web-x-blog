---
title: [MFW-737] RSC 的 Context 跨边界传递
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-737：RSC 的 Context 跨边界

**答**:
- RSC 的 Context 限制：1) **server 组件无 Context**（React Context 是 client 机制——server 组件无状态/hook——不能 createContext/useContext）；2) **provider 必须 client**（Context.Provider 是 client 组件（'use client'——provider 有 useState/useMemo）；3) **children 模式传递**（client provider 包 server children——server children 作为 props 传入 provider（children 从 server 侧传入——不是 provider 内部渲染 RBL-686）。
- 传递的实际方案：1) **props 直传**（server 直接把值传给 client 组件 props——不需要 context（server → client 单向数据流）；2) client Context（client 子树内的 Context——client 组件间的状态共享）；3) ALS（server 端的请求级上下文——RBL-519 的 ALS 替代 server Context）。
- 追问钩子：为什么「server 组件无 Context」是架构设计而非功能缺失？——Context = 「隐式依赖注入」（子树自动获取——无需 props 传递）；server 组件的「显式数据流」（props 单向——每个组件的数据来源明确）——「显式 vs 隐式」的设计哲学：RSC 的 server 端选择显式（可追踪/可审计——props 链是数据流的完整记录）；client 端保留 Context（交互态的便利性）——两端各自选择适合的范式。

```tsx
// 反模式：server 组件用 Context（编译报错）
// server-page.tsx: <ThemeProvider><Content /></ThemeProvider>
//  ← ThemeProvider 是 client——但 server children 可以传给 client provider

// 正确：children 模式
// providers.tsx ('use client')
'use client';
import { createContext, useContext } from 'react';
const ThemeContext = createContext('light');
export function ThemeProvider({ children, initial }: { children: ReactNode; initial: string }) {
  return <ThemeContext.Provider value={initial}>{children}</ThemeContext.Provider>;
}
export const useTheme = () => useContext(ThemeContext);
// layout.tsx（server）
export default function Layout({ children }) {
  const theme = headers().get('x-theme') ?? 'light';   // server 侧读
  return (
    <ThemeProvider initial={theme}>                     {/* client provider 包 server children */}
      {children}                                         {/* server 渲染的 children 作为 props 传入 */}
    </ThemeProvider>
  );
}
// children 内的 server 组件仍可读 server 数据（server 树不变）
// client provider 的 context 值只对 client 子树有效
```
