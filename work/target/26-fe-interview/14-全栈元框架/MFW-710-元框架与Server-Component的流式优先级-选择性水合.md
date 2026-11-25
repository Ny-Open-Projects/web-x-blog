---
title: [MFW-710] 选择性水合：交互驱动的水合顺序
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-710：选择性水合

**答**:
- 选择性水合（Selective Hydration）：HTML 先渲染（SSR 完成）——水合按「用户交互」驱动：用户点击未水合区域 → React 优先水合该区域（Suspense 边界内的交互区域优先 RBL-641）；「水合的驱动模式」：全序（默认树根开始）vs 交互驱动（用户意图）。
- 实现的机制：React 18 的 hydration 优化——**事件委托**（document 级监听——水合前的点击被捕获并缓存 → 水合完成后重放（RBL-641 的机制）；「交互驱动的优先水合」= 点击 → 该 Suspense 边界优先（React 18 对 discrete 事件的捕获与重放，点击目标所在的 Suspense 边界优先水合）。
- RSC 下的流序与水合序的分离：SSR 流序 = 数据到达顺序（server 侧 RBL-655）；水合序 = client JS 加载 + 交互驱动（client 侧）——「流序 ≠ 水合序」（流式先到的组件可能后水合——水合顺序由 client JS 决定）。
- 追问钩子：为什么「流序 ≠ 水合序」的分离是 RSC 架构的进步？——传统 SSR：HTML 与 JS 绑定（水合按 JS 加载顺序——与 HTML 无关）；RSC：流式 HTML 即时渲染（用户立即看到）+ 水合独立调度（交互驱动）——「视觉就绪与交互就绪的解耦」：用户先看到内容（流式渲染）后获得交互（水合）——两阶段各自由不同机制优化（流式 = server 数据调度、水合 = client JS 优先级），是 RSC 架构的核心进步之一。

```tsx
// 选择性水合的语义（React 18+）
// app/page.tsx
export default function Page() {
  return (
    <>
      <Suspense fallback={<Skeleton />}><Sidebar /></Suspense>       {/* 慢边界 */}
      <Suspense fallback={<MainSkeleton />}><MainContent /></Suspense>  {/* 快边界 */}
      <Suspense fallback={null}><InteractiveWidget /></Suspense>     {/* 交互组件 */}
    </>
  );
}
// 流序：MainContent 先到（快）→ Sidebar 后到（慢）
// 水合：用户点击 InteractiveWidget → React 优先水合该边界
// → 其余边界后台水合——用户无需等待全页水合
// 全局事件委托（水合前的点击缓存与重放）
document.addEventListener('click', (e) => {
  if (!window.__hydrated) {
    (window.__pendingEvents ??= []).push(e);
  }
}, { capture: true });
// 水合完成后重放
window.__hydrated = true;
(window.__pendingEvents ?? []).forEach(e => {
  e.target.dispatchEvent(new MouseEvent('click', { bubbles: true }));
});
```
