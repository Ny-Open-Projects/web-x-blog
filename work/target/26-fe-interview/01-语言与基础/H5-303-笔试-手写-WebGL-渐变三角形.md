---
title: [H5-303] 笔试：手写 WebGL 渐变三角形
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, WebGL]
type: 笔试题
---

## H5-303：笔试：手写 WebGL 渐变三角形

**题目**：用 WebGL 原生 API 画一个三顶点颜色分别为红/绿/蓝的渐变三角形（顶点色插值）。要求完整可运行：着色器编译、缓冲、attribute、draw。

**答**：
```javascript
const canvas = document.createElement('canvas');
document.body.appendChild(canvas);
const gl = canvas.getContext('webgl');

function makeShader(type, src) {
  const s = gl.createShader(type);
  gl.shaderSource(s, src);
  gl.compileShader(s);
  if (!gl.getShaderParameter(s, gl.COMPILE_STATUS))
    throw new Error(gl.getShaderInfoLog(s));
  return s;
}
const prog = gl.createProgram();
gl.attachShader(prog, makeShader(gl.VERTEX_SHADER, `
  attribute vec3 aPos; attribute vec3 aColor;
  varying vec3 vColor;
  void main() { gl_Position = vec4(aPos, 1.0); vColor = aColor; }`));
gl.attachShader(prog, makeShader(gl.FRAGMENT_SHADER, `
  precision mediump float;
  varying vec3 vColor;
  void main() { gl_FragColor = vec4(vColor, 1.0); }`));
gl.linkProgram(prog);
gl.useProgram(prog);

function buffer(data) {
  const b = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, b);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(data), gl.STATIC_DRAW);
  return b;
}
const posLoc = gl.getAttribLocation(prog, 'aPos');
gl.bindBuffer(gl.ARRAY_BUFFER, buffer([0, .8, 0,  -.8, -.6, 0,  .8, -.6, 0]));
gl.enableVertexAttribArray(posLoc);
gl.vertexAttribPointer(posLoc, 3, gl.FLOAT, false, 0, 0);

const colLoc = gl.getAttribLocation(prog, 'aColor');
gl.bindBuffer(gl.ARRAY_BUFFER, buffer([1,0,0,  0,1,0,  0,0,1]));
gl.enableVertexAttribArray(colLoc);
gl.vertexAttribPointer(colLoc, 3, gl.FLOAT, false, 0, 0);

gl.drawArrays(gl.TRIANGLES, 0, 3); // varying 插值产生渐变
```

**评分点**：
- 着色器编译错误检查（getShaderParameter）体现工程性
- varying 声明在两个着色器中一致——插值的载体
- 两个 attribute 各自 bindBuffer + vertexAttribPointer（buffer 切换顺序不能错）
- precision mediump float 在片元着色器必写（WebGL1 要求）
