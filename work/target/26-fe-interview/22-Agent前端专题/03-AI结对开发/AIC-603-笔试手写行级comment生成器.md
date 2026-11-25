---
title: [AIC-603] 笔试：手写行级 comment 生成器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-603：笔试：手写行级 comment 生成器

**答**：实现 `generateComments(diff, issues)`。diff: `Array<{ file, line, content }>`（变更行）；issues: `Array<{ file, line, type, message, suggestion? }>`。规则：1) **位置匹配**：issue 的 file+line 必须在 diff 中存在（不存在 = 丢弃——AI 幻觉位置 RBL-507）；2) 排序：按 type 优先级（bug > security > suggestion > question > nitpick）→ 同类型按 line 升序；3) **suggestion 格式验证**：suggestion 存在且非空才包含；4) 返回 `{ comments: LineComment[], summary: { byType: Record<type, count>, total } }`。边界：issues 空（空 comments）；diff 空（全部丢弃——位置不在 diff 中）；同一行多个 issue（合并——保留最高优先级的）。

```javascript
const TYPE_ORDER = { bug: 0, security: 1, suggestion: 2, question: 3, nitpick: 4 };
function generateComments(diff = [], issues = []) {
  const diffKeys = new Set(diff.map(d => `${d.file}:${d.line}`));
  // 1) 位置匹配过滤
  const valid = issues.filter(i => diffKeys.has(`${i.file}:${i.line}`));
  // 2) 同行去重（保留最高优先级）
  const byLine = new Map();
  for (const i of valid) {
    const key = `${i.file}:${i.line}`;
    const existing = byLine.get(key);
    if (!existing || TYPE_ORDER[i.type] < TYPE_ORDER[existing.type])
      byLine.set(key, i);
  }
  // 3) 排序
  const comments = [...byLine.values()].sort((a, b) =>
    TYPE_ORDER[a.type] - TYPE_ORDER[b.type] || a.line - b.line);
  // 4) summary
  const byType = {};
  for (const c of comments) byType[c.type] = (byType[c.type] ?? 0) + 1;
  return { comments, summary: { byType, total: comments.length } };
}

// 自测
const diff = [
  { file: 'a.ts', line: 5, content: 'const x = fetch(url);' },
  { file: 'a.ts', line: 10, content: 'if (!user) return;' },
  { file: 'b.ts', line: 3, content: 'localStorage.setItem(key, val);' },
];
const issues = [
  { file: 'a.ts', line: 5, type: 'suggestion', message: 'Consider caching' },
  { file: 'a.ts', line: 5, type: 'bug', message: 'N+1 query' },           // 同行：bug 优先
  { file: 'a.ts', line: 99, type: 'bug', message: 'hallucinated line' },  // 不在 diff 中——丢弃
  { file: 'b.ts', line: 3, type: 'security', message: 'XSS risk' },
  { file: 'a.ts', line: 10, type: 'nitpick', message: 'naming' },
];
let r = generateComments(diff, issues);
console.log(r.comments.length === 3);                    // 4 valid - 1 同行去重 = 3
console.log(r.comments[0].type === 'bug');               // 排序第一
console.log(r.comments[0].line === 5);                   // bug 与 suggestion 同行取 bug
console.log(r.summary.byType.bug === 1);
console.log(r.summary.byType.security === 1);
console.log(r.summary.byType.nitpick === 1);
console.log(r.summary.total === 3);
// 空
console.log(generateComments([], issues).comments.length === 0);   // diff 空 → 全丢弃
console.log(generateComments(diff, []).comments.length === 0);
```

**评分点**：
- 位置匹配过滤（AI 幻觉位置丢弃——RBL-507 的 diff 级检测）；同行去重（保留最高优先级——bug > suggestion）
- 排序：类型优先级（bug > security > suggestion > question > nitpick）→ 同类型 line 升序
- 边界（空 issues/空 diff/同行多 issue）；summary 的 byType 统计
- 能说清「行级 comment 的位置匹配：AI 幻觉位置（不在 diff 中的行）必须丢弃——位置精确是行级 comment 可信的前提」属于加分
