---
title: [NODE-222] 高水位线的选择策略？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-222：高水位线的选择策略？
**答**：
- highWaterMark 是缓冲阈值：默认 64KB（字节流）/16（对象流）。太小：切换频繁（_read 调用多、syscall 开销）；太大：内存占用高（积压数据）、延迟增加。
- 选择原则：吞吐优先（本地文件复制）可加大（256KB~1MB）；延迟优先（实时流/代理）压小（16~32KB）；对象流看单对象成本。
- 实测方法：clinic/heap diff 观察缓冲占用，autocannon 对比 P95——水位线是可量化的调优参数（NODE-083）。
- 特殊场景：子进程 stdio（NODE-24x）与网络流的默认值不同；多级 pipeline 的水位线是各段独立累积的（链越长缓冲越多）。

```javascript
// 吞吐型：大文件复制
createReadStream(src, { highWaterMark: 1024 * 1024 })     // 1MB：减少 syscall
  .pipe(createWriteStream(dst, { highWaterMark: 1024 * 1024 }));
// 延迟型：SSE 代理
createReadStream(tail, { highWaterMark: 16 * 1024 })      // 16KB：低延迟优先
// 验证：进程 RSS 与 P95 的权衡曲线
// pipeline 多级缓冲：64KB × 4 段 ≈ 256KB 内在缓冲，链长时按段评估
```
