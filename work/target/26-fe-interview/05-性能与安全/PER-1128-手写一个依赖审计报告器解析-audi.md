---
title: [PER-1128] 手写一个依赖审计报告器：解析 audit 结果输出门禁判定
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1128：手写一个依赖审计报告器：解析 audit 结果输出门禁判定

**答**：
- 需求：实现 auditGate(auditJson, policy)。auditJson 为 npm audit --json 输出（vulnerabilities: { name: { severity, via, range, fixAvailable } }）；policy: { block: [critical, high], allowlist: [包名], requireFix: true }；输出 { verdict, blocked: [{ name, severity, fixAvailable }], waived }；verdict = fail 当存在非豁免的 block 级漏洞；requireFix 且 fixAvailable 为 false 时单独列出 unfixed。
- 边界：via 为数组（可能含字符串或对象）只取 severity 依据；allowlist 豁免进 waived；空 vulnerabilities 全过。
- 评分点：级别判定；豁免清单；无修复单列；人话 summary

```javascript
function auditGate(auditJson, policy) {
  const vulns = auditJson.vulnerabilities ?? {};
  const blocked = [], waived = [], unfixed = [];
  for (const [name, v] of Object.entries(vulns)) {
    if (policy.allowlist.includes(name)) { waived.push(name); continue; }
    const sev = v.severity;
    if (policy.block.includes(sev)) {
      blocked.push({ name, severity: sev, fixAvailable: !!v.fixAvailable });
      if (policy.requireFix && !v.fixAvailable) unfixed.push(name);
    }
  }
  return { verdict: blocked.length ? 'fail' : 'pass',
    blocked, waived, unfixed,
    summary: blocked.length
      ? `拦截 ${blocked.length} 个高危依赖` + (unfixed.length ? `，其中 ${unfixed.length} 个无修复版本需人工处理` : '')
      : '依赖审计通过' };
}
```
