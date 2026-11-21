---
title: [RBL-477] 笔试：手写增量式 E2E 选择
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-477：手写增量式 E2E 选择
**需求**：实现 `selectE2E(changedFiles, coverage)`：1) coverage：路由/页面 → E2E 用例映射 + 页面→模块依赖映射（预计算）；2) 选择：变更模块 → 影响页面 → 对应 E2E；3) 保守规则：路由级配置变更 → 该路由全部用例；全局资源（layout/公共组件）→ 全量 E2E（保守正确）；4) 用例优先级：冒烟集必跑（即使无变更——核心路径守门）+ 变更集增量；5) 输出 { mustRun: smoke, selected: [], reason: Map }（选择可解释）；6) 假阴性追踪：增量 E2E 通过但全量失败的案例统计（覆盖率索引修正依据）。

```javascript
export function selectE2E(changedFiles, coverage, { globalPatterns = ['layout', 'common'] } = {}) {
  const changed = new Set(changedFiles)
  const reason = new Map()
  const selected = new Set()

  // 全局资源 → 全量（保守正确）
  if (changedFiles.some((f) => globalPatterns.some((g) => f.includes(g)))) {
    coverage.e2e.forEach((t) => { selected.add(t.id); reason.set(t.id, 'global resource changed') })
    return { mustRun: [], selected: [...selected], reason, fullRun: true }
  }

  // 模块 → 页面 → E2E
  const affectedPages = new Set()
  for (const page of coverage.pages) {
    if (page.modules.some((m) => changed.has(m))) affectedPages.add(page.route)
  }
  for (const t of coverage.e2e) {
    if (t.routes.some((r) => affectedPages.has(r))) {
      selected.add(t.id)
      reason.set(t.id, `covers affected route: ${t.routes.find((r) => affectedPages.has(r))}`)
    }
  }
  // 配置变更 → 路由全量
  for (const t of coverage.e2e)
    if (t.routeConfigFiles?.some((c) => changed.has(c)) && !selected.has(t.id)) {
      selected.add(t.id); reason.set(t.id, 'route config changed')
    }

  return { mustRun: coverage.smoke, selected: [...selected], reason, fullRun: false,
    note: '假阴性追踪：增量通过但全量失败 → 修正 coverage 索引（对齐驱动）' }
}
```
**评分点**：
- 三级选择（全局资源全量 / 页面级增量 / 冒烟必跑——保守性与速度平衡）
- 路由配置变更 → 路由全量（配置影响跨页面）
- reason 可解释（每个用例为什么被选中）
- 假阴性追踪闭环（增量漏测案例 → 修正 coverage 索引——增量体系的自校准）
