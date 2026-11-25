---
title: [MFW-640] INP 的 RSC 交互优化
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-640：INP 的 RSC 交互优化

**答**:
- INP（交互到下一次绘制）在 RSC 架构的来源：1) **水合未完成时的交互**（SSR HTML 可见但未水合——点击无响应（事件还没绑定）：INP 爆炸；缓解：选择性水合（交互区域优先水合）/渐进增强（无 JS 也能响应——form 原生提交 RBL-512））；2) **乐观更新的渲染延迟**（action await server 往返——乐观 UI 让 INP = 本地渲染时间）；3) **长任务阻塞**（client 组件的大计算——transition/worker）。
- 优化的优先级：水合期间的交互（最大 INP 来源）——「水合前的交互处理」（事件委托 + 未水合队列：点击先记录、水合后重放——React 的 capture 层）；乐观更新覆盖所有「server 往返」交互（INP < 100ms）。
- INP 的 RUM 归因（RBL-940 闭环）：INP 事件的 target/时机（水合前 vs 后——归因到水合问题 vs 渲染问题）。
- 追问钩子：为什么「SSR 页面的水合前点击」是 INP 的最大来源且最常被忽略？——LCP/TTFB 优化后页面秒开（视觉就绪）→ 用户立即交互 → 事件未绑定（JS 还在下载/水合中）→ 无响应 500ms+；「视觉就绪 ≠ 交互就绪」的鸿沟在 SSR 页最大（HTML 先到 JS 后到）；解法的层次：渐进增强（原生表单——无 JS 也有响应）> 优先水合交互区 > 乐观 UI——「可交互时间」（TTI）而非「可看见时间」才是 SSR 页的交互质量指标。

```tsx
// 1) 渐进增强：水合前也响应
// <form action={serverAction}>  原生提交——水合前点击仍提交（整页）
// 2) 乐观更新：INP = 本地渲染
'use client';
function AddButton({ id }) {
  const [optimistic, add] = useOptimistic(0, (c) => c + 1);
  return (
    <button onClick={async () => {                       // 点击瞬间 +1（本地渲染）
      add(1);                                            // INP < 100ms
      await serverAction(id);                            // server 往返在后台
    }}>Buy ({optimistic})</button>
  );
}
// 3) INP 归因：水合前 vs 后
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    const hydrated = (window as any).__hydrated;
    report({ inp: e.duration, beforeHydration: !hydrated,
      target: e.target?.nodeName, buildId: window.__BUILD_ID });
  }
}).observe({ type: 'event', buffered: true, durationThreshold: 200 });
```
