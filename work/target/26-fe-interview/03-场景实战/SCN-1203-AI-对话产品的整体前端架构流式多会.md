---
title: [SCN-1203] AI 对话产品的整体前端架构（流式/多会话/多模型）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1203：AI 对话产品的整体前端架构（流式/多会话/多模型）

**答**：
- 架构：会话管理（多会话/历史）+ 流式渲染（SSE/WS）+ 模型路由（多模型切换）+ 工具调用渲染。
- 流式：SSE 逐 token 渲染，Markdown 增量解析（代码块/公式）。
- 降级：流式失败回退非流式（一次性返回）。

```javascript
// 对话架构骨架
class ChatApp {
  async send(msg, model) {
    const stream = await fetch('/chat', { method: 'POST',
      body: JSON.stringify({ msg, model, sessionId: this.sessionId }),
      headers: { Accept: 'text/event-stream' } });
    await this.renderStream(stream);
  }
  async renderStream(stream) {
    const reader = stream.body.getReader();
    const dec = new TextDecoder();
    let buf = '';
    for (;;) {
      const { value, done } = await reader.read();
      if (done) break;
      buf += dec.decode(value, { stream: true });
      const events = buf.split('\n\n');
      buf = events.pop();
      events.forEach(e => this.onEvent(e));
    }
  }
  onEvent(e) { /* delta 渲染 */ }
}
```
