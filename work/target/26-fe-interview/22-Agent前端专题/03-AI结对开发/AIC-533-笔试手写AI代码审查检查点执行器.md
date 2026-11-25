---
title: [AIC-533] 笔试：手写 AI 代码审查检查点执行器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-533：笔试：手写 AI 代码审查执行器

**答**：实现 `reviewAICode(code, { intent, securityPatterns, hasEdgeCaseTests })`。securityPatterns: RegExp[]。规则：1) **意图验证**（intent 关键词与 code 中的函数名/注释匹配 → intentMatch；2) **安全扫描**：securityPatterns 匹配 code → issues；3) **边界检测**：有 `if (!x)` 或 `?? ` 或 `?.` → 边界处理 ok；无 → warn 'missing-edge-cases'；4) **副作用检测**：有 `fetch(` 或 `localStorage.` 且不在函数内 → warn 'top-level-side-effect'；5) **分级结论**：intent 不匹配 → 'reject-rewrite'；安全问题 → 'reject-security'；边界缺失 → 'approve-fix-edge'；全过 → 'approve'。返回 `{ verdict, issues, priority }`。边界：intent 空（跳过意图检查）；securityPatterns 空（跳过安全检查）；code 空（reject-rewrite）。

```javascript
function reviewAICode(code = '', { intent = '', securityPatterns = [], hasEdgeCaseTests = false } = {}) {
  if (!code.trim()) return { verdict: 'reject-rewrite', issues: [{ type: 'empty' }], priority: 1 };
  const issues = [];
  // 1) 意图验证
  if (intent) {
    const keywords = intent.toLowerCase().split(/\s+/).filter(w => w.length > 3);
    const codeLower = code.toLowerCase();
    const matched = keywords.filter(k => codeLower.includes(k)).length;
    const intentMatch = matched >= Math.ceil(keywords.length * 0.3);  // 30% 关键词命中
    if (!intentMatch)
      return { verdict: 'reject-rewrite', issues: [{ type: 'intent-mismatch', priority: 1 }], priority: 1 };
  }
  // 2) 安全扫描
  for (const pattern of securityPatterns)
    if (pattern.test(code))
      return { verdict: 'reject-security', issues: [{ type: 'security', pattern: pattern.source, priority: 2 }], priority: 2 };
  // 3) 边界条件
  const hasEdgeHandling = /\?\?|\?\.|if\s*\(\s*!|===\s*(?:null|undefined)|\.length\s*===\s*0/.test(code);
  if (!hasEdgeHandling && !hasEdgeCaseTests)
    issues.push({ type: 'missing-edge-cases', severity: 'warn' });
  // 4) 副作用
  const topLevelSideEffect = /^\s*(?:fetch|localStorage|document)\./m.test(code);
  if (topLevelSideEffect)
    issues.push({ type: 'top-level-side-effect', severity: 'warn' });
  const hasWarnings = issues.length > 0;
  return {
    verdict: hasWarnings ? 'approve-fix-edge' : 'approve',
    issues, priority: 3,
  };
}

// 自测
const securityPatterns = [/eval\(/, /innerHTML\s*=/, /document\.write/];
// 意图匹配 + 安全 + 边界 → approve
let r = reviewAICode(
  `function validateUser(user) {
    if (!user) return null;
    if (!user.email?.includes('@')) return null;
    return user;
  }`,
  { intent: 'validate user input', securityPatterns, hasEdgeCaseTests: true });
console.log(r.verdict === 'approve');

// 意图不匹配 → reject-rewrite
r = reviewAICode(
  'function sortArray(arr) { return arr.sort(); }',
  { intent: 'validate user input', securityPatterns, hasEdgeCaseTests: false });
console.log(r.verdict === 'reject-rewrite');

// 安全问题 → reject-security
r = reviewAICode(
  'function process(input) { document.write(input); }',
  { intent: 'process data', securityPatterns, hasEdgeCaseTests: false });
console.log(r.verdict === 'reject-security');

// 边界缺失 → approve-fix-edge
r = reviewAICode(
  'function getName(user) { return user.name; }',       // 无边界检查
  { intent: 'get user name', securityPatterns, hasEdgeCaseTests: false });
console.log(r.verdict === 'approve-fix-edge');
console.log(r.issues.some(i => i.type === 'missing-edge-cases'));

// 空 code
console.log(reviewAICode('', { intent: 'test', securityPatterns: [] }).verdict === 'reject-rewrite');
```

**评分点**：
- 按优先级逐步深入（intent → security → edge → side effect——不匹配即停止 RBL-532）
- 边界检测启发式（??/?. / if(!x) 的存在性判断）；空 code reject-rewrite
- 边界（intent 空/空 patterns/空 code）；verdict 的四级行动
- 能说清「AI 代码审查按优先级逐步深入：意图不匹配立即停止（避免在错误方向上浪费时间审细节）」属于加分
