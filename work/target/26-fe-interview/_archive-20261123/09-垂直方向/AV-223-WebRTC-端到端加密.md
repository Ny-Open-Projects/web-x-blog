---
title: [AV-223] WebRTC 端到端加密：_insertableStreams 与 E2EE
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-223：WebRTC 端到端加密：_insertableStreams 与 E2EE

**答**：
- 默认加密：DTLS-SRTP（端到服务器）——SFU 可见明文帧；E2EE：Insertable Streams（Encoded Transform）在编码后加密，SFU 只见密文。
- 前端实现：RTCRtpSender transform（Worker 中逐帧加解密），密钥协商走信令（端到端）。
- 代价：SFU 无法转码/录制明文——SIMDcast/SVC 转发不受影响（包级操作）。

```javascript
// E2EE Worker（Encoded Transform）
self.onmessage = async (e) => {
  const { operation, readable, writable } = e.data;
  const reader = readable.getReader();
  const writer = writable.getWriter();
  const key = await crypto.subtle.importKey('raw', e.data.key, 'AES-GCM', false, ['encrypt', 'decrypt']);
  while (true) {
    const { value: frame, done } = await reader.read();
    if (done) break;
    const iv = crypto.getRandomValues(new Uint8Array(12));
    const data = await crypto.subtle[operation]({ name: 'AES-GCM', iv }, key, frame.data);
    frame.data = new Uint8Array(data);
    writer.write(frame);                                    // 逐帧加解密
  }
};
// sender.transform = new RTCRtpScriptTransform(worker, { operation: 'encrypt', key });
// receiver.transform = new RTCRtpScriptTransform(worker, { operation: 'decrypt', key });
```
