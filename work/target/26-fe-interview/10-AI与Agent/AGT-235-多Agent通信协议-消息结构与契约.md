---
title: [AGT-235] 多 Agent 通信协议——Agent 间消息契约怎么定义？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-235：多 Agent 系统中 Agent 之间的消息契约怎么设计？

**答**:
- 消息信封结构：元信息（消息 id/类型/来源/目标/trace id/时间戳）+ 内容（任务或结果的 schema 化负载）+ 控制（优先级/超时/重试策略）——信封与负载分离，负载按业务 schema 校验。
- 类型化消息：TASK_REQUEST（任务书）、TASK_RESULT（结构化结果）、QUERY（同步问询）、EVENT（状态广播）、ERROR（含可恢复标志）——每种类型有明确语义与响应要求，禁止自由文本乱流。
- 契约校验：收到消息先 schema 校验（坏消息拒绝并回 ERROR，不让垃圾进上下文）；版本化 schema（演进时兼容旧字段，新增字段可选）。
- 与 trace 联动：每条消息带 trace_id 与 causality 链（由哪条消息触发），跨 Agent 的分布式追踪靠它串联（AGT-158）。

```javascript
const Envelope = z.object({
  id: z.string(), type: z.enum(['TASK','RESULT','QUERY','EVENT','ERROR']),
  from: z.string(), to: z.string(),
  traceId: z.string(), causeId: z.string().optional(),
  ts: z.number(), ttlMs: z.number().default(60000),
  payload: z.unknown(),                    // 按类型二次校验
});
function validate(msg) {
  const env = Envelope.safeParse(msg);
  if (!env.success) return replyError(msg, 'SCHEMA_VIOLATION');
  if (Date.now() - env.data.ts > env.data.ttlMs)
    return replyError(msg, 'EXPIRED');
  return dispatch(env.data);
}
```
