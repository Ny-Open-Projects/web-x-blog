---
title: [MFW-655] 多个 Suspense 的协调：优先级与流序
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-655：多个 Suspense 的协调

**答**:
- 多 Suspense 边界的流序：1) **树序决定流序**（浅层边界先 resolve 先发——嵌套深度的隐式优先级 RBL-520）；2) 同层多个边界的顺序（完成顺序——先到先发（数据到达驱动）；3) 「关键内容优先」的显式控制：关键数据放浅层边界、次要数据深层（RBL-520 层次化优先级）。
- 流序与用户体验：首包 = shell + 先完成的边界（渐进填充）；「后到的边界」用户体验（骨架到内容的替换——替换的视觉稳定性（占位尺寸 RBL-565））。
- 多 Suspense 的协调算法：React 的流调度——每个边界独立 resolve（数据到达即 flush——不等其他边界）；「全局超时」（某边界一直未 resolve——超时降级（超时 fallback：变体数据源/默认值））。
- 追问钩子：为什么「同层边界按完成顺序发」而不是「按树序固定等待」？——按树序 = 最慢的边界阻塞所有后续（header 等 footer 的数据——不必要的串行）；按完成序 = 独立流式（先到的先渲染——并行度最大化）；「流式的本质 = 解耦完成顺序与显示顺序」——协议层（Flight 的 ID 引用）让任意顺序的完成都可正确渲染（RBL-501 设计动机）。

```tsx
// 多 Suspense 的流序
export default async function Page() {
  return (
    <>
      {/* 浅层：先 resolve 先发 */}
      <Suspense fallback={<HeaderSkeleton />}><Header /></Suspense>
      {/* 同层：按数据到达顺序 */}
      <div className="grid">
        <Suspense fallback={<CardSkeleton />}><Trending /></Suspense>       {/* 快查询先发 */}
        <Suspense fallback={<CardSkeleton />}><Personalized /></Suspense>   {/* 慢查询后发 */}
      </div>
      {/* 深层：最后发 */}
      <Suspense fallback={null}><Footer /></Suspense>
    </>
  );
}
// 超时降级（某边界未 resolve）
async function Trending() {
  const data = await Promise.race([
    getTrending(),
    new Promise((_, rej) => setTimeout(() => rej(new TimeoutError()), 3000)),
  ]).catch(() => DEFAULT_TRENDING);                     // 超时 → 默认值（超时 fallback）
  return <List items={data} />;
}
```
