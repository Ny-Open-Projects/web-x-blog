---
title: [OPS-317] 笔试题——实现多端 flag 决策一致性校验（同用户跨端同分组）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## OPS-317：手写多端一致性校验

**需求与边界**：
- 需求：验证同一用户在 Web/App/小程序的 flag 决策一致（SCN-OPS-272）——① 服务端决策单源对比（三端 SDK 上报的决策 vs 服务端计算值）；② 漂移归因（端内缓存滞后/规则快照版本旧/SDK 版本差异）；③ 不一致率分端统计与告警。
- 边界：① 决策上报带端类型与规则快照版本；② 缓存滞后有合理窗口（10 分钟内不一致容忍）；③ 一致性按「会话粒度」比对（同用户同会话内）。

**答**：
```javascript
function multiEndConsistency(reports, flagEngine, { tolerance = 10 * 60_000 } = {}) {
  const mismatches = [];
  for (const r of reports) {
    const expected = flagEngine.evaluateForUser(r.userId, r.flag);   // 服务端权威
    const lag = Date.now() - r.snapshotTs;
    if (r.decision !== expected && lag > tolerance) {  // 缓存滞后容忍
      mismatches.push({
        userId: r.userId, flag: r.flag, platform: r.platform,
        got: r.decision, expected, lag,
        cause: r.snapshotVersion < flagEngine.version ? 'STALE_RULES'
          : r.sdkVersion !== LATEST ? 'SDK_VERSION' : 'UNKNOWN',
      });
    }
  }
  const byPlatform = groupBy(mismatches, 'platform');
  return {
    rate: mismatches.length / reports.length,
    byPlatform: Object.fromEntries(Object.entries(byPlatform)
      .map(([p, list]) => [p, list.length / reports.filter(r => r.platform === p).length])),
    topCause: mode(mismatches.map(m => m.cause)),      // 主要漂移原因
    alert: mismatches.length / reports.length > 0.01,
  };
}
```

**评分点**:
- 服务端权威决策对比（端上报 vs 服务端计算）。
- 缓存滞后容忍窗口（10 分钟内不一致不误报）。
- 漂移归因三分类（STALE_RULES/SDK_VERSION/UNKNOWN）。
- 分端不一致率 + 主要原因（修复方向可导航）。
