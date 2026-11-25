---
title: [AIC-515] 笔试：手写 AI 注释质量评分器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-515：笔试：手写 AI 注释质量评分

**答**：实现 `scoreComments(code)`。规则：1) 提取注释（`//` 和 `/** */`）；2) 评分维度（每注释 0~10 分）：**意图性**（含动词"validate/parse/fetch/ensure" → +3；**约束性**（含"IMPORTANT/DO NOT/NEVER/MUST" → +2；**精确性**（含类型/参数名/变量名 → +2；**长度**（10~100 chars → +1；太短 <5 → -2；太长 >200 → -1）；3) 总分 = 所有注释平均分 + AI 友好度（含 `@ai-` 标记 → +2 bonus）；4) 返回 `{ comments: Array<{ text, score, reasons }>, average, aiFriendly }`。边界：无注释（average 0）；全无用注释（average < 3 → 建议"添加意图注释"）。

```javascript
function scoreComments(code = '') {
  const comments = [];
  const lines = code.split('\n');
  lines.forEach((line, i) => {
    const trimmed = line.trim();
    let comment = null;
    if (trimmed.startsWith('//')) comment = trimmed.slice(2).trim();
    else if (trimmed.startsWith('*') && !trimmed.startsWith('/**')) comment = trimmed.slice(1).trim();
    if (!comment || comment.length < 3) return;
    let score = 0; const reasons = [];
    if (/\b(validate|parse|fetch|ensure|check|handle|create|update|delete)\b/i.test(comment)) {
      score += 3; reasons.push('intent');
    }
    if (/\b(IMPORTANT|DO NOT|NEVER|MUST|WARNING)\b/i.test(comment)) {
      score += 2; reasons.push('constraint');
    }
    if (/\w+\.\w+|@\w+|<\w+>|\(\)/.test(comment)) {
      score += 2; reasons.push('precise');
    }
    if (comment.length >= 10 && comment.length <= 100) { score += 1; reasons.push('concise'); }
    else if (comment.length < 5) { score -= 2; reasons.push('too-short'); }
    else if (comment.length > 200) { score -= 1; reasons.push('too-long'); }
    comments.push({ text: comment, line: i + 1, score: Math.max(0, Math.min(10, score)), reasons });
  });
  const average = comments.length
    ? +(comments.reduce((s, c) => s + c.score, 0) / comments.length).toFixed(1) : 0;
  const aiFriendly = /@ai-(skip|rule|note)/.test(code);
  if (aiFriendly) { /* bonus applied to average */ }
  return { comments, average: aiFriendly ? Math.min(10, average + 2) : average, aiFriendly };
}

// 自测
const goodCode = [
  '// Validate request body against schema and return 422 on failure',
  'function validate(body: unknown) {}',
  '// IMPORTANT: Do NOT use useState here - server component',
  'export default async function Page() {}',
  '// @ai-skip',
  'const config = { key: "value" };',
].join('\n');
let r = scoreComments(goodCode);
console.log(r.average >= 5);                         // 好注释：intent + constraint
console.log(r.aiFriendly === true);                  // @ai-skip
console.log(r.comments[0].reasons.includes('intent'));

// 无用注释
const badCode = '// This function does stuff\nfunction foo() {}';
r = scoreComments(badCode);
console.log(r.average < 3);                          // 无动词/约束/精确

// 空代码
console.log(scoreComments('const x = 1;').average === 0);
console.log(scoreComments('').comments.length === 0);
```

**评分点**：
- 多维评分（intent +3/constraint +2/precise +2/长度调整——AI 友好度的量化）；@ai- 标记 bonus
- 评分范围 clamp（0~10）；无用注释的低分检测（建议添加意图注释）
- 边界（无注释/全无用/@ai- 标记）；注释即 Prompt 的工程量化
- 能说清「注释的质量影响 AI 补全的质量——精确的意图注释是零成本 Prompt 工程」属于加分
