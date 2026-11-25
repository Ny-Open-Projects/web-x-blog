---
title: [VIZ-206] WebGPU 性能方法论：时间戳查询与帧预算分析
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-206：WebGPU 性能方法论：时间戳查询与帧预算分析

**答**：
- timestamp-query 特性：GPU 侧计时（pass 起止时间戳），定位瓶颈在哪个 pass（VS/FS/混合）。
- 帧预算：60fps = 16.7ms，GPU 占用建议 < 12ms（留 JS 与合成）；超预算手段：降分辨率渲染（renderScale）+ 上采样。
- 瓶颈判定：draw call 多 → 合批；fillrate 高 → 降分辨率/简化片元；带宽高 → 减纹理采样。

```javascript
if (device.features.has('timestamp-query')) {
  const querySet = device.createQuerySet({ type: 'timestamp', count: 4 });
  pass.writeTimestamp(querySet, 0);                      // pass 开始
  // ... 绘制
  pass.writeTimestamp(querySet, 1);                      // pass 结束
  // resolve 到 buffer → mapAsync 读取 → diff = GPU 耗时（纳秒）
}
// 超预算降级链：renderScale 0.5 渲染 → CSS/canvas 上采样 → 视觉略糊但帧率稳
// 瓶颈判定表：GPU 时间戳高 + CPU 空闲 → GPU bound（降 fillrate）；反之 CPU bound（合批/减编码）
```
