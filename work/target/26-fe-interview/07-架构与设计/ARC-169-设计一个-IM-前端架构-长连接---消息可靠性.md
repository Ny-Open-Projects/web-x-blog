---
title: [ARC-169] 设计一个 IM 前端架构（长连接 / 消息可靠性 / 多端同步）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-169：设计一个 IM 前端架构（长连接 / 消息可靠性 / 多端同步）？
**答**：
- 连接层：独立长连接网关（鉴权/心跳/断线重连退避），业务层只见"消息流"；多端在线时同一账号多设备各自持有连接，服务端扇出。
- 可靠性协议：消息全局 seq（会话内单调），客户端 ACK 机制——超时未 ACK 服务端重发，客户端按 seq 去重排序；断线重连后按本地最大 seq 拉增量（gap 检测补拉）。
- 发送可靠性：本地先写（pending 态）→ 发送 → 确认翻转为 sent；失败进重发队列（指数退避），撤回/编辑等操作依赖服务端确认。
- 存储分层：内存态（当前会话热数据）+ IndexedDB（会话持久化，按会话分表）+ 服务端漫游（换设备可拉历史）。

```typescript
// IM 消息可靠性协议核心
interface Message { msgId: string; seq: number; convId: string; body: unknown; status: 'pending' | 'sent' | 'failed' }

class IMClient {
  private sendQueue: Message[] = [];
  private ackedSeq = new Map<ConvId, number>();       // 每会话已确认最大 seq

  // 发送：本地先写 pending → 发送 → ACK 翻转
  async send(convId: ConvId, body: unknown) {
    const msg: Message = { msgId: uuid(), seq: -1, convId, body, status: 'pending' };
    await this.localDB.put(msg);                       // 1. 本地持久化（离线也不丢）
    this.sendQueue.push(msg);
    this.flush();
  }
  private async flush() {
    while (this.sendQueue.length) {
      const m = this.sendQueue[0];
      try {
        const { seq } = await this.conn.sendWithAck(m, { timeout: 5000, retries: 3 });
        m.seq = seq; m.status = 'sent';
        await this.localDB.put(m);                     // 2. 服务端确认落库
        this.sendQueue.shift();
      } catch { await sleep(backoff(++this.retry)); }  // 指数退避重发
    }
  }
  // 接收：按 seq 去重排序 + gap 补拉
  onServerPush(msg: Message) {
    const last = this.ackedSeq.get(msg.convId) ?? 0;
    if (msg.seq <= last) return;                       // 去重（重发的消息丢弃）
    if (msg.seq > last + 1) this.fetchGap(msg.convId, last + 1, msg.seq - 1);  // gap 补拉
    this.ackedSeq.set(msg.convId, msg.seq);
    this.conn.ack(msg.seq);                            // 显式 ACK
    this.render(msg.convId, msg);
  }
}
```
