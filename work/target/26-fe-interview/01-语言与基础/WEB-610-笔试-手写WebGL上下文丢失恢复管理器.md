---
title: [WEB-610] 笔试：手写 WebGL 上下文丢失恢复管理器
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 浏览器架构]
type: 笔试题
---

## WEB-610：笔试：手写 WebGL 上下文丢失恢复管理器

**答**：实现 `GLContextManager`：① 创建 WebGL 上下文并注册丢失/恢复事件；② contextlost 时 preventDefault 声明可恢复，暂停渲染循环，状态进入 `lost`；③ contextrestored 后重建资源（重传纹理/重编 shader，通过注册的 initResources 回调），恢复渲染；④ 短时间多次丢失（30s 内 ≥3 次）判定 GPU 环境不可用，永久降级到 Canvas2D 回调 `onPermanentLoss`；⑤ 提供状态查询。写出核心实现。

```javascript
class GLContextManager {
  constructor(canvas, { initResources, onPermanentLoss } = {}) {
    this.canvas = canvas; this.initResources = initResources; this.onPermanentLoss = onPermanentLoss;
    this.lossTimes = []; this.running = false;
    this.gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
    canvas.addEventListener('webglcontextlost', (e) => {
      e.preventDefault();                      // 必须声明可恢复
      this.running = false;
      this.lossTimes.push(Date.now());
      this.lossTimes = this.lossTimes.filter(t => Date.now() - t < 30_000);
      if (this.lossTimes.length >= 3) this.onPermanentLoss?.(); // GPU 环境不可用
    });
    canvas.addEventListener('webglcontextrestored', () => {
      this.gl = canvas.getContext('webgl2');
      this.initResources?.(this.gl);           // 全量重建 GPU 资源
      this.running = true;
    });
  }
  get state() { return this.running ? 'running' : 'lost'; }
  start(loopFn) {
    this.running = true;
    const loop = () => { if (!this.running) return; loopFn(this.gl); requestAnimationFrame(loop); };
    requestAnimationFrame(loop);
  }
  stop() { this.running = false; }
}
```

**评分点**：
- contextlost 必须 preventDefault 才会触发 restored，关键语义点
- 恢复时全量重建 GPU 资源（纹理/shader/缓冲不跨上下文存活）
- 渲染循环按 running 状态暂停/恢复
- 频繁丢失阈值判定 + 永久降级路径
