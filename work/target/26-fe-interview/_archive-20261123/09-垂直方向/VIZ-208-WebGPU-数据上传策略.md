---
title: [VIZ-208] WebGPU 数据上传策略：writeBuffer、mapAsync 与 ring buffer
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-208：WebGPU 数据上传策略：writeBuffer、mapAsync 与 ring buffer

**答**：
- 每帧更新顶点数据的三种方式：writeBuffer（队列拷贝，简单）、mapAsync（CPU 写映射，零拷贝）、ring buffer（N 帧轮转避免 CPU-GPU 同步阻塞）。
- 同步陷阱：writeBuffer 到「正在被上一帧读取」的 buffer 会强制 GPU 等待——ring buffer 每帧用不同区段规避。
- 量化：ring buffer 3 帧轮转可消除数据上传造成的帧间等待。

```javascript
class RingBuffer {
  constructor(device, byteSize, frames = 3) {
    this.device = device;
    this.buf = device.createBuffer({ size: byteSize * frames,
      usage: GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST });
    this.frameSize = byteSize; this.frame = 0;
  }
  write(data) {                                          // 每帧写不同区段
    const offset = this.frame * this.frameSize;
    this.device.queue.writeBuffer(this.buf, offset, data);
    this.frame = (this.frame + 1) % 3;
    return offset;                                       // 渲染时 bind 带 offset
  }
}
// 无 ring：第 N 帧写与第 N-1 帧读同 buffer → GPU 强制串行 → 帧率腰斩
// ring 3 帧：写与读永不同区段 → CPU/GPU 流水线并行
```
