---
title: [AV-353] 视频硬解 vs 软解的性能边界
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-353：视频硬解 vs 软解的性能边界

**答**：
- 硬解：功耗低性能高，但受编解码器支持限制（AV1 硬解覆盖率 2024~50%）。
- 软解：任何编码都行，但 1080p60 软解 AV1 需 4 核满载——移动端不可行。
- 探测：navigator.mediaCapabilities.decodingInfo 精确查询（含功耗/powerEfficient）。

```javascript
// 解码能力探测
async function decodeCapable(config) {
  const r = await navigator.mediaCapabilities.decodingInfo({
    type: 'file',
    video: { contentType: config.mime, width: config.w,
      height: config.h, bitrate: config.kbps * 1000, framerate: config.fps },
  });
  return { supported: r.supported,
    smooth: r.smooth, efficient: r.powerEfficient,
    decision: r.smooth && r.powerEfficient ? '硬解可用'
      : r.smooth ? '可播但耗电（软解风险）' : '不支持' };
}
```
