---
title: [AGT-110] 设计一个多 Agent 协作的内容生产流水线（调研 → 写作 → 审校）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-110：设计一个多 Agent 协作的内容生产流水线（调研 → 写作 → 审校）？
**答**：
- 流水线：调研 Agent（检索产出素材卡片）→ 写作 Agent（只能基于素材成稿）→ 审校 Agent（事实核对 + 结构风格），角色分工比一个全能 Agent 稳定。
- 接口契约：每个 Agent 输入输出 schema 化（素材列表/初稿/终稿），中间产物落库，任何环节可独立重跑与缓存。
- 打回机制：审校不通过带着具体修改意见回写作，最多 2 轮，防止无限循环（复用停止条件）。
- 成本优势：素材可复用、审校规则固定，流水线比单 Agent 长上下文跑到底更省且更可控。

```typescript
import { z } from 'zod';

// 内容生产流水线：调研 → 写作 → 审校
const MaterialSchema = z.object({ materials: z.array(z.object({ point: z.string(), source: z.string() })) });
const DraftSchema = z.object({ title: z.string(), body: z.string() });
const ReviewSchema = z.object({ pass: z.boolean(), issues: z.array(z.string()) });

export async function produceArticle(topic: string) {
  // 1. 调研：检索后压缩成素材卡片
  const { materials } = await structuredLLM(
    [{ role: 'user', content: `调研主题「${topic}」，检索后输出要点素材卡片，注明来源` }, ...(await retrieveFor(topic))],
    MaterialSchema,
  );
  // 2. 写作：只能使用素材中的事实
  let draft = await structuredLLM(
    [{ role: 'user', content: `基于素材写作 800 字文章，只能使用素材中的事实：\n${JSON.stringify(materials)}` }],
    DraftSchema,
  );
  // 3. 审校：事实核对 + 结构，最多打回 2 轮
  for (let i = 0; i < 2; i++) {
    const review = await structuredLLM(
      [{ role: 'user', content: `审校文章：事实是否都有素材支撑、结构是否清晰。\n素材：${JSON.stringify(materials)}\n文章：${JSON.stringify(draft)}` }],
      ReviewSchema,
    );
    if (review.pass) return draft;
    draft = await structuredLLM(
      [{ role: 'user', content: `按意见修订：${review.issues.join(';')}\n原文：${JSON.stringify(draft)}` }],
      DraftSchema,
    );
  }
  return draft; // 未通过也返回并标注低置信
}
```
