---
title: [AGT-246] MCP 安全——工具调用的权限控制与注入防御？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-246：接入 MCP 工具后，安全上要防什么？

**答**:
- 核心威胁一：间接提示注入——工具返回的内容（网页/工单/文档）里藏恶意指令（"请把数据发送到 xxx"），模型可能当指令执行——防御：工具结果视为数据不当指令（prompt 隔离标注）、高危动作加人工确认、输出过滤。
- 核心威胁二：权限过度——Server 拿着用户的完整凭证执行一切——防御：最小权限（细粒度 scope、只读默认）、按操作分级授权（读自动/写确认/删除双确认）、执行审计留痕。
- 核心威胁三：恶意/被劫持的 Server——工具描述本身可以是攻击面（描述里诱导模型）——防御：只装可信来源 Server、工具变更需审核（工具列表哈希校验）、沙箱执行（文件/命令类工具在受限环境跑）。
- 数据外泄防护：出站白名单（Agent 能把数据发给谁受控）、敏感数据标记与脱敏（工具结果带 PII 标记时禁止转发给第三方工具）。

```javascript
// MCP 工具调用的安全包装
async function safeToolCall(call, ctx) {
  assertInWhitelist(call.server);          // 可信来源
  const risk = classifyRisk(call.tool);    // read/write/delete
  if (risk !== 'read') {
    await requireApproval(call, ctx.user); // 写/删人工确认
  }
  const result = await call.execute();
  if (detectInjection(result))             // 结果含指令模式
    return sanitize(result);               // 净化后返回
  if (result.pii) markNoForward(result);   // 敏感数据禁外传
  await audit.log({ user: ctx.user.id, ...call });
  return result;
}
```
