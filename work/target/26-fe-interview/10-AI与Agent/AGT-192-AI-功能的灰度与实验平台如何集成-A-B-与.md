---
title: [AGT-192] AI 功能的灰度与实验平台如何集成（A/B 与 LLM 的特殊之处）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-192：AI 功能的灰度与实验平台如何集成（A/B 与 LLM 的特殊之处）？
**答**：
- LLM 实验与普通 A/B 的差异：一是变异维度多（prompt/模型/参数/工具，实验配置是复合对象），二是结果非确定性（同用户同输入两次结果不同，不能用「用户级去重」直接判定），三是质量指标依赖 judge 与人工反馈，回收周期长。
- 集成方式：实验平台下发「实验配置 = Agent bundle + 分流规则 + 指标埋点计划」，网关按分流执行（AGT-141 的灰度路由即是实验的执行层）；埋点自动带上 experimentId/variantId，指标归因不靠猜。
- LLM 特有的实验卫生：变异隔离（实验组 prompt 版本必须指纹不同，防止缓存串组）、质量护栏指标（护栏指标劣化自动停实验）、时长要求（LLM 反馈周期长，最小实验时长按「收集足够负反馈样本」倒推而非天数）。
- 序贯检验替代固定样本量：LLM 指标方差大，用序贯检验（边跑边看，达标即停）避免长期承担劣化变体的损失。

```typescript
// 实验平台集成：实验配置 → 分流 → 埋点归因 → 序贯判定
import { z } from 'zod';

const Experiment = z.object({
  id: z.string(),
  variants: z.array(z.object({
    name: z.string(), bundleId: string0(), allocation: z.number(),
  })),
  metrics: z.object({ primary: z.string(), guards: z.array(z.string()) }),
  stopRule: z.object({ minSamples: z.number(), maxDays: z.number(), guardThreshold: z.number() }),
});
function string0() { return z.string(); }
type Experiment = z.infer<typeof Experiment>;

export function assignVariant(exp: Experiment, userId: string): string {
  const h = [...`${exp.id}:${userId}`].reduce((s, c) => (s * 31 + c.charCodeAt(0)) >>> 0, 7) % 100;
  let acc = 0;
  for (const v of exp.variants) { acc += v.allocation; if (h < acc) return v.name; } // 稳定分流
  return exp.variants[0].name;
}

// 序贯判定：护栏破线立即停，主指标序贯显著即胜出
export function sequentialJudge(exp: Experiment, obs: Map<string, { samples: number; primary: number; guards: number[] }>) {
  const control = obs.get('control')!;
  for (const [name, o] of obs) {
    if (name === 'control') continue;
    const guardBad = o.guards.some((g, i) => g < control.guards[i] * (1 - exp.stopRule.guardThreshold));
    if (guardBad) return { action: 'stop', reason: `${name} 护栏指标劣化超过 ${(exp.stopRule.guardThreshold * 100).toFixed(0)}%` };
    if (o.samples >= exp.stopRule.minSamples && significanceTest(o.primary, control.primary, o.samples))
      return { action: o.primary > control.primary ? 'promote' : 'stop', winner: name };
  }
  return { action: 'continue' };
}
function significanceTest(a: number, b: number, n: number) { return Math.abs(a - b) > 1.96 * Math.sqrt((a * (1 - a) + b * (1 - b)) / n); }
```
