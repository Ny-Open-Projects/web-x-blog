---
title: [VIZ-452] GC 抖动的图形侧专项：Buffer/Texture 复用
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-452：GC 抖动的图形侧专项：Buffer/Texture 复用

**答**：
- 问题：每帧 create/deleteBuffer、new Float32Array 触发 GC 与驱动开销。
- 对策：buffer 池（复用同尺寸）、scratch 数组模块级缓存、WebGL 对象生命周期管理（引用计数）。
- 验证：Memory 面板无锯齿 + Performance 无周期性 GC 块。

```javascript
// GPU 资源池
class GLPool {
  constructor(gl) { this.gl = gl; this.free = new Map(); }
  getBuffer(size) {
    const pool = this.free.get(size) ?? [];
    const buf = pool.pop() ?? this.gl.createBuffer();
    return buf;
  }
  releaseBuffer(size, buf) {
    const pool = this.free.get(size) ?? [];
    if (pool.length < 32) pool.push(buf);            // 上限防泄漏
    this.free.set(size, pool);
  }
}
```
