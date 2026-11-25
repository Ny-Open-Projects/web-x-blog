---
title: [RBL-875] 笔试：手写 SSE 流解析器（跨 chunk 事件边界 + 重连 Last-Event-ID）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-875：笔试：手写 SSE 流解析器（跨 chunk 边界 + id 追踪）

**答**：实现 `createSSEParser()`。`push(text)`：接收流式到达的文本块（事件可能跨 chunk 切断）；返回本次解析出的完整事件数组 `{ id?, event?, data }[]`。SSE 格式：事件以空行分隔；行格式 `id: x` / `event: y` / `data: z`（data 可多行拼接）；`data: [DONE]` 也是事件。规则：1) 跨 chunk 缓冲（不完整事件保留待后续 push）；2) 事件字段聚合（同事件多 data 行以 \n 连接）；3) `lastId()` 返回最近事件的 id（重连时作 Last-Event-ID）；4) 注释行（`:` 开头）忽略。边界：push 空串；末尾未终止事件不产出。

```javascript
function createSSEParser() {
  let buf = ''; let lastId = null;
  const FIELD = /^(\w+):\s?(.*)$/;
  function push(text) {
    buf += text;
    const events = [];
    let idx;
    while ((idx = buf.indexOf('\n\n')) !== -1) {
      const block = buf.slice(0, idx);
      buf = buf.slice(idx + 2);
      const ev = {};
      for (const line of block.split('\n')) {
        if (line.startsWith(':')) continue;              // 注释
        const m = FIELD.exec(line);
        if (!m) continue;
        if (m[1] === 'id') { ev.id = m[2]; lastId = m[2]; }
        else if (m[1] === 'event') ev.event = m[2];
        else if (m[1] === 'data') ev.data = ev.data ? ev.data + '\n' + m[2] : m[2];
      }
      if (ev.data !== undefined) events.push(ev);        // 无 data 不算事件
    }
    return events;
  }
  return { push, lastId: () => lastId };
}

// 自测
const p = createSSEParser();
// 跨 chunk：事件 1 被切断
let out = p.push('id: 1\nevent: message\nda');
console.log(out.length === 0);                           // 未终止
out = p.push('ta: hello\n\n');
console.log(JSON.stringify(out));
// [{ id: '1', event: 'message', data: 'hello' }]

// 多 data 行 + 注释
out = p.push(': keepalive\ndata: line1\ndata: line2\n\n');
console.log(out[0].data === 'line1\nline2');
console.log(p.lastId() === '1');

// 新事件 id 更新 + [DONE]
out = p.push('id: 2\ndata: [DONE]\n\n');
console.log(out[0].data === '[DONE]' && p.lastId() === '2');

// 空串
console.log(p.push('').length === 0);
// 半截 data 行（含冒号的 data 内容）
out = p.push('data: a:b:c\n\n');
console.log(out[0].data === 'a:b:c');
```

**评分点**：
- 跨 chunk 缓冲正确（不完整事件留存，\n\n 边界切分）；半截字段行续接
- 字段聚合（多 data 行 \n 连接）、注释行忽略、id 追踪（lastId 供重连）
- data 含冒号的解析（split 首个冒号而非全部）；无 data 块不产出
- 能说清「SSE 解析必须处理 chunk 切断——按事件边界而非行边界缓冲是流式正确性的核心」属于加分
