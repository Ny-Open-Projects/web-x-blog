---
title: [R19-041] React.lazy 与 Suspense 如何做代码分割？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-041：React.lazy 与 Suspense 如何做代码分割？
**答**：
- React.lazy 接收一个返回 `import()` 的工厂函数，构建工具把目标模块拆成独立 chunk。
- 首次渲染该组件时才加载 chunk，期间由包在外层的 Suspense 显示 fallback。
- lazy 的组件必须以默认导出形式提供，否则用 `then(mod => ({ default: mod.X }))` 适配。
- 典型实践：路由级分割必做，重依赖图表/编辑器按需分割。

```jsx
import { lazy, Suspense } from 'react';

// Chart 及其依赖会被拆成独立 chunk，用到时才加载
const Chart = lazy(() => import('./Chart'));

export default function Dashboard() {
  return (
    <Suspense fallback={<p>图表加载中...</p>}>
      <Chart />
    </Suspense>
  );
}
```
