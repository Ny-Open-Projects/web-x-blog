---
title: [TST-850] 笔试：手写一个「CSP 合规检查器」（违规上报解析与判定）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-850：笔试：手写一个「CSP 合规检查器」（违规上报解析与判定）
**答**：
- 需求：实现 checkCSP(report, policy) —— report 是浏览器 CSP violation 上报对象，policy 定义允许的指令来源。
- 规则：解析 report['csp-report'] 的 violated-directive 与 blocked-uri；若 blocked-uri 的来源不在 policy 白名单则记为违规。
- 边界：report 格式错误返回 invalid；违规去重（同 directive+uri 只记一次）；输出违规列表与是否合规。

```javascript
function checkCSP(report, policy) {
  const r = report?.['csp-report'];
  if (!r || !r['violated-directive']) return { valid: false, reason: '格式错误' };
  const directive = r['violated-directive'].split(' ')[0];
  const uri = r['blocked-uri'] || '';
  const allowed = policy[directive] || [];
  const origin = uri.startsWith('http') ? new URL(uri).origin : uri;
  const violated = !allowed.some(a => origin === a || a === "'self'" && origin === policy.__self);
  return { valid: true, violated, directive, uri, origin };
}
function dedupe(results) {
  const seen = new Set();
  return results.filter(r => {
    const k = `${r.directive}|${r.uri}`;
    if (seen.has(k)) return false; seen.add(k); return true;
  });
}
console.log(checkCSP({ 'csp-report': {
  'violated-directive': 'script-src', 'blocked-uri': 'https://evil.com/x.js'
} }, { 'script-src': ["'self'"], __self: 'https://my.app' })); // violated:true
```
**评分点**：
- 正确解析 csp-report 字段并匹配白名单来源。
- 违规去重（directive+uri）避免重复上报。
- 格式错误返回 valid:false，边界健壮。
- 能点出 CSP 违规上报是「运行时安全监控」而非仅构建期配置——加分项。
