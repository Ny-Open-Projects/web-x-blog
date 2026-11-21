---
title: [AV-035] 多人会议为什么必须用 SFU？simulcast 和级联是什么？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-035：多人会议为什么必须用 SFU？simulcast 和级联是什么？
**答**：
- 6 人以上 Mesh 上行带宽爆炸（每人 5 路上行），SFU 让每人只上行 1 路，服务器按订阅转发。
- SFU 不解码不混流，只转发 RTP 包：CPU 低、延迟低（<100ms 转发开销）、端到端加密保持。
- simulcast：发送端同传高中低三档，SFU 依据每个订阅端的带宽与窗口大小选层，解决"发送一份但消费端能力不一"的矛盾。
- 订阅模型：客户化 SFU（如 mediasoup/Janus/livekit）中发布者 publish、订阅者 consume，服务端下发 consumer 的 rtpParameters。
- 级联：多个 SFU 机房间互联（A 机房订阅 B 机房房间流），实现跨地域大房间的带宽与延迟均衡。

```javascript
// mediasoup 风格客户端：publish + simulcast + consume 订阅
async function joinMeeting(device, transport, track) {
  // 发布：三档 simulcast
  const producer = await transport.produce({
    track,
    encodings: [
      { rid: 'r0', maxBitrate: 150_000, scaleResolutionDownBy: 4 },
      { rid: 'r1', maxBitrate: 500_000, scaleResolutionDownBy: 2 },
      { rid: 'r2', maxBitrate: 1_200_000 },
    ],
    codecOptions: { videoGoogleStartBitrate: 1000 },
  });

  // 订阅他人：服务端下发 consume 参数后创建 consumer
  const consumer = await transport.consume({
    id: serverConsumer.id,
    producerId: serverConsumer.producerId,
    kind: serverConsumer.kind,
    rtpParameters: serverConsumer.rtpParameters,
  });
  const remoteStream = new MediaStream([consumer.track]);
  document.querySelector(`#peer-${serverConsumer.peerId}`).srcObject = remoteStream;

  // 弱网时向服务端请求降低订阅档位
  window.addEventListener('online', () => signal.requestLayers({ high: true }));
}
```
