---
title: [ARC-235] 权限模型迁移：从硬编码 if-else 到 RBAC 怎么落地？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-235：权限模型迁移：从硬编码 if-else 到 RBAC 怎么落地？
**答**：
- 现状盘点：全仓库扫 `role ===`、`isAdmin` 等硬编码点位，按资源域聚类产出"事实权限清单"——先承认现状再建模。
- 迁移策略（绞杀者模式）：新代码一律走 `can()` 引擎；存量按"改一次顺手迁一个"推进，不动的地方包一层兼容谓词（isAdmin() 内部查快照），让硬编码表达式语义不变但数据源换掉。
- 对齐验证期：新旧并行（影子判定）——can() 结果与旧硬编码结果不一致时上报，人工确认是"旧逻辑错"还是"建模错"，归零后删旧代码。
- 切换开关：按域灰度启用 RBAC 判定，出问题一键回退硬编码。

```typescript
// 兼容谓词：旧代码不动，数据源已换
export function isAdmin(): boolean { return can(store.snap, 'admin', 'platform'); }
// 影子判定
function shadow(old: boolean, resource: string, action: string) {
  const neo = can(store.snap, action, resource);
  if (neo !== old) report('perm-shadow-diff', { resource, action, old, neo }); // 人工归因
  return old;                                    // 迁移期以旧为准
}
// 灰度开关：config.useRbacFor('order') ? can(...) : legacyCheck(...)
```
