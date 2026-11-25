---
title: [AGT-004] 上下文窗口有限，token 超限怎么办？前端如何做截断策略？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-004：上下文窗口有限，token 超限怎么办？前端如何做截断策略？
**答**：
- 先估算 token：精确方案用 `js-tiktoken`/`tiktoken`，快速方案中文约 1 字符 1 token、英文约 4 字符 1 token。
- 常见策略：保留 system + 最近 N 条消息的滑动窗口；被裁掉的远期对话压缩成一条摘要挂回去（见 AGT-036）。
- 预算要给回复留空间：`可用上下文 = 窗口上限 - 预留 max_tokens`。
- 超限报错（部分服务返回 400 `context_length_exceeded`）要做兜底，不能直接把异常抛给用户。

```typescript
// 粗估 token：中文 1 字符约 1 token，其余约 4 字符 1 token
function estimateTokens(text: string): number {
  const cjk = (text.match(/[\u4e00-\u9fa5]/g) ?? []).length;
  const rest = text.length - cjk;
  return Math.ceil(cjk + rest / 4);
}

const MAX_CONTEXT_TOKENS = 8000;
const RESERVE_FOR_REPLY = 1500;

// 滑动窗口截断：永远保留 system，从最新消息往前装，装不下就停
function truncate(messages: ChatMessage[]): ChatMessage[] {
  const [system, ...rest] = messages;
  const kept: ChatMessage[] = [];
  let used = estimateTokens(system.content) + RESERVE_FOR_REPLY;

  for (let i = rest.length - 1; i >= 0; i--) {
    const cost = estimateTokens(rest[i].content);
    if (used + cost > MAX_CONTEXT_TOKENS) break;
    used += cost;
    kept.unshift(rest[i]);
  }
  return [system, ...kept];
}

// 发送前统一过一遍截断
const safeMessages = truncate(conv.history());
```
