---
title: [ARC-221] RBAC 数据权限如何与前端权限模型融合？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-221：RBAC 数据权限如何与前端权限模型融合？
**答**：
- RBAC 管"操作权限"（能否点删除），数据权限管"行范围"（只能看华东区的订单）。前端两者都要表达，否则会出现"有按钮但列表全是空的"这种割裂体验。
- 融合模型：权限码扩展为 `resource:action:scope`（如 `order:read:region-huadong`），后端下发**用户可见的资源过滤条件**而非数据本身；前端把它转成查询参数与 UI 提示。
- 前端职责边界：前端只做**体验层**过滤（默认带条件、隐藏无权筛选选项），**安全判定永远在后端**——前端过滤只是防误操作，防不了绕过。
- 体验要点：无权行不渲染"假置灰"而是整行隐藏或提示"仅可见你负责的 32 条"；数据范围选择器由权限元数据驱动生成。

```typescript
// 权限元数据驱动的数据范围
interface DataScopeMeta { resource: string; field: string; allowed: string[] } // 后端下发
const scope: DataScopeMeta = { resource: 'order', field: 'region', allowed: ['huadong', 'huanan'] };

// 列表查询：强制带上范围条件（用户改不掉）
function buildQuery(userInput: Query) {
  const q = { ...userInput, [scope.field]: intersect(userInput[scope.field], scope.allowed) };
  return q; // intersect 保证用户筛选 ⊆ 权限范围
}
// 筛选 UI：范围选择器只渲染 allowed 的选项，无权项不展示
const regionOptions = allRegions.filter(r => scope.allowed.includes(r.value));
// 后端兜底：接口层同样校验，前端条件可被篡改——前端只为体验
```
