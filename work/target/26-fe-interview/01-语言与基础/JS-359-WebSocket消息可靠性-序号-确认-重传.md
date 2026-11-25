---
title: [JS-359] WebSocket 消息可靠性：序号、确认与重传
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-359：WebSocket 消息可靠性：序号、确认与重传

**答**：
- WS 本身只保证「可靠有序」（TCP 之上），但断线期间的消息会丢——业务可靠性协议：客户端序号 + 服务端 ACK + 断线补拉
- 上行确认：每条消息带 cid（客户端自增序号），服务端 ack 最后 cid；未 ack 的消息存本地待发队列，重连后重发（幂等键防重复）
- 下行补拉：服务端每条消息全局 seq，客户端记录 lastSeq；重连后 `?after=lastSeq` 拉增量（HTTP 接口），再切回 WS 实时流——HTTP 补拉 + WS 实时的双通道结构
- 消息幂等：重发可能重复，服务端按 cid 去重；前端渲染按 seq 去重排序（乱序防御）
- 心跳与半开检测：ping/pong 周期（服务端 idle timeout 约束）+ 未收到 pong 判死立即重连——「连接活着但消息不通」的半开态检测

```javascript
class ReliableWS {
  constructor(url) {
    this.url = url; this.cid = 0; this.pending = new Map(); this.lastSeq = 0;
    this.connect();
  }
  send(type, payload) {
    const cid = ++this.cid;
    const msg = { type, payload, cid };
    this.pending.set(cid, msg);
    this.ws?.send(JSON.stringify(msg));
    setTimeout(() => { if (this.pending.has(cid)) this._resend(cid); }, 5000);  // ack 超时重发
    return cid;
  }
  _onMessage({ seq, ackCid, ...m }) {
    if (ackCid) this.pending.delete(ackCid);            // 上行确认
    if (seq) {
      if (seq <= this.lastSeq) return;                  // 去重
      this.lastSeq = seq; this.onMessage?.(m);
    }
  }
  async _onReconnect() {
    await api.get(`/msg/missed?after=${this.lastSeq}`); // HTTP 补拉增量
    for (const [cid, msg] of this.pending) this.ws.send(JSON.stringify(msg));  // 重发未 ack
  }
}
```

## 追问（补充）

**追问**：

1. WebSocket 已经在 TCP 上可靠有序，业务为什么还要序号？ → TCP 只保证连接存活期间可靠，断线期间收发的消息全丢，业务 seq 用于重连后增量补拉与前端去重排序。
2. 上行 ack 只回「最后 cid」有什么隐患？ → 累计确认在消息乱序或中间缺失时无法定位缺口，需服务端按 cid 连续确认，或回传已收到的 cid 集合。
3. 为什么不能只依赖 onclose 判断连接断开？ → 中间设备静默断流时 TCP 连接仍在，onclose 不触发，形成半开态；只有应用层 ping/pong 超时才能发现并主动重连。
