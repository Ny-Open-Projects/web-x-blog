---
title: [AGT-125] A2A（Agent-to-Agent）协议与 MCP 的定位差异是什么？什么时候需要 A2A？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-125：A2A（Agent-to-Agent）协议与 MCP 的定位差异是什么？什么时候需要 A2A？
**答**：
- MCP 连接「Agent 与工具/数据」，解决能力供给；A2A 连接「Agent 与 Agent」，解决任务委托——一个是插 USB，一个是发工单。
- A2A 的核心抽象是 Agent Card（能力名片：名字/技能/端点/鉴权）+ Task（带生命周期的任务对象：submitted→working→completed/failed，支持流式状态上报与工件产出）。
- 需要A2A 的信号：对方是独立的、有自己 prompt/记忆/权限的完整 Agent，而不是一个无状态的函数；且跨组织边界（不同团队/公司运维）。
- 不需要 A2A 的信号：同进程内的多 Agent 协作（直接函数调用/事件总线更简单）、只是想让 Agent 用一个外部 API（那是 MCP 或普通工具的事）。

```typescript
// A2A 风格的 Agent Card 与任务委托客户端（概念实现）
interface AgentCard {
  name: string;
  description: string;
  url: string;               // 对方 Agent 的 A2A 端点
  skills: { id: string; description: string }[];
  authentication: { schemes: string[] };
}

interface A2aTask {
  id: string;
  status: 'submitted' | 'working' | 'completed' | 'failed';
  message?: { role: 'agent'; parts: { type: 'text'; text: string }[] };
  artifacts?: { name: string; parts: { type: 'text'; text: string }[] }[];
}

async function discoverAgent(cardUrl: string): Promise<AgentCard> {
  const res = await fetch(cardUrl, { headers: { Accept: 'application/json' } });
  if (!res.ok) throw new Error(`Agent Card 获取失败：${res.status}`);
  return res.json(); // 类似 .well-known/agent.json 的能力发现
}

async function delegateTask(agent: AgentCard, goal: string, onStatus?: (t: A2aTask) => void) {
  const taskId = crypto.randomUUID();
  const res = await fetch(agent.url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Authorization: 'Bearer <service-token>' },
    body: JSON.stringify({ jsonrpc: '2.0', id: taskId, method: 'tasks/send',
      params: { id: taskId, message: { role: 'user', parts: [{ type: 'text', text: goal }] } } }),
  });
  // 轮询或 SSE 订阅任务状态；对方作为黑盒 Agent 自己决定用哪些工具完成
  let task: A2aTask = (await res.json()).result;
  while (task.status === 'working') {
    await new Promise((r) => setTimeout(r, 2000));
    task = (await fetch(`${agent.url}/tasks/${taskId}`).then((r) => r.json())) as A2aTask;
    onStatus?.(task);
  }
  if (task.status !== 'completed') throw new Error(`委托任务失败：${taskId}`);
  return task.artifacts?.[0]?.parts[0]?.text ?? '';
}
```
