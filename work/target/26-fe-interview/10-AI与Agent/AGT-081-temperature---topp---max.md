---
title: [AGT-081] temperature / top_p / max_tokens / stop 等推理参数按场景如何调优？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-081：temperature / top_p / max_tokens / stop 等推理参数按场景如何调优？
**答**：
- temperature 控随机性：抽取/分类/SQL 用 0-0.2（要稳定可复现）；对话 0.7 左右；创意文案 0.9-1.0。
- top_p 与 temperature 二选一调，不要同时大改；stop 序列约束输出边界（如遇到代码围栏停止）。
- max_tokens 必须显式设置：防失控输出烧钱，也防截断破坏 JSON 完整性。
- 参数按场景固化成模板并版本管理，与 prompt 一起过回归评测；线上异常输出先查参数再查模型。

```typescript
import { z } from 'zod';

// 场景化参数模板
type Scenario = 'extract' | 'sql' | 'chat' | 'creative' | 'code';

const PARAM_MATRIX: Record<Scenario, { temperature: number; top_p: number; max_tokens: number; stop?: string[] }> = {
  extract:  { temperature: 0,   top_p: 1,    max_tokens: 1024 },                  // 抽取要可复现
  sql:      { temperature: 0,   top_p: 1,    max_tokens: 512,  stop: [';'] },     // SQL 要确定
  chat:     { temperature: 0.7, top_p: 0.9,  max_tokens: 2048 },                  // 对话要自然
  creative: { temperature: 1.0, top_p: 0.95, max_tokens: 2048 },                  // 创意要发散
  code:     { temperature: 0.2, top_p: 1,    max_tokens: 4096, stop: ['```'] },   // 代码要克制
};

export function buildRequest(scenario: Scenario, messages: ChatMessage[]) {
  return {
    model: scenario === 'sql' || scenario === 'extract' ? 'gpt-4o-mini' : 'gpt-4o',
    messages,
    ...PARAM_MATRIX[scenario],
    response_format: scenario === 'extract' ? { type: 'json_object' } : undefined,
  };
}
```
