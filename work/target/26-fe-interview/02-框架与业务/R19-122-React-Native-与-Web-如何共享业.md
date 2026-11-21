---
title: [R19-122] React Native 与 Web 如何共享业务逻辑？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-122：React Native 与 Web 如何共享业务逻辑？
**答**：
- 分层复用：state、hooks、请求、校验下沉到 shared 包（零平台依赖），只有渲染层按平台实现。
- 判定标准：文件里不 import 任何 DOM/RN API 的逻辑才能进 shared。
- 平台差异用依赖注入：shared 暴露接口，web 注入 react-router 的跳转，native 注入 navigation。
- monorepo（pnpm workspace）承载：packages/shared + apps/web + apps/native。

```javascript
// monorepo 结构：业务层复用的载体
// packages/
//   shared/            # 纯逻辑层：零平台依赖
//     hooks/           # useCart, useAuth —— 只用 React API
//     store/
//     api/
//     utils/
//   ui/                # 可选：跨端组件层（web 用 dom，native 用 RN 组件）
// apps/
//   web/               # React DOM 实现
//   native/            # React Native 实现

// packages/shared/hooks/useAuth.ts —— 不 import 任何平台 UI，两端直接复用
import { useSyncExternalStore } from 'react';
import { authStore } from '../store/authStore';

export function useAuth() {
  const user = useSyncExternalStore(authStore.subscribe, authStore.getState);
  return { user, login: authStore.login, logout: authStore.logout };
}

// 平台差异用依赖注入：shared 暴露接口，web 传 router，native 传 navigation
// const { login } = useAuth({ navigate: (path) => router.push(path) });
// 分层原则：state / 逻辑 / 请求下沉 shared，只有渲染层按平台实现
```
