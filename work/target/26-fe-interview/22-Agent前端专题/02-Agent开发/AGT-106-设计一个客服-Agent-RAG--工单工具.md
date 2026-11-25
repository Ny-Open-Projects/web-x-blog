---
title: [AGT-106] 设计一个客服 Agent（RAG + 工单工具 + 人工转接）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-106：设计一个客服 Agent（RAG + 工单工具 + 人工转接）？
**答**：
- 三能力组合：RAG 检索知识库回答、工具办业务（查订单/创建工单）、人工转接（低置信/用户情绪/主动要求）。
- 转接要显式可解释：告知用户工单号与预计响应时间，并把完整对话摘要传给坐席，避免用户重复描述。
- 业务工具必须幂等与确认：创建工单前把参数给用户过目（复用 AGT-055 确认流）。
- 护栏：知识库没有就明确说不知道并转人工，绝不编造政策；多轮工具调用不收敛就走兜底转接。

```typescript
import { z } from 'zod';

// 客服 Agent：RAG + 工具 + 转接
const CUSTOMER_TOOLS = [
  defineTool({ name: 'search_kb', description: '检索客服知识库', schema: z.object({ q: z.string() }),
    run: ({ q }) => hybridSearch(q) }),
  defineTool({ name: 'get_order', description: '查询当前用户订单', schema: z.object({ orderId: z.string() }),
    run: getOrderByUser }),
  defineTool({ name: 'escalate', description: '无法解决时转人工', schema: z.object({ reason: z.string() }),
    run: async ({ reason }) => {
      const summary = await chatOnce([{ role: 'user', content: `把客服对话压缩成坐席可用的摘要：\n${transcript}` }]);
      const ticket = await createTicket({ title: `转人工-${reason}`, detail: summary });
      return `已转人工，工单号 ${ticket.id}，请告知用户预计响应时间`;
    } }),
];

export async function customerServiceTurn(sessionId: string, userMsg: string) {
  const messages = await loadHistory(sessionId, CUSTOMER_SYSTEM);
  messages.push({ role: 'user', content: userMsg });
  for (let step = 0; step < 6; step++) {                    // 步数上限防失控
    const { tool_calls, content } = await callWithTools(messages, CUSTOMER_TOOLS);
    if (!tool_calls?.length) return content;                // 最终回答
    messages.push(...await runParallelToolCalls(tool_calls, toolRegistry(CUSTOMER_TOOLS)));
  }
  return runTool('escalate', { reason: '多轮工具调用仍未解决' }); // 兜底转人工
}
```
