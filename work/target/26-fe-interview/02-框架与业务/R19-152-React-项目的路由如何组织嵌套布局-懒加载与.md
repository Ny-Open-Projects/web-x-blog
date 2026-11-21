---
title: [R19-152] React 项目的路由如何组织？嵌套布局、懒加载与路由守卫封装怎么做？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-152：React 项目的路由如何组织？嵌套布局、懒加载与路由守卫封装怎么做？
**答**：
- 路由按"布局"组织：`<Route element={<Layout/>}>` 下挂 children，Outlet 承接子渲染；鉴权布局、公开布局、错误页都是不同布局节点。
- 懒加载统一 `lazy()` + Suspense，路由级 chunk 天然分割；顶层包一个全局 Suspense/错误边界兜底。
- 守卫封装成 `<RequireAuth>` 布局组件：校验 -> 通过渲染 Outlet，不通过 Navigate 重定向，并记录来源 path 供登录后回跳。
- 数据守卫用 loader（react-router 6.4+）在进入路由前拉数据，把"能否进入"的判断从渲染期前移。

```tsx
// router.tsx —— 嵌套布局 + 懒加载 + 守卫
import {
  createBrowserRouter, RouterProvider, Outlet, Navigate,
  useLocation, Link,
} from 'react-router-dom';
import { lazy, Suspense, type ReactNode } from 'react';

const Dashboard = lazy(() => import('./pages/dashboard'));
const Users = lazy(() => import('./pages/users'));
const Login = lazy(() => import('./pages/login'));

function PageSuspense({ children }: { children: ReactNode }) {
  return <Suspense fallback={<div>页面加载中...</div>}>{children}</Suspense>;
}

function AppLayout() {
  return (
    <div className="app-shell">
      <aside>导航</aside>
      <main><Outlet /></main> {/* 子路由渲染点 */}
    </div>
  );
}

// 守卫组件：包在需要鉴权的布局外层
function RequireAuth({ children }: { children: ReactNode }) {
  const token = localStorage.getItem('token'); // 实际项目从 auth store 读
  const location = useLocation();
  if (!token) {
    return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  }
  return children;
}

export const router = createBrowserRouter([
  { path: '/login', element: <PageSuspense><Login /></PageSuspense> },
  {
    path: '/',
    element: (
      <RequireAuth>
        <AppLayout />
      </RequireAuth>
    ),
    errorElement: <div>404 或渲染错误兜底 <Link to="/">回首页</Link></div>,
    children: [
      { index: true, element: <PageSuspense><Dashboard /></PageSuspense> },
      { path: 'users', element: <PageSuspense><Users /></PageSuspense> },
    ],
  },
]);

export function App() {
  return <RouterProvider router={router} />;
}
```
