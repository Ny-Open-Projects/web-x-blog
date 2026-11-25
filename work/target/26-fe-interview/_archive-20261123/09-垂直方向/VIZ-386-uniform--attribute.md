---
title: [VIZ-386] uniform / attribute / varying 的作用域与限制
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-386：uniform / attribute / varying 的作用域与限制

**答**：
- attribute（in）：每顶点数据，来自 buffer；uniform：全局常量，每次 draw 前设置；varying（in/out）：顶点到片元插值。
- 数量限制：WebGL2 至少 256 个 vec4 uniform、16 个 attribute、16 个 texture unit——超限报错或静默失败。
- 优化：相关 uniform 打包成 struct/block（UBO 共享跨 program），减少 setUniform 调用。

```javascript
// uniform 打包与限制探测
function probeLimits(gl) {
  return {
    maxVertexUniformVectors: gl.getParameter(gl.MAX_VERTEX_UNIFORM_VECTORS),
    maxFragUniformVectors: gl.getParameter(gl.MAX_FRAGMENT_UNIFORM_VECTORS),
    maxAttributes: gl.getParameter(gl.MAX_VERTEX_ATTRIBS),
    maxTextures: gl.getParameter(gl.MAX_COMBINED_TEXTURE_IMAGE_UNITS),
  };
}
// UBO（WebGL2）：
// uniform Lights { vec4 pos[8]; vec4 color[8]; } uLights;
// 一次 bufferSubData 更新全部光源
```
