---
title: [AIC-540] AI 交互日志到团队知识库
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-540：AI 交互日志到团队知识库

**答**:
- AI 交互日志的知识沉淀：1) **交互日志**（每次 AI 对话的记录——prompt/output/用户反馈（接受/修改/拒绝 RBL-516 接受率的原始数据）；2) **知识提取**：高价值交互的识别（多轮收敛的交互 = 问题解决的完整路径；高接受率的输出 = 有效的 prompt 模式）；3) **知识库的结构**：FAQ（常见问题 + AI 最佳回答 RBL-848）；prompt 模板库（经过验证的 prompt——新项目复用）；反模式库（AI 常犯的错误 + 修正方法——RBL-956 静默清单的 AI 版）；4) **沉淀的自动化**：FAQ 自动提取（RBL-848 答疑 → FAQ 的 AI 版——AI 交互的重复问题 → 自动生成 FAQ）。
- 沉淀的触发条件（Rule of three）：同一问题被 3 个不同开发者问过 → 自动提为 FAQ；同一 prompt 模式 3 次高接受率 → 提为推荐模板。
- 追问钩子：为什么「AI 交互日志的沉淀」比「人写文档」更完整？——人写文档 = 记忆偏差（只记录"印象深刻"的问题——常见但简单的问题被忽略）；AI 日志 = 完整记录（每次交互的 prompt/output/反馈——无遗漏）；「沉淀的完整性」：AI 日志是客观记录（不受记忆偏差影响）——高频问题的统计可以从日志中自动提取（不需要人"记住"哪些问题重要）；日志驱动的知识库 = 数据驱动的文档（RBL-851 收益追踪的 AI 版）。

```typescript
// AI 交互日志的知识提取
interface AIInteraction {
  prompt: string;
  output: string;
  action: 'accepted' | 'modified' | 'rejected';
  modifiedLines?: number;
  context: { language: string; fileType: string };
  userId: string;
}
function extractKnowledge(interactions: AIInteraction[]) {
  // 1) 高接受率 prompt 模式
  const promptPatterns = groupBy(interactions.filter(i => i.action === 'accepted'),
    i => normalizePrompt(i.prompt));
  const goodPatterns = Object.entries(promptPatterns)
    .filter(([_, items]) => items.length >= 3)           // Rule of three
    .map(([pattern, items]) => ({ pattern, usage: items.length }));
  // 2) 常见拒绝原因
  const rejected = interactions.filter(i => i.action === 'rejected');
  const rejectReasons = groupBy(rejected, i => classifyRejection(i));
  // 3) FAQ 候选
  const faqCandidates = goodPatterns.map(p => ({
    question: summarizePrompt(p.pattern),
    answer: bestOutput(promptPatterns[p.pattern]),
  }));
  return { goodPatterns, rejectReasons, faqCandidates };
}
```
