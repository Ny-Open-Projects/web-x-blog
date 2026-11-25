---
title: [ARC-380] 端智能（on-device AI 推理）的前端架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-380：端智能（on-device AI 推理）的前端架构如何设计？
**答**：
- 端侧推理栈：ONNX Runtime Web / TensorFlow.js / WebLLM（WebGPU 跑 LLM）；加速后端 WebGL → WebGPU → WASM SIMD。
- 云端 vs 端侧决策：隐私敏感（人脸/语音不离端）、离线可用、低延迟高频（手势/滤镜）→ 端侧；大模型/复杂任务 → 云端；混合模式端侧粗筛 + 云端精算。
- 模型分发架构：模型文件大（几 MB~几百 MB），CDN 分发 + 版本管理 + 增量更新 + 缓存到 Cache Storage；按设备能力分级加载不同量化版本。
- 性能预算：推理耗时 < 100ms（交互级）、加载预热在 idle 时进行、内存峰值控制（模型常驻 vs 按需卸载）。
- 降级与评估：不支持 WebGPU 的设备自动换量化小模型或纯云方案；端云结果抽样对齐评估（精度一致性监控）。
```javascript
// 端侧推理编排
async function initModel() {
  const backend = navigator.gpu ? 'webgpu' : 'wasm';
  const session = await ort.InferenceSession.create(modelUrl(quantTier), // 分级量化
    { executionProviders: [backend], graphOptimizationLevel: 'all' });
  requestIdleCallback(() => warmup(session));        // idle 预热
  return (input) => timeIt(() => session.run(input), 'inference');
}
```
