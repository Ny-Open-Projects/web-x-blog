---
title: [AGT-244] MCP Server 开发实践——写一个生产可用的工具服务？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-244：怎么开发一个生产可用的 MCP Server？

**答**:
- 基本骨架：用官方 SDK（TypeScript/Python）声明工具（名称/描述/Zod schema/处理函数），注册传输层（stdio 或 HTTP），错误统一包装（返回 isError 消息而不是抛异常——异常会断连接）。
- 描述质量是核心竞争力：工具描述与参数描述是给 LLM 看的使用说明书——写"何时用/何时不用/参数含义/返回结构"，含糊描述是模型调用错误的第一原因。
- 生产化清单：输入校验（Zod schema 挡脏参数）、超时与重试（下游 API 级）、限流与配额（防 Agent 循环调用打爆下游）、审计日志（谁在什么上下文调了什么）、幂等键支持（Agent 重试友好）。
- 测试方法：协议一致性测试（initialize/发现/调用生命周期）+ 用真实 Host（Claude Desktop/Cursor）人工冒烟 + 给 LLM 的调用准确率评测（用标准任务集测模型能否选对工具传对参数）。

```typescript
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';

const server = new McpServer({ name: 'order-tools', version: '1.0' });
server.tool(
  'queryOrder',   // 名称
  '按订单号查询订单状态。仅在用户提供订单号时使用；不用于列表查询。',
  { orderId: z.string().regex(/^ORD\\d+$/) },
  async ({ orderId }) => {
    try {
      const order = await api.get(`/orders/${orderId}`, { timeout: 5000 });
      return { content: [{ type: 'text', text: JSON.stringify(order) }] };
    } catch (e) {
      return { isError: true, content: [{ type: 'text', text: `查询失败: ${e.message}` }] };
    }
  });
server.connect(new StdioServerTransport());
```
