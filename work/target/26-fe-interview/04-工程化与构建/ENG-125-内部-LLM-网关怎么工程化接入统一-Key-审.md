---
title: [ENG-125] 内部 LLM 网关怎么工程化接入？统一 Key、审计与成本分摊怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-125：内部 LLM 网关怎么工程化接入？统一 Key、审计与成本分摊怎么做？
**答**：
- 统一入口：应用不直连各家模型 API，全部走内部网关，上游可换模型、可做限流与故障切换。
- 鉴权与分摊：网关按团队/场景发放 token，请求带 X-Team、X-Scenario 标头，用量按标头归集出成本报表。
- 审计合规：记录调用方、模型、token 用量与脱敏后的请求摘要；涉密场景走内网私有化部署通道。
- 工程配套：超时与重试统一封装、按场景设 max_tokens 预算，防止失控调用烧穿预算。

```typescript
// 前端基建统一封装：所有 AI 调用走内部网关
export async function gatewayChat(req: {
  scenario: string;
  messages: { role: string; content: string }[];
}) {
  const res = await fetch('https://llm-gw.internal/v1/chat', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.LLM_GW_TOKEN}`, // 网关统一发放，按团队计费
      'X-Team': 'frontend',
      'X-Scenario': req.scenario,                          // 场景标签用于成本分摊
    },
    body: JSON.stringify({
      model: 'glm-4.7',
      messages: req.messages,
      max_tokens: 2048,
      timeout_ms: 15000,
    }),
  });
  if (!res.ok) throw new Error(`llm-gw ${res.status}`);
  await audit(req, { via: 'gateway' }); // 审计留痕
  return res.json();
}
```
