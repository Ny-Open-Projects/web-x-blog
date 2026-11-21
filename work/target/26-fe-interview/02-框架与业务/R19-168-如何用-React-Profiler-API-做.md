---
title: [R19-168] 如何用 React Profiler API 做编程式性能测量？onRender 回调怎么用？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-168：如何用 React Profiler API 做编程式性能测量？onRender 回调怎么用？
**答**：
- `<Profiler id onRender>` 是组件级性能探针：包住可疑子树，任何内部提交都会回调 onRender，携带耗时、阶段、原因。
- 关键字段：`actualDuration`（本次渲染真实耗时）、`baseDuration`（不含 memo 的完整渲染耗时，二者差值即 memo 收益）、`phase`（mount/update）、`interactions`（Trace 网关联的用户操作）。
- 生产采集：把 onRender 上报到监控（超过阈值才上报，避免噪声），结合用户 ID/路径分析慢渲染分布。
- 与 DevTools Profiler 的分工：DevTools 用于人工定位，Profiler API 用于自动化、线上度量与回归看板。

```tsx
// measured-section.tsx —— 编程式渲染测量
import { Profiler, type ProfilerOnRenderCallback } from 'react';

// 采集器：慢渲染才上报，生产零成本
const onOrderListRender: ProfilerOnRenderCallback = (
  id,        //Profiler 的 id 标识
  phase,     // mount | update | nested-update
  actualDuration, // 本次提交实际耗时 ms
  baseDuration,   // 不带 memo 的预估完整耗时 ms
  startTime,
  commitTime,
  interactions,   // Trace 关联的用户交互
) => {
  if (actualDuration > 16) { // 超过一帧预算才关心
    // 上报到监控平台：哪块子树、哪次交互、慢了多少
    navigator.sendBeacon('/api/perf/render', JSON.stringify({
      id, phase, actualDuration, baseDuration,
      path: location.pathname,
      t: commitTime,
    }));
  }
  // 诊断技巧：baseDuration - actualDuration ≈ memo/save 带来的节省
  // 若 baseDuration 巨大而 actual 也巨大 -> 子树里全是同步重计算，先拆 memo
};

export function MeasuredOrderSection() {
  return (
    <Profiler id="order-list" onRender={onOrderListRender}>
      <OrderFilterBar />
      <OrderTable />
    </Profiler>
  );
}

// 多探针统一治理：一个 context 收集所有探针数据
import { createContext, useContext, useRef } from 'react';

const PerfReportCtx = createContext<(entry: RenderEntry) => void>(() => {});

type RenderEntry = { id: string; phase: string; duration: number };

export function PerfProvider({ children }: { children: React.ReactNode }) {
  const buffer = useRef<RenderEntry[]>([]);
  const report = (entry: RenderEntry) => {
    buffer.current.push(entry);
    if (buffer.current.length >= 50) flush(buffer.current.splice(0)); // 攒批上报
  };
  return <PerfReportCtx.Provider value={report}>{children}</PerfReportCtx.Provider>;
}

export function usePerfProbe(id: string) {
  const report = useContext(PerfReportCtx);
  const onRender: ProfilerOnRenderCallback = (_i, phase, actualDuration) =>
    report({ id, phase, duration: actualDuration });
  return { onRender };
}
// 使用：<Profiler id="cart" onRender={usePerfProbe('cart').onRender}>...</Profiler>
```
