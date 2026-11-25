---
title: [AGT-119] 多语言 Agent 的本地化架构与离线弱网降级怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-119：多语言 Agent 的本地化架构与离线弱网降级怎么设计？
**答**：
- 本地化三层：提示层（AGT-051 locale 模板与术语表）、数据层（知识库按语言分索引，检索带语言过滤）、体验层（UI 文案 ICU 格式化、输出日期货币 locale 化）。
- 跨语言检索：用户中文提问、知识库英文文档时，用多语言 embedding 模型或「翻译成文档语言再检索」双路召回合并。
- 弱网降级分级：弱网切小模型 + 限制输出长度（快出短答）；离线走本地缓存 FAQ、浏览器端小模型、纯规则兜底。
- 降级必须显式告知用户（「当前离线，回答来自缓存」），恢复联网后可一键重试。

```typescript
import { z } from 'zod';

// 弱网与离线分级降级
type NetState = 'online' | 'slow' | 'offline';

function detectNet(): NetState {
  if (!navigator.onLine) return 'offline';
  const conn = (navigator as any).connection;
  return conn?.effectiveType && /2g/.test(conn.effectiveType) ? 'slow' : 'online';
}

export async function chatWithDegradation(messages: ChatMessage[]) {
  switch (detectNet()) {
    case 'offline': {
      const faq = await cachedFaqLookup(messages.at(-1)!.content); // 本地 FAQ 缓存命中
      return { text: faq ?? '当前离线，仅可查询缓存的常见问题', degraded: true };
    }
    case 'slow':
      // 弱网：小模型 + 截断历史，快出短答
      return { text: await chatOnce(messages.slice(-4), 'gpt-4o-mini'), degraded: true, note: '弱网模式，已简化回答' };
    default:
      return { text: await chatOnce(messages), degraded: false };
  }
}

// 跨语言检索：双路召回
export async function multilingualRetrieve(query: string, uiLocale: string) {
  const [sameLang, translated] = await Promise.all([
    vectorStore.search(await embed(query), 5, { filter: { lang: uiLocale } }),
    translate(query, 'en').then((q) => vectorStore.search(await embed(q), 5, { filter: { lang: 'en' } })), // 英文知识库通道
  ]);
  return [...sameLang, ...translated];
}
```
