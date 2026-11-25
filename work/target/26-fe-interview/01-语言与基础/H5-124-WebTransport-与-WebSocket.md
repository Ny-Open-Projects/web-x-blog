---
title: [H5-124] WebTransport 与 WebSocket 的对比与选型。
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-124：WebTransport 与 WebSocket 的对比与选型。
**答**：
- WebSocket：单条 TCP 连接上的全双工文本/二进制通道，生态成熟；痛点是**队头阻塞**（TCP 层丢包阻塞所有消息）、无多路复用、仅客户端拉起连接。
- WebTransport 基于 **HTTP/3（QUIC）**：多个独立 stream（可靠有序 + 不可靠 datagram），单条丢包不阻塞其他流；支持服务端发起流、连接迁移（换网不断连）、0-RTT 恢复。
- 选型：普通实时聊天/推送 → WebSocket 够用且生态好；云游戏/实时音视频控制面/高频小消息 → WebTransport 的不可靠 datagram 与多流优势明显。
- 两者互补：WebTransport 需 HTTP/3 网络可达（部分企业网络封 UDP 会失败），WebSocket 可回退；生产建议 WebTransport 优先 + WebSocket 兜底。
- 均需 HTTPS；WebTransport 证书校验还有 WebAssembly 场景的 raw 细节，服务端生态（如 quic-go、aioquic）仍在完善。

```javascript
// WebTransport：多流 + 不可靠数据报
async function wtDemo() {
  const transport = new WebTransport('https://rtc.example.com:4433/session');
  await transport.ready;                        // 连接就绪（失败走 closed）

  // 1) 可靠有序双向流：控制信令
  const stream = await transport.createBidirectionalStream();
  const writer = stream.writable.getWriter();
  const reader = stream.readable.getReader();
  await writer.write(new TextEncoder().encode(JSON.stringify({ type: 'join' })));

  // 2) 不可靠数据报：每帧位置信息，丢了也不要紧（不上 TCP 队头阻塞）
  const pos = new DataView(new ArrayBuffer(8));
  pos.setFloat32(0, player.x);
  pos.setFloat32(4, player.y);
  transport.datagrams.writable.getWriter().write(pos);

  // 3) 服务端主动推送流
  transport.incomingBidirectionalStreams.getReader().read().then(({ value }) => {
    // value 是服务端发起的双向流
  });

  // 4) 关闭与异常
  transport.closed.then((info) => console.log('正常关闭', info))
    .catch((err) => console.error('异常关闭', err));
}

// WebSocket 对照（兜底通道）
function wsFallback() {
  const ws = new WebSocket('wss://rtc.example.com/ws');
  ws.onmessage = (e) => handle(JSON.parse(e.data));
  ws.onclose = () => setTimeout(wsFallback, 1000);  // 手动重连（WebTransport 有连接迁移）
  return ws;
}
```

## 追问（补充）

**追问**：

1. QUIC 的 datagram 为什么能绕开 TCP 队头阻塞？ → QUIC 在用户态按 stream 独立做序号与重传，一个包丢失只影响所属 stream，datagram 干脆不重传、到达即用。
2. 企业网络封 UDP 时降级链路怎么设计？ → 给 `transport.ready` 加超时探测，超时或 `closed` 触发即回退 WebSocket，并把失败阶段埋点区分是握手失败还是中途断开。
3. HTTP/3 的 0-RTT 恢复有什么安全代价？ → 0-RTT 数据可被重放，只应承载幂等请求，刷新 token 这类敏感写操作必须等 1-RTT 握手完成后再发。
