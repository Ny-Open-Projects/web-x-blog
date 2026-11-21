---
title: [AGT-224] KV 缓存与前缀缓存——长上下文推理的成本怎么优化？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-224：什么是 prompt caching——它为什么能大幅降低长上下文成本？

**答**:
- 原理：Transformer 推理时每 token 生成都要对全部前文做注意力计算，prefix caching（KV 缓存）把已计算的前缀 KV 缓存复用——命中前缀的部分按缓存价计费（通常 1/10 甚至更低）且 TTFT 显著下降。
- 工程条件：前缀必须完全一致才命中——所以 prompt 结构要"稳定前缀在前"：系统提示/工具定义/知识库大块放最前，每次变化的内容（用户消息）放最后；随机内容（时间戳/随机 ID）不能出现在前缀里。
- 应用场景：超长系统提示、固定知识库段落、多轮长对话（每轮历史是上一轮的前缀）、批量评测（相同 instruction 批量跑）——长上下文应用的标配优化。
- 注意事项：多供应商缓存行为不同（自动 vs 显式标记、TTL 不同），命中率要监控；缓存价与存储费要进成本模型，对短 prompt 收益有限不必强行改造。

```javascript
// 前缀缓存友好的 prompt 结构
const messages = [
  { role: 'system', content: SYSTEM_PROMPT +
      KNOWLEDGE_BLOCK },          // 稳定大块在前（可缓存）
  ...history,                     // 历史是前缀的自然延续
  { role: 'user', content: query } // 变化内容最后
];
// 禁止：前缀中插入 Date.now() / 随机 ID
// 监控：cached_tokens 占比 = 缓存命中率
```
