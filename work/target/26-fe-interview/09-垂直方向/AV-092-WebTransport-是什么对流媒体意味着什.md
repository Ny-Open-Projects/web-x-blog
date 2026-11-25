---
title: [AV-092] WebTransport 是什么？对流媒体意味着什么？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-092：WebTransport 是什么？对流媒体意味着什么？
**答**：
- 基于 HTTP/3（QUIC）的客户端-服务端流式传输 API：流（streams，可靠有序）、数据报（datagrams，不可靠无序）、双向流，兼顾可靠与低延迟。
- 对比 WebSocket：多路复用无队头阻塞、支持不可靠投递、0-RTT 重连，天然适合"信令走可靠流 + 媒体走 datagram"。
- 流媒体场景：替代 HTTP-FLV 的下一代低延迟拉流；WebCodecs 解码 + WebTransport 传裸帧可实现 <500ms 的自研低延迟播放器；云游戏/远程桌面主力候选。
- 现状：Chrome/Edge 稳定支持，Safari/Firefox 落地中；服务端需 QUIC 栈（如 quic-go、envoy）；HTTP/2 fallback 必须设计。
- 前端要点：connection.closed/negotiate、datagram 容量上限（约 1200B）、发送背压（writer.desiredSize）。

```javascript
// WebTransport 拉流：可靠流走元数据，datagram 走实时帧
async function wtStreamingPlayer(url, videoRenderer) {
  const wt = new WebTransport(url); // wss 协商
  await wt.ready;
  console.log('拥塞控制侧', wt.congestionControl); // throughput/low-latency

  // 1. 元数据/关键信息：可靠双向流
  const bi = await wt.createBidirectionalStream();
  const writer = bi.writable.getWriter();
  writer.write(new TextEncoder().encode(JSON.stringify({ cmd: 'init', codec: 'av01' })));

  // 2. 实时帧数据：不可靠 datagram（超时即丢，不做重传 —— 适合实时）
  const reader = wt.datagrams.readable.getReader();
  (async () => {
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      const { type, ts, data } = parseFrameDatagram(value);
      videoRenderer.enqueue(type, ts, data); // 喂 WebCodecs VideoDecoder
    }
  })();

  // 3. 断线恢复：session ID 支持 0-RTT 重连
  wt.closed.then((info) => console.log('closed', info));
  wt.closed.catch((e) => {
    console.warn('连接异常', e);
    reconnectWithSessionId(wt.sessionId); // 0-RTT 恢复
  });
}
```

## 追问（补充）

**追问**：

1. datagram 超过 1200B 会怎样，分片怎么定 → 超限直接抛错或丢弃，所以应用层要按 MTU 自己切帧（视频按 NAL 单元切并带序号），关键帧走可靠流、P 帧走 datagram，丢帧由解码器容忍。
2. 连接断了播放器怎么无感恢复 → 监听 closed 与 draining，用 0-RTT 重连并带上次流序号续传，重连期间保持最后一帧不黑屏。
3. Safari 不支持时降级路径怎么设计 → 能力探测后按 WebTransport、WebSocket 加 WebCodecs、HTTP-FLV 的顺序一次性选定并锁死，运行中不因单次失败来回切协议，首帧时间反而更差。
