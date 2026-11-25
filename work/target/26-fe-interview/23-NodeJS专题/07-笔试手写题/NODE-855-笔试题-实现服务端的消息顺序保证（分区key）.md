---
title: [NODE-855] 笔试题——实现消息顺序保证（分区 key + 并行消费顺序窗口）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-855：手写顺序消费

**需求与边界**：
- 需求：顺序消费（SCN-NODE-651 进阶）——① 分区 key（同聚合同分区——SCN-NODE-733）；② 消费端顺序窗口（并行消费但同 key 串行——per-key 队列，SCN-联想-733）；③ 乱序检测（seq 单调守卫——SCN-FIN-548）；④ 顺序 vs 吞吐权衡（key 分区数——并行度）。
- 边界：① per-key 串行的实现（异步队列 per key——SCN-联想-733）；② key 热点（某 key 消息密集——该分区积压，SCN-NODE-689）；③ 顺序失败的恢复（失败消息阻塞后续——跳过/死信决策）。

**答**：
```javascript
const keyQueues = new Map();                           // per-key 串行队列（SCN-联想-733）
consumer.run({ eachMessage: async ({ message }) => {
  const key = message.key;                             // 分区 key（SCN-NODE-733）
  const seq = +message.headers.seq;
  if (seq <= lastSeq(key)) return;                     // 乱序丢弃（SCN-FIN-548 守卫）
  const q = keyQueues.get(key) ?? keyQueues.set(key, new AsyncQueue()).get(key);
  await q.push(async () => {                           // 同 key 串行
    if (seq !== lastSeq(key) + 1) throw new GapDetected(key);   // 空洞检测（SCN-NODE-640）
    await handler(message);
    lastSeq(key, seq);
  });
}});
// 权衡：key 分区数 = 并行度；热点 key → 拆子 key（SCN-NODE-689 打散——牺牲全局顺序换吞吐）
```

**评分点**:
- 分区 key + per-key 串行队列（SCN-NODE-733）。
- seq 单调守卫 + 空洞检测（SCN-FIN-548/640）。
- 顺序与吞吐权衡（热点 key 拆散——SCN-NODE-689）。
- 顺序失败的恢复决策（跳过/死信——显式）。
