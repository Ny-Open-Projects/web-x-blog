---
title: [NODE-484] Node 服务内部 API 的权限粒度（服务级/接口级/数据级）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-484：内部 API 权限粒度
**答**:
- 三层粒度：服务级（调用方准入：服务 A 能不能调服务 B——注册表 + mTLS 身份 NODE-369）、接口级（接口声明允许的调用方角色：内部读/内部写/管理）、数据级（行级权限：调用方携带的用户上下文的资源归属校验 NODE-361）。
- 接口级实现：接口注解（@internal('trade:read')）→ 中间件按调用方服务身份 + 接口要求校验；调用方角色登记（服务注册时声明权限需求，审批后授予——最小权限）。
- 数据级红线：内部调用必须透传用户上下文（x-internal-user NODE-369），数据权限在数据层强制（NODE-361/395）——"内部服务"不是越权借口。
- 治理：权限矩阵审计（服务 × 接口 的授权矩阵定期 review——僵尸授权清理）、越权尝试告警（403 事件按调用方聚合）、权限申请流程（自助申请 + owner 审批）。
- 防滥用：管理类接口（数据修复/配置）单独角色 + 双人授权（NODE-451 危险操作对齐）。
```javascript
// 接口级权限注解
router.get('/internal/stock/:sku', requireInternal('inventory:read'), handler);
router.post('/internal/stock/adjust', requireInternal('inventory:write', { dual: true }), handler); // 高危双人
// requireInternal：校验调用方服务身份 ∈ inventory:read 授权清单 → 403 记审计
```
