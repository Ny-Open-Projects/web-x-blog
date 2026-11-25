---
title: [MFW-795] Suspense 水合顺序对用户体验的影响
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-795：Suspense 水合顺序与 UX

**答**:
- 水合顺序对用户感知的影响（RBL-710/641 的 UX 维度）：1) **流序与视觉感知**（先到的内容先渲染——用户从上到下阅读：header → main → footer 的自然流序；2) **交互阻塞**（用户点击未水合区域 → 事件被缓存 RBL-710 → 水合后重放——用户感知 = 点击延迟）；3) **水合顺序与布局**（水合顺序不影响布局（HTML 已渲染——布局固定）——水合影响交互响应性（RBL-640 INP）；4) **最优水合序**：用户最可能交互的区域优先（视口内 > 视口外、主内容 > 次要内容——RUM 交互热图驱动 RBL-641）。
- RSC 流式下的感知阶段：1) TTFB（HTML shell 可见——骨架屏）；2) 流式填充（各 Suspense resolve——内容逐段出现）；3) 水合完成（可交互）；4) 「感知三阶段」= 用户的不同期待（可见 → 完整 → 可交互）——每阶段的优化策略不同。
- 追问钩子：为什么「TTI（可交互时间）」比「FCP/LCP」在 RSC 场景更值得关注？——RSC 的 FCP/LCP 已经很快（SSR HTML 即时渲染——流式填充）；TTI（可交互）是「水合完成后的时间」（JS 下载 + 水合 = TTI 的延迟来源）；「三阶段的用户期待」：看到内容后立即尝试交互——但交互不响应直到水合完成——「视觉就绪但不可交互」的间隙是 RSC 的 UX 关键问题（RBL-640 INP）——优化方向：缩小这个间隙（选择性水合/渐进增强——水合前也响应）。

```tsx
// RSC 页面的三阶段 UX
// Phase 1: HTML 可见（TTFB ~200ms）
// Phase 2: 内容完整（流式 ~1s）——LCP
// Phase 3: 可交互（水合 ~2s）——TTI
// 用户的感知：200ms 看到内容 → 立即点击 → 1.8s 后才响应 ← 间隙问题
// 优化：水合优先级（RBL-641）+ 渐进增强（RBL-512）+ 乐观 UI（RBL-580）
// Suspense 的水合顺序
<Suspense fallback={<NavSkeleton />}><Nav /></Suspense>       ← 用户常交互：高优先
<Suspense fallback={null}><MainContent /></Suspense>
<Suspense fallback={null}><Footer /></Suspense>               ← 低优先
// Nav 的 JS chunk 前置（HTML 流序控制）
// <script src="nav-chunk.js"> → 提前加载 → 先水合
```
