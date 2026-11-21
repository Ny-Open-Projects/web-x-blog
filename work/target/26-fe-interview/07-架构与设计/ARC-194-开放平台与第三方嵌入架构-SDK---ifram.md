---
title: [ARC-194] 开放平台与第三方嵌入架构（SDK / iframe 安全）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-194：开放平台与第三方嵌入架构（SDK / iframe 安全）如何设计？
**答**：
- 两种交付形态：JS SDK（第三方页面引入，跑在对方域）与 iframe 嵌入（我们的页面被嵌，跑在我们域）——安全模型完全不同：SDK 要防"被恶意宿主滥用"，iframe 要防"被恶意宿主窥探"。
- SDK 安全设计：命名空间隔离（不污染全局）、能力白名单（按 appKey 授权）、通信走 postMessage 且校验 origin、防嵌套劫持（禁止被未授权域加载核心 iframe）。
- iframe 侧防护：CSP frame-ancestors 白名单（只允许授权方嵌入）、postMessage 消息协议带签名与 origin 校验、sandbox 属性最小权限、Cookie SameSite 防 CSRF。
- 版本与兼容承诺：SDK 遵循严格 semver + N-2 支持， breaking 提前 90 天公告；SDK 体积与加载性能是第三方接入的第一体验，做懒加载与按需子包。

```typescript
// 开放平台 postMessage 协议与安全校验
interface OpenMessage {
  v: 1;                                   // 协议版本
  appId: string;
  nonce: string;                          // 防重放
  action: string;                         // 白名单动作
  payload: unknown;
  sig: string;                            // appId secret 对 payload 的 HMAC
}

// iframe 侧（我们的页面被嵌入）：严格 origin 校验
window.addEventListener('message', async (e) => {
  const allowed = await acl.verifyOrigin(e.origin, e.data.appId);   // 1. origin + appId 双校验
  if (!allowed) return;
  if (!verifySig(e.data)) return;                                   // 2. 签名防篡改
  if (seenNonces.has(e.data.nonce)) return;                         // 3. 防重放
  seenNonces.add(e.data.nonce);
  const result = await dispatch(e.data.action, e.data.payload);     // 4. 动作白名单分发
  e.source!.postMessage({ ...e.data, result }, { targetOrigin: e.origin });  // 回信也锁 origin
});
// 我们侧防护清单：
// 1. CSP: frame-ancestors https://partner-a.com https://partner-b.com
// 2. Cookie: SameSite=Lax; Secure
// 3. 敏感操作二次确认（宿主环境不可信）
// SDK 交付约定：
//   semver 严格版控 + N-2 支持 + breaking 提前 90 天公告
//   体积预算：核心 SDK < 30KB gzip，子能力动态 import
```
