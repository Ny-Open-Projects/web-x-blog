---
title: [VIZ-207] WebGPU 兼容层设计：WebGL 降级双后端架构
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-207：WebGPU 兼容层设计：WebGL 降级双后端架构

**答**：
- 题目：可视化库同时支持 WebGPU 与 WebGL（兼容率），设计双后端渲染抽象：统一接口（创建管线/绘制/资源上传），WebGPU 不可用时自动切 WebGL2。
- 思路：Renderer 接口（createPipeline/uploadBuffer/drawFrame）；GPUBackend = WebGPUBackend | WebGLBackend；特性探测 + 降级 + 统一着色器翻译（WGSL→GLSL 预编译对或统一中间语言）。
- 评分点：接口抽象完整性；着色器双写或翻译策略；特性探测与降级路径。

```javascript
class WebGPURenderer {                                  // 后端 A
  async init(canvas) { /* adapter/device */ }
  createPipeline(desc) { /* WGSL */ }
  draw(scene) { /* render pass */ }
}
class WebGL2Renderer {                                  // 后端 B（降级）
  async init(canvas) { this.gl = canvas.getContext('webgl2'); }
  createPipeline(desc) { /* GLSL：预编译对——WGSL 与 GLSL 由构建期从同一中间表示生成 */ }
  draw(scene) { /* 同语义映射：draw call 数组 */ }
}
async function createRenderer(canvas) {
  if (navigator.gpu && (await navigator.gpu.requestAdapter())) {
    try { return await new WebGPURenderer().init(canvas); } catch { /* 降级 */ }
  }
  return new WebGL2Renderer().init(canvas);              // 自动降级
}
// 着色器策略：构建期写两份（语法差异大）或用 naga/tint 类工具转译——面试说清取舍
```
