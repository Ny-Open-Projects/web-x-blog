---
title: [1112] 笔试手写：实现 useStreamToStore
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, 流式]
type: 笔试题
---

## 1112：笔试手写：实现 useStreamToStore

**答**：实现 createStreamSink(store, { flushMs })：返回 sink.push(token) 与 sink.end()。token 先进缓冲，flushMs 窗口内批量 set 到 store（store.append(text)）；end() 立即 flush 并调用 store.finalize()。同一窗口多次 push 合并一次 set（渲染节流）；end 后 push 被忽略（终局保护）。

```js
function createStreamSink(store, flushMs = 50) {
  let buf = '', timer = null, ended = false;
  const flush = () => {
    if (!buf) return;
    const chunk = buf; buf = '';
    store.append(chunk); // 一窗口一次 set
  };
  return {
    push(token) {
      if (ended) return; // 终局保护
      buf += token;
      if (!timer) timer = setTimeout(() => { timer = null; flush(); }, flushMs);
    },
    end() {
      if (ended) return;
      clearTimeout(timer); timer = null;
      flush();
      store.finalize();
      ended = true;
    },
  };
}
```

**评分点**：
- 缓冲 + 定时窗口批量 set（高频 token 不逐字触发渲染）
- end 的终局性（后到 token 丢弃 + 防重复 finalize）
- flush 后 buf 清空防重复写入
- 能讨论：与 AGT 流式合帧器的分工——sink 管数据写入，合帧管渲染帧
