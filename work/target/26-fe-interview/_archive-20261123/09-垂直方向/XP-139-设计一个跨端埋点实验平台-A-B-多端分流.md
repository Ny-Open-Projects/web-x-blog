---
title: [XP-139] 设计一个跨端埋点实验平台（A/B 多端分流）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-139：设计一个跨端埋点实验平台（A/B 多端分流）？
**答**：
- 分流引擎核心：**分层正交模型**——流量层（layer）内实验互斥、层间正交（不同层实验可叠加），分流因子 `hash(layerId, experimentId, userId) % 100`，同一用户在任意端（App/H5/小程序）按同一 userId 分到同一桶——**跨端一致分流是硬要求**（未登录用户用设备指纹桥接，登录后切 userId 并做桶迁移记录）。
- 实验配置：变体（含参数 JSON）、目标人群（圈选条件）、指标（核心+护栏）、时长与样本量预估（功效分析）；配置下发热更新生效（XP-067 flag 通道）。
- 端上执行：SDK 启动 handshake 拉取实验分配（XP-112），暴露 `getVariant(experiment)`；曝光/转化事件自动带实验标记（XP-134 管线补全字段）。
- 分析与决策：指标看板（AA 期检验、显著性、护栏告警——崩溃率/性能劣化自动停实验）、MDE 未达提前判定、实验复盘归档（结论沉淀进知识库）。
- 治理：实验生命周期状态机（draft→running→concluded），超期实验强制收敛；同域实验冲突检测（分流层设计即预防）；埋点字典统一管理（XP-134 schema 同源）。

```typescript
// packages/ab/core —— 分层正交分流引擎（跨端一致）
export interface ExperimentCfg {
  id: string; layer: string;              // layer 内互斥，layer 间正交
  variants: Array<{ key: string; params: Record<string, unknown>; weight: number }>;
  audience?: { region?: string[]; tier?: Tier[]; minVersion?: string };
}

export function assign(cfg: ExperimentCfg, ctx: { userId: string; region: string; tier: Tier; version: string }): Variant | null {
  if (cfg.audience && !matchAudience(cfg.audience, ctx)) return null;
  // 分桶：hash 因子含 layerId 与 experimentId —— 层内互斥 层间正交
  const bucket = murmur3(`${cfg.layer}#${cfg.id}#${ctx.userId}`) % 100;
  let acc = 0;
  for (const v of cfg.variants) {
    acc += v.weight;                       // 权重和 = 100
    if (bucket < acc) return v;            // 同一 userId 任意端计算结果相同 → 跨端一致
  }
  return null;                             // 未命中（如灰度放量中）
}
// 未登录：设备指纹桥接；登录后切 userId + 桶迁移记录（分析侧修正）
// SDK：启动 handshake 拉实验配置（XP-112）→ getVariant() → 曝光事件自动带实验标记
// 平台侧：AA 检验 / 显著性 / 护栏自动停实验（崩溃率 劣化即停）；超期实验强制收敛
```
