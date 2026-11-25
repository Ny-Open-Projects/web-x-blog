---
title: [BLD-312] 笔试题——实现构建遥测的 hook 级采样与聚合？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-312：手写构建遥测聚合

**需求与边界**：
- 需求：构建遥测的聚合分析（SCN-ENG-269）——① 按项目/任务聚合 P50/P95/缓存命中率；② 劣化检测（7 日基线——SCN-BLD-261 常态化）；③ 本地 vs CI 比值诊断（>3 = 环境问题）；④ 输出优化建议（瓶颈组件）。
- 边界：① 分位用 t-digest（流式聚合省内存——SCN-SLA-739）；② 样本量下限（<20 样本不归因）；③ 劣化排除「配置变更引起的合理变化」（键变更标记）。

**答**：
```javascript
class BuildTelemetry {
  constructor() { this.digests = new Map(); }          // key -> TDigest
  push(sample) {                                       // { project, task, ms, cacheHit, scope, configVer }
    const key = `${sample.project}:${sample.task}:${sample.scope}`;
    (this.digests.get(key) ?? this.digests.set(key, new TDigest()).get(key)).push(sample.ms);
    this.byConfigVer(key, sample);
  }
  report({ degradeThreshold = 1.2, minSamples = 20 } = {}) {
    const out = [];
    for (const [key, d] of this.digests) {
      if (d.count < minSamples) continue;              // 样本下限
      const p95 = d.quantile(0.95);
      const baseline = this.baseline7d(key);           // 7 日基线（排除键变更）
      const entry = { key, p50: d.quantile(0.5), p95, hitRate: this.hitRate(key) };
      const ratio = this.ciLocalRatio(key);
      if (baseline && p95 > baseline * degradeThreshold && !configChangedRecently(key))
        entry.degraded = true;                         // 排除配置变更的合理变化
      if (ratio > 3) entry.hint = 'CI 比本地慢 3×+，排查环境而非配置';
      out.push(entry);
    }
    return { entries: out.sort((a, b) => b.p95 - a.p95),
      degraded: out.filter(e => e.degraded) };
  }
}
```

**评分点**:
- t-digest 流式分位（内存守恒——SCN-SLA-739 复用）。
- 劣化检测排除配置变更（合理变化不误报）。
- 本地/CI 比值诊断（SCN-BLD-261 环境归因）。
- 样本量下限（小样本不归因）。

## 变体与延伸（补充）

**变体与延伸**：

1. 采样率怎么定才不丢长尾？ → 分层采样：慢 hook 全采、快 hook 低采样，聚合时按采样率加权还原分位，避免长尾被平均掉。
2. 怎么保证采样本身不拖慢构建？ → 打点用 process.hrtime.bigint，聚合统一放到结束阶段，落盘异步批量写，避免在热路径上做 IO。
3. 怎么做 hook 耗时归因？ → 记录 parent/child 调用关系形成调用树，再算自耗时（总时长减去直接子节点），否则嵌套 hook 会重复计时。
