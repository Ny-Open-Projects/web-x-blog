---
title: [XP-054] 设计一个跨端 IM 应用，如何保证消息一致性？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-054：设计一个跨端 IM 应用，如何保证消息一致性？
**答**：
- 一致性核心：**服务端 seq 权威化**——每会话单调递增 seq，客户端按 seq 排序去重，乱序补拉。
- 收发链路：本地先渲染（乐观消息，pending 态）→ 上行带 clientMsgId（幂等）→ 服务端落库分配 seq → ACK 后转 confirmed；失败转 failed 可重试。
- 同步模型：每个设备维护 `syncCursor`，重连/离线后按 cursor 增量拉取（拉取接口幂等分页），多端在线用已读回执与 seq 对齐状态。
- 跨端要点：消息**存储层抽象**（各端本地 DB：SQLite/MMKV/IndexedDB）+ 同步引擎独立成包（core，XP-047）；断线重连指数退避+消息补洞。
- 顺序保证：UI 展示按 seq 插入，发送方本地时间只用于显示不用于排序。

```typescript
// packages/core/im/sync-engine.ts —— 跨端消息同步引擎
interface Msg { clientMsgId: string; seq?: number; state: 'pending' | 'confirmed' | 'failed'; body: any }

export class SyncEngine {
  #cursor = 0;                       // 设备级同步位点（持久化到本地 DB）
  #outbox: Msg[] = [];

  async send(text: string) {
    const msg: Msg = { clientMsgId: uuid(), state: 'pending', body: { text } };
    this.#outbox.push(msg); this.emit(msg);                   // 乐观上屏
    try {
      const ack = await api.sendMsg({ clientMsgId: msg.clientMsgId, body: msg.body }); // 幂等键
      msg.seq = ack.seq; msg.state = 'confirmed'; this.emit(msg);   // ACK 转正
    } catch { msg.state = 'failed'; this.emit(msg); }
  }

  async onConnect() {                                   // 重连/启动：按 cursor 增量对账
    let page = await api.pullSince(this.#cursor);
    for (const m of page.msgs.sort((a, b) => a.seq! - b.seq!)) {
      if (m.seq! <= this.#cursor) continue;             // 去重（服务端可能重复下发）
      this.db.upsert(m); this.#cursor = m.seq!;         // 按 seq 单调推进
      // 补洞：发现 seq 跳跃（m.seq > cursor+1）→ 回退拉取缺口
    }
    if (page.hasMore) return this.onConnect();
  }
}
// 各端绑定：RN/小程序用 SQLite，H5 用 IndexedDB；UI 按 seq 排序渲染，
// pending 消息以占位插入confirmed 流的尾部，ACK 后替换（clientMsgId 关联）
```
