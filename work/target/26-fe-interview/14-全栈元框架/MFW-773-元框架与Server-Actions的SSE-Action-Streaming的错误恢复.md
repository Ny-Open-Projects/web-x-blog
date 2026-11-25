---
title: [MFW-773] Action Streaming 的错误恢复
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-773：Action Streaming 错误恢复

**答**:
- Action 流式错误的恢复（RBL-698 的策略化）：1) **自动重试**（幂等生成（LLM 的 prompt 重发——非幂等（不同结果——但「新生成」可接受——LLM 生成不需要幂等（内容不重复即可）；2) **部分内容恢复**（保留已生成的 token + 续传（prompt 包含已有内容——「继续生成」——LLM 的续写能力）；3) **错误分类**：超时（LLM 响应慢——重试带更长 timeout）；内容审核拒绝（不可重试——修改 prompt）；速率限制（等待后重试——退避）。
- 续传的实现：prompt = 原始 prompt + 已生成内容（「继续写」指令——LLM 的 continuation 能力）；「续传 vs 重做」的权衡：续传 = 节省 tokens（已生成部分不重复）但连贯性风险（上下文切换——LLM 可能不一致）；重做 = 一致性（从头生成——token 成本）。
- 追问钩子：为什么「LLM 流式的续传」比「重做」更节省但不一定更好？——续传：已生成 500 token 不浪费（成本节省）；但 LLM 的续传可能「上下文断裂」（prompt 中包含部分生成内容——LLM 可能重复或不连贯）；重做：一致性好（完整上下文）但 token 成本×2；「成本 vs 质量」的权衡：续传适合「内容容忍度高」的场景（聊天——重复无妨）；重做适合「一致性要求高」的场景（代码生成——不一致 = 编译错）——内容类型决定恢复策略。

```typescript
// Action 流式的续传
'use server';
export async function* chatWithRecovery(message: string, partial?: string): AsyncGenerator<string> {
  const prompt = partial
    ? `${message}\n\n[已生成部分，请继续]: ${partial}`      // 续传 prompt
    : message;
  const stream = await llm.create({ prompt, stream: true });
  for await (const token of stream) yield token;
}
// client 侧恢复
async function handleStreamError(receivedTokens: string[], originalMessage: string) {
  if (receivedTokens.length > 50) {
    // 续传：已有内容够多 → 续写
    const partial = receivedTokens.join('');
    return chatWithRecovery(originalMessage, partial);   // 续传 generator
  }
  // 重做：内容太少 → 从头
  return chatWithRecovery(originalMessage);
}
```
