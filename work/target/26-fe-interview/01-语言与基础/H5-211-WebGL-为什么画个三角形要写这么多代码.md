---
title: [H5-211] WebGL 为什么画个三角形要写这么多代码
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-211：WebGL 为什么画个三角形要写这么多代码

**答**：
- WebGL 是「GPU 的汇编接口」：它不封装任何绘制逻辑，只提供原始管道，灵活性最大、样板代码也最多
- 样板四件套：着色器编译链接（GPU 程序装载）、缓冲区管理（数据上传）、attribute 关联（数据与着色器对接）、状态机设置（WebGL 是全局状态机，所有调用都是改状态）
- 封装层的价值：three.js/PixiJS 做的就是把这些样板收敛为场景对象；理解原生流程才能看懂它们的 API 设计
- 面试话术：答「状态机 + 无固定管线」两个词，比抱怨「代码多」高一个档次

```javascript
// WebGL 全局状态机：绑定即切换上下文
gl.bindBuffer(gl.ARRAY_BUFFER, bufA);   // 之后所有 buffer 操作都作用于 bufA
gl.vertexAttribPointer(locA, ...);      // 指向当前绑定的 buffer
gl.bindBuffer(gl.ARRAY_BUFFER, bufB);   // 切换状态
gl.vertexAttribPointer(locB, ...);
// 每帧 draw 前都要恢复需要的状态——three.js 内部就在做这种状态管理
```
