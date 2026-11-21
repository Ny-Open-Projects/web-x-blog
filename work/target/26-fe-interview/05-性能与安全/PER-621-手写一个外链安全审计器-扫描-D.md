---
title: [PER-621] 手写一个外链安全审计器：扫描 DOM 中所有跳转链接，检查 opener 风险与 javascript: 协议
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-621：手写一个外链安全审计器：扫描 DOM 中所有跳转链接，检查 opener 风险与 javascript: 协议

**答**：
- 审计三类问题：`target=_blank` 缺 `rel=noopener noreferrer`（tabnabbing 反向）、`href` 为 `javascript:` 或 `data:` 协议（XSS sink）、外链未走跳转中转（无法做外链安全提示）。
- 实现：遍历 `document.querySelectorAll('a[href]')`，逐条判定输出报告；对动态渲染的 SPA，监听 MutationObserver 持续审计。
- 边界：同域锚点跳转（#section）不算外链；中转确认页可白名单豁免；审计工具本身不修改 DOM（只报告），修复建议给出标准 rel 值。
- 评分点：协议白名单校验与 SPA 动态审计。

```javascript

const SAFE_PROTOCOL = /^(https?:|mailto:|tel:)/i;
function auditLinks(root = document) {
  const issues = [];
  root.querySelectorAll('a[href]').forEach(a => {
    const href = a.getAttribute('href')?.trim() ?? '';
    if (href.startsWith('#')) return;                        // 页内锚点跳过
    if (!SAFE_PROTOCOL.test(href)) {
      issues.push({ a, type: 'danger-protocol', href: href.slice(0, 50) });
      return;
    }
    const rel = a.rel;
    if (a.target === '_blank' && !(rel?.includes('noopener') && rel?.includes('noreferrer'))) {
      issues.push({ a, type: 'opener-risk', fix: 'rel="noopener noreferrer"' });
    }
  });
  return issues;
}
// SPA 持续审计
const mo = new MutationObserver(() => {
  auditLinks().forEach(i => console.warn('[link-audit]', i.type, i.a));
});
mo.observe(document.body, { childList: true, subtree: true });
```
