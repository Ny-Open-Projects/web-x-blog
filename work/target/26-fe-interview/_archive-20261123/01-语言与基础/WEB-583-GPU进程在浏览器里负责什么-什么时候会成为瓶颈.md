---
title: [WEB-583] GPU 进程在浏览器里负责什么，什么时候成为瓶颈
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 浏览器架构]
type: 面试题
---

## WEB-583：GPU 进程在浏览器里负责什么，什么时候成为瓶颈

**答**：
- GPU 进程是独立进程，负责：所有合成与光栅化（软件/硬件加速）、WebGL/WebGPU 指令转发、视频解码（部分平台）、Canvas2D 加速
- 它是全浏览器共享的：所有 tab 的 GPU 任务排队进同一进程，一个页面的疯狂 WebGL 渲染会拖慢其他页面动画——这就是「卡顿跨页面传染」的机制
- 常见瓶颈场景：Canvas2D 大面积频繁重绘走 GPU 纹理上传；WebGL 上下文过多（每个 ~几十 MB 显存）触发 `webglcontextlost`；视频硬解码资源占满导致合成掉帧
- 排查入口：Chrome `chrome://gpu` 看加速是否开启/黑名单；`about://tracing` 里看 GPU 进程任务队列；开发者工具 Rendering 面板的 Paint flashing 粗定位
- 前端优化方向：减少强制合成层爆炸（层越多纹理上传越多）、WebGL 用 `powerPreference` 与上下文数控制、离屏渲染复用

```javascript
// WebGL 上下文丢失防护与恢复
const gl = canvas.getContext('webgl2', { powerPreference: 'high-performance' });
canvas.addEventListener('webglcontextlost', (e) => {
  e.preventDefault();               // 必须阻止默认行为才允许恢复
  setTimeout(() => canvas.addEventListener('webglcontextrestored', initGL, { once: true }), 0);
});
// 上下文数量: 同页 <8~16 个, 超出浏览器会丢最老的上下文
```
