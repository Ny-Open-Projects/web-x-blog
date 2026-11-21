---
title: [H5-086] DataView 处理字节序为什么是网络二进制协议的标配？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-086：DataView 处理字节序为什么是网络二进制协议的标配？
**答**：
- `ArrayBuffer` 是"无类型的字节内存"，`TypedArray`（Uint8/Int16/Float32…）按**本机字节序**解释，`DataView` 可**逐字段指定** `littleEndian` 参数。
- 网络协议与文件格式（BMP、MP4 box、Protobuf）通常规定**大端**（网络字节序），而 x86/ARM JS 引擎本机是小端——必须显式传 `false`，否则跨平台数值错乱。
- `getUint16/getInt32/getFloat64(offset, littleEndian)` 读，`setXxx` 写；逐字段偏移寻址，适合"变长头部 + 多字段"的二进制解析。
- `TypedArray` 的隐藏坑：`new Uint16Array(buffer)` 视图按小端解释，另一台设备写入的大端数据直接读出垃圾值；同理 `Float32Array` 不能跨端二进制交换。
- 实战组合：DataView 解析头部结构 → 切出 payload 区间再交给对应 TypedArray 处理。

```javascript
// 模拟一个二进制协议帧：[magic 2B 大端][version 1B][length 4B 大端][payload]
const packet = new Uint8Array([
  0xAB, 0xCD,                  // magic 0xABCD
  0x02,                        // version
  0x00, 0x00, 0x00, 0x05,      // length = 5（大端）
  0x68, 0x65, 0x6C, 0x6C, 0x6F // "hello"
]);

// 1) DataView 逐字段解析，显式声明大端
const dv = new DataView(packet.buffer);
const magic = dv.getUint16(0, false);        // false = 大端
const version = dv.getUint8(2);
const length = dv.getUint32(3, false);
console.log(magic.toString(16), version, length); // "abcd" 2 5

// 2) payload 切给 TypedArray：纯字节内容无需关心字节序
const payload = packet.subarray(7, 7 + length);
console.log(new TextDecoder().decode(payload));   // "hello"

// 3) 序列化：写回时同样指定大端
function encode(magic, version, payload) {
  const buf = new ArrayBuffer(7 + payload.length);
  const out = new DataView(buf);
  out.setUint16(0, magic, false);
  out.setUint8(2, version);
  out.setUint32(3, payload.length, false);
  new Uint8Array(buf, 7).set(payload);
  return new Uint8Array(buf);
}
const frame = encode(0xABCD, 2, new TextEncoder().encode('ok'));

// 4) 反例：TypedArray 按本机（小端）解释，大端数据读出垃圾
console.log(new Uint16Array(packet.buffer)[0].toString(16)); // "cdab" 错乱
```
