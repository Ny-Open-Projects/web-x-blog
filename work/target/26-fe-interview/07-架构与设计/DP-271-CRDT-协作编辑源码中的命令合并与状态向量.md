---
title: [DP-271] 源码识别：Yjs/CRDT 源码中的合并策略与状态向量？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-271：源码识别：Yjs/CRDT 源码中的合并策略与状态向量？
**答**:
- 状态向量（因果追踪）：每个副本维护 clock 向量，同步只交换"对方缺的部分"——diff 同步而非全量。
- 合并策略：并发操作按确定性规则合并（插入按 origin+客户端 id 排序，删除是 tombstone 标记）——任意顺序到达结果一致（CRDT 核心保证）。
- 命令流：本地编辑产生 operation，广播给其他副本；undo 是"插入逆操作"而非回滚（保留他人改动）。
- 识别要点：能说清"OT（服务端定序）vs CRDT（无中心确定性合并）"的取舍——离线协作/去中心化选 CRDT。

```javascript
// Yjs 心智模型（简化）
class Doc {
  ops = [];                                  // 操作日志（tombstone 保留）
  clock = new Map();                         // state vector: client → seq
  localUpdate(op) {
    this.clock.set(op.client, (this.clock.get(op.client) ?? 0) + 1);
    this.ops.push(op);                       // op: { client, seq, origin, content, deleted? }
    broadcast(op);
  }
  applyRemote(op) {
    if ((this.clock.get(op.client) ?? 0) >= op.seq) return;   // 幂等：已见过的 op 跳过
    this.ops.push(op);
    integrate(op);                           // 确定性合并：按 origin 与 client id 排序插入
    this.clock.set(op.client, op.seq);
  }
  sync(remoteVector) {
    return this.ops.filter(op => op.seq > (remoteVector.get(op.client) ?? 0));   // 只发对方缺的
  }
}
// undo：不是删除历史，而是插入"标记删除"的新 op（保留协作者的插入——CRDT undo 语义）
```
