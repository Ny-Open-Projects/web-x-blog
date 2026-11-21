---
title: [AGT-044] WebSocket 与 SSE 各适合什么场景？WebSocket 传 LLM 输出如何落地？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-044：WebSocket 与 SSE 各适合什么场景？WebSocket 传 LLM 输出如何落地？
**答**：
- SSE 单向、基于 HTTP、自动重连、易过网关与 CDN，LLM 单向推流首选；WebSocket 双向、帧级低延迟，适合语音对讲、协作、频繁双向控制信令。
- WS 的隐性成本：心跳保活、断线重连、协议升级要自己实现，部分企业代理对 WS 不友好；SSE 这些都白送。
- 常用组合：LLM 输出走 HTTP+SSE，WS 只做控制信令（中断/续传/状态同步）；全双工语音对话才全走 WS。
- WS 推流按「帧」分边界，比 SSE 的行解析简单，但消息仍是字符串协议，要自己定义 type 字段。

```javascript
// ws server：LLM 输出按帧推送，控制消息反向流动
import { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });
wss.on('connection', (ws) => {
  let ctrl = new AbortController();
  ws.on('message', async (raw) => {
    const msg = JSON.parse(raw);
    if (msg.type === 'stop') { ctrl.abort(); return; }   // 双向优势：随时叫停
    if (msg.type === 'chat') {
      ctrl = new AbortController();
      const res = await upStream({ model: 'gpt-4o-mini', messages: msg.messages, stream: true }, ctrl.signal);
      for await (const ev of parseSSE(res.body!)) {
        if (ev.data === '[DONE]') { ws.send(JSON.stringify({ type: 'done' })); break; }
        ws.send(JSON.stringify({ type: 'delta', text: JSON.parse(ev.data)?.choices?.[0]?.delta?.content ?? '' }));
      }
    }
  });
});

// client：按帧渲染
const ws = new WebSocket('wss://example.com/llm');
ws.onmessage = (e) => {
  const msg = JSON.parse(e.data);
  if (msg.type === 'delta') appendToBubble(msg.text);
  if (msg.type === 'done') finishBubble();
};
ws.send(JSON.stringify({ type: 'chat', messages }));     // 中断：ws.send(JSON.stringify({ type: 'stop' }))
```
