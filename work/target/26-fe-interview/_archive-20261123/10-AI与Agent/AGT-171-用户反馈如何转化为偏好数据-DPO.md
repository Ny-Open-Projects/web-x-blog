---
title: [AGT-171] 用户反馈如何转化为偏好数据（DPO）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-171：用户反馈如何转化为偏好数据（DPO）？
**答**：
- 偏好对的三种来源，按质量排序：同会话内显式对比（用户 regenerate 后点选更好的那个——天然成对）、编辑行为（用户修改了 AI 输出，原版 vs 修改版即一对）、隐式信号（采纳/拒绝/复制/点踩，噪声大需加权降噪）。
- 构建规则：正负样本除了「偏好差异」要尽量只差一个变量（同 prompt、同上下文），否则模型学到的是上下文差异而非偏好；置信度低的对（如仅隐式信号）降权或丢弃。
- 数据卫生：移除包含敏感信息的对、偏好翻转矛盾的用户单独分桶（有些用户反馈与质量无关）、错标检测（judge 复核人工标注一致性，低于阈值的标注员数据隔离）。
- 用途分层：小规模高质量对 → DPO 训练；大规模弱信号 → 只做 RLHF 奖励模型训练或线上 banding 排序，别直接进 SFT。

```typescript
// 用户反馈 → DPO 偏好对构建
import { z } from 'zod';

const PreferencePair = z.object({
  promptCtx: z.string(),                       // 共同上下文
  chosen: z.string(), rejected: z.string(),
  source: z.enum(['regenerate_pick', 'user_edit', 'implicit']),
  weight: z.number(),                          // 信号置信权重
});
type PreferencePair = z.infer<typeof PreferencePair>;

export function buildPreferencePairs(events: FeedbackEvent[]): PreferencePair[] {
  const pairs: PreferencePair[] = [];
  for (const e of events) {
    if (e.type === 'regenerate_pick' && e.variantA && e.variantB && e.picked) {
      // 同上下文 regenerate 后点选：最高质量，唯一变量是两次生成
      pairs.push({ promptCtx: e.context, chosen: e.picked === 'A' ? e.variantA : e.variantB,
        rejected: e.picked === 'A' ? e.variantB : e.variantA, source: 'regenerate_pick', weight: 1.0 });
    } else if (e.type === 'user_edit' && e.original && e.edited) {
      // 用户编辑：原版 vs 编辑版，但排除「编辑仅为删 PII」等非偏好差异
      if (editIsSubstantive(e.original, e.edited))
        pairs.push({ promptCtx: e.context, chosen: e.edited, rejected: e.original, source: 'user_edit', weight: 0.7 });
    } else if (e.type === 'implicit' && e.action) {
      const w = { copied: 0.3, thumbs_down: 0.5, abandoned: 0.1 }[e.action] ?? 0;
      if (w >= 0.3 && e.variantA) pairs.push({ promptCtx: e.context, chosen: e.altBest ?? '', rejected: e.variantA,
        source: 'implicit', weight: w });      // 弱信号：低权重，仅供奖励模型
    }
  }
  return pairs.filter((p) => p.chosen && p.chosen !== p.rejected).map(sanitizePair);
}

function editIsSubstantive(a: string, b: string): boolean {
  const diff = Math.abs(a.length - b.length) + levenshte(a, b);
  return diff > 10 && !/[\d@]/.test(b.slice(0, 5)); // 粗过滤：过小差异与疑似纯脱敏编辑
}
function levenshte(a: string, b: string): number { return Math.abs(a.length - b.length) || 3; }
function sanitizePair(p: PreferencePair) { return { ...p, promptCtx: p.promptCtx.replace(/1[3-9]\d{9}/g, fakePhone()) }; }
type FeedbackEvent = { type: string; context: string; variantA?: string; variantB?: string; altBest?: string;
  picked?: 'A' | 'B' | null; original?: string; edited?: string; action?: string };
```
