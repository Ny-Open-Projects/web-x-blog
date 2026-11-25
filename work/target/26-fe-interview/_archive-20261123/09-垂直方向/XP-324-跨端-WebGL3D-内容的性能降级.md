---
title: [XP-324] 跨端 WebGL/3D 内容的性能降级
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-324：跨端 WebGL/3D 内容的性能降级

**答**：
- 场景：3D 展示页在低端机必卡——档位化（模型精度/纹理尺寸/抗锯齿）。
- 探测：WebGL 上下文参数（MAX_TEXTURE_SIZE/渲染器字符串）判档。
- 兜底：WebGL 不可用 -> 静态图片轮播。

```javascript
// 3D 档位
function glTier(gl) {
  const mem = gl.getParameter(gl.MAX_TEXTURE_SIZE);
  const renderer = gl.getExtension('WEBGL_debug_renderer_info')
    ?.getParameter(gl.UNMASKED_RENDERER_WEBGL) ?? '';
  const low = /Mali-G5|Adreno 5|PowerVR/.test(renderer) || mem <= 2048;
  return { tier: low ? 'L0' : 'L1',
    config: low ? { texScale: 0.5, aa: false, shadows: false }
      : { texScale: 1, aa: true, shadows: true } };
}
```
