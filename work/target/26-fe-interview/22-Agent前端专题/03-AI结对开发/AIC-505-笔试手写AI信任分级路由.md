---
title: [AIC-505] 笔试：手写 AI 信任分级路由
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-505：笔试：手写 AI 信任分级路由

**答**：实现 `routeReview(pr, config)`。pr: `{ files: Array<{ path, linesChanged, provenance }>, testsPass: boolean }`；config: `{ criticalPaths: RegExp[], trustThreshold: number }`. 规则：1) 每个 file → assignTrustLevel（RBL-504）；2) **汇总**：T0 存在 → 'manual-review-required'（阻断合并）；全部 T3 → 'auto-merge'；T1 且 testsPass → 'merge-with-note'；T2 → 'sample-review'；3) **审批人建议**：T0 → 指定 security reviewer；T1 → 指定 owner；4) 返回 `{ action, reviewers: string[], level: TrustLevel, files: Array<{ path, level }> }`。边界：provenance 混合（AI+human——按 per-file 分级）；testsPass=false（T1 降为 T0——测试未过 = 全审）；空 files。

```javascript
const CRITICAL_PATHS = [/auth\//, /payment\//, /crypto\//, /security\//];

function assignLevel(file, testsPass) {
  const { path: fp, linesChanged = 0, provenance } = file;
  if (provenance === 'human') return 3;
  if (CRITICAL_PATHS.some(p => p.test(fp))) return 0;
  if (linesChanged > 200) return 0;
  if (fp.match(/\.(test|spec)\./)) return testsPass ? 1 : 0;
  if (fp.match(/\.(css|scss|json|md)$/)) return 3;
  return testsPass ? 1 : 0;                             // 测试不过 = 降级
}
function routeReview(pr, config = { criticalPaths: CRITICAL_PATHS, trustThreshold: 2 }) {
  if (!pr.files?.length) return { action: 'auto-merge', reviewers: [], level: 3, files: [] };
  const fileLevels = pr.files.map(f => ({
    path: f.path, level: assignLevel(f, pr.testsPass ?? false),
  }));
  const minLevel = Math.min(...fileLevels.map(f => f.level));
  const reviewers = [];
  let action;
  if (minLevel === 0) {
    action = 'manual-review-required';
    if (pr.files.some(f => /auth|payment|crypto/.test(f.path)))
      reviewers.push('security-team');
    reviewers.push('tech-lead');
  } else if (minLevel === 1 && pr.testsPass) {
    action = 'merge-with-note';
    reviewers.push('owner');
  } else if (minLevel === 1) {
    action = 'manual-review-required';                   // testsPass=false → 降级
    reviewers.push('tech-lead');
  } else if (minLevel === 2) {
    action = 'sample-review';
    reviewers.push('owner');
  } else {
    action = 'auto-merge';
  }
  return { action, reviewers: [...new Set(reviewers)], level: minLevel, files: fileLevels };
}

// 自测
// 安全路径 → T0 → manual
let r = routeReview({ files: [{ path: 'auth/login.ts', linesChanged: 50, provenance: 'ai' }],
  testsPass: true });
console.log(r.action === 'manual-review-required');
console.log(r.reviewers.includes('security-team'));
console.log(r.level === 0);

// 测试通过 → T1 → merge-with-note
r = routeReview({ files: [{ path: 'src/utils.ts', linesChanged: 30, provenance: 'ai' }],
  testsPass: true });
console.log(r.action === 'merge-with-note' && r.level === 1);

// 测试未过 → T0
r = routeReview({ files: [{ path: 'src/utils.ts', linesChanged: 30, provenance: 'ai' }],
  testsPass: false });
console.log(r.action === 'manual-review-required');

// 全人写 → T3 → auto-merge
r = routeReview({ files: [{ path: 'src/a.ts', linesChanged: 10, provenance: 'human' }],
  testsPass: true });
console.log(r.action === 'auto-merge' && r.level === 3);

// 混合 provenance
r = routeReview({ files: [
  { path: 'src/a.ts', linesChanged: 10, provenance: 'ai' },
  { path: 'src/b.ts', linesChanged: 10, provenance: 'human' },
], testsPass: true });
console.log(r.level === 1);                              // min(AI=1, human=3) = 1
console.log(r.action === 'merge-with-note');
```

**评分点**：
- 分级路由完整：T0 manual → T1 merge-with-note → T2 sample → T3 auto（四级审查路由）
- testsPass=false 的降级（T1 → T0——测试是信任的基础）；混合 provenance 的 per-file 分级
- 边界（空 files/混合 provenance/security 路径的 reviewer 建议）；审批人建议的自动化
- 能说清「AI 代码审查的信任分级不是二元的——按风险路径、变更大小、测试覆盖动态分级」属于加分
