---
title: [H5-032] ArrayBuffer、TypedArray、DataView 的关系？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-032：ArrayBuffer、TypedArray、DataView 的关系？
**答**：
- ArrayBuffer 是固定长度的原始内存块，不能直接读写；视图决定如何解释这些字节。
- TypedArray（Uint8Array/Float32Array 等）：定长、同类型元素的视图，适合像素、音频采样等规则数据。
- DataView：支持任意偏移、任意字节序的读写，适合解析网络协议、文件头等不规则二进制。
- 注意 Uint8ClampedArray（canvas ImageData 用它，越界值钳制到 0~255）；字节序默认本机序，跨端协议用 DataView 显式指定。

```javascript
// ArrayBuffer 是裸内存，必须通过视图访问
const buffer = new ArrayBuffer(16); // 16 字节

// TypedArray：按类型解读同一块内存
const u8 = new Uint8Array(buffer);
const i32 = new Int32Array(buffer);
console.log(u8.length, i32.length); // 16 与 4：同一块内存的不同解读粒度

i32[0] = 0x12345678; // 写入 4 字节
console.log(u8[0].toString(16)); // 78（小端机器上低位在前）

// DataView：精确控制偏移与字节序，用于二进制协议解析
const view = new DataView(buffer);
view.setUint32(0, 0x12345678, false); // false = 大端序（网络字节序）
console.log(view.getUint8(0).toString(16)); // 12：大端高位在前

// 实战：解析一个 PNG 文件头，验证 8 字节签名
async function checkPngHeader(file) {
  const head = new Uint8Array(await file.slice(0, 8).arrayBuffer());
  const pngSig = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
  return pngSig.every((byte, i) => head[i] === byte);
}
```
