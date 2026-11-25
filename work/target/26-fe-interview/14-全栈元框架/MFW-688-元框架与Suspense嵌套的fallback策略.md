---
title: [MFW-688] Suspense 嵌套的 fallback 策略
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-688：Suspense 嵌套 fallback 策略

**答**:
- 嵌套 Suspense 的 fallback 行为：1) **最近祖先 fallback**（子 Suspense 挂起 → 最近的 Suspense 边界显示 fallback——不是所有祖先都 fallback）；2) 嵌套的粒度控制（外层 fallback = 页面级骨架（首次加载）；内层 fallback = 细粒度占位（局部更新））；3) 「fallback 的尺寸精度」（RBL-565 骨架尺寸 = 内容尺寸的预估——嵌套层级越深 fallback 越细粒度）。
- fallback 的分层策略：1) 页面级（loading.tsx——路由段级 fallback RBL-524）；2) 组件级（Suspense fallback prop——局部占位）；3) inline fallback（null——不显示占位（后台静默加载））。
- 嵌套流式（RBL-520 多 Suspense）的 fallback 协调：外层未完成时内层已完成——内层内容不渲染（外层 fallback 显示——流序由树序 RBL-655）；「嵌套的流序」= 外层先 resolve（数据到达）→ 外层内容流出 → 内层边界开始 resolve。
- 追问钩子：为什么「嵌套 Suspense 的最近祖先 fallback」会导致「外层骨架覆盖内层内容」？——子 Suspense 挂起 → 最近祖先（外层 Suspense）显示 fallback——但内层子树已完成的部分也一起被 fallback 覆盖（嵌套的粒度语义：外层挂起 = 整个外层子树显示 fallback——内层已完成的也被遮挡）；「嵌套的 fallback 粒度」：外层挂起覆盖内层 = 粗粒度 fallback（页面级骨架）；内层独立 Suspense（非嵌套）= 细粒度（局部占位）——嵌套结构决定 fallback 的粒度语义。

```tsx
// 嵌套 Suspense 的 fallback 粒度
export default function Page() {
  return (
    <>
      {/* 外层：页面级骨架（首次加载） */}
      <Suspense fallback={<PageSkeleton />}>
        <ProductDetails />                                {/* 慢：外层挂起 */}
        <Suspense fallback={null}>                        {/* 内层：局部更新 */}
          <Reviews />                                     {/* 快：内层完成 */}
        </Suspense>
      </Suspense>
    </>
  );
}
// 外层 ProductDetails 未 resolve → 整个外层 fallback（含内层 Reviews）——粗粒度
// 修正：平级拆分（非嵌套）
export default function Page() {
  return (
    <>
      <Suspense fallback={<DetailSkeleton />}><ProductDetails /></Suspense>
      <Suspense fallback={null}><Reviews /></Suspense>   {/* 平级：独立流式 RBL-655 */}
    </>
  );
}
// 平级：各自独立流式（Reviews 先到先渲染——不被外层骨架遮挡）
```
