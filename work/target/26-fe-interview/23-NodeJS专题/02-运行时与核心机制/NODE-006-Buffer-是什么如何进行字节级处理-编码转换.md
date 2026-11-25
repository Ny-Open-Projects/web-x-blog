---
title: [NODE-006] Buffer 是什么？如何进行字节级处理（编码转换/二进制协议解析）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-006：Buffer 是什么？如何进行字节级处理（编码转换/二进制协议解析）？
**答**：
- `Buffer` 是 V8 堆外的**固定长度字节序列**（`Uint8Array` 子类），用于处理 TCP 流、文件、二进制协议。`Buffer.allocUnsafe` 不清零（快但可能泄露旧数据），生产用 `Buffer.alloc`。
- 编码支持：utf8 / utf16le / latin1 / base64 / hex / ascii。Node 18+ 默认编码统一为 utf8，`Buffer` 全局可用但推荐显式 `require('node:buffer')`。
- 高频点：**字符串与字节不是一一对应**（中文 UTF-8 占 3 字节），分块读取文件时块边界可能截断多字节字符，需用 `string_decoder` 或设置 `state.remaining` 拼接。

```javascript
const buf = Buffer.from('前端 Node', 'utf8');
console.log(buf.length);                    // 11：2 个中文 ×3 + 空格 1 + Node 4
console.log(buf.toString('hex'));           // 字节十六进制
console.log(buf.toString('base64'));        // 5YiY5L2TIE5vZGU=

// 二进制协议解析：前 4 字节长度 + 2 字节类型 + 剩余 payload
function decodePacket(buffer) {
  const length = buffer.readUInt32BE(0);
  const type = buffer.readUInt16BE(4);
  const payload = buffer.subarray(6, 6 + length).toString('utf8');
  return { length, type, payload };
}
const body = Buffer.from(JSON.stringify({ msg: 'ping' }));
const head = Buffer.alloc(6);
head.writeUInt32BE(body.length, 0);
head.writeUInt16BE(0x01, 4);
console.log(decodePacket(Buffer.concat([head, body])));

// 多字节字符跨块问题：string_decoder 保证不产生乱码
const { StringDecoder } = require('node:string_decoder');
const decoder = new StringDecoder('utf8');
const chunk1 = Buffer.from([0xe5, 0x89, 0x8d]); // '前' 的前 2 字节被截断的场景模拟
console.log(JSON.stringify(decoder.write(chunk1))); // 空字符串，缓冲到下一块
```
