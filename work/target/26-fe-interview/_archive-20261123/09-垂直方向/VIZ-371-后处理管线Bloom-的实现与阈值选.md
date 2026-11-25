---
title: [VIZ-371] 后处理管线：Bloom 的实现与阈值选择
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-371：后处理管线：Bloom 的实现与阈值选择

**答**：
- Bloom：提取高亮（> 阈值）→ 降采样模糊（多级 mip 链）→ 叠加回原图。
- 阈值：HDR 下用 soft knee（软阈值过渡），避免硬边；经验值 1.0~1.5（HDR 空间）。
- 成本：多级降采样模糊 ≈ 全屏 3~4 次纹理采样带宽，移动端用半分辨率。

```javascript
// Bloom 管线（伪代码）
function bloom(sceneHDR, { threshold = 1.2, knee = 0.5 } = {}) {
  const bright = sceneHDR.map(px => {
    const l = luminance(px);
    const soft = clamp(l - threshold + knee, 0, 2 * knee) / (2 * knee);
    const w = Math.max(soft * soft, l > threshold ? 1 : 0) * l / (l || 1);
    return px.map(c => c * w);                       // 提取亮部
  });
  const mips = downsampleChain(bright, 5);           // 5 级降采样
  return upsampleBlurAdd(sceneHDR, mips);            // 逐级上采叠加
}
function luminance([r, g, b]) { return 0.2126*r + 0.7152*g + 0.0722*b; }
function clamp(v, a, b) { return Math.min(b, Math.max(a, v)); }
```
