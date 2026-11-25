---
title: [VIZ-396] storage buffer vs uniform buffer 的选择
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-396：storage buffer vs uniform buffer 的选择

**答**：
- uniform：只读、容量小（64KB）、访问快；storage：读写、大容量（128MB+）、稍慢。
- 数据方向：每帧更新（相机/光源）用 uniform 写优化；大数据（顶点数据集/结果输出）用 storage。
- WebGPU 差异：storage read_only 可与采样并行；read_write 需注意 race（同组内 barrier）。

```javascript
// 类型选择表
const BUFFER_CHOICE = {
  'camera':   { type: 'uniform', size: '64B',  update: '每帧' },
  'lights':   { type: 'uniform', size: '<64KB', update: '低频' },
  'particles':{ type: 'storage', size: '10万×32B', update: 'GPU 内更新' },
  'pickResult':{ type: 'storage-read', size: '小', update: 'GPU 写 CPU 读' },
};
```
