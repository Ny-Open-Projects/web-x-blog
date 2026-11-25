---
title: [MFW-601] 隐私合规的埋点架构：无 cookie 追踪与同意门控
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-601：隐私合规的埋点架构

**答**:
- GDPR 下的埋点分层：1) **无 cookie 统计**（Plausible/Fathom 类：不设 cookie 不做跨站追踪——「匿名聚合」：同意前可用的统计层）；2) **同意后全量**（用户行为流：GA/自建——consent gate 后加载 RBL-827）；3) **同意状态管理**（CMP SDK → consent 事件 → 埋点系统订阅——「同意状态的单一来源」）。
- 埋点的事件 schema：版本化（RBL-912 新旧版本并存——schema registry）；「事件的最小化原则」：只收业务必需字段（GDPR data minimization——location 只到国家级）。
- server 侧埋点的优势：RSC 的服务端事件（action 完成即埋点——server 侧天然无 cookie 依赖、无 consent 问题？——不：匿名用户标识仍是个人信息——「IP/设备指纹 = 个人数据」GDPR 认定：server 埋点也要最小化）。
- 追问钩子：为什么「无 cookie 统计」在 GDPR 下不需要同意弹窗？——GDPR 的同意要求针对「个人数据处理」；匿名聚合（无标识符/不可回溯个体）不属于个人数据 → 免同意；但「匿名」的标准严格：IP 截断/无指纹/无跨会话 id——「合规的关键是数据处理方式而非工具」：同样用 GA，匿名模式 vs 追踪模式的合规性不同——架构层要设计「数据最小化的统计通道」而非「买一个合规工具」。

```typescript
// 分层埋点
// 1) 无 cookie 层（匿名聚合：免同意）
function trackAnonymized(event: string) {
  fetch('/api/track', { method: 'POST', body: JSON.stringify({
    event, country: headers.get('x-vercel-ip-country'),   // 国家级：非个人
    ts: Date.now(), path: location.pathname,
    // 无 userId/无 IP/无 fingerprint
  }), keepalive: true });
}
// 2) 同意后层（CMP gate）
let consentGranted = false;
window.addEventListener('cmp-consent', (e) => { consentGranted = e.detail.analytics; });
function trackFull(event: string, data: Record<string, unknown>) {
  if (!consentGranted) { queueFull.push({ event, data }); return; }   // 未同意先排队
  gtag(event, data);
}
// 3) 同意后补发队列
window.addEventListener('cmp-consent', () => {
  if (consentGranted) queueFull.forEach(d => gtag(d.event, d.data));
});
// server 侧（action 完成埋点）
'use server';
export async function placeOrder(...) {
  await db.orders.create(...);
  await track('order_created', { country, value: order.total });   // 最小化：无 PII
}
```
