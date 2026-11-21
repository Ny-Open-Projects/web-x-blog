---
title: [XP-119] 端侧 AI 能力如何集成？RN / Flutter / Web 跑模型的路径？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-119：端侧 AI 能力如何集成？RN / Flutter / Web 跑模型的路径？
**答**：
- 三条主路径：**平台原生 AI SDK**（Core ML / NNAPI / MediaPipe Tasks）、**推理运行时框架**（onnxruntime / TFLite 的跨端绑定：RN 用 onnxruntime-react-native、react-native-fast-tflite；Flutter 用 tflite_flutter / onnxruntime）、**Web 路径**（ONNX Runtime Web / WebGPU / wasm，Electron 走 Node 原生推理性能更佳）。
- 选型逻辑：优先平台 SDK（厂商加速、生态成熟），需要跨端同构模型时用 ONNX/TFLite 统一模型格式，端上只做推理与前处理（量化 int8/fp16 模型，100MB 内可控）。
- 工程架构：模型分发与热更走 CDN+版本校验（大模型不进安装包），推理封装为**统一端侧推理接口**（load/infer/stream），各端 adapter 对接底层运行时（风格同 XP-070 桥接层）。
- 性能与功耗：推理放后台线程/isolate/独立进程，防阻塞 UI；分档降级（低端机换更小模型或云端兜底）；功耗敏感场景（连续推理）做节流。
- 隐私卖点：端侧推理数据不出设备，但**遥测与模型更新链路**要合规声明；云端兜底方案必须显式告知用户数据流向。

```typescript
// packages/core/ai —— 统一端侧推理接口：load/infer/stream，各端 adapter 对接
export interface LocalInference {
  load(model: { url: string; version: string; quant: 'int8' | 'fp16' }): Promise<void>;
  infer(input: TensorInput): Promise<TensorOutput>;
  stream(input: TensorInput, onChunk: (t: TensorOutput) => void): () => void;
}

// 模型管理：CDN 分发 + 版本校验 + 不进安装包
export async function ensureModel(m: ModelMeta, cache: Storage): Promise<string> {
  const local = await cache.get(`model:${m.id}`);
  if (local?.version === m.version && local.intact) return local.path;   // 命中本地
  const path = await downloadWithVerify(m.url, m.md5);                    // 分片下载+校验
  await cache.set(`model:${m.id}`, { version: m.version, path, intact: true });
  return path;
}

// 各端 adapter 落位：
//   RN       adapter → onnxruntime-react-native（JSI 直连）或 fast-tflite
//   Flutter  adapter → tflite_flutter（isolate 内推理，UI 不阻塞）
//   Web/H5   adapter → onnxruntime-web（webgpu ep，无 webgpu 退 wasm）
//   Electron adapter → onnxruntime-node（原生线程，性能最佳）
// 运行策略：推理进后台线程；deviceTier=lowend 自动换小模型或云端兜底（显式告知数据流向）
// 功耗：连续推理（实时字幕类）200ms 节流 + 温度回退
```
