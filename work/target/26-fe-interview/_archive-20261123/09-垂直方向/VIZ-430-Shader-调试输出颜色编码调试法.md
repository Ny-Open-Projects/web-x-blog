---
title: [VIZ-430] Shader 调试输出：颜色编码调试法
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-430：Shader 调试输出：颜色编码调试法

**答**：
- 技巧：把中间值编码为颜色输出（正=红绿、负=蓝、NaN=品红）逐 pass 检查。
- 常用：法线可视化（N*0.5+0.5）、UV 可视化（fract）、深度线性化灰度。
- 纪律：调试 uniform 开关（uDebugMode）而非注释代码；发布前移除。

```javascript
// 调试视图
`uniform int uDebugMode;
vec4 debugOut(vec3 N, vec2 uv, float depthLinear) {
  if (uDebugMode == 1) return vec4(N * 0.5 + 0.5, 1.0);       // 法线
  if (uDebugMode == 2) return vec4(fract(uv * 8.0), 0, 1);    // UV 网格
  if (uDebugMode == 3) return vec4(vec3(depthLinear / uFar), 1); // 深度
  return vec4(-1);   // 未知模式
}`
```
