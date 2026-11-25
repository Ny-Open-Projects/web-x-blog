---
title: [RBL-792] 笔试：手写 CSP 样式审计器（注入向量分类 + nonce 适配建议）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-792：笔试：手写 CSP 样式审计器（向量分类 + 建议）

**答**：实现 `auditStyleVectors(files, csp)`。files: `{ name, code }[]`；csp: `{ styleSrc: string[], styleSrcAttr?: string[] }`（数组为指令值列表，如 ["'self'", "'unsafe-inline'"] 或 ["'self'", "'nonce-abc'"]）。检测三种向量并判定：1) style 标签注入（createElement('style')/insertRule/adoptStyleSheets）——style-src 含 'unsafe-inline' 或有效 'nonce-'/  'sha256-' → pass，否则 violation；2) style 属性注入（.style.cssText/.style.xxx =）——style-src-attr 有 'unsafe-inline' → pass，无该指令 → 默认继承 style-src；3) 返回 `{ findings: Array<{ file, vector, verdict: 'pass'|'violation', suggest }>, cspSafe }`（cspSafe = 无 violation）。边界：空 files；指令大小写不敏感。

```javascript
function auditStyleVectors(files, csp = {}) {
  const styleSrc = (csp.styleSrc ?? []).map(s => s.toLowerCase());
  const attrSrc = (csp.styleSrcAttr ?? csp.styleSrc ?? []).map(s => s.toLowerCase());
  const allows = (list) => list.includes("'unsafe-inline'") ||
    list.some(v => v.startsWith("'nonce-") || v.startsWith("'sha256-"));

  const findings = [];
  for (const f of files) {
    const code = f.code ?? '';
    const tagInject = /createElement\(\s*['"]style['"]\s*\)|insertRule\(|adoptedStyleSheets/.test(code);
    const attrInject = /\.style\.(cssText|setProperty)/.test(code);
    if (tagInject)
      findings.push({ file: f.name, vector: 'style-tag',
        verdict: allows(styleSrc) ? 'pass' : 'violation',
        suggest: allows(styleSrc) ? null : '配置 nonce 或静态提取（RBL-752）' });
    if (attrInject)
      findings.push({ file: f.name, vector: 'style-attr',
        verdict: allows(attrSrc) ? 'pass' : 'violation',
        suggest: allows(attrSrc) ? null : 'style 属性需 style-src-attr 指令放行' });
  }
  return { findings, cspSafe: !findings.some(x => x.verdict === 'violation') };
}

// 自测
const files = [
  { name: 'a.js', code: "const s = document.createElement('style');" },
  { name: 'b.js', code: 'el.style.setProperty("--x", "1");' },
];
let r = auditStyleVectors(files, { styleSrc: ["'self'", "'nonce-abc'"] });
console.log(r.findings[0].verdict === 'pass');           // nonce 放行
console.log(r.findings[1].verdict === 'pass');           // attr 继承 style-src 的 nonce

r = auditStyleVectors(files, { styleSrc: ["'self'"] });
console.log(r.findings[0].verdict === 'violation');
console.log(r.findings[0].suggest.includes('nonce'));
console.log(r.findings[1].verdict === 'violation');
console.log(r.cspSafe === false);

r = auditStyleVectors(files, { styleSrc: ["'self'", "'unsafe-inline'"] });
console.log(r.cspSafe === true);

console.log(auditStyleVectors([], { styleSrc: ["'self'"] }).cspSafe === true);
```

**评分点**：
- 双向量分类正确（style 标签 vs style 属性，指令归属不同）
- nonce/sha 值视为放行、'unsafe-inline' 判定；attr 无独立指令继承 style-src 的规范语义
- suggest 给可操作建议；cspSafe 汇总
- 能说清「nonce 是迁移期桥梁（每响应唯一与 CDN 缓存冲突），静态提取才是终态」属于加分
