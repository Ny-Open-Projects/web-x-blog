---
title: [H5-210] WebGL 纹理贴图的最小流程是什么
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-210：WebGL 纹理贴图的最小流程是什么

**答**：
- 流程：创建纹理 → 上传图像（texImage2D）→ 设置采样参数（过滤/环绕）→ 片元着色器里 texture2D 采样
- 图片必须加载完成才能上传；跨域图片需要 CORS 否则画布污染（同 Canvas 2D）
- 常见坑：图片尺寸非 2 的幂在 WebGL1 需要 CLAMP_TO_EDGE + 非 mipmap 过滤；翻转问题（UNPACK_FLIP_Y_WEBGL）——图片 y 轴与纹理 v 轴相反
- mipmap：远处的纹理采样低分辨率层级，防摩尔纹，但要求尺寸为 2 的幂（WebGL1）
- 钩子：纹理上传是异步总线拷贝，大纹理首次上传会掉帧，可用 KTX 压缩纹理优化

```javascript
const tex = gl.createTexture();
gl.bindTexture(gl.TEXTURE_2D, tex);
gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true); // 图片与纹理坐标对齐
gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, img);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); // 非2幂必须线性过滤
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
```
