---
title: [H5-304] 笔试：手写 WebGL 纹理加载渲染最小代码
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, WebGL]
type: 笔试题
---

## H5-304：笔试：手写 WebGL 纹理加载渲染最小代码

**题目**：实现 `drawTexture(canvas, imgSrc)`：加载图片为纹理，绘制一个铺满画布的矩形（两个三角形），片元着色器采样纹理。要求处理图片 y 轴翻转与跨域。

**答**：
```javascript
async function drawTexture(canvas, imgSrc) {
  const gl = canvas.getContext('webgl');
  const img = new Image();
  img.crossOrigin = 'anonymous';
  img.src = imgSrc;
  await new Promise(r => img.onload = r);

  // 最小着色器
  const src = {
    v: `attribute vec2 p; varying vec2 uv;
        void main(){ gl_Position=vec4(p,0.,1.); uv=(p+1.)/2.; }`,
    f: `precision mediump float; varying vec2 uv; uniform sampler2D tex;
        void main(){ gl_FragColor=texture2D(tex, uv); }`,
  };
  function shader(t, s) { const sh = gl.createShader(t); gl.shaderSource(sh, s); gl.compileShader(sh); return sh; }
  const prog = gl.createProgram();
  gl.attachShader(prog, shader(gl.VERTEX_SHADER, src.v));
  gl.attachShader(prog, shader(gl.FRAGMENT_SHADER, src.f));
  gl.linkProgram(prog); gl.useProgram(prog);

  const buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 1,-1, -1,1, 1,1]), gl.STATIC_DRAW);
  const loc = gl.getAttribLocation(prog, 'p');
  gl.enableVertexAttribArray(loc);
  gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);

  const tex = gl.createTexture();
  gl.bindTexture(gl.TEXTURE_2D, tex);
  gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true);      // y 轴翻转
  gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, img);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); // 非2幂必需
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
  gl.uniform1i(gl.getUniformLocation(prog, 'tex'), 0);

  gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4); // 条带画矩形
}
```

**评分点**：
- UNPACK_FLIP_Y_WEBGL 翻转处理（图片与纹理 v 轴方向相反）
- 非 2 的幂尺寸必须 LINEAR 过滤 + CLAMP_TO_EDGE（WebGL1）
- uv 由顶点坐标推导 `(p+1)/2`，省一个 uv attribute
- TRIANGLE_STRIP 四顶点画矩形（比 TRIANGLES 六顶点省）

## 变体与延伸（补充）

**变体与延伸**：

1. 换成 WebGL2 要改什么？ → `texture2D`/`gl_FragColor` 改为 `texture()` 与 `out` 变量声明；NPOT 限制消失，但 CLAMP_TO_EDGE 仍建议保留，避免边缘采样越界。
2. 一次画多张纹理怎么做？ → 每张图绑定到不同纹理单元：`gl.activeTexture(gl.TEXTURE0 + i)` 后 `uniform1i(sampler, i)`，片元着色器里按 uv 分段采样或混合。
3. 4K 大图首帧卡顿怎么解？ → 用 `createImageBitmap` 在 Worker 里解码，主线程只做 `texImage2D` 上传；同时生成 mipmap，否则缩小显示时会出现严重摩尔纹。
