---
title: [AGT-821] 给企业前端开发者的平台 SDK（嵌入 Agent 会话组件），SDK 设计要点？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-821：给企业前端开发者的平台 SDK（嵌入 Agent 会话组件），SDK 设计要点

**答**：
- SDK 分层：核心（会话/流式/工具 UI 状态机）、UI 组件（开箱可用的对话组件，主题可定制）、hooks（自定义渲染）。核心原则：核心层零 UI 依赖（headless），UI 层可选——企业要深度定制界面时只用核心层。
- 集成三要素：鉴权托管（短期 token 交换，SDK 不存长期密钥）、事件透传（traceId/租户上下文自动带）、能力探测（服务端能力版本协商，旧 SDK 不炸）。
- 体积纪律：核心 <30KB，重组件（markdown/高亮）全部懒加载；提供 tree-shaking 友好的 ESM。

```javascript
import { AgentSession } from '@platform/sdk-core';   // headless 核心
import { ChatPanel } from '@platform/sdk-ui';        // 可选UI

const session = new AgentSession({
  tokenExchange: () => fetch('/api/agent-token'),   // 短期token
  tenant: 'acme', trace: true,
});
// headless 用法：企业自绘 UI
session.on('delta', render);
// 组件用法：开箱即用
<ChatPanel session={session} theme={corpTheme} />
```

