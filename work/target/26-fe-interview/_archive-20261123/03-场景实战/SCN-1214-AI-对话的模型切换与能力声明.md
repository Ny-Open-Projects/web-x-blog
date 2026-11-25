---
title: [SCN-1214] AI 对话的模型切换与能力声明
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1214：AI 对话的模型切换与能力声明

**答**：
- 切换：多模型选择器（模型能力标签：上下文长度/多模态/联网），切换保留上下文（转译）。
- 声明：模型幻觉风险提示（关键决策需人工核实）。
- 成本：不同模型计价差异展示（切换前提示成本变化）。

```javascript
// 模型切换
const MODELS = {
  'gpt-4o': { ctx: 128_000, multimodal: true, price: 10 },
  'glm-4': { ctx: 128_000, multimodal: false, price: 1 },
};
function switchModel(to, ctxLen) {
  const m = MODELS[to];
  return {
    ok: ctxLen <= m.ctx,
    note: !m.multimodal && hasImages(ctxLen) ? '该模型不支持图片，将丢失图片上下文' : null,
    priceChange: m.price / MODELS[current].price,
  };
}
function hasImages(ctx) { return ctx.includes('image'); }
```
