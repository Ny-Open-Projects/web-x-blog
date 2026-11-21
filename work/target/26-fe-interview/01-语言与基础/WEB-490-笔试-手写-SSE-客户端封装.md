---
title: [WEB-490] 笔试：手写 SSE 客户端封装
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 网络]
type: 笔试题
---

## WEB-490：笔试：手写 SSE 客户端封装

**题目**：用 fetch 实现一个 SSE 客户端（不用 EventSource）：支持自定义 headers（带 token）、自动解析 `data:` 事件流、断线自动重连、支持取消。

**答**：
```javascript
function createSSE(url, { headers = {}, onEvent } = {}) {
  let ctrl = new AbortController();
  let closed = false;

  async function run() {
    try {
      const res = await fetch(url, {
        headers: { Accept: 'text/event-stream', ...headers },
        signal: ctrl.signal,
      });
      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buf = '';
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buf += decoder.decode(value, { stream: true });
        const events = buf.split('\n\n'); // SSE 以空行分隔事件
        buf = events.pop();               // 最后一段可能不完整，留到下一轮
        events.forEach(e => {
          const data = e.split('\n').filter(l => l.startsWith('data:'))
            .map(l => l.slice(5).trim()).join('\n');
          if (data) onEvent?.(data);
        });
      }
    } catch (e) {
      if (!closed && e.name !== 'AbortError') setTimeout(run, 3000); // 断线重连
    }
  }
  run();
  return { close() { closed = true; ctrl.abort(); } };
}
```

**评分点**：
- 用 TextDecoder 处理流式解码，注意 `{ stream: true }` 防多字节字符截断
- 按 `\n\n` 分事件，残包缓冲（buf）处理是核心考点
- 断线重连 + close 可取消，且取消后不再重连
- 能对比 EventSource：不支持自定义 header 是手写的动机（加分）
