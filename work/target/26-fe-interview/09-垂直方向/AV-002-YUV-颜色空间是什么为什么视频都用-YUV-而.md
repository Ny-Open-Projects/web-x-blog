---
title: [AV-002] YUV 颜色空间是什么？为什么视频都用 YUV 而不用 RGB？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-002：YUV 颜色空间是什么？为什么视频都用 YUV 而不用 RGB？
**答**：
- YUV 把颜色拆成亮度 Y 和色度 U/V，人眼对亮度敏感、对色度不敏感，可对色度做下采样（4:2:0 最常见）。
- 4:2:0 表示每 4 个亮度像素共享 1 组 UV，数据量是 RGB888 的 1.5/4 ≈ 37.5%，是 H264/VP9 标准输入格式。
- YUV 与 RGB 需要矩阵转换（BT.601/709 系数不同），前端在 Canvas/WebGL 渲染解码帧时必须处理。
- 兼容性问题高频：黑白/偏绿画面通常是 YUV 转 RGB 矩阵用错（601 当 709 用）或 UV 通道错位。

```javascript
// YUV420p 转 RGB 的核心公式（BT.601），前端 WebGL 渲染解码帧时常用
function yuv420ToRgb(y, u, v) {
  // 输入 0-255
  const yy = y - 16, uu = u - 128, vv = v - 128;
  const r = 1.164 * yy + 1.596 * vv;
  const g = 1.164 * yy - 0.392 * uu - 0.813 * vv;
  const b = 1.164 * yy + 2.017 * uu;
  const clamp = (x) => Math.max(0, Math.min(255, Math.round(x)));
  return [clamp(r), clamp(g), clamp(b)];
}
console.log(yuv420ToRgb(235, 128, 128)); // 近似白色

// WebGL 渲染 YUV 的经典做法：三分纹理 + fragment shader 矩阵转换
const FRAG_SHADER = `
  precision mediump float;
  varying vec2 v_texCoord;
  uniform sampler2D u_y;
  uniform sampler2D u_u;
  uniform sampler2D u_v;
  void main() {
    float y = texture2D(u_y, v_texCoord).r;
    float u = texture2D(u_u, v_texCoord).r - 0.5;
    float v = texture2D(u_v, v_texCoord).r - 0.5;
    vec3 rgb = vec3(y + 1.402 * v,
                    y - 0.344 * u - 0.714 * v,
                    y + 1.772 * u);
    gl_FragColor = vec4(rgb, 1.0);
  }
`;
```
