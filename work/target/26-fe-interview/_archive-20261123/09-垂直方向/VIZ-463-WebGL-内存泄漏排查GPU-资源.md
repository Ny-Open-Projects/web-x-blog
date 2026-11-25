---
title: [VIZ-463] WebGL 内存泄漏排查：GPU 资源的生命周期审计
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-463：WebGL 内存泄漏排查：GPU 资源的生命周期审计

**答**：
- 泄漏源：texture/buffer/program 创建后未 delete（场景切换/组件卸载）。
- 审计：包装 GL 对象记录创建点（debug 模式），destroy 时校验；定期统计 active 资源数趋势。
- 工具：Spector.js 资源面板、内存面板 WebGLMemory 分类。

```javascript
// GPU 资源审计
function auditedCreate(gl, kind, tag) {
  const obj = kind === 'texture' ? gl.createTexture() : gl.createBuffer();
  registry.push({ obj, kind, tag, stack: new Error().stack });
  return obj;
}
function auditLeak() {
  return { active: registry.length,
    suspects: registry.filter(r => r.age > 60_000).map(r => r.tag) };
}
// 组件卸载：deleteTexture/deleteBuffer 必须与 create 成对
```
