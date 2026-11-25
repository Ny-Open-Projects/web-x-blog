---
title: [AGT-291] 前端与 Agent 集成——流式协议（SSE/分帧）怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-291：Agent 的流式输出到前端，协议层怎么设计？

**答**:
- 事件流设计：Agent 的流不只是文本 token——工具调用开始/结束、思考状态、进度事件都要流式传达；统一事件信封 `{type: 'delta'|'tool_start'|'tool_end'|'status'|'done'|'error', seq, payload}`，seq 保序（乱序重排），类型驱动前端渲染分支。
- SSE vs WebSocket：单向流（Agent→前端）SSE 足够且自动重连（Last-Event-ID 续传）；双向（前端打断/交互式确认）需要 WebSocket 或"SSE 下行+HTTP 上行"组合——打断操作（取消生成）走独立 POST。
- 帧与缓冲：SSE 有 4k 行缓冲限制（部分代理），长 token 帧要切片；反压处理——消费慢时服务端积压，考虑丢弃中间 status 事件（保 delta 与关键事件）。
- 兜底：不支持 SSE 的环境降级轮询（长任务）或 WebSocket；重连续传协议——服务端事件持久化带 seq，客户端断线后带 Last-Event-ID 拉取增量。

```javascript
// 服务端事件流
res.writeHead(200, { 'Content-Type': 'text/event-stream' });
function emit(ev) {
  res.write(`id: ${ev.seq}\nevent: ${ev.type}\ndata: ${JSON.stringify(ev)}\n\n`);
}
run.stream(prompt, {
  onDelta: t => emit({ type: 'delta', seq: s++, payload: t }),
  onToolStart: t => emit({ type: 'tool_start', seq: s++, payload: t }),
});
// 客户端：EventSource + Last-Event-ID 续传；
// 打断：POST /cancel 会话，服务端 abort。
```
