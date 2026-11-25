---
title: [AV-225] WebRTC RTCRtpScriptTransform 进阶：帧级处理（水印/打标）
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-225：WebRTC RTCRtpScriptTransform 进阶：帧级处理（水印/打标）

**答**：
- Encoded Transform 能逐帧访问编码后数据——用途：帧级水印（嵌入标识）、帧打标（时间戳注入）、帧级加密（AV-223）。
- 帧元数据：RTCEncodedVideoFrame 的 timestamp/synchronizable——可注入业务元数据。
- 性能：Worker 内零拷贝（transferable frame），但每帧处理开销 ~0.1ms——只做轻操作。

```javascript
// 帧级水印（编码后帧数据尾部追加标识）
self.onmessage = async ({ data: { readable, writable, watermark } }) => {
  const reader = readable.getReader(), writer = writable.getWriter();
  while (true) {
    const { value: frame, done } = await reader.read();
    if (done) break;
    const buf = new Uint8Array(frame.data.length + watermark.length);
    buf.set(new Uint8Array(frame.data));
    buf.set(watermark, frame.data.length);                  // 尾部追加水印
    frame.data = buf;
    writer.write(frame);
  }
};
// 解码端剥离水印 → 溯源（泄露追踪）
// 注意：改帧长度可能影响解码器——生产用加解密而非追加（或利用未用 RTP 头扩展位）
```
