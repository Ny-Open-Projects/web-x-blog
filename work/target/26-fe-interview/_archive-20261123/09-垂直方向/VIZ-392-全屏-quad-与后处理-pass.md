---
title: [VIZ-392] 全屏 quad 与后处理 pass 的标准写法
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-392：全屏 quad 与后处理 pass 的标准写法

**答**：
- 后处理标准流程：全屏三角形（3 顶点大三角优于 quad）+ 各后处理链依次处理。
- 不再需要 vertex buffer：用 gl_VertexID 生成（WebGL2）顶点位置。
- 链式管理：pass 数组依次执行，中间结果 ping-pong 双 FBO 复用（避免分配）。

```javascript
// 全屏三角形（WebGL2）
const FULLSCREEN_VS = `#version 300 es
out vec2 vUV;
void main() {
  vec2 p = vec2((gl_VertexID << 1) & 2, gl_VertexID & 2);
  vUV = p;
  gl_Position = vec4(p * 2.0 - 1.0, 0.0, 1.0);
}`;
// ping-pong：
function pingPong(fboA, fboB, passes) {
  let src = fboA, dst = fboB;
  for (const pass of passes) {
    gl.bindFramebuffer(gl.FRAMEBUFFER, dst.fb);
    pass.run(src.tex);
    [src, dst] = [dst, src];               // 交换
  }
  return src;
}
```
