---
title: [NODE-932] 笔试题——实现降级预案自动生成（发布→预案卡片）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-932：手写预案生成

**需求与边界**：
- 需求：降级预案自动生成（SCN-OPS-217/932）——① 发布声明 → 预案卡片（依赖/降级策略——SCN-OPS-217 卡片三段）；② 预案与降级矩阵联动（SCN-OPS-329）；③ 预案的演练绑定（SCN-OPS-269）；④ 预案审计（SCN-OPS-220）。
- 边界：① 卡片的字段完整（症状/定位/处置/升级——SCN-OPS-217）；② 卡片的生成来源（发布计划声明——SCN-OPS-261）；③ 卡片的保鲜（演练绑定——SCN-OPS-311）。

**答**：
```javascript
function generateDegradeCards(release) {
  return release.dependencies.map(d => ({
    id: `card-${d.target}`,
    symptom: `${d.target} 故障时 ${release.app} 的表现`,
    locate: `breaker(${d.target}).state + fallback logs`,
    action: degradationMatrix[d.target]?.strategies ?? [],   // 降级矩阵联动（SCN-OPS-329）
    escalate: '10min 无效 → oncall-mgr',
    drill: bindDrill(d.target),                        // 演练绑定（SCN-OPS-269/311）
  }));
}
```

**评分点**:
- 卡片三段（症状/定位/处置/升级——SCN-OPS-217）。
- 降级矩阵联动（SCN-OPS-329）。
- 演练绑定（SCN-OPS-269/311）。
- 发布声明驱动（SCN-OPS-261）。
