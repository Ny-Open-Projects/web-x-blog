---
title: [PER-1031] SSE 与长轮询的选型：什么场景还轮询
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1031：SSE 与长轮询的选型：什么场景还轮询

**答**：
- SSE（EventSource）：单向推送、文本、自动重连、HTTP 原生兼容代理——通知/进度条/新闻流首选。
- 长轮询：兼容性兜底（SSE 不可用时），成本高（每轮一次请求头开销），实时性不如 SSE/WS。
- 双向需求（协作/IM）→ WebSocket；纯下行 → SSE；低频状态同步 → 轮询或即时性要求低时用指数间隔轮询。
- 统一封装：传输层可切换（SSE→SSE polyfill 长轮询→WS），业务层只关心消息事件。

```javascript
// SSE 接收 + 断线回退长轮询
function subscribe(url, onMsg) {
  if ('EventSource' in window) {
    const es = new EventSource(url);
    es.onmessage = e => onMsg(JSON.parse(e.data));
    es.onerror = () => es.close();
    return () => es.close();
  }
  let stop = false;
  (async function poll(cursor = null) {
    while (!stop) {
      const r = await fetch(`${url}?cursor=${cursor}`);
      const { events, next } = await r.json();
      events.forEach(onMsg); cursor = next;
      await new Promise(r => setTimeout(r, 3000));
    }
  })();
  return () => stop = true;
}
```
