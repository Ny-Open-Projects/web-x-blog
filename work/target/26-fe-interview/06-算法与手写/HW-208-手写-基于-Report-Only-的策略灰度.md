---
title: [HW-208] 手写 CSP 策略灰度——按用户分桶下发不同策略强度（Report-Only/强制/严格）的实验
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-208：手写 CSP 策略灰度——按用户分桶下发不同策略强度（Report-Only/强制/严格）的实验
**答**：CSP 强度灰度实验：策略分级（L0 宽松/L1 nonce/L2 strict-dynamic 严格）→ 按用户分桶下发（HW-231 ALG 分桶思路，服务端按桶返回 CSP 头）→ 双头观察（强制桶 + Report-Only 精细桶）→ 违规率/业务错误率对比决定放量。边缘函数实现（CDN 层按 cookie 分桶注入头）。

```javascript
// CDN edge function（伪码）：按分桶下发策略（部署时作为默认导出：export default handler）
async function handler(request) {
  const bucket = hash(request.headers.get('cookie')?.match(/uid=([^;]+)/)?.[1] ?? 'anon') % 100;
  const POLICIES = {
    l0: "script-src 'self' https: 'unsafe-inline'",
    l1: "script-src 'self' 'nonce-{NONCE}' https:",
    l2: "script-src 'self' 'nonce-{NONCE}' 'strict-dynamic'",
  };
  const level = bucket < 10 ? 'l2' : bucket < 40 ? 'l1' : 'l0';   // 10% 严格 / 30% 中间 / 60% 宽松
  const nonce = crypto.randomUUID();
  const html = await render(request, { nonce });
  const headers = {
    'Content-Security-Policy': POLICIES[level].replaceAll('{NONCE}', nonce),   // 强制桶
    'Content-Security-Policy-Report-Only': POLICIES.l2.replaceAll('{NONCE}', nonce),  // 全量精细观察
    'X-CSP-Level': level,                                 // 上报关联：违规报告带级别
  };
  return new Response(html, { headers });
}
// 灰度语义：
// 强制桶验证业务无报错；Report-Only 全量桶观察"升级到 L2 会拦什么"
// X-CSP-Level 随违规上报 —— 分桶对比违规率（l2 桶拦截率 < 0.1% 才可扩量）
// 对照指标：业务错误率（l2 桶不高于 l0 桶）—— 性能/安全实验的联合门禁（PER-493）
```

**评分点**：
- 分桶下发不同强度 CSP（边缘函数实现）——本题核心。
- 强制桶 + Report-Only 全量桶的双通道观察。
- X-CSP-Level 关联违规上报（分桶对比放量依据）。
- 业务错误率对照的安全实验门禁（PER-493 联动）。
