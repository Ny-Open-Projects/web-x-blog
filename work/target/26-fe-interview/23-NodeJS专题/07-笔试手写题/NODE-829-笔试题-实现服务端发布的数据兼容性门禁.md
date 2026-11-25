---
title: [NODE-829] 笔试题——实现发布数据兼容性门禁（canary 准入）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-829：手写兼容门禁

**需求与边界**：
- 需求：发布数据兼容门禁（SCN-NODE-793/OPS-829）——① 写路径扫描（新版本写的数据 schema——双写声明）；② 旧版本读新数据实测（fixture——SCN-OPS-277）；③ 双写漂移门禁（SCN-OPS-331）；④ 未兼容阻断（canary 准入——SCN-OPS-229 分级）。
- 边界：① 兼容声明 vs 实测（声明不足——实测兜底）；② 兼容矩阵（canary 版本 × stable 版本——SCN-OPS-211）；③ 门禁豁免（SCN-OPS-229 豁免记录）。

**答**：
```javascript
async function dataCompatGate(newVersion, stableVersion) {
  const writes = scanWritePaths(newVersion);           // 写路径扫描（新 schema 声明）
  const incompat = [];
  for (const w of writes) {
    const sample = fixtureFromSchema(w.schema);        // fixture 生成
    const oldOk = await stableVersion.read(sample);    // 旧版本读新数据实测（SCN-OPS-277）
    if (!oldOk.ok) incompat.push({ path: w.path, err: oldOk.err });
  }
  const drift = await dualWriteDriftCheck(canaryTable, { tolerance: 0.001 });   // SCN-OPS-331
  const blocked = incompat.length || drift.drifted;
  return {
    blocked,                                           // canary 准入阻断（SCN-OPS-229）
    incompat, drift,
    waiver: blocked ? requireWaiver({ reason, expiresAt: required }) : null,   // 豁免记录
  };
}
```

**评分点**:
- 写路径扫描 + 旧版本实测（声明 vs 实测——SCN-OPS-277）。
- 双写漂移门禁（SCN-OPS-331 联动）。
- canary 准入阻断 + 豁免记录（SCN-OPS-229）。
- 兼容矩阵意识（canary × stable——SCN-OPS-211）。
