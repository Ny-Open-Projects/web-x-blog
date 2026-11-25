---
title: [AGT-132] 多模态上下文（图片/音频）的 token 成本怎么估算与控制？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-132：多模态上下文（图片/音频）的 token 成本怎么估算与控制？
**答**：
- 图片 token 不是按字节算的：主流计法是「分辨率分块」——图像按固定块尺寸切，块数×每块 token + 基础开销；即使如此同一张图在 detail high/low 下可差 10 倍以上。
- 音频按秒计费换算 token，视频按抽帧后的帧数×单帧 token 估算；前端上传前就能完成估算，把成本控制做在请求之前。
- 控制手段：请求级指定 detail: 'low'、服务端预压缩（长边限制+重编码）、多图任务改「先生成图注再传文字」的两段式。
- 高频考点：估算器要在前端/网关双侧实现，超预算直接拒绝或降档，而不是发出去等 400。

```typescript
// 多模态上下文的 token 估算器（以 OpenAI 风格分块计法为例）
const TILE = 512, TILE_TOKENS = 170, BASE_TOKENS = 85; // 512x512 一块约 170 token + 每图基础 85

export function estimateImageTokens(w: number, h: number, detail: 'low' | 'high' = 'high'): number {
  if (detail === 'low') return BASE_TOKENS + TILE_TOKENS; // 低细节固定小开销
  const scale = Math.min(1, 2048 / Math.max(w, h));       // 长边压到 2048 内
  const tw = Math.ceil((w * scale) / TILE), th = Math.ceil((h * scale) / TILE);
  return BASE_TOKENS + tw * th * TILE_TOKENS;
}

export function estimateAudioTokens(seconds: number): number {
  return Math.ceil(seconds * 100); // 约 100 token/秒（按 44.1kHz 语音的经验换算，随模型校准）
}

// 会话级预算闸门：上传即估算，超限自动降档
export async function gateMultimodal(parts: { img?: { w: number; h: number }; audioSec?: number }[], budget = 8000) {
  let total = 0;
  const plan = parts.map((p) => {
    if (p.img) {
      let detail: 'low' | 'high' = 'high';
      let t = estimateImageTokens(p.img.w, p.img.h, detail);
      if (total + t > budget) { detail = 'low'; t = estimateImageTokens(p.img.w, p.img.h, 'low'); }
      total += t;
      return { kind: 'image' as const, detail, tokens: t };
    }
    const t = estimateAudioTokens(p.audioSec ?? 0);
    total += t;
    return { kind: 'audio' as const, tokens: t };
  });
  if (total > budget) throw new Error(`多模态输入 ${total} token 超出预算 ${budget}，请减少附件`);
  return { plan, total };
}
```
