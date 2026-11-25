---
title: [VIZ-022] 描述 WebGL 的渲染管线，一次 draw 调用经历了什么？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-022：描述 WebGL 的渲染管线，一次 draw 调用经历了什么？
**答**：管线流程：JS 提交顶点缓冲 → **顶点着色器**（每个顶点执行一次，算出裁剪空间坐标）→ **图元装配**（顶点组装成点/线/三角形）→ **裁剪与透视除法** → **光栅化**（图元离散成片元，varying 在此插值）→ **片元着色器**（每个片元执行一次，算颜色）→ **逐片元操作**（深度测试、模板测试、混合）→ 写入帧缓冲。核心心智模型：CPU 只负责喂数据 + 一次 `drawArrays/drawElements`，剩下全是 GPU 并行，这就是它比 Canvas 快的根源。

```mermaid
flowchart LR
    A[顶点数据 Buffer] --> B[顶点着色器]
    B --> C[图元装配]
    C --> D[光栅化 varying 插值]
    D --> E[片元着色器]
    E --> F[深度与模板测试]
    F --> G[混合 Blend]
    G --> H[帧缓冲 Framebuffer]
```

```javascript
const gl = canvas.getContext('webgl');
const compile = (g, type, src) => {
  const s = g.createShader(type);
  g.shaderSource(s, src); g.compileShader(s);
  if (!g.getShaderParameter(s, g.COMPILE_STATUS)) throw new Error(g.getShaderInfoLog(s));
  return s;
};
function createProgram(g, vsSrc, fsSrc) {
  const p = g.createProgram();
  g.attachShader(p, compile(g, g.VERTEX_SHADER, vsSrc));
  g.attachShader(p, compile(g, g.FRAGMENT_SHADER, fsSrc));
  g.linkProgram(p);
  return p;
}
// 一帧 = clearColor + clear -> useProgram -> 绑定 VBO/设置 attribute -> drawArrays
// CPU 只提交数据与一次 draw，其余全部在 GPU 并行执行
```
