---
title: [AGT-070] Human-in-the-loop 如何实现（Agent 中断询问用户并恢复执行）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-070：Human-in-the-loop 如何实现（Agent 中断询问用户并恢复执行）？
**答**：
- 需要人工的时机：高危工具执行前、关键方案选择时、Agent 置信度低或连续失败时。
- 实现要点：Agent 暂停 ≠ 进程结束——状态持久化（复用 AGT-065 断点续跑），把「问题 + 选项 + 上下文」推给用户，异步等待回复。
- 交互载体：聊天里嵌确认卡片（批准/拒绝/修改参数）或结构化表单；超时策略要明确（超时视为拒绝并选择更安全路径）。
- 恢复：用户回复后从持久化状态唤醒任务，把回答作为观察结果注入上下文继续。

```typescript
import { z } from 'zod';

// 中断询问：暂停持久化 + 异步等待用户答复
interface AskPayload { question: string; options: string[] }

async function askHuman(sessionId: string, payload: AskPayload, timeoutMs = 5 * 60_000): Promise<string> {
  await pushConfirmCard(sessionId, payload);          // 前端渲染卡片：选项按钮 + 自由输入
  const answer = await waitForMessage(`human-reply:${sessionId}`, timeoutMs) // 订阅消息队列/长轮询
    .catch(() => 'TIMEOUT');
  if (answer === 'TIMEOUT') {
    await pushMessage(sessionId, '等待超时，本次操作已取消');
    return '用户未在时限内回复，视为拒绝，请选择更安全的方案';
  }
  return `用户的答复：${answer}`;                     // 作为观察结果注入 Agent 上下文
}

// Agent 可主动申请人工介入：注册成工具
const askUserTool = defineTool({
  name: 'ask_user',
  description: '当信息不足或操作有风险时，向用户提问并等待答复',
  schema: z.object({ question: z.string(), options: z.array(z.string()).optional() }),
  run: ({ question, options }) => askHuman(currentSessionId, { question, options: options ?? [] }),
});
// 等待期间任务状态保持持久化，用户回复唤醒后从断点继续（复用 AGT-065）
```

---

## 十六、RAG 进阶
