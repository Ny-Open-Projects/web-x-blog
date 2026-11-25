---
title: [NODE-938] 笔试题——实现多版本并存清理验证（清理后无 404）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-938：手写清理验证

**需求与边界**：
- 需求：清理验证（SCN-OPS-301/938）——① 清理前残留检查（SCN-OPS-301）；② 清理后验证（旧资源无 404 请求——SCN-OPS-938）；③ 清理的回滚（误清理恢复——SCN-OPS-256）；④ 清理的排程（低峰——SCN-NODE-764）。
- 边界：① 残留率阈值（SCN-OPS-301）；② 404 监控（SCN-OPS-256）；③ 清理的白名单（回滚目标——SCN-OPS-243）。

**答**：
```javascript
async function cleanupWithVerify(release) {
  if (residueRate(release.prev2) > 0.01) return defer('残留 >1%——SCN-OPS-301');   // 残留检查
  if (release.prev === release.rollbackTarget) return defer('回滚目标——SCN-OPS-243');   // 白名单
  await cleanAssets(release.prev2);
  const notFoundRate = await monitor404(release.prev2.assets, { window: 1 * 3600_000 });   // 清理后 404 监控
  if (notFoundRate > 0) {                              // 有 404：恢复 + 告警
    await restoreAssets(release.prev2);
    alert({ type: 'CLEANUP_404', version: release.prev2 });
  }
  audit({ action: 'cleanup', version: release.prev2, notFoundRate });
}
```

**评分点**:
- 残留检查前置（SCN-OPS-301）。
- 回滚目标白名单（SCN-OPS-243）。
- 清理后 404 监控 + 恢复（SCN-OPS-256）。
- 低峰排程（SCN-NODE-764）。
