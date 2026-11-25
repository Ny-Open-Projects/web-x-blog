---
title: [OPS-328] 笔试题——实现 RACI 责任矩阵生成（随风险级别变化）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## OPS-328：手写 RACI 矩阵

**需求与边界**：
- 需求：按发布风险级别生成责任矩阵（SCN-OPS-278）——① 每环节唯一 Accountable（避免都管都不管）；② L0 全自动环节（无人工角色）与 L3 全人工的映射；③ 模糊地带显式分配（指标业务解读归业务方）；④ 矩阵随发布计划输出（责任前置可见）。
- 边界：① 每环节 A 只能一个（多个 A = 没有负责）；② 角色 → 人员解析（代理规则复用 SCN-OPS-302）；③ 矩阵缺失环节告警（新环节未定义责任）。

**答**：
```javascript
function raciMatrix(plan, { roles = RACI_TEMPLATES } = {}) {
  const template = roles[plan.level];                  // L0 自动 / L3 全人工
  const matrix = {};
  for (const [phase, assignment] of Object.entries(template)) {
    if (!assignment) { matrix[phase] = null; continue; }   // L0 自动环节
    const accountable = assignment.A;
    matrix[phase] = {
      A: resolveRole(accountable),                     // 唯一 A（角色路由）
      R: assignment.R?.map(resolveRole),
      C: assignment.C?.map(resolveRole),
      I: assignment.I?.map(resolveRole),
    };
    if (Array.isArray(matrix[phase].A))
      throw new Error(`环节 ${phase} 有多个 Accountable——无人负责`);
  }
  const undefinedPhases = ALL_PHASES.filter(p => !(p in matrix));
  if (undefinedPhases.length)
    warn(`环节未定义责任: ${undefinedPhases}（新环节需补充矩阵）`);
  plan.raci = matrix;                                  // 责任前置可见
  return matrix;
}
```

**评分点**:
- 唯一 Accountable 校验（多 A 抛错——SCN-OPS-278 核心）。
- L0/L3 分级模板（自动化环节无人工角色）。
- 未定义环节告警（新环节责任前置补充）。
- 矩阵写入发布计划（前置可见而非事后追责）。
