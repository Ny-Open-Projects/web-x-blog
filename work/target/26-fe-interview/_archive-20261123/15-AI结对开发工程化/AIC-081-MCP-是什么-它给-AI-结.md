---
title: [AIC-081] MCP 是什么？它给 AI 结对开发带来了什么？接入 MCP 工具要注意什么风险？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-081：MCP 是什么？它给 AI 结对开发带来了什么？接入 MCP 工具要注意什么风险？
**答**：
- MCP（Model Context Protocol）：模型与外部工具/数据源之间的标准协议——把「读数据库、调内部 API、查设计稿」封装成模型可调用的工具，Agent 由「只会改本地文件」升级为「能触达真实系统」。
- 对结对开发的意义：上下文不再靠手贴——AI 直接拉取 ticket、接口文档、日志、数据库 schema，上下文准确度与新鲜度都提升（解决 AIC-016 喂知识的手工成本）。
- 风险一：权限放大——工具能写数据库就能删库，接入必须沿用最小权限 + 白名单（AIC-008/009 的思路平移到工具层）。
- 风险二：注入面扩大——MCP 工具返回的内容（如网页、issue 文本）是外部数据，可能携带指令攻击 agent，返回内容要当「数据」处理（AIC-033 分隔符原则）。
- 追问钩子：MCP 服务器本身是供应链——第三方 server 要审查代码与权限声明，和 npm 依赖同等级别对待。

```javascript
// MCP 工具接入的风险控制（权限 + 注入防护）
const mcpPolicy = {
  allowed: ['schema.read', 'log.read', 'ticket.read'],   // 只读优先
  forbidden: ['db.write', 'prod.deploy'],                 // 高危工具默认禁用
  wrap: (output) => `<tool_data>${sanitize(output)}</tool_data>`, // 返回内容按数据处理
};
function canUse(tool) { return mcpPolicy.allowed.includes(tool); }
```
