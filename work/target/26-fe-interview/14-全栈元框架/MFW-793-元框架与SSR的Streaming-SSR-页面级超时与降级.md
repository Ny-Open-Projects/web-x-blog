---
title: [MFW-793] 页面级超时与降级
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-793：页面级超时与降级

**答**:
- SSR 页面的超时策略（RBL-505 + RBL-655 深化）：1) **全局超时**（页面渲染超时（如 10s）→ 取消渲染 → 发送降级 HTML（RBL-648 降级方案）；2) **per-Suspense 超时**（单个边界超时 → 该段 fallback（不影响其他段——RBL-655 的超时降级）；3) **降级的层次**：S超时 → fallback → 数据缺失渲染（默认值/缓存数据）→ 全页 error——「降级的渐进性」：每级降级保留更多功能；4) **超时的实现**：Promise.race(fetch, timeout)——per-fetch 超时（组件内）+ 全页超时（middleware/Next 配置）。
- 大促场景的超时降级：LCP 内容超时 → 降级到缓存快照（上次大促的静态页面——有数据但可能过时——比白屏好）；「降级的可接受度」= 数据时效敏感度（价格可缓存 vs 库存必须实时——RBL-618 缓存角色的降级映射）。
- 追问钩子：为什么「超时降级比全页 error」在大促场景更必要？——全页 error = 用户白屏（流失）；超时降级 = 部分内容可用（用户至少看到页面结构 + 缓存数据——转化率虽降但非零）；「部分可用优于完全不可用」——大促场景的降级优先级（RBL-648 的功能降级 × 渲染降级 = 页面级降级矩阵）；「降级的自动化」= 超时阈值驱动的自动降级（RBL-649 决策器的 SSR 版）。

```tsx
// 页面级超时降级
export default async function CampaignPage() {
  return (
    <>
      <Suspense fallback={<HeroFallback />}>
        <HeroWithTimeout />                               {/* LCP 洞：带超时 */}
      </Suspense>
      <Suspense fallback={<StockFallback />}>
        <RealtimeStock />                                 {/* 实时库存：带超时 */}
      </Suspense>
    </>
  );
}
// 超时组件
async function HeroWithTimeout() {
  const data = await Promise.race([
    getCampaignData(),
    new Promise((_, rej) => setTimeout(() => rej(new TimeoutError()), 3000)),
  ]).catch(() => getCachedCampaign());                   // 超时 → 缓存数据降级
  return <Hero data={data} />;
}
// 超时降级层次
// L1: per-fetch timeout → 组件级缓存数据降级
// L2: per-Suspense timeout → fallback UI（RBL-655）
// L3: 全页 timeout → 静态壳（RBL-648 L3）
// L4: 全页 error → error.tsx（RBL-536）
```
