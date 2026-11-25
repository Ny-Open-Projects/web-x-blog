---
title: [MFW-678] 安全头全清单
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-678：安全响应头全清单

**答**:
- 安全头清单（元框架的 middleware 统一注入）：1) **HSTS**（Strict-Transport-Security: max-age=31536000; includeSubDomains——强制 HTTPS）；2) **CSP**（RBL-602 nonce/hash）；3) **X-Frame-Options: DENY**（防点击劫持——或 CSP frame-ancestors）；4) **X-Content-Type-Options: nosniff**（MIME 嗅探防护）；5) **Referrer-Policy: strict-origin-when-cross-origin**（referrer 泄漏最小化）；6) **Permissions-Policy**（camera=(), geolocation=()——API 权限声明）；7) **COOP/COEP**（RBL-892 跨域隔离）。
- 注入策略：middleware 统一（全站默认 + 路由覆盖（API 路由的 CSP 不同——/api 的 CSP 宽松或无需）；「头的默认值 vs 路由覆盖」。
- HSTS 的启用条件：全站 HTTPS 确认后（pre-load 提交前的谨慎——回滚困难：HSTS 的 max-age 是单向的）；「HSTS 的预加载」是单向决策。
- 追问钩子：为什么「安全头的注入统一在 middleware」而不是「每 route 自行设置」？——统一注入 = 全站默认一致（遗漏某 route 的头 = 安全漏洞——手动设置易漏）；middleware 的默认 + 路由覆盖（特殊路由的例外显式化）——「安全默认值的统一性」：安全头的遗漏是静默漏洞（RBL-956 清单）——middleware 统一是防遗漏的架构选择（RBL-953 默认值纪律的安全版）。

```typescript
// middleware：安全头统一注入
export function middleware(req) {
  const res = NextResponse.next();
  const headers = {
    'strict-transport-security': 'max-age=31536000; includeSubDomains',
    'x-frame-options': 'DENY',
    'x-content-type-options': 'nosniff',
    'referrer-policy': 'strict-origin-when-cross-origin',
    'permissions-policy': 'camera=(), microphone=(), geolocation=()',
    'cross-origin-opener-policy': 'same-origin',
  };
  // CSP：动态 nonce（RBL-602）
  const nonce = crypto.randomUUID();
  headers['content-security-policy'] =
    `script-src 'self' 'nonce-${nonce}' 'strict-dynamic'; object-src 'none'`;
  for (const [k, v] of Object.entries(headers)) res.headers.set(k, v);
  res.headers.set('x-nonce', nonce);
  return res;
}
// 路由覆盖（API 的 CSP 例外）
// /api/** 的 CSP 宽松（JSON 响应——无 script 面）
```
