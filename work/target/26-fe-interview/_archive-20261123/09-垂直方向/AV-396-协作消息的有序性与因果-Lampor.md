---
title: [AV-396] 协作消息的有序性与因果（ Lamport 时钟）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-396：协作消息的有序性与因果（ Lamport 时钟）

**答**：
- 问题：多端消息乱序到达，UI 展示顺序需一致。
- 方案：Lamport 逻辑时钟（每消息带 counter+nodeId），展示按 (counter, nodeId) 排序；或服务端统一 seq。
- 一致性验证：各端对同一操作序列渲染结果 hash 一致。

```javascript
// Lamport 时钟
class LamportClock {
  constructor(nodeId) { this.nodeId = nodeId; this.counter = 0; }
  tick() { return { c: ++this.counter, n: this.nodeId }; }
  receive(msg) { this.counter = Math.max(this.counter, msg.lc.c) + 1; }
  static before(a, b) {
    return a.c < b.c || (a.c === b.c && a.n < b.n);   // 全序比较
  }
}
// 一致性验证：
function convergeCheck(clients) {
  const hashes = clients.map(c => hashDoc(c.doc));
  return new Set(hashes).size === 1;                   // 全端一致
}
```
