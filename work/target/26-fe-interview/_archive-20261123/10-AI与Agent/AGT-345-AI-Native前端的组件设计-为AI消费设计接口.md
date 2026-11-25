---
title: [AGT-345] 为 AI 设计前端——Agent 可消费的 UI 接口怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-345：前端应用怎么为 AI（爬取/自动化/Agent 调用）优化接口？

**答**:
- 结构化出口：为自动化提供机器可读层——语义化 HTML/ARIA（accessibility tree 即 Agent 的 DOM 接口，AGT-332）、关键数据的 JSON-LD/结构化数据、稳定 data-testid——给 Agent 的接口与给测试的接口同源。
- MCP/API 通道：核心能力直接提供 MCP Server 或 API（比"让 Agent 爬页面"可靠一万倍——界面是给人用的，能力出口给机器）——"页面+结构化出口+MCP"三层服务不同消费者。
- 反爬与授权的平衡：公开内容开放给善意 Agent（ robots/agent 协议），私有操作走授权（OAuth for Agent）；恶意自动化走风控（AGT-300）——不是全防而是分级。
- 可解释的 UI：Agent 在你的应用上执行操作时给足反馈（操作确认对话框语义化、loading/错误状态明确）——为 Agent 优化错误呈现同时提升可访问性，两者同源。

```html
<!-- Agent 友好的标记 -->
<article itemscope itemtype="https://schema.org/Product">
  <h1 itemprop="name">…</h1>
  <meta itemprop="price" content="299">
</article>
<button data-testid="checkout-confirm">…</button>
<!-- 三层出口：语义 HTML + JSON-LD
     + MCP Server（能力直供）
     分级：公开开放 / 私有 OAuth /
     恶意走风控 -->
```
