---
title: [AGT-005] temperature 和 top_p 分别控制什么？不同场景怎么选采样参数？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-005：temperature 和 top_p 分别控制什么？不同场景怎么选采样参数？
**答**：
- `temperature` 控制整体随机性：越低分布越尖、输出越确定；越高越发散，过高会语无伦次。
- `top_p`（核采样）控制候选词范围：只从累计概率前 p 的词里采样，与 temperature 二选一调整即可，同时大调容易互相干扰。
- `max_tokens` 限制回复长度，同时用于给上下文预留预算。
- 经验值：抽取/分类/结构化输出用 0，代码生成 0.2 左右，通用对话 0.7，创意写作 0.9 以上。

```typescript
// 按场景维护采样参数预设，调用处只声明场景不散落魔法数字
type SamplingParams = { temperature?: number; top_p?: number; max_tokens?: number };

const PRESETS: Record<string, SamplingParams> = {
  '结构化抽取与分类': { temperature: 0, max_tokens: 512 },
  '代码生成': { temperature: 0.2, top_p: 0.9, max_tokens: 2048 },
  '通用对话': { temperature: 0.7, max_tokens: 1024 },
  '创意写作': { temperature: 0.9, top_p: 0.95, max_tokens: 4096 },
};

function buildRequestBody(messages: ChatMessage[], scene: string): string {
  const params = PRESETS[scene];
  if (!params) throw new Error(`未知场景 ${scene}`);
  return JSON.stringify({ model: 'gpt-4o-mini', messages, ...params });
}
```
