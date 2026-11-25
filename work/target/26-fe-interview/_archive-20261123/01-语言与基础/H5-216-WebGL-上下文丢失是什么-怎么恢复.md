---
title: [H5-216] WebGL 上下文丢失是什么，怎么恢复
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-216：WebGL 上下文丢失是什么，怎么恢复

**答**：
- 上下文丢失：GPU 驱动重置/内存压力下，浏览器强制回收 WebGL 上下文，所有缓冲、纹理、程序全部失效
- 触发原因：显存占用过大（多 tab 开 3D 页面）、驱动崩溃、移动端系统回收
- 监听与恢复：`webglcontextlost`（preventDefault 表示愿意处理）→ 重建所有 GPU 资源 → `webglcontextrestored` 里重新初始化
- 工程要求：3D 应用的初始化必须写成可重入函数（丢失后可完整重跑），资源加载要有缓存
- 预防：限制纹理尺寸、及时 deleteBuffer/deleteTexture、后台 tab 暂停渲染

```javascript
canvas.addEventListener('webglcontextlost', (e) => {
  e.preventDefault(); // 声明我们会处理
  pauseRendering();
});
canvas.addEventListener('webglcontextrestored', () => {
  initGL();   // 重新编译着色器/建缓冲/上传纹理
  resumeRendering();
});
```
