---
title: [MFW-645] 笔试：手写埋点 schema 审计器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-645：笔试：手写埋点 schema 审计器

**答**：实现 `auditTracking(code, registry)`。code: 源码字符串；registry: `Record<event, string[]>`（事件 → 合法字段）。规则（RBL-644）：1) 未注册事件 → 'unregistered-event'；2) 未注册字段 → 'unregistered-field'；3) PII 泄漏（payload 含 email/phone/token/ssn 模式）→ 'pii-leak'（error 级）；4) 重复埋点（同文件同事件名 ≥2 次 → 'duplicate'——不含条件分支内的不同路径）。按行扫描返回 `{ findings: Array<{ line, event, type, field? }>, piiCount }`。边界：无 track 调用（空）；registry 空（全部 unregistered——schema 未建时降级为 warn 而非 error：opts.strict）。

```javascript
function auditTracking(code = '', registry = {}, { strict = true } = {}) {
  const findings = []; let piiCount = 0;
  const PII = /email|phone|token|ssn|credit/i;
  const seen = new Map();                                // file-level 去重（简化为 code 级）
  code.split('\n').forEach((line, i) => {
    const t = line.trim();
    if (t.startsWith('//') || t.startsWith('*')) return;
    for (const m of line.matchAll(/track\(\s*['"](\w+)['"]\s*,\s*\{([^}]*)\}/g)) {
      const [, event, fields] = m;
      if (PII.test(fields)) { piiCount++;
        findings.push({ line: i + 1, event, type: 'pii-leak', severity: 'error' }); }
      const known = registry[event];
      if (!known) {
        findings.push({ line: i + 1, event, type: 'unregistered-event',
          severity: strict ? 'error' : 'warn' });
        continue;
      }
      for (const f of fields.matchAll(/(\w+)\s*:/g))
        if (!known.includes(f[1]))
          findings.push({ line: i + 1, event, type: 'unregistered-field', field: f[1] });
      const key = event + ':' + fields;
      if (seen.has(key)) findings.push({ line: i + 1, event, type: 'duplicate' });
      seen.set(key, i);
    }
  });
  return { findings, piiCount };
}

// 自测
const registry = {
  order_created: ['orderId', 'value'],
  page_view: ['path'],
};
const code = [
  "track('order_created', { orderId: '1', value: 9.9 });",       // ok
  "track('order_craeted', { orderId: '1' });",                   // 拼错：unregistered-event
  "track('order_created', { orderId: '1', email: 'x@y.com' });", // PII + 未注册字段
  "track('page_view', { path: '/p' });",
  "track('page_view', { path: '/p' });",                         // duplicate
].join('\n');
let r = auditTracking(code, registry);
console.log(r.piiCount === 1);
console.log(r.findings.filter(f => f.type === 'unregistered-event').length === 1);
console.log(r.findings.some(f => f.type === 'pii-leak' && f.line === 3));
console.log(r.findings.filter(f => f.type === 'unregistered-field').length === 1);   // email
console.log(r.findings.some(f => f.type === 'duplicate' && f.line === 5));
console.log(r.findings.some(f => f.severity === 'error' && f.line === 3));

// 非严格模式
r = auditTracking(code, registry, { strict: false });
console.log(r.findings.find(f => f.type === 'unregistered-event').severity === 'warn');

console.log(auditTracking('const x = 1;', registry).findings.length === 0);
console.log(auditTracking("track('x', {})", {}).findings[0].type === 'unregistered-event');
```

**评分点**：
- 四类发现（unregistered event/field、PII、duplicate）+ 严重度分级（PII error / strict 模式控制 unregistered）
- PII 的正则模式检测（最小化违规——GDPR data minimization RBL-601）；行号定位
- 边界（无调用/空 registry 的 strict 降级）；typed track 作为编译期前置（事后审计兜底）
- 能说清「typed track 让 schema 变更在编译期暴露——事后审计兜底动态事件与外部注入」属于加分
