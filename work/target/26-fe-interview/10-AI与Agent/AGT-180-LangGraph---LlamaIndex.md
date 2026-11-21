---
title: [AGT-180] LangGraph / LlamaIndex / Vercel AI SDK / CrewAI 各自定位是什么？如何选型？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-180：LangGraph / LlamaIndex / Vercel AI SDK / CrewAI 各自定位是什么？如何选型？
**答**：
- 四个定位一句话：LangGraph 是「有状态的 Agent 编排图」（循环/分支/HITL/checkpoint 是一等公民）；LlamaIndex 是「数据接入与检索框架」（RAG 管线/连接器生态最深）；Vercel AI SDK 是「前端优先的 LLM 工具库」（useChat/hooks/流式 UI 绑定 React 生态最好）；CrewAI 是「角色化多 Agent 协作 DSL」（用角色/目标/任务描述团队，上手最快）。
- 选型按「你缺什么」：缺检索与数据管线 → LlamaIndex；缺复杂状态机与可控编排 → LangGraph；缺前端流式交互层 → Vercel AI SDK；缺多角色协作的快速原型 → CrewAI。
- 前端工程师的典型组合：Vercel AI SDK（UI 层）+ 后端 LangGraph 或自研 Runtime（编排层）+ 向量库直连（数据层）——层与层通过 HTTP/SSE 解耦，可独立替换。
- 框架的隐藏成本：抽象泄漏（复杂调试时必须穿透框架看原始请求）、版本动荡、锁定于框架的数据结构——核心生产链路保持「薄依赖」是稳妥策略。

```typescript
// 分层选型示例：Vercel AI SDK 前端 + 自编排后端，通过协议解耦
// 前端（React + Vercel AI SDK）：
//   const { messages, input, handleSubmit, stop } = useChat({ api: '/api/agent' });
//   —— 流式 UI、消息状态、中断都由 SDK 管，前端不写 SSE 解析
//
// 后端只承诺一个协议：输入 messages，输出 AI SDK 兼容的流（data stream protocol）
import { streamText, tool } from 'ai';
import { z } from 'zod';

export async function agentEndpoint(messages: { role: string; content: string }[]) {
  const result = streamText({
    model: gateway.model('gpt-4o-mini'),                     // 经 AGT-178 抽象层取模型，可替换
    messages,
    tools: {
      searchDocs: tool({
        description: '搜索内部知识库',
        parameters: z.object({ query: z.string() }),
        execute: async ({ query }) => retriever.search(query), // 检索层自持，可换 LlamaIndex 管线
      }),
      createTicket: tool({
        description: '创建工单',
        parameters: z.object({ title: z.string() }),
        execute: async ({ title }) => `ticket-${title}`,
      }),
    },
    maxSteps: 5,                                             // 编排层自控步数（循环/熔断自研或 LangGraph）
  });
  return result.toDataStreamResponse();                      // AI SDK 流协议：前端 useChat 直接消费
}
const gateway = { model: (id: string) => ({ id }) };
const retriever = { search: async (q: string) => ({ hits: [q] }) };
```
