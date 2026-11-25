---
title: [MFW-603] 笔试：手写 CSP nonce 中间件
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-603：笔试：手写 CSP nonce 中间件

**答**：实现 `cspMiddleware(req, { isStaticPage })`。规则：1) nonce = randomUUID base64；2) CSP 策略按页面类型：动态页（nonce + strict-dynamic）；静态页（hash 模式：hashes 参数注入 + 不用 nonce——CDN 缓存友好 RBL-602）；3) 返回 `{ nonce, cspHeader, requestHeaders: { x-nonce } }`；4) report-only 模式（cspReportOnly: true → `Content-Security-Policy-Report-Only` 头——先观察不拦截 RBL-892 渐进收紧）；5) dev 模式：放宽（'unsafe-eval'——HMR 需要 eval）；6) 危险：允许 'unsafe-inline' 的选项必须显式 deny（opts.allowUnsafeInline 只在测试用）。边界：静态页无 nonce（返回 null）；reportOnly 头名替换。

```javascript
function cspMiddleware(req, { isStaticPage = false, hashes = [], reportOnly = false,
  dev = false, allowUnsafeInline = false } = {}) {
  const nonce = isStaticPage ? null : Buffer.from(crypto.randomUUID()).toString('base64');
  const headerName = reportOnly
    ? 'Content-Security-Policy-Report-Only' : 'Content-Security-Policy';
  let csp;
  if (isStaticPage) {
    csp = `script-src 'self' ${hashes.map(h => `'sha256-${h}'`).join(' ')}`;
  } else {
    csp = `script-src 'self' 'nonce-${nonce}' 'strict-dynamic'`;
    if (dev) csp += " 'unsafe-eval'";                    // HMR 需要
    if (allowUnsafeInline) csp += " 'unsafe-inline'";    // 仅测试
  }
  csp += "; object-src 'none'; base-uri 'self'; frame-ancestors 'self'";
  return {
    nonce,
    headerName,
    cspHeader: csp,
    requestHeaders: nonce ? { 'x-nonce': nonce } : {},
  };
}

// 自测
// 动态页
let r = cspMiddleware(req, {});
console.log(r.nonce.length > 0 && r.headerName === 'Content-Security-Policy');
console.log(r.cspHeader.includes(`'nonce-${r.nonce}'`) && r.cspHeader.includes('strict-dynamic'));
console.log(r.requestHeaders['x-nonce'] === r.nonce);

// 静态页：hash 模式
r = cspMiddleware(req, { isStaticPage: true, hashes: ['h1', 'h2'] });
console.log(r.nonce === null);                           // 静态无 nonce
console.log(r.cspHeader.includes("'sha256-h1'") && !r.cspHeader.includes('nonce'));
console.log(r.requestHeaders['x-nonce'] === undefined);

// report-only
r = cspMiddleware(req, { reportOnly: true });
console.log(r.headerName === 'Content-Security-Policy-Report-Only');

// dev 放宽
r = cspMiddleware(req, { dev: true });
console.log(r.cspHeader.includes("'unsafe-eval'"));

// production 不允许 unsafe-inline（显式拒绝）
r = cspMiddleware(req, {});
console.log(!r.cspHeader.includes("'unsafe-inline'"));

// 静态页 + reportOnly 组合
r = cspMiddleware(req, { isStaticPage: true, hashes: ['h1'], reportOnly: true });
console.log(r.headerName.includes('Report-Only') && r.cspHeader.includes('h1'));
```

**评分点**：
- 双模式 CSP（动态 nonce/静态 hash——缓存性与安全性的分层 RBL-602）
- strict-dynamic 传播 + dev 的 unsafe-eval（HMR 现实）+ production 无 unsafe-inline
- report-only 渐进收紧（COEP 同策略 RBL-892）；静态页 nonce=null（缓存兼容）
- 能说清「nonce 与 CDN 缓存的冲突决定 CSP 架构：静态 hash、动态 nonce——按页面角色分层」属于加分
