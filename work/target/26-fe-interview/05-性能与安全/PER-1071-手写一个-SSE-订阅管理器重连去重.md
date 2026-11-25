---
title: [PER-1071] 手写一个 SSE 订阅管理器：重连、去重与退订
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1071：手写一个 SSE 订阅管理器：重连、去重与退订

**答**：
- 需求：实现 createSSE(url) 返回 { on(type, fn), close() }。内部维护 EventSource；断线自动重连（浏览器自带的除外，onerror 后 1s 重建，最多 5 次）；同 type 多监听器依次调用；close() 停止并清空监听器；消息统一 JSON.parse（失败丢弃并上报）。
- 边界：重连计数在成功 onopen 后清零；5 次失败后进入 stopped 状态且 on 增加无效；解析失败的 data 上报 sse-parse-fail。
- 评分点：重连上限与清零；多监听器分发；JSON 容错；close 清理

```javascript
function createSSE(url) {
  let es = null, retries = 0, stopped = false;
  const handlers = new Map();
  function connect() {
    if (stopped) return;
    es = new EventSource(url);
    es.onopen = () => retries = 0;
    es.onerror = () => {
      es.close();
      if (++retries >= 5) { stopped = true; report({ type: 'sse-dead', url }); return; }
      setTimeout(connect, 1000);
    };
    es.onmessage = e => {
      let data;
      try { data = JSON.parse(e.data); }
      catch { report({ type: 'sse-parse-fail', raw: e.data.slice(0, 80) }); return; }
      (handlers.get('message') ?? []).forEach(fn => fn(data));
    };
  }
  connect();
  return {
    on(type, fn) {
      if (stopped) return () => {};
      if (!handlers.has(type)) handlers.set(type, []);
      handlers.get(type).push(fn);
      return () => {
        const arr = handlers.get(type);
        const i = arr.indexOf(fn); if (i >= 0) arr.splice(i, 1);
      };
    },
    close() { stopped = true; es?.close(); handlers.clear(); },
  };
}
```
