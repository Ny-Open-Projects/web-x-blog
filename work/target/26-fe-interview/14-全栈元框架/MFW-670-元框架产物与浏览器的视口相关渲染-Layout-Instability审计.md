---
title: [MFW-670] Layout Instability 审计
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-670：Layout Instability 审计

**答**:
- CLS 的系统性审计（RBL-565 扩展）：1) **构建期预检**（SSR HTML 的布局骨架——占位尺寸 vs 真实尺寸的偏差预估：商品图 4:3 固定 vs 用户头像 1:1 假设）；2) **RUM 归因**（layout-shift 的 source 元素 + 来源组件——CLS 归因到组件级（RBL-565 的 performance observer）；3) **审计门禁**（CLS > 0.1 的页面 fail——预算化）。
- CLS 的常见源与修复：1) 图片无尺寸（aspect-ratio 占位 RBL-565）；2) 字体 swap（metrics 对齐 RBL-564）；3) 动态内容插入（骨架尺寸精度——预留 vs 真实）；4) 广告/第三方（固定容器尺寸 RBL-882）；5) 水合后的状态渲染（client state 渲染条件内容——骨架对齐）。
- CLS 的量级感知：0.1 = 「需要滚动内容的页面」（Google 阈值）、0.25 = 「差」；「CLS 的分位值」（P75 用户的 CLS——不是均值（少数页面差但多数好 = P75 反映真实体验））。
- 追问钩子：为什么「CLS 的 P75」比「均值」更真实？——CLS 是长尾指标（多数页面 CLS≈0、少数页面 0.5——均值被稀释为 0.05 看起来健康）；P75（75 分位用户的体验）= 真实用户感知（25% 用户 CLS 0.3+ 的页面 = 真实痛点）；「Web Vitals 的分位值哲学」（Google 的 Core Web Vitals 都用 P75）——均值掩盖长尾是性能监控的经典陷阱（RBL-588 p50/p90 的用户感知版）。

```typescript
// CLS 审计（RUM 归因）
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    if (e.hadRecentInput) return;                        // 用户交互后的偏移不计（Google 规范）
    const sources = (e.sources ?? []).map(s => ({
      node: s.node?.nodeName, cls: s.node?.className?.slice?.(0, 30),
      rect: { top: s.previousRect?.top, height: s.previousRect?.height },
    }));
    report({ cls: e.value, sources, route: location.pathname,
      buildId: window.__BUILD_ID });                     // 归因到组件/路由
  }
}).observe({ type: 'layout-shift', buffered: true });
// 分位值聚合
function clsP75(entries: { cls: number }[]) {
  const sorted = entries.map(e => e.cls).sort((a, b) => a - b);
  return sorted[Math.floor(sorted.length * 0.75)] ?? 0;
}
// 门禁：CLS P75 > 0.1 fail（RBL-662 预算）
```
