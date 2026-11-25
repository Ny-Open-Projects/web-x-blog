---
title: [AGT-508] 对话记录的本地持久化怎么做（IndexedDB 结构、同步冲突、清理策略）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-508：对话记录的本地持久化怎么做（IndexedDB 结构、同步冲突、清理策略）

**答**：
- IndexedDB 存消息流（按会话分 objectStore，流式 delta 先进内存缓冲、节流落盘），而不是 localStorage（5MB 上限 + 同步阻塞）。
- 与服务端的同步用「服务端为准 + 本地乐观」：本地先显示，确认后替换为服务端 ID；断网期间的消息带 pending 状态，恢复后按序补传。
- 清理策略：超龄会话/超出容量的旧会话 LRU 淘汰，但用户置顶/含未同步修改的会话跳过。

```javascript
const db = idb.open('ai-chat', 1, (s) => {
  s.createObjectStore('sessions', { keyPath: 'id' });
  s.createObjectStore('messages', { keyPath: 'id' })
    .createIndex('bySession', 'sessionId');
});
let flushTimer;
function appendDelta(msgId, delta) {
  buffer[msgId] = (buffer[msgId] || '') + delta;   // 内存缓冲
  clearTimeout(flushTimer);                         // 节流落盘：流式期间别每 token 写库
  flushTimer = setTimeout(() => db.put('messages',
    { id: msgId, content: buffer[msgId], dirty: true }), 500);
}
```

