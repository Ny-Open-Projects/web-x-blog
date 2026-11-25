---
title: [NODE-927] 笔试题——实现多版本并存兼容矩阵（运行时校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-927：手写兼容矩阵

**需求与边界**：
- 需求：多版本兼容（SCN-OPS-211/256）——① 版本矩阵声明（canary×stable——SCN-OPS-211）；② 运行时组合校验（实际版本组合——SCN-OPS-231）；③ 未声明组合的告警（SCN-OPS-256）；④ 矩阵的 CI 校验（SCN-OPS-829）。
- 边界：① 矩阵的来源（发布计划——SCN-OPS-251）；② 运行时组合的采集（trace——SCN-OPS-920）；③ 矩阵的消费（灰度路由——SCN-NODE-776）。

**答**：
```javascript
async function compatMatrixRuntime(release) {
  const combos = await runtimeVersionCombos(release);   // 运行时组合（trace——SCN-OPS-920）
  const declared = release.compatMatrix;               // 声明矩阵（SCN-OPS-211）
  const undeclared = combos.filter(c => !declared.has(c));   // 未声明（SCN-OPS-256）
  if (undeclared.length)
    alert({ type: 'UNDECLARED_COMBO', combos: undeclared,
      risk: '未声明的版本组合——兼容性未知' });
  return {
    declared, undeclared,
    allCompatible: !undeclared.length,
    gate: undeclared.length ? 'BLOCK' : 'PASS',        // SCN-OPS-829 门禁
  };
}
```

**评分点**:
- 声明矩阵 + 运行时组合比对（SCN-OPS-211/231）。
- 未声明组合告警（SCN-OPS-256）。
- 门禁联动（SCN-OPS-829）。
- 矩阵消费（路由——SCN-NODE-776）。
