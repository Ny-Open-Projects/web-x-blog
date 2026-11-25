---
title: [AV-219] WebRTC SFU 信令协议设计：加入/订阅/踢人的状态机
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 笔试题, 26]
type: 笔试题
---

## AV-219：WebRTC SFU 信令协议设计：加入/订阅/踢人的状态机

**答**：
- 题目：设计 SFU 信令协议（基于 WebSocket JSON）：join/peer-join/subscribe/unsubscribe/mute/kick 消息与客户端状态机（idle→joined→connecting→connected）。
- 思路：消息带 seq 与 ack（可靠确认）；状态机：idle → join 请求 → joined（收成员列表）→ 逐成员 subscribe → connected；异常：join 超时重试 3 次。
- 评分点：消息 schema；状态机完整；Glare/重试处理。

```javascript
const SIGNAL_SCHEMA = {
  join: { roomId: 'string', peerId: 'string' },
  'peer-list': { peers: 'array' },
  subscribe: { producerId: 'string', kind: 'audio|video' },
  'peer-join': { peerId: 'string' },
  kick: { targetPeerId: 'string', reason: 'string' },
};
class SfuClient {
  constructor(ws) { this.state = 'idle'; this.seq = 0; this.pending = new Map(); }
  async send(type, payload) {                              // 带确认的信令
    const seq = ++this.seq;
    this.ws.send(JSON.stringify({ type, payload, seq }));
    return new Promise((res, rej) => this.pending.set(seq, { res, rej,
      timer: setTimeout(() => rej(new Error('signal-timeout')), 5000) }));   // 超时重试上层
  }
  async join(roomId) {
    this.state = 'joining';
    const { peers } = await this.send('join', { roomId, peerId: this.peerId });
    this.state = 'joined';
    for (const peer of peers) await this.subscribePeer(peer);   // 逐个订阅
    this.state = 'connected';
  }
  onKick({ reason }) { this.cleanup(); this.onKicked?.(reason); }   // 被踢处理
}
```
