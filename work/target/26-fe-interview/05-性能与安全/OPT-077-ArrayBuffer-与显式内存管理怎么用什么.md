---
title: [OPT-077] ArrayBuffer 与显式内存管理怎么用？什么场景值得？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-077：ArrayBuffer 与显式内存管理怎么用？什么场景值得？

**答**：
- `ArrayBuffer` 是固定长度的原始字节块，分配后长度不可变、无 GC 对象头开销，配合 `TypedArray/DataView` 读写，内存占用比对象数组低数倍。
- 典型收益：10 万个 {x,y,z} 对象数组约几十 MB 且分散在堆上；Float32Array 同数据量内存减半以上且内存连续，遍历对缓存友好，还能 Transferable 零拷贝传给 Worker。
- 显式管理：`ArrayBuffer.prototype.transfer()`（转移所有权，原引用即失效）与 `postMessage(buf, [buf])` 零拷贝转移，避免克隆造成的双倍峰值内存。
- 注意溢出：TypedArray 越界赋值静默忽略（不报错），用 DataView 或断言保护关键写入；释放只是"可回收"，峰值内存仍需自己控制分块。

```javascript
// 一一对应：对象数组 -> TypedArray 的迁移与零拷贝转移
// 原始：10 万个粒子对象
const particles = Array.from({ length: 100_000 }, () => ({
  x: Math.random(), y: Math.random(), z: Math.random(),
}));
// 坐标一批次更新后传 Worker：postMessage 默认深克隆，峰值内存翻倍

// 优化一：SoA 结构，一个 Float32Array 装全部坐标
const STRIDE = 3;
const buf = new ArrayBuffer(100_000 * STRIDE * 4); // 4 字节/float，约 1.2MB
const pos = new Float32Array(buf);
particles.forEach((p, i) => { pos[i * 3] = p.x; pos[i * 3 + 1] = p.y; pos[i * 3 + 2] = p.z; });

// 优化二：Transferable 零拷贝转移所有权，无克隆、无双倍峰值
worker.postMessage(pos, [pos.buffer]); // 注意：转移后本线程的 pos 不可再读写
// Worker 回传同理：self.postMessage(result, [result.buffer])

// 优化三：transfer() 管理所有权（不可转移给 Worker 时同线程转移引用）
const newBuf = buf.transfer(); // buf 此后 detached，长度 0，防止误用旧引用
console.log(buf.byteLength);   // 0

// 越界保护：TypedArray 越界写入静默失败
const small = new Uint8Array(2);
small[5] = 9;
console.log(small[5]); // undefined 风格 -> 实际输出 undefined（写入被丢弃）
function safeSet(arr, i, v) {
  if (i < 0 || i >= arr.length) throw new RangeError(`index ${i} out of ${arr.length}`);
  arr[i] = v;
}
```
