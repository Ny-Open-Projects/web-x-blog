---
title: [AGT-036] Agent 的短期记忆和长期记忆分别怎么实现？上下文过长如何做摘要压缩？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-036：Agent 的短期记忆和长期记忆分别怎么实现？上下文过长如何做摘要压缩？
**答**：
- 短期记忆 = 当前会话 messages（滑动窗口内原文）；长期记忆 = 跨会话持久化，通常存向量库按语义检索（RAG 式记忆）。
- 压缩策略：超过阈值时把远期对话交给模型生成摘要，替换原文，只保留最近 N 条原文。
- 摘要要保留关键事实、用户偏好与未完成任务，摘要本身作为一条 system 消息注入。
- 混合方案：近期原文 + 摘要 + 按当前问题从长期记忆检索相关片段，三者拼装上下文。

```typescript
// 滚动摘要压缩：远期对话并入摘要，近期保留原文
interface Memory {
  summary: string;
  recent: ChatMessage[];
}

const KEEP_RECENT = 10;
const TRIGGER_LEN = 30;

async function compactMemory(memory: Memory): Promise<Memory> {
  if (memory.recent.length < TRIGGER_LEN) return memory;

  const toCompress = memory.recent.slice(0, memory.recent.length - KEEP_RECENT);
  const summary = await llmComplete(
    `这是旧的对话摘要：\n${memory.summary || '（无）'}\n\n` +
    '请把下面的新对话并入摘要，保留关键事实、用户偏好与未完成事项，控制在 500 字内：\n' +
    toCompress.map((m) => `${m.role}: ${m.content}`).join('\n'),
  );

  return { summary, recent: memory.recent.slice(-KEEP_RECENT) };
}

// 上下文拼装：system + 摘要 + 近期原文
function buildContextMessages(memory: Memory): ChatMessage[] {
  const messages: ChatMessage[] = [{ role: 'system', content: '你是持久助手。' }];
  if (memory.summary) {
    messages.push({ role: 'system', content: `历史对话摘要：${memory.summary}` });
  }
  return messages.concat(memory.recent);
}
```

---

## 九、多 Agent 协作
