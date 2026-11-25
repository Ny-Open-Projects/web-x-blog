---
title: [AIC-586] 多轮对话的上下文衰减与强化
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-586：多轮对话的上下文衰减

**答**:
- 多轮对话中的上下文衰减：1) **注意力稀释**（对话轮次增加 → 早期 prompt 的注意力权重递减（LLM 的 attention 窗口限制——最近的对话权重高、最早的低 RBL-538 漂移原因）；2) **需求遗忘**（第 1 轮的需求在第 10 轮被"遗忘"——AI 生成的代码不再满足第 1 轮的需求；3) **矛盾累积**（多轮中 AI 的输出可能自相矛盾（第 3 轮说用 Redux、第 8 轮说用 Zustand——上下文衰减导致一致性丢失）。
- 强化策略：1) **需求重述**（每 N 轮重复关键需求——"记住：我们需要 cursor-based 分页"——强化注意力；2) **系统 prompt 固定**（需求写在 system prompt 而非对话中——system prompt 的注意力权重恒定 RBL-510 rules 的对话版）；3) **上下文摘要**（每 N 轮总结已完成的/待完成的——压缩历史（避免注意力稀释 RBL-502 裁剪的对话版）。
- 追问钩子：为什么「系统 prompt 固定需求」比「对话中重述需求」更可靠？——对话中的重述 = 需求仍在对话流中（后续轮次可能再次稀释——重复只是暂时强化）；system prompt = 需求在固定位置（每个请求都携带——不随对话轮次衰减）；「位置的确定性」：system prompt 的位置固定且每个请求都有——对话中的内容位置可变且可能被截断（长对话的 context window 裁剪——最早的先被裁掉 RBL-502）；system prompt = "不会被裁剪的上下文"。

```typescript
// 多轮对话的上下文管理
function manageConversationContext(history: { role: string; content: string }[],
  requirements: string[], { restateEvery = 5 } = {}) {
  const turns = history.length;
  // 1) 检测衰减风险
  const needsRestate = turns > 0 && turns % restateEvery === 0;
  // 2) 构建 system prompt（需求固定）
  const systemPrompt = `You are a coding assistant. Requirements:\n${requirements.map(r => `- ${r}`).join('\n')}`;
  // 3) 对话历史压缩（每 10 轮摘要）
  if (turns > 10) {
    const summary = summarizeHistory(history.slice(0, turns - 5));
    return { systemPrompt, history: [summary, ...history.slice(-5)], needsRestate };
  }
  return { systemPrompt, history, needsRestate };
}
function summarizeHistory(history) {
  return { role: 'system', content: `[Previous conversation summarized: ${history.length} turns completed]` };
}
```
