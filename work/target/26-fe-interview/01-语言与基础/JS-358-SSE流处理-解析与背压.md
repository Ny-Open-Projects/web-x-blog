---
title: [JS-358] SSE 流处理：解析、重连与背压
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-358：SSE 流处理：解析、重连与背压

**答**：
- SSE 协议要点：text/event-stream、`event:`/`data:`/`id:`/`retry:` 行协议、双换行分帧——EventSource 自动解析，但 fetch + ReadableStream 方式要自己解析（可控性更强，可带 header）
- 解析器设计：缓冲区累积 chunk → 按双换行切分事件 → 逐行解析字段 → 分发；chunk 边界切断事件的防御（残行保留到下一 chunk）
- 重连语义：EventSource 内置自动重连（Last-Event-ID 头补漏）；fetch 方式要自己实现——断线后带 lastEventId 重连，服务端从 id 之后续传
- 背压：SSE 服务端推送快于前端消费时——消费端队列缓冲 + 节流渲染（UI 更新合帧）；丢消息策略（允许丢的用最新值覆盖）
- 与 WebSocket 选型：单向推送 SSE 够用（简单、自动重连、HTTP 兼容基础设施），双向用 WS；fetch-SSE 是 LLM 流式输出的主流实现

```javascript
async function sseFetch(url, onEvent, { lastId } = {}) {
  const res = await fetch(url, { headers: { Accept: 'text/event-stream', 'Last-Event-ID': lastId ?? '' } });
  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buf = '';
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true });
    let idx;
    while ((idx = buf.indexOf('\n\n')) >= 0) {        // 双换行分帧
      const raw = buf.slice(0, idx); buf = buf.slice(idx + 2);
      const ev = {};
      for (const line of raw.split('\n')) {
        const [k, ...v] = line.split(': ');
        if (k === 'id') ev.id = v.join(' ');
        if (k === 'event') ev.event = v.join(' ');
        if (k === 'data') ev.data = (ev.data ?? '') + v.join(' ');
      }
      onEvent(ev);                                     // 消费端可再队列节流
    }
  }
}
```

## 追问（补充）

**追问**：

1. 为什么用 fetch + ReadableStream 而不是 EventSource？ → EventSource 不能自定义 Authorization 等请求头且只能 GET，fetch 才能带鉴权头并支持 POST 触发，LLM 流式场景必须用它。
2. `TextDecoder` 为什么要传 `{ stream: true }`？ → 一个多字节汉字可能正好被 chunk 边界切断，stream 模式会保留不完整字节序列到下一块拼接，否则出现乱码。
3. 断线重连后如何避免事件重复消费？ → 重连带 `Last-Event-ID` 让服务端从该 id 之后续传，前端再按 id 单调递增过滤，丢弃小于等于已处理 id 的事件。
