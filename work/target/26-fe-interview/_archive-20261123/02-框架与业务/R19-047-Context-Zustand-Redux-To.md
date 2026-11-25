---
title: [R19-047] Context、Zustand、Redux Toolkit 怎么选型？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-047：Context、Zustand、Redux Toolkit 怎么选型？
**答**：
- 服务端数据（请求缓存、重验证）交给 TanStack Query 或 SWR，不要塞进通用状态库。
- 中小型客户端状态：Context + useReducer 起步；出现性能或嵌套问题时换 Zustand。
- 大型团队协作、需要严格数据流、中间件与时间旅行的项目选 Redux Toolkit。
- 决策关键：变更频率、订阅粒度、团队规模与可维护性，而不是"哪个更流行"。

```javascript
// 选型速查表
// 服务端数据       -> TanStack Query / SWR
// 低频全局配置     -> Context（主题 语言 用户信息）
// 中型客户端状态   -> Zustand（无样板 按切片订阅）
// 大型严格数据流   -> Redux Toolkit（中间件 DevTools 团队约定）
// 表单状态         -> react-hook-form / 受控组件局部状态

// Zustand 一行定义 store
const useThemeStore = create((set) => ({
  mode: 'light',
  toggle: () =>
    set((s) => ({ mode: s.mode === 'light' ? 'dark' : 'light' })),
}));
```

---

## 第七章 性能优化与 React Compiler（R19-048 ~ R19-052）
