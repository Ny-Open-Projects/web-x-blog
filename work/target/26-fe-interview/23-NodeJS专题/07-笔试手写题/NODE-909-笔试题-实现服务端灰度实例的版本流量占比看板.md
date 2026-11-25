---
title: [NODE-909] 笔试题——实现版本流量占比看板（灰度进度可视化）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-909：手写占比看板

**需求与边界**：
- 需求：版本流量占比（SCN-OPS-256/850）——① 实时占比（版本维度流量统计——SCN-OPS-850）；② 进度看板（灰度目标 vs 实际——SCN-OPS-242）；③ 堆积告警（版本数超限——SCN-OPS-256）；④ 占比的完整性（100%——SCN-OPS-850）。
- 边界：① 占比的统计口径（请求级——样本侧版本，SCN-OPS-231）；② 长尾残留（SCN-OPS-232 残留率）；③ 看板的灰度联动（放量建议——SCN-OPS-242）。

**答**：
```javascript
async function versionShareBoard(release) {
  const share = await versionTrafficShare();           // 实时占比（SCN-OPS-850）
  assert(sum(share.values()) === 100);                 // 完整性（SCN-OPS-850）
  const stale = share.filter(v => v.version !== release.current && v.pct > 0.01);
  return {
    share, target: release.gray.target,
    progress: share.get(release.canary) / release.gray.target,   // 进度（SCN-OPS-242）
    stale: stale.length ? { versions: stale, cleanup: 'SCN-OPS-301' } : null,   // 残留（SCN-OPS-232）
    sprawl: activeVersions() > 5 ? '版本堆积——SCN-OPS-256' : null,   // 堆积
    ramp: rampSuggest(share, release),                 // 放量建议（SCN-OPS-242）
  };
}
```

**评分点**:
- 实时占比 + 完整性校验（SCN-OPS-850）。
- 进度与放量建议（SCN-OPS-242）。
- 残留/堆积告警（SCN-OPS-232/256）。
- 统计口径样本侧（SCN-OPS-231）。
