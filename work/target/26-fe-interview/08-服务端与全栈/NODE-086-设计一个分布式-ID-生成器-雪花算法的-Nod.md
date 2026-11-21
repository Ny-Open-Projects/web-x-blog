---
title: [NODE-086] 设计一个分布式 ID 生成器（雪花算法的 Node 实现）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-086：设计一个分布式 ID 生成器（雪花算法的 Node 实现）？
**答**：
- 需求：全局唯一、趋势递增（利于 B+ 树索引）、高性能本地生成。雪花算法 64 位结构：`1 符号位 + 41 时间戳(ms，约 69 年) + 10 机器 id + 12 序列号(单机每 ms 4096 个)`。
- Node 要点：JS 位运算只有 32 位，64 位 id 用 **BigInt** 计算；**时钟回拨**处理（回拨小则等待，大则报错切换 workerId）；workerId 分配用 Redis INCR 或 ZooKeeper 顺序节点。
- 对比：号段模式（DB 一次取一段，依赖 DB）、UUID（无序索引差）、Redis INCR（强依赖 Redis）。

```javascript
class Snowflake {
  constructor(workerId, dataCenterId = 0) {
    if (workerId < 0 || workerId > 31) throw new Error('workerId 超出范围 0-31');
    const EPOCH = 1288834974657n;              // 起始纪元：自定义，决定可用年限
    this.EPOCH = EPOCH;
    this.workerIdBits = 5n;
    this.dataCenterBits = 5n;
    this.sequenceBits = 12n;
    this.workerId = BigInt(workerId);
    this.dataCenterId = BigInt(dataCenterId);
    this.sequence = 0n;
    this.lastTs = -1n;
    // 各字段的位移
    this.workerIdShift = this.sequenceBits;                    // 12
    this.dataCenterShift = this.sequenceBits + this.workerIdBits; // 17
    this.timestampShift = this.sequenceBits + this.workerIdBits + this.dataCenterBits; // 22
    this.sequenceMask = (1n << this.sequenceBits) - 1n;        // 4095
  }

  nextId() {
    let now = BigInt(Date.now());
    if (now < this.lastTs) {
      // 时钟回拨：小回拨（<5ms）自旋等待，大回拨直接拒绝
      const drift = this.lastTs - now;
      if (drift > 5n) throw new Error(`时钟回拨 ${drift}ms，拒绝发号`);
      while (now <= this.lastTs) now = BigInt(Date.now());
    }
    if (now === this.lastTs) {
      this.sequence = (this.sequence + 1n) & this.sequenceMask;
      if (this.sequence === 0n) {                              // 本 ms 序列用尽，自旋到下一 ms
        while (BigInt(Date.now()) <= this.lastTs) {}
        now = BigInt(Date.now());
      }
    } else {
      this.sequence = 0n;
    }
    this.lastTs = now;
    return ((now - this.EPOCH) << this.timestampShift)
      | (this.dataCenterId << this.dataCenterShift)
      | (this.workerId << this.workerIdShift)
      | this.sequence;
  }
}

// workerId 分配：Redis INCR 取模
async function createIdGenerator() {
  const workerId = (await redis.incr('snowflake:worker:seq')) % 32;
  return new Snowflake(workerId);
}
const gen = await createIdGenerator();
console.log(gen.nextId());   // 4829037215478901001n，趋势递增
```
