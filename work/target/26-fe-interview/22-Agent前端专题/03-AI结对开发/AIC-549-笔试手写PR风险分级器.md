---
title: [AIC-549] 笔试：手写 PR 风险分级器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-549：笔试：手写 PR 风险分级

**答**：实现 `classifyPR(files, { hasTests, touchesCache, securityPaths })`。files: `{ path, linesChanged, provenance }[]`. 规则：1) T0：securityPaths 命中或 linesChanged > 500；2) T1：有测试文件变更或 touchesCache（缓存/测试是高风险变更）；3) T2：普通业务代码变更；4) T3：纯文档/配置/样式变更（不含 JS/TS 逻辑）；5) 返回 `{ level: 'T0'|'T1'|'T2'|'T3', reasons: string[], requiresHuman: boolean }`（requiresHuman = T0 或 T1 且无测试）。边界：files 空（T3）；多文件不同级别（取最高——min(T)）；provenance='human' 的文件不影响分级（人写的不需要 AI 分级——但仍计入影响面）。

```javascript
function classifyPR(files = [], { hasTests = false, touchesCache = false,
  securityPaths = [/auth\//, /payment\//, /crypto\//] } = {}) {
  if (!files.length) return { level: 'T3', reasons: [], requiresHuman: false };
  let level = 3; const reasons = [];
  for (const f of files) {
    const isSecurity = securityPaths.some(p => p.test(f.path));
    const isDoc = /\.(md|txt|css|scss)$/.test(f.path);
    if (isSecurity) { level = Math.min(level, 0); reasons.push(`${f.path}: security path`); }
    if (f.linesChanged > 500) { level = Math.min(level, 0); reasons.push(`${f.path}: large change (${f.linesChanged} lines)`); }
    if (f.path.match(/\.(test|spec)\./)) { hasTests = true; }
    if (f.path.includes('cache') || f.path.includes('middleware')) { touchesCache = true; }
    if (!isDoc && !isSecurity && f.linesChanged <= 500 && level > 2) level = Math.min(level, 2);
    if (isDoc && level > 3) level = 3;
  }
  if (touchesCache) { level = Math.min(level, 1); reasons.push('touches cache layer'); }
  if (hasTests) { level = Math.min(level, 1); reasons.push('includes test changes'); }
  const requiresHuman = level === 0 || (level === 1 && !hasTests);
  return { level: `T${level}`, reasons, requiresHuman };
}

// 自测
// T0：security path
let r = classifyPR([{ path: 'auth/login.ts', linesChanged: 50, provenance: 'ai' }]);
console.log(r.level === 'T0' && r.requiresHuman === true);
console.log(r.reasons.some(x => x.includes('security')));

// T0：大变更
r = classifyPR([{ path: 'src/app.ts', linesChanged: 600, provenance: 'ai' }]);
console.log(r.level === 'T0' && r.reasons.some(x => x.includes('large change')));

// T1：有测试变更
r = classifyPR([{ path: 'src/utils.test.ts', linesChanged: 20, provenance: 'ai' }], { hasTests: true });
console.log(r.level === 'T1');

// T2：普通业务
r = classifyPR([{ path: 'src/components/List.tsx', linesChanged: 30, provenance: 'ai' }]);
console.log(r.level === 'T2' && !r.requiresHuman);

// T3：纯文档
r = classifyPR([{ path: 'README.md', linesChanged: 10, provenance: 'ai' }]);
console.log(r.level === 'T3' && !r.requiresHuman);

// 多文件：取最高
r = classifyPR([
  { path: 'README.md', linesChanged: 5, provenance: 'ai' },
  { path: 'payment/charge.ts', linesChanged: 30, provenance: 'ai' },
]);
console.log(r.level === 'T0');                          // min(3, 0) = 0
// 空
console.log(classifyPR([]).level === 'T3');
```

**评分点**：
- 四级分级完整（T0 security/large → T1 cache/tests → T2 business → T3 docs）
- requiresHuman 语义（T0 强制 / T1 无测试时强制——RBL-505 信任路由的 PR 版）
- 多文件取最高级别（min(T)——最高风险决定整体）；边界（空 files）
- 能说清「PR 风险分级不是全有全无：多文件 PR 取最高风险文件的级别——一个安全文件 = 整个 PR 需要 security review」属于加分
