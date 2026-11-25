---
title: [VIZ-301] 手写 WebGPU 点云渲染器：百万点分级管线（笔试）
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-301：手写 WebGPU 点云渲染器：百万点分级管线（笔试）

**答**：
- 题目：完整实现百万点云渲染器：数据分块上传、实例化绘制、LOD 三档、拾取 ID pass。给出核心代码框架。
- 思路：分块 buffer（每 10 万一个，增量上传）；LOD 按相机距离切档（全量/抽样/网格聚合）；ID pass 独立纹理拾取。
- 评分点：分块上传；LOD 切档防抖；拾取 readback 单像素。

```javascript
class PointCloudRenderer {
  constructor(device, canvas) {
    this.device = device; this.chunks = [];                 // 数据分块
    this.camera = { pos: [0, 0, 10], fov: 60 };
    this.lod = 0;
  }
  upload(points) {                                          // 分块上传
    const CHUNK = 100000;
    for (let i = 0; i < points.length; i += CHUNK) {
      const data = points.slice(i, i + CHUNK);
      const buf = this.device.createBuffer({ size: data.length * 16,
        usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_DST });
      this.device.queue.writeBuffer(buf, 0, packInstances(data));
      this.chunks.push({ buf, count: data.length });
    }
  }
  frame(zoom) {                                             // LOD 切档（防抖 200ms）
    const target = zoom > 8 ? 0 : zoom > 3 ? 1 : 2;
    if (target !== this.lod && !this.lodTimer) {
      this.lodTimer = setTimeout(() => { this.lod = target; this.lodTimer = null; }, 200);
      return;                                              // 防抖期不切
    }
    const step = this.lod === 0 ? 1 : this.lod === 1 ? 4 : 16;   // 抽样步长
    const pass = encoder.beginRenderPass({ colorAttachments: [{ view, loadOp: 'clear',
      storeOp: 'store' }] });
    for (const chunk of this.chunks) {
      pass.setBindGroup(0, bindGroup(chunk.buf));
      pass.draw(6, Math.ceil(chunk.count / step));          // 实例化
    }
    pass.end();
  }
  pick(x, y) {                                              // ID pass 单像素回读
    return readIdPixel(this.device, this.idTexture, x, y);   // 复用 VIZ-209
  }
}
```
