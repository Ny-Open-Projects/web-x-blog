---
title: [NODE-913] 笔试题——实现发布后资源清理编排（旧资源/旧配置/旧实例）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-913：手写清理编排

**需求与边界**：
- 需求：发布后清理（SCN-OPS-256/227）——① 旧资源清理（N-2——SCN-OPS-301 残留检查前置）；② 旧配置清理（废弃配置项——SCN-NODE-694 废弃统计）；③ 旧实例清理（缩容——SCN-NODE-834）；④ 清理的编排顺序（依赖顺序——清理前验证无流量，SCN-OPS-301 探测）。
- 边界：① 清理的守卫（回滚目标资源永不清理——SCN-OPS-243）；② 清理的审计（SCN-OPS-220）；③ 清理失败的告警（SCN-OPS-256）。

**答**：
```javascript
async function postReleaseCleanup(release) {
  const checks = [
    { name: 'stale-versions', guard: () => residueRate() < 0.01,   // 残留检查前置（SCN-OPS-301）
      run: () => cleanAssets(release.prev2) },
    { name: 'deprecated-config', guard: () => noTraffic(deprecatedKeys),   // SCN-NODE-694
      run: () => removeDeprecatedConfig() },
    { name: 'scale-down', guard: () => qpsStable(), run: () => scaleDown() },   // SCN-NODE-834
  ];
  for (const c of checks) {
    if (!(await c.guard())) { deferCleanup(c); continue; }   // 守卫（SCN-OPS-243 永不清理回滚目标）
    await c.run(); audit({ action: 'cleanup', name: c.name });
  }
}
```

**评分点**:
- 三类清理（资源/配置/实例——SCN-OPS-301/694/834）。
- 守卫前置（残留检查/无流量探测——SCN-OPS-301）。
- 回滚目标永不清理（SCN-OPS-243）。
- 审计 + 延迟清理（SCN-OPS-220）。
