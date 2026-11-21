---
title: [AIC-294] 评估工具的扩展生态（MCP/插件/技能）时应关注什么？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-294：评估工具的扩展生态（MCP/插件/技能）时应关注什么？
**答**：
- MCP 服务器质量参差：评估其权限模型（能读什么/能执行什么）、稳定性与维护活跃度。
- 企业内部 MCP：接内部系统（工单/文档/CI 状态）让 Agent 拿到真实上下文，价值最大。
- 安全：MCP 是第三方代码，需审核其数据流向；工具调用要有审计与最小权限。
- 可移植性：MCP 是开放协议，跨工具可复用——优先标准协议而非私有插件。

```javascript
const mcpPolicy = {
  allowlist: ['internal-jira', 'internal-ci', 'docs-search'],
  review: '每个 MCP 上线前：数据流向审计 + 最小权限声明',
  audit: '工具调用全量日志（谁/何时/调用参数摘要）',
};
r
```
