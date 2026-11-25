---
title: [MFW-612] Durable Objects：有状态边缘的协调原语
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-612：Durable Objects 有状态边缘

**答**:
- DO 的能力：单实例强一致（每个 DO 名 = 全球唯一单实例——计数器/房间/协作会话）；「有状态边缘」填补了 edge 无状态的空缺（RBL-517 的补充：边缘需要协调时用 DO）；WebSocket 持久连接（DO 可持 WS 连接——协作/聊天的 edge 原生方案）。
- 语义约束：单线程串行（DO 内请求串行执行——无并发问题但吞吐受限于单实例）；「单实例 = 瓶颈」：热点房间（万人在线单 DO）→ 分片设计（按子房间拆 DO）；「DO 的定位 = 协调点而非计算点」。
- 与 SSR 的集成：页面渲染在边缘 → 协作状态在 DO（fetch DO 的 RPC——RSC 里调 DO：`env.ROOM.get(id).fetch()`）；「渲染无状态 + 协调有状态」的分层。
- 追问钩子：为什么 DO 的「单线程串行」不是缺陷而是设计？——串行 = 无锁编程（并发问题的消除：计数器原子性/房间状态一致性——不用分布式锁）；吞吐瓶颈 = 分片的明确信号（拆 DO 即扩容）——「正确性优先的简化」：串行让协作逻辑（OT/CRDT 应用/房间管理）在单线程语义下正确；分布式锁的复杂度（RBL-13 目录）被 DO 的单实例语义消除。

```typescript
// Durable Object：协作房间
export class RoomDO {
  state: DurableObjectState;
  sessions: Map<WebSocket, string> = new Map();
  async fetch(req: Request) {
    const url = new URL(req.url);
    if (url.pathname === '/connect') {
      const pair = new WebSocketPair();
      this.state.acceptWebSocket(pair[0]);               // WS 持久连接
      this.sessions.set(pair[0], new URL(req.url).searchParams.get('user'));
      return new Response(null, { status: 101, webSocket: pair[1] });
    }
    if (url.pathname === '/op') {
      const op = await req.json();
      this.applyOp(op);                                   // 串行执行：无锁
      this.broadcast(op);
      return new Response('ok');
    }
  }
  applyOp(op) { /* CRDT/OT 应用：单线程语义下正确 */ }
  broadcast(op) {
    for (const ws of this.sessions.keys())
      ws.send(JSON.stringify(op));
  }
}
// SSR 里调 DO（RSC 数据层）
export async function getRoomState(roomId: string, env) {
  const id = env.ROOM.idFromName(roomId);                 // 名字 → 全球唯一实例
  const room = env.ROOM.get(id);
  return await room.fetch(`https://do/state`).then(r => r.json());
}
```
