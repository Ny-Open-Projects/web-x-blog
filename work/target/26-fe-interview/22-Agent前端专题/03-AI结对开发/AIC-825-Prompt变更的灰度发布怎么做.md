---
title: [AIC-825] Prompt 改了一个词就可能翻车，如何做灰度发布？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-825：Prompt 改了一个词就可能翻车，如何做灰度发布？
**答**：
- Prompt 必须**版本化**：每次变更生成唯一 `promptVersion`，线上请求记录用的是哪个版本（血缘 AIC-810），才能把指标变化归因到 prompt 而非模型或流量。
- 灰度分层：先离线跑 golden 集（A/B 对比统计显著性），通过后按流量比例 1% → 5% → 20% → 100% 逐步放量；每一档观察足够时间与样本量再进下一档。
- 分流要**粘性**：按 `userId`/`sessionId` 哈希分流，保证同一用户始终看到同一版本，避免同一会话里回答风格突变造成困惑。
- 自动回滚：监控核心指标（幻觉率、拒答率、用户重试率、延迟），设告警阈值；灰度版本指标显著劣于基线时自动切回旧版本——回滚开关要能在分钟级生效。
- 追问钩子：追问「灰度期间两个版本 prompt 共存怎么管理」——能答出「用配置中心按版本下发 + 分流层与业务解耦」的候选人具备发布系统经验。

```typescript
// 基于用户 ID 的粘性分流 + 比例灰度
function assignVersion(userId: string, versions: Array<{ v: string; pct: number }>) {
  if (!userId) return versions[0].v;
  // 稳定哈希：同一用户永远落到同一桶
  let h = 0;
  for (const ch of userId) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
  const bucket = h % 100;
  let acc = 0;
  for (const { v, pct } of versions) {
    acc += pct;
    if (bucket < acc) return v;
  }
  return versions[versions.length - 1].v; // 兜底
}

const versions = [{ v: 'p7', pct: 95 }, { v: 'p8', pct: 5 }];
console.log(assignVersion('user-123', versions)); // 稳定返回 p7 或 p8
// 监控 p8 的指标，劣化则把 pct 改回 0 实现秒级回滚
```
