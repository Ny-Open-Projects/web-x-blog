---
title: [VIZ-410] 渲染目标格式选择：RGBA8 vs RGBA16F vs RGB10A2
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-410：渲染目标格式选择：RGBA8 vs RGBA16F vs RGB10A2

**答**：
- RGBA8：LDR 输出；RGBA16F：HDR + 精度（后处理链标准）；RGB10A2：色域够精度省内存（G-Buffer albedo）。
- 带宽账：4K RGBA16F 单 pass 读写 ≈ 66MB——后处理链长时优先低精度中间格式。
- 兼容：EXT_color_buffer_float 支持 RGBA16F 渲染（WebGL2 必查）；不支持降级 RGBA8+编码。

```javascript
// 格式选择器
function pickRT(gl, { hdr = true, bandwidthTight = false } = {}) {
  const floatOK = gl.getExtension('EXT_color_buffer_float');
  if (hdr && floatOK && !bandwidthTight) return 'RGBA16F';
  if (hdr && floatOK && bandwidthTight) return 'R11F_G11F_B10F';  // 无 alpha 更省
  return 'RGBA8';
}
// 带宽估算：4K×(16F=8B)×2 ≈ 132MB/帧；R11G11B10 = 6B -> 100MB
```
