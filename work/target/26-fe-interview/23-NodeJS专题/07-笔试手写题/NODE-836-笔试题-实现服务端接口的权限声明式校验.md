---
title: [NODE-836] 笔试题——实现权限声明式校验（装饰器 + 矩阵）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-836：手写权限校验

**需求与边界**：
- 需求：声明式权限（SCN-OPS-609/643）——① 权限装饰器（@require('order:read')——路由声明）；② 权限矩阵校验（角色×动作——SCN-OPS-609）；③ 数据范围校验（部门/租户——SCN-OPS-643 deny 原因码）；④ 权限缓存（同用户同请求缓存——SCN-NODE-742 memoize）。
- 边界：① deny 结构化（原因码可展示——SCN-OPS-643）；② 权限与租户上下文合并（SCN-NODE-745）；③ 权限变更即时生效（缓存失效——SCN-FIN-688）。

**答**：
```javascript
const PERMISSIONS = { approver: ['order:read', 'order:approve'], auditor: ['order:read'] };
function requirePermission(action) {
  return (req, res, next) => {
    const user = ctx.getStore()?.user;
    const role = resolveRole(user, ctx);
    const matrix = PERMISSIONS[role];
    const allowed = matrix?.includes('*') || matrix?.includes(action);   // SCN-OPS-609 矩阵
    if (!allowed) return res.status(403).json({ code: 'PERM_DENIED', reason: 'NO_ROLE' });   // deny 结构化（SCN-OPS-643）
    if (action === 'order:read' && ctx.getStore()?.tenant !== req.params.tenant)
      return res.status(403).json({ code: 'OUT_OF_SCOPE', reason: '跨租户' });   // 数据范围（SCN-OPS-643）
    next();
  };
}
router.get('/orders/:id', auth(), requirePermission('order:read'), handler);   // 声明式
```

**评分点**:
- 装饰器声明式（路由声明——SCN-OPS-609）。
- 数据范围校验（跨租户 deny——SCN-OPS-643）。
- deny 结构化原因码（可展示——SCN-OPS-643）。
- 与租户上下文合并（SCN-NODE-745）。
