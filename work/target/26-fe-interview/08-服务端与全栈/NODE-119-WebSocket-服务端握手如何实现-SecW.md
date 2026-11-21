---
title: [NODE-119] WebSocket 服务端握手如何实现（Sec-WebSocket-Accept 计算）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-119：WebSocket 服务端握手如何实现（Sec-WebSocket-Accept 计算）？
**答**：
- 握手借道 HTTP：客户端发 `Upgrade: websocket` + 随机 `Sec-WebSocket-Key`；服务端回 **101** + `Sec-WebSocket-Accept = base64(sha1(key + 固定 GUID))`，GUID 为协议魔数 `258EAFA5-E914-47DA-95CA-C5AB0DC85B11`。
- 校验意义：证明服务端理解 WS 协议而非普通 HTTP 代理误处理；key 是 base64 的 16 字节随机数，防缓存与重放。
- 握手后切到 WS 帧协议：BYTE0（FIN+opcode）、BYTE1（MASK+长度），客户端帧必须 mask，服务端帧不 mask；ping/pong 心跳 opcode 0x9/0xA。
- 生产用 `ws` 库；手写只为理解协议与面试。

```javascript
const http = require('http');
const crypto = require('crypto');
const MAGIC = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11';

const server = http.createServer();
server.on('upgrade', (req, socket) => {
  if (req.headers.upgrade?.toLowerCase() !== 'websocket') return socket.destroy();
  const accept = crypto.createHash('sha1')
    .update(req.headers['sec-websocket-key'] + MAGIC).digest('base64');
  socket.write(
    'HTTP/1.1 101 Switching Protocols\r\n' +
    'Upgrade: websocket\r\n' +
    'Connection: Upgrade\r\n' +
    `Sec-WebSocket-Accept: ${accept}\r\n\r\n`);

  // 最小帧处理：opcode 0x9 ping 回 0xA pong；0x8 close
  socket.on('data', (buf) => {
    const opcode = buf[0] & 0x0f;
    if (opcode === 0x9) socket.write(Buffer.from([0x8a, 0x00])); // 掩码位简化处理
  });
});
server.listen(3000);
// 子协议协商 Sec-WebSocket-Protocol、压缩扩展 permessage-deflate 同在握手期完成
```
