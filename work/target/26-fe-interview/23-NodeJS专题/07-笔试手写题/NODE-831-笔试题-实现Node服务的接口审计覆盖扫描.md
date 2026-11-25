---
title: [NODE-831] 笔试题——实现接口审计覆盖扫描（哪些接口缺审计）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-831：手写审计覆盖

**需求与边界**：
- 需求：审计覆盖扫描（SCN-NODE-775）——① 敏感操作路由扫描（写操作/管理操作——路由表枚举）；② 审计中间件覆盖校验（每个敏感路由有审计——SCN-NODE-775）；③ 审计字段完整性（operator/action/target——SCN-OPS-220 要素）；④ 缺口清单（哪些接口缺审计——修复清单）。
- 边界：① 敏感操作的定义（写操作默认敏感——fail-closed）；② 路由枚举的来源（express router 栈——自动化提取）；③ 覆盖率报告（CI——SCN-OPS-289 跑数据）。

**答**：
```javascript
function auditCoverage(routerStack) {
  const sensitive = routerStack.filter(r =>
    ['POST', 'PUT', 'DELETE'].includes(r.method) || isAdminPath(r.path));   // fail-closed（SCN-NODE-775）
  const uncovered = sensitive.filter(r => !r.middleware.includes('audit'));
  const fieldIssues = auditRoutes().filter(r =>
    !['operator', 'action', 'target', 'ts'].every(f => f in r));   // 要素完整性（SCN-OPS-220）
  return {
    coverage: 1 - uncovered.length / sensitive.length,
    uncovered: uncovered.map(r => ({ path: r.path, method: r.method,
      fix: '加 audit 中间件（SCN-NODE-775）' })),
    fieldIssues,
    ci: '覆盖率 < 100% 阻断发布（SCN-OPS-289 跑数据）',
  };
}
```

**评分点**:
- fail-closed 敏感操作定义（写操作默认敏感——SCN-NODE-775）。
- 路由栈自动枚举（express router——自动化）。
- 要素完整性校验（SCN-OPS-220 四要素）。
- CI 覆盖率门禁（SCN-OPS-289）。
