---
title: [ALG-547] 手写雪花 ID 与时钟回拨：ID 生成
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-547：手写雪花 ID 与时钟回拨：ID 生成

**答**：
- 题目：分布式 ID 生成——雪花算法（时间戳+机器+序列），处理时钟回拨（等待或备用位）。64 位布局：1 符号 + 41 时间戳 + 10 机器 + 12 序列。
- 思路：同毫秒序列自增；序列溢出等下一毫秒；时钟回拨：小回拨自旋等待，大回拨报错（或用备用机器位）。
- 评分点：位布局；序列溢出等待；回拨策略分级。

```javascript
class SnowflakeID {
  constructor(machineId) {                                  // machineId 0~1023
    this.machine = BigInt(machineId) << 12n;
    this.sequence = 0n;
    this.lastTs = 0n;
    this.epoch = 1288834974657n;                            // Twitter 纪元
  }
  next() {
    let ts = BigInt(Date.now());
    if (ts < this.lastTs) {                                 // 时钟回拨
      const drift = this.lastTs - ts;
      if (drift <= 5n) {
        // 小回拨：自旋等待追平
        while (BigInt(Date.now()) < this.lastTs) { /* spin */ }
        ts = this.lastTs;
      } else throw new Error(`clock-back-${drift}ms`);      // 大回拨：报错切备
    }
    if (ts === this.lastTs) {
      this.sequence = (this.sequence + 1n) & 4095n;        // 12 位序列
      if (this.sequence === 0n) {                          // 溢出：等下一毫秒
        while (BigInt(Date.now()) <= this.lastTs) { /* spin */ }
        return this.next();
      }
    } else this.sequence = 0n;
    this.lastTs = ts;
    return ((ts - this.epoch) << 22n) | this.machine | this.sequence;
  }
}
```
