---
title: [MFW-008] 第三方库在 Server 渲染时报 window is not defined 怎么办？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-008：第三方库在 Server 渲染时报 window is not defined 怎么办？
**答**：
- 根因：库顶层就访问浏览器全局对象（如 echarts、monaco、部分地图 SDK），而 Client Component 也会先在服务端跑一次 SSR。
- 方案一：`'use client'` + **`dynamic(() => import(...), { ssr: false })`**——该组件完全不参与服务端渲染，只在客户端挂载后动态加载。
- 方案二：库 import 也可能炸（顶层副作用）——必须用动态 import 放在 useEffect 里，确保只在浏览器执行。
- 方案三：把库访问封装进自定义 hook 的 mounted 守卫，或直接给父容器 `'use client'` 并推迟到交互后才初始化。
- 经验：重交互/重资源的三方组件（图表、编辑器）统一走 `next/dynamic` 懒加载，还能顺带减首屏 bundle。

```jsx
// app/chart-wrapper.tsx
'use client';
import dynamic from 'next/dynamic';

// ssr: false：服务端渲染时跳过，避免 window 未定义；客户端时才加载 chunk
const EChartsPanel = dynamic(() => import('./echarts-panel'), {
  ssr: false,
  loading: () => <div style={{ height: 300 }}>图表加载中…</div>,
});

export default function ChartWrapper({ data }) {
  return <EChartsPanel data={data} />;
}
```

```jsx
// app/echarts-panel.tsx —— 顶层就依赖 window 的库
'use client';
import { useEffect, useRef } from 'react';

export default function EChartsPanel({ data }) {
  const ref = useRef(null);
  useEffect(() => {
    // 动态 import：确保 echarts 只在浏览器执行（顶层 import 会在 SSR 时炸）
    let chart;
    import('echarts').then((echarts) => {
      chart = echarts.init(ref.current);
      chart.setOption({ xAxis: { type: 'category' }, series: [{ data }] });
    });
    return () => chart?.dispose();
  }, [data]);
  return <div ref={ref} style={{ height: 300 }} />;
}
```
