---
title: [AGT-174] 端侧模型（WebGPU 跑 LLM）现状如何？前端什么场景值得用？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-174：端侧模型（WebGPU 跑 LLM）现状如何？前端什么场景值得用？
**答**：
- 技术现状：WebGPU + WebGL 回退让浏览器能跑量化后的小模型（1B~3B，Q4 量化），框架有 WebLLM、Transformers.js、llama.cpp WASM 等；内存是硬约束（3B Q4 约 2GB），首次下载模型几百 MB 到数 GB 需 Cache/OPFS 缓存。
- 值得端侧的场景：隐私强诉求（输入不离开设备：病历史、合同、密钥相关）、离线可用（弱网/机密环境）、超低延迟的轻任务（补全、改写、分类，无需网络往返）。
- 不值得的场景：需要长上下文/强推理/最新知识的任务——端侧小模型能力差距明显，硬上只会伤害体验。
- 混合架构是答案：端侧做「第一道」（本地意图识别、敏感内容本地脱敏后再上云、离线兜底话术），云端做「重活」；前端工程师的价值在模型加载调度（Web Worker 不阻塞 UI）、显存管理与降级链。

```typescript
// WebGPU 端侧模型加载调度（WebLLM 风格）与混合降级
import * as webllm from '@mlc-ai/web-llm';

export async function initLocalModel(onProgress: (p: number) => void): Promise<webllm.MLCEngineInterface | null> {
  if (!navigator.gpu) return null;                                 // 无 WebGPU：直接走云端
  try {
    const engine = new webllm.MLCEngine();
    await engine.reload('Qwen2.5-1.5B-Instruct-q4f16_1-MLC', {     // 1.5B Q4：约 1GB，主流设备可跑
      initProgressCallback: (r) => onProgress(r.progress),
    });
    return engine;
  } catch (e) {
    console.warn('端侧模型加载失败，回退云端', e);
    return null;
  }
}

// 混合推理：轻任务端侧，重任务或端侧不可用走云端
export async function hybridInfer(input: string, local: webllm.MLCEngineInterface | null): Promise<{ text: string; where: 'local' | 'cloud' }> {
  const light = /改写|总结这句话|修正错别字|分类/.test(input);       // 任务复杂度粗判（生产用小分类器）
  if (local && light) {
    try {
      const r = await local.chat.completions.create({
        messages: [{ role: 'user', content: input }], max_tokens: 128,
      });
      return { text: r.choices[0].message.content ?? '', where: 'local' };
    } catch { /* OOM 等：降级云端 */ }
  }
  return { text: await cloudChat(input), where: 'cloud' };
}

async function cloudChat(input: string) {
  const res = await fetch('/api/chat', { method: 'POST', body: JSON.stringify({ input }) });
  return (await res.json()).text as string;
}
```

---

## 三十、平台与生态
