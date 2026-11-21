---
title: [ARC-119] 协同光标与选区同步（presence）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-119：协同光标与选区同步（presence）如何设计？
**答**：
- 光标/选区走独立的 presence 通道，与文档数据通道分离：presence 高频、易失（断线即消失）、不需要持久化；文档 op 低频、必须可靠。混在一条通道会让文档协议被 presence 洪水拖垮。
- 关键算法：收到远端文档 op 时，本地和远端的**光标位置也要 transform**，否则别人在前面插入文字后你的光标会错位。
- 工程细节：presence 广播节流（如 100ms 批量）、自动清理超时用户、身份元信息（名字/颜色/头像）随 presence 附带、选区折叠成光标的展示策略。
- Yjs 类库直接提供 awareness 协议；自研时把它当独立子系统设计。

```typescript
// presence 协议与光标 transform
interface CursorState { clientId: string; name: string; color: string; anchor: number; head: number; ts: number }

// 1. 本地光标变化 → 节流广播（presence 通道，不落库）
const broadcastCursor = throttle((c: CursorState) => presenceChannel.send(c), 100);
// 服务端维护在线表：超过 10s 无心跳即广播该用户下线

// 2. 收到远端文档 op → 远端与本地光标都要 transform
function applyRemoteOp(op: DocOp, op2: Op) {
  doc.apply(op2);
  for (const peer of peers.values()) {
    const t = transformCursor(peer.anchor, peer.head, op2);   // 远端光标对 op 变换
    peer.anchor = t.anchor; peer.head = t.head;
  }
  const local = transformCursor(myCursor.anchor, myCursor.head, op2);
  myCursor.anchor = local.anchor; myCursor.head = local.head; // 自己的光标也要变
}
function transformCursor(anchor: number, head: number, op: Op) {
  const shift = (p: number) =>
    op.type === 'insert' ? (p >= op.pos ? p + op.text!.length : p)
                         : (p > op.pos + op.len! ? p - op.len! : Math.max(p, op.pos));
  return { anchor: shift(anchor), head: shift(head) };
}
```
