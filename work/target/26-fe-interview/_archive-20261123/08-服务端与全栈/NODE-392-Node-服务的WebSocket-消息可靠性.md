---
title: [NODE-392] Node 服务的 WebSocket 消息可靠性（不丢/不重/有序）如何保证？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-392：WebSocket 消息可靠性
**答**:
- 三性问题：不丢（ack + 重发 + 离线补拉）、不重（seq 去重）、有序（会话内单通道保证或版本向量）。设计：服务端每消息递增 seq（按用户/会话维度），客户端 ack（收到回执），超时未 ack 重发（指数退避）；断线重连带 lastSeq → 服务端补发 gap（消息暂存窗口 N 分钟，更早走离线拉取接口）。
- 实现细节：暂存窗口用 Redis list/zset（seq 索引），ack 后滚动清理；重发与补拉都幂等（客户端 seq 去重）；多设备同账号各自独立 seq 流（设备号维度）。
- 心跳与半开连接：服务端 ping 超时主动断开（防僵尸连接占资源）；客户端重连退避 + 抖动（NODE-416 配合）。
- 业务语义：IM 类"送达/已读"是业务层回执（与传输层 ack 分开）；通知类可丢（最新值覆盖，不追历史）。
- 容量：ack 暂存窗口内存 = 消息速率 × 窗口时长 × 平均大小，纳入容量模型。
```javascript
class ReliableChannel {
  async push(uid, msg) {
    const seq = await redis.incr(`seq:${uid}`);
    await redis.zadd(`pending:${uid}`, seq, JSON.stringify(msg)); // 暂存
    this.sendLocal(uid, { ...msg, seq });
    this.scheduleAckTimeout(uid, seq);                            // 超时重发
  }
  onAck(uid, seq) { redis.zremrangebyscore(`pending:${uid}`, 0, seq); } // 滚动清理
  async onReconnect(uid, lastSeq) {
    const gap = await redis.zrangebyscore(`pending:${uid}`, lastSeq + 1, '+inf');
    gap.forEach(m => this.sendLocal(uid, m));                     // 补发 gap
  }
}
```
