---
title: [985] 笔试手写：实现 SSE 客户端解析器（断线缓冲与事件分发）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 成本延迟, 流式]
type: 笔试题
---

## 985：笔试手写：实现 SSE 客户端解析器（断线缓冲与事件分发）

**答**：实现 createSSEParser()：feed(chunk) 接收可能不完整的文本流片段；按 SSE 规范解析 event/data 字段（data 多行拼接）；通过 on(event, fn) 注册监听；正确处理事件边界跨 chunk 的情况。

```js
function createSSEParser() {
  let buf = '';
  const handlers = {};
  function dispatch(ev) {
    if (ev.event && handlers[ev.event]) handlers[ev.event](ev.data);
  }
  function feed(chunk) {
    buf += chunk;
    let idx;
    while ((idx = buf.indexOf('\n\n')) !== -1) {   // 事件以空行分隔
      const raw = buf.slice(0, idx); buf = buf.slice(idx + 2);
      const ev = { event: 'message', data: '' };
      const dataLines = [];
      for (const line of raw.split('\n')) {
        if (line.startsWith('event:')) ev.event = line.slice(6).trim();
        else if (line.startsWith('data:')) dataLines.push(line.slice(5).replace(/^ /, ''));
      }
      ev.data = dataLines.join('\n');               // 多行 data 拼接
      dispatch(ev);
    }
  }
  return { feed, on: (e, fn) => (handlers[e] = fn) };
}
const p = createSSEParser();
p.on('delta', d => console.log('got', d));
p.feed('event: delta\ndata: hel');   // 跨 chunk：第一个事件不完整
p.feed('lo\n\nevent: done\n\n');  // 补完 -> 输出 'got hello'，然后 done
```

**评分点**：
- 事件边界以空行分隔，跨 chunk 缓冲处理正确（高频考点）
- data 多行拼接语义符合规范；字段解析兼容 `data:` 后可选空格
- 不完整事件保留在 buf 等待后续 chunk，不提前分发
- 能讨论：JSON data 要 try/catch 解析防脏数据；SSE 注释行（`:` 开头）应跳过

