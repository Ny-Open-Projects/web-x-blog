---
title: [AIC-602] 行级 comment 的 AI 生成
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-602：行级 comment 的 AI 生成

**答**:
- PR 行级 comment 的 AI 自动生成：1) **精确位置标注**（AI 审查不是"整体通过/不通过"——而是在 diff 的具体行上添加 comment（"第 42 行：这里可能存在 N+1 查询"——位置精确的反馈 RBL-532 检查点的 diff 级实现）；2) **comment 的类型**：bug（逻辑错误——error 级）、suggestion（改进建议——info 级）、question（需要开发者确认——question 级）、nitpick（风格建议——nit 级）；3) **comment 的优先级排序**：bug > security > suggestion > nitpick——审查者按优先级处理。
- 行级 comment 的生成流程：1) AI 读取 diff（变更行及其上下文——不只看变更行还要看周围代码 RBL-502 上下文裁剪的 diff 版）；2) 逐行分析（每个变更行 → 检查是否有问题 → 有则在对应行生成 comment）；3) comment 的结构化输出（`{ file, line, type, message, suggestion? }`——GitHub PR comment 的格式）。
- 追问钩子：为什么「行级 comment」比「总结式 review」更有用？——总结式（"这个 PR 有 N+1 问题和安全问题"——审查者需要自己找到具体位置）；行级（在第 42 行直接标注 N+1——审查者直接看到位置和上下文）；「行级的定位精度」= 审查效率的关键：reviewer 不需要搜索问题位置——AI 已经标好了——审 AI 的 comment 而非审代码（效率提升 = 位置精确 × 上下文完整）。

```typescript
// 行级 comment 的生成
interface LineComment {
  file: string;
  line: number;
  type: 'bug' | 'security' | 'suggestion' | 'question' | 'nitpick';
  message: string;
  suggestion?: string;   // 建议的修复代码
}
async function generateLineComments(diff: string, context: string): Promise<LineComment[]> {
  const prompt = `Review this diff. For each issue, output a JSON comment:
  { "file", "line", "type": "bug|security|suggestion|question|nitpick", "message", "suggestion?" }
  
  Context: ${context}
  Diff: ${diff}`;
  const response = await llm.generate(prompt);
  return JSON.parse(response);                          // 结构化 comment
}
// GitHub PR comment 格式
function toGitHubComment(comment: LineComment) {
  const icons = { bug: '🐛', security: '🔒', suggestion: '💡', question: '❓', nitpick: '🎨' };
  return `${icons[comment.type]} **${comment.type.toUpperCase()}**: ${comment.message}` +
    (comment.suggestion ? `\n\nSuggestion:\n\`\`\`suggestion\n${comment.suggestion}\n\`\`\`` : '');
}
```
