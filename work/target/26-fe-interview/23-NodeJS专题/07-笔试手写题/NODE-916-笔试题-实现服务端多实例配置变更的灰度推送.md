---
title: [NODE-916] 笔试题——实现配置变更灰度推送（按实例百分比）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-916：手写配置灰度推送

**需求与边界**：
- 需求：配置灰度推送（SCN-OPS-228/NODE-663）——① 按实例百分比推送（实例 hash——SCN-OPS-228）；② 推送的生效验证（实例上报——SCN-NODE-902 心跳）；③ 灰度暂停/回退（SCN-OPS-228 快照）；④ 全量推送的门槛（灰度验证通过——SCN-OPS-242）。
- 边界：① 实例级推送的幂等（SCN-NODE-655）；② 推送失败的实例重试（SCN-NODE-663）；③ 灰度期的配置一致性（SCN-NODE-902）。

**答**：
```javascript
async function grayPushConfig(cfg, { stages = [10, 50, 100] } = {}) {
  const snapshot = snapshotOld(cfg);                   // 旧值快照（SCN-OPS-228）
  for (const pct of stages) {
    const targets = pickInstancesByHash(pct);          // 实例 hash 分组（SCN-OPS-228）
    await pushTo(targets, cfg);                        // 推送
    const verified = await waitForHeartbeat(targets);  // 生效验证（SCN-NODE-902）
    if (!verified.allOk) { await rollbackTo(snapshot, targets); break; }   // 回退（SCN-OPS-228）
    await observe(5 * 60_000);                         // 观察（SCN-OPS-242）
  }
  audit({ cfg: cfg.version, stages });
}
```

**评分点**:
- 实例 hash 分组灰度（SCN-OPS-228）。
- 心跳验证 + 失败回退（SCN-NODE-902/663）。
- 观察窗（SCN-OPS-242）。
- 快照回滚（SCN-OPS-228）。
