---
title: [WCN-982] 大促端到端：从 islands SSR 到运行时信号更新，全链路怎么保证不崩
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-982：大促端到端：从 islands SSR 到运行时信号更新，全链路怎么保证不崩

**答**：
- 结论先行：大促链路要「静态兜底、动态增强、故障可退」——SSR 输出完整可下单的 HTML（零 JS 可用），islands 只水合核心交互，运行时信号更新做合帧与降级。
- SSR 阶段：DSD 输出完整商品卡，首屏 token/aria 内联，零 JS 也能加购（原生表单跳确认页）。
- 水合阶段：核心岛（SKU/加购）优先水合，非核心岛延后；单岛 chunk 失败不影响整页（前文降级策略）。
- 运行时：库存/价格高频更新走 rAF 合帧 + Worker 下沉，低端机降档；监控水合失败率、a11y、性能指标。
- 追问钩子：面试官问「大促峰值怎么压测这条链路」——答：分别压 SSR 吞吐、chunk CDN 命中、WS 消息频率、主线程长任务，瓶颈在哪层就扩容/降级哪层。

```javascript
// 大促链路分层兜底
async function enhanceBuyBox(el) {
  try { (await import('./buy.js')).hydrate(el); } // 增强：交互 water
  catch { el.dataset.degraded = 'true'; }        // 失败：保留 SSR 原生表单
}
// 运行时高频更新合帧
let pending = null;
function onStock(sku, n) {
  pending = { ...(pending||{}), [sku]: n };
  requestAnimationFrame(() => { applyStock(pending); pending = null; });
}
function applyStock(data) { /* 最小 DOM patch */ }
```
