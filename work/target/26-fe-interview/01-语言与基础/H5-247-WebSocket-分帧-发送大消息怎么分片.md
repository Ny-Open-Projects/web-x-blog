---
title: [H5-247] WebSocket 分帧：发送大消息怎么分片
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebSocket]
type: 面试题
---

## H5-247：WebSocket 分帧：发送大消息怎么分片

**答**：
- 大消息的问题：单帧过大（几 MB）导致接收方解析卡顿、网关缓冲区超限（默认常 1MB）、一条大消息阻塞后续消息（应用层队头）
- 分片协议：应用层拆包——`{ type: 'CHUNK', streamId, idx, total, data }` + 最后带 END 标记；接收方按 streamId 聚合
- 服务端配置：ws 库的 maxPayload 限制单帧大小，超限直接断连（安全防护）；发大文件建议走 HTTP 上传 + WS 只发「文件就绪通知」
- 取舍话术：WS 是信令通道不是传输通道，大payload走 HTTP/WebTransport，WS 只负责通知与控制
- 二进制方案：WS 支持 ArrayBuffer 帧，二进制分片效率高于 base64 JSON

```javascript
function sendBig(data, streamId) {
  const json = JSON.stringify(data);
  const CHUNK = 64 * 1024;
  const total = Math.ceil(json.length / CHUNK);
  for (let i = 0; i < total; i++) {
    ws.send(JSON.stringify({
      type: 'CHUNK', streamId, idx: i, total,
      data: json.slice(i * CHUNK, (i + 1) * CHUNK),
    }));
  }
  ws.send(JSON.stringify({ type: 'CHUNK_END', streamId }));
}
```
