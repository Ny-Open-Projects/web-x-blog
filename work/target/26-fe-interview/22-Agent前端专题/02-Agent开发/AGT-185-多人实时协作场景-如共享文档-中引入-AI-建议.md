---
title: [AGT-185] 多人实时协作场景（如共享文档）中引入 AI 建议时，冲突怎么处理？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-185：多人实时协作场景（如共享文档）中引入 AI 建议时，冲突怎么处理？
**答**：
- 冲突三源：AI 建议与用户新编辑的文本冲突（建议基于的锚点已变）、AI 自动写入与另一用户的并发写入冲突、两个 AI 建议互相冲突。
- 核心原则：AI 建议永远以「建议层」存在（CRDT/OT 之上的独立 overlay），不直接进入文档操作流；采纳时才作为一次普通用户操作参与协同算法，享受同样的冲突解决规则。
- 锚点失效检测：建议基于的文本片段被编辑后（内容哈希或 range 校验失败），建议自动标记 stale 并折叠，绝不盲目应用到新文本上。
- 体验设计：建议只对发起人可见还是全员可见是产品决策——工程上建议对象要带 author=ai 与 targetUser，权限系统按普通协作者对待 AI（AI 是一个有权限边界的「虚拟用户」）。

```typescript
// 协作文档中的 AI 建议 overlay：锚点校验 + 采纳即普通操作
interface Suggestion {
  id: string; author: 'ai';
  anchor: { start: number; end: number; contentHash: string }; // 建议基于的原文片段
  replacement: string;
  targetUser: string;                                          // 建议展示给谁
  status: 'active' | 'stale' | 'applied' | 'dismissed';
}

function hash(s: string): string { let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) | 0; return String(h); }

export function validateAnchor(s: Suggestion, docText: string): Suggestion {
  const current = docText.slice(s.anchor.start, s.anchor.end);
  return hash(current) === s.anchor.contentHash ? s : { ...s, status: 'stale' }; // 锚点已变：标记失效，不应用
}

export function applySuggestion(s: Suggestion, docText: string, userId: string): string {
  if (s.status !== 'active') throw new Error('建议已失效或已被处理');
  const v = validateAnchor(s, docText);
  if (v.status === 'stale') throw new Error('锚点失效，请基于最新文本重新生成建议');
  // 关键：采纳 = 以「用户 userId」身份提交一次编辑操作，进入与人工编辑相同的 OT/CRDT 流程
  collabServer.submitOp({ userId, type: 'replace', range: s.anchor, text: s.replacement, meta: { fromSuggestion: s.id } });
  return docText.slice(0, s.anchor.start) + s.replacement + docText.slice(s.anchor.end);
}

// 两个 AI 建议重叠时：只保留最早的一条，其余标记冲突折叠
export function dedupOverlapping(suggestions: Suggestion[]): Suggestion[] {
  const sorted = suggestions.filter((s) => s.status === 'active').sort((a, b) => a.anchor.start - b.anchor.start);
  const keep: Suggestion[] = [];
  let lastEnd = -1;
  for (const s of sorted) {
    if (s.anchor.start < lastEnd) { s.status = 'stale'; continue; }  // 与前一条重叠
    keep.push(s); lastEnd = s.anchor.end;
  }
  return keep;
}
const collabServer = { submitOp: (x: unknown) => { void x; } };
```
