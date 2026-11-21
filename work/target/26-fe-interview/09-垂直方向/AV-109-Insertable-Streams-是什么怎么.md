---
title: [AV-109] Insertable Streams 是什么？怎么做端到端加密与自定义帧处理？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-109：Insertable Streams 是什么？怎么做端到端加密与自定义帧处理？（高频）
**答**：
- 定位：在"编码后/传输前"与"接收后/解码前"插入 JS 回调，直接操作每一帧的加密字节流，可看可改。
- E2EE 场景：SFU 只转发密文，密钥只在终端持有，服务器无法窥探内容——企业会议/医疗的核心卖点。
- API 形态：新标准 RTCRtpScriptTransform（配 Worker），Chrome 旧接口 RTCRtpSender.createEncodedStreams()（AV-181 Safari 差异）。
- 帧上可附加自定义元数据（帧号/时间戳），用于同步校准与防重放；密钥轮换靠 postMessage 通知 worker。
- 注意：处理必须在 worker 里做避免阻塞主线程；transform 流处理完必须 enqueue，否则画面冻结。

```javascript
// e2ee.js worker：发送端加密 / 接收端解密（演示级异或，生产用 AES-GCM）
let currentKey = new Uint8Array(32);
self.onmessage = ({ data }) => { if (data.key) currentKey = data.key; }; // 密钥轮换入口

function handleTransform(rtcrtpScriptTransformer, isSender) {
  const transform = new TransformStream({
    transform(frame, controller) {
      const view = new DataView(frame.data);
      const payloadStart = view.getUint16(2) * 4 + 12;   // 跳过 RTP 头与 CSRC
      const payload = new Uint8Array(frame.data, payloadStart);
      for (let i = 0; i < Math.min(payload.length, 64); i++) {
        payload[i] ^= currentKey[i % currentKey.length]; // 就地修改即生效
      }
      controller.enqueue(frame);                          // 必须 enqueue 否则画面冻结
    },
  });
  if (isSender) rtcrtpScriptTransformer.transform = transform; // readable/writable 接线方向两侧相反
  else rtcrtpScriptTransformer.transform = transform;
}
self.onrtctransform = (ev) => handleTransform(ev.transformer, ev.transformer.options?.role === 'sender');
// 主线程注册：pc 的 sender/receiver 各挂 new RTCRtpScriptTransform(worker, { role: 'sender' | 'receiver' })
```
