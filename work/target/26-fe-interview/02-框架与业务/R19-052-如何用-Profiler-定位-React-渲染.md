---
title: [R19-052] 如何用 Profiler 定位 React 渲染性能问题？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-052：如何用 Profiler 定位 React 渲染性能问题？
**答**：
- React DevTools 的 Profiler 面板录制渲染，能看到每个组件的渲染次数与耗时。
- 代码级用 `<Profiler>` 包裹目标区域，onRender 回调上报 id、phase、actualDuration。
- 常见问题：状态提升过高导致大范围渲染、Context value 不稳定、长列表无虚拟化。
- 优化顺序：先量（找出真热点），再拆（状态下放/拆 Provider），再缓存（memo/useMemo），最后虚拟化。

```jsx
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration) {
  // phase 是 mount 或 update，actualDuration 为本次渲染毫秒数
  if (actualDuration > 16) {
    console.warn('渲染超帧', id, phase, actualDuration);
  }
}

export default function App() {
  return (
    <Profiler id="Dashboard" onRender={onRenderCallback}>
      <Dashboard />
    </Profiler>
  );
}
```

---

## 第八章 SSR 与 Next.js（R19-053 ~ R19-056）

```mermaid
flowchart LR
  A["用户请求页面"] --> B["服务端执行组件树"]
  B --> C["生成 HTML 并流式返回"]
  C --> D["浏览器立即显示首屏"]
  D --> E["加载 JS bundle"]
  E --> F["hydration 附加交互能力"]
```
