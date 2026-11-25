---
title: [VIZ-376] 颜色拾取 vs ID 拾取的防伪细节
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-376：颜色拾取 vs ID 拾取的防伪细节

**答**：
- 颜色拾取会被抗锯齿/后处理污染——ID pass 必须关 AA、无后处理、清屏为背景 ID。
- ID 编码：实例 ID -> RGB 通道（24bit 支持千万级）；读取时 +1 偏移避免 0 与清屏色混淆。
- 精度：readPixels 用 UNSIGNED_BYTE 足够；WebGPU 可用 storage buffer 直读。

```javascript
// ID 编解码
const BG_ID = 0;
function encodeId(id) {
  return [(id >> 16) & 255, (id >> 8) & 255, id & 255, 255];
}
function decodeId(px) {
  const id = (px[0] << 16) | (px[1] << 8) | px[2];
  return id === BG_ID ? null : id;                  // 背景返回 null
}
// ID pass 配置：gl.disable(gl.BLEND); gl.disable(gl.DITHER); AA off
```
