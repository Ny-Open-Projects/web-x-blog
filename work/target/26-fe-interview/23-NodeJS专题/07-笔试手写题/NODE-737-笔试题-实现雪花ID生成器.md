---
title: [NODE-737] 笔试题——实现雪花 ID 生成器（时钟回拨防护 + 机器 ID）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-737：手写雪花 ID

**需求与边界**：
- 需求：Snowflake（SCN-NODE-657）——① 结构（41 时间戳 + 10 机器 + 12 序列）；② 同毫秒序列自增（超 4096 等下一毫秒）；③ 时钟回拨防护（小回拨等待/大回拨拒绝——SCN-NODE-657）；④ 机器 ID 分配（env/协调服务领取）。

**答**：
```javascript
class Snowflake {
  constructor(machineId) {
    if (machineId < 0 || machineId >= 1024) throw new Error('BAD_MACHINE_ID');
    this.machineId = BigInt(machineId);
    this.EPOCH = 1704038400000n;                       // 2024-01-01
    this.lastTs = 0n; this.seq = 0n;
  }
  next() {
    let ts = BigInt(Date.now());
    if (ts < this.lastTs) {                            // 时钟回拨
      const drift = this.lastTs - ts;
      if (drift <= 100n) ts = this.lastTs;             // 小回拨：沿用上次时间戳（生成连续）
      else throw new Error(`CLOCK_BACKWARD_${drift}ms`);   // 大回拨：拒绝 + 告警（SCN-NODE-657）
    }
    if (ts === this.lastTs) {
      if (++this.seq > 4095n) {                        // 序列耗尽：等下一毫秒
        while (BigInt(Date.now()) <= this.lastTs);
        ts = BigInt(Date.now()); this.seq = 0n;
      }
    } else this.seq = 0n;
    this.lastTs = ts;
    return ((ts - this.EPOCH) << 22n) | (this.machineId << 12n) | this.seq;
  }
}
// 机器 ID 分配（启动领取——SCN-NODE-657 难点）
const machineId = await claimMachineId(instanceId);    // DB 表 + 租约（冲突检测）
```

**评分点**:
- 位结构正确（41/10/12 移位）。
- 同毫秒序列耗尽等待下一毫秒（4096 上限）。
- 时钟回拨双策略（小回拨沿用/大回拨拒绝——SCN-NODE-657）。
- 机器 ID 工程化分配（DB 租约——重复 ID 是静默事故）。
