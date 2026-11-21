---
title: [R19-117] React DevTools Profiler 怎么高效定位性能问题？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-117：React DevTools Profiler 怎么高效定位性能问题？
**答**：
- 四步法：录制一次交互 -> 看火焰图 -> 找宽条与重复窄条 -> 对症下药。
- 宽条 = 组件自身渲染慢（重计算、大列表），用 useMemo/虚拟化优化；大量重复窄条 = 不必要重渲染，查 props 引用与 Context。
- 开启 Highlight updates，交互时直接看谁在闪，快速验证 Context 风暴。
- Profiler 组件可在生产埋渲染耗时，采集真实用户的慢渲染分布。

```jsx
// Profiler 定位法：录制 -> 火焰图 -> 找宽条 -> 对症下药
import { Profiler, useCallback } from 'react';

function App() {
  const onRender = useCallback((id, phase, actualDuration) => {
    // 生产上也可以借此上报真实用户渲染耗时
    if (actualDuration > 16) {
      console.warn(`${id} ${phase} 耗时 ${actualDuration.toFixed(1)}ms`);
    }
  }, []);

  return (
    <Profiler id="OrderList" onRender={onRender}>
      <OrderList />
    </Profiler>
  );
}
// DevTools 里：Flame Graph 看每次 commit 的耗时条；
// Highlight updates when components render 直观看到谁在闪；
// 宽条 = 组件本身慢，重复窄条 = 不必要重渲染（补 memo / 稳定 props）。
```
