---
title: [927] 多 Agent 之间传递什么：自然语言还是结构化消息
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 通信协议]
type: 面试题
---

## 927：多 Agent 之间传递什么：自然语言还是结构化消息

**答**：
- Agent 间通信必须结构化（JSON Schema 约束）：task、artifact、result、error 四类消息；纯自然语言交接会让下游 Agent 产生「转述损耗」，两跳之后任务就变形了。
- 上下文隔离原则：子 Agent 只拿「完成本任务所需的最小上下文」，不传主对话全史——既省 token 又防止无关信息干扰。
- 产物传引用不传全文：大文件/长检索结果存 artifact store，消息里传 URI + 摘要，需要时按需拉取。
- 追问钩子：结构化消息的失败模式？——Schema 太严会卡住边缘情况，生产允许 extra 字段透传 + 入口校验只验证必需字段。

```ts
const MsgSchema = z.object({
  type: z.enum(['task', 'artifact', 'result', 'error']),
  from: z.string(), to: z.string(),
  payload: z.unknown(),
  contextRef: z.string().optional(),   // 指向 artifact store
});
async function dispatch(msg: Msg) {
  parse(MsgSchema, msg);               // 入口校验必需字段
  const agent = registry[msg.to];
  return agent.run({ ...msg, payload: await loadArtifact(msg) });
}
```

