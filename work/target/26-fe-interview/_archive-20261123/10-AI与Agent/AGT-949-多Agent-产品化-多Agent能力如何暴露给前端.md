---
title: [949] 多 Agent 系统的结果怎么给前端展示过程与产物
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 产品化]
type: 面试题
---

## 949：多 Agent 系统的结果怎么给前端展示过程与产物

**答**：
- 过程可视化：SSE 推送「当前执行到哪个子任务、哪个 Agent、耗时」，用户对等待有预期；事件流按 traceId 过滤。
- 产物分级展示：最终答案在前、中间产物（检索结果、代码 diff）折叠可展开、工具调用摘要列表；移动端默认只推最终结果。
- 中断与修正：用户可随时打断并在「任一子任务结果」上批注重跑，前端要把「批注作用于哪个环节」表达清楚。
- 追问钩子：过程流会不会泄露敏感信息？——推送前过展示过滤器（内部系统名、密钥、PII），trace 全量留内部、展示层白名单字段。

```ts
// SSE 推送事件设计
type Ev = { type: 'phase_start'|'agent_msg'|'artifact'|'final'; traceId: string;
  agent?: string; label?: string; payload: unknown };
function toClient(ev: Ev) {
  if (ev.type === 'agent_msg') return { type: ev.type, agent: ev.agent,
    label: ev.label };                        // 只推摘要，不推原始内容
  return redactForDisplay(ev);                // 白名单字段过滤
}
```

