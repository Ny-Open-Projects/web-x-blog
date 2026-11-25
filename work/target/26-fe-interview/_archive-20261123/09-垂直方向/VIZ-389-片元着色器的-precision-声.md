---
title: [VIZ-389] 片元着色器的 precision 声明为什么重要
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-389：片元着色器的 precision 声明为什么重要

**答**：
- 移动端默认 mediump（16bit float）——UV/位置计算精度不足导致条纹与错位。
- 规范：片元头部 precision highp float（高端）或按需 mediump（低端性能）；位置类一律 highp。
- 检测：gl.getShaderPrecisionFormat 查询设备支持；老设备 highp 片元可能不可用。

```javascript
// 精度探测与降级
function fragPrecision(gl) {
  const f = gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.HIGH_FLOAT);
  return { highpSupported: f.precision > 0, rangeMin: f.rangeMin };
}
// 模板：
// #ifdef GL_FRAGMENT_PRECISION_HIGH
// precision highp float;
// #else
// precision mediump float;
// #endif
```
