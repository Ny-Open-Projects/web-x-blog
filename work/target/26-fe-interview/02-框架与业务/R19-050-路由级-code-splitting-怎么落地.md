---
title: [R19-050] 路由级 code splitting 怎么落地？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-050：路由级 code splitting 怎么落地？
**答**：
- 用 React.lazy + Suspense 把每个页面拆成独立 chunk，首屏只加载当前路由代码。
- 构建产物可通过 build.rollupOptions.output.manualChunks 进一步抽公共 vendor。
- fallback 做成骨架屏，避免闪白；预加载关键路由可用 `import()` 提前触发。
- 衡量指标：看首屏 JS 体积与 LCP，而不是 chunk 数量。

```jsx
import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

const Home = lazy(() => import('./pages/Home'));
const Admin = lazy(() => import('./pages/Admin'));

export default function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<p>页面加载中...</p>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/admin" element={<Admin />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```
