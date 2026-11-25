---
title: [SCN-195] 要在业务后台嵌入"AI 助手"，用户说"帮我把这个订单改成加急"，如何安全落地对话式操作？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-195：要在业务后台嵌入"AI 助手"，用户说"帮我把这个订单改成加急"，如何安全落地对话式操作？
**答**：
- 核心安全设计：AI 只产出"意图 + 参数"的草案，不直接执行；执行走受控 action 白名单，且高危操作（改单、退款）必须预览确认。
- 上下文注入要克制：给模型的信息是页面当前实体的结构化摘要（订单号、状态、权限），不是整个 DOM 或全量数据，控制 token 与敏感信息外泄。
- 结果校验：AI 返回的参数按 action schema 校验（枚举、格式），不合法直接要求澄清，不进入执行。
- 埋点与审计：每次对话、每次确认执行都落审计日志（谁、在哪个页面、让 AI 做了什么），这是 B 端 AI 功能的合规底线。

```javascript
// 对话式操作：意图草案 -> schema 校验 -> 预览确认 -> 白名单执行
const ACTIONS = {
  markUrgent: {
    schema: { orderId: /^\d{10,}$/, level: ['high', 'normal'] },
    risk: 'medium',
    preview: (p, ctx) => `将订单 ${p.orderId} 改为${p.level === 'high' ? '加急' : '常规'}`,
    execute: p => api.updateOrder(p.orderId, { urgent: p.level === 'high' }),
    permission: 'order:write',
  },
  queryOrder: { schema: { orderId: /^\d{10,}$/ }, risk: 'low',
    execute: p => api.getOrder(p.orderId) },
};

export async function handleUserUtterance(text, ctx) {
  // 1. 意图解析：模型只输出结构化草案，带页面上下文摘要
  const draft = await llm.chat({
    system: `你是订单后台助手。只输出 JSON：{action, params, clarify?}。
可用 action：${Object.keys(ACTIONS).join(', ')}。信息不足时输出 clarify 字段。禁止编造订单号。`,
    user: `用户输入：${text}\n当前页面上下文：${JSON.stringify(ctx.summary)}`, // 摘要而非全量
    json: true,
  });
  const parsed = safeParse(draft);
  if (parsed.clarify) return askUser(parsed.clarify);  // 信息不足先澄清

  // 2. 白名单 + schema 校验：不认识或参数不合法一律不执行
  const def = ACTIONS[parsed.action];
  if (!def || !checkPermission(ctx.user, def.permission)) return deny('无权限或操作不支持');
  if (!validateSchema(def.schema, parsed.params)) return askUser('参数校验失败，请确认订单号与选项');

  // 3. 高危操作预览确认：AI 不碰执行按钮
  if (def.risk !== 'low') {
    const ok = await confirmDialog({ title: 'AI 待执行操作', body: def.preview(parsed.params, ctx) });
    if (!ok) return cancel();
  }
  // 4. 执行 + 审计
  const result = await def.execute(parsed.params);
  auditLog({ userId: ctx.user.id, action: parsed.action, params: parsed.params, utterance: text });
  return result;
}
```
