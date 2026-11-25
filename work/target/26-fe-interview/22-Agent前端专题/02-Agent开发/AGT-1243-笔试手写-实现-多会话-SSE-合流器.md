---
title: [1243] 笔试手写：实现 多会话 SSE 合流器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## 1243：笔试手写：实现 多会话 SSE 合流器

**答**：实现 mergeStreams(streams)：streams 为 { id, seq, text }[] 的多路流事件数组（同一 id 内 seq 单调递增、跨路交错到达）。要求输出按「全局到达序」但同一会话内按 seq 排序的合并文本序列；某一路连续 5 个事件未到（seq 缺口）时将该路降级挂起不阻塞其他路，返回 { merged, suspended }。

```js
function mergeStreams(streams) {
  const byId = new Map();
  for (const ev of streams) {
    if (!byId.has(ev.id)) byId.set(ev.id, { buf: [], next: 0, suspended: false });
    const s = byId.get(ev.id);
    if (ev.seq >= s.next) s.buf[ev.seq] = ev.text; // 丢弃重放旧 seq
  }
  const merged = [], suspended = [];
  let progress = true;
  while (progress) { // 轮询各路，可推进才继续
    progress = false;
    for (const [id, s] of byId) {
      if (s.suspended) continue;
      if (s.buf[s.next] !== undefined) {
        merged.push({ id, text: s.buf[s.next] }); s.next++; progress = true;
      } else if (s.buf.length - s.next >= 5) { // seq 缺口过大
        s.suspended = true; suspended.push(id);
      }
    }
  }
  return { merged, suspended };
}
```

**评分点**：
- 每路独立维护 next 期望 seq，乱序缓存不乱序输出
- 重放旧事件直接丢弃（幂等）
- 缺口阈值挂起单路、不阻塞全局（公平性）
- 轮询循环用 progress 标记防死循环
