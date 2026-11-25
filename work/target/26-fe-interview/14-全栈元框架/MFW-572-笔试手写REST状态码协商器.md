---
title: [MFW-572] 笔试：手写 REST 状态码协商器（CRUD 语义映射）
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-572：笔试：手写 REST 状态码协商器

**答**：实现 `restResponse(method, ctx)`。ctx: `{ found, valid, authorized, conflict, payload }`。规则映射：1) 未授权 → 401（无凭证）/403（有凭证无权限——authorized=false 且有 session）；2) 404：资源不存在（任何方法）；3) 校验失败 → 422；冲突 → 409；4) 成功：GET → 200+payload；POST 创建 → 201+payload；PATCH → 200+payload；DELETE → 204（无体）；5) 优先级：auth > 404 > validation > conflict > success。返回 `{ status, body? }`。边界：payload 为 undefined 时 201/200 仍可返回（body null）；DELETE found=false 也 404。

```javascript
function restResponse(method, ctx = {}) {
  const { found = true, valid = true, authorized = true, hasSession = false,
    conflict = false, payload } = ctx;
  if (!authorized) return { status: hasSession ? 403 : 401 };      // 权限分级
  if (!found) return { status: 404 };
  if (!valid) return { status: 422 };
  if (conflict) return { status: 409 };
  switch (method.toUpperCase()) {
    case 'GET': return { status: 200, body: payload ?? null };
    case 'POST': return { status: 201, body: payload ?? null };
    case 'PATCH': case 'PUT': return { status: 200, body: payload ?? null };
    case 'DELETE': return { status: 204 };               // 无体
    default: return { status: 405 };                     // 方法不支持
  }
}

// 自测
// 读成功
console.log(restResponse('GET', { payload: { id: 1 } }))
  .status === 200);
// 创建 → 201
console.log(restResponse('POST', { payload: { id: 2 } }).status === 201);
// 删除 → 204 无体
const d = restResponse('DELETE', {});
console.log(d.status === 204 && d.body === undefined);
// 未认证 vs 无权限
console.log(restResponse('GET', { authorized: false, hasSession: false }).status === 401);
console.log(restResponse('GET', { authorized: false, hasSession: true }).status === 403);
// 优先级：auth > 404
console.log(restResponse('GET', { authorized: false, found: false }).status === 401);
// 404 > 校验
console.log(restResponse('POST', { found: false, valid: false }).status === 404);
// 422 vs 409 顺序按声明（valid 先）
console.log(restResponse('POST', { valid: false, conflict: true }).status === 422);
console.log(restResponse('POST', { valid: true, conflict: true }).status === 409);
// 不支持的方法
console.log(restResponse('TRACE', {}).status === 405);
```

**评分点**：
- 优先级链正确（auth > 404 > 422 > 409 > success——安全优先于资源语义）
- 401/403 的区分（凭证有无——认证与授权分离）；204 无体语义
- 405 兜底（方法不支持——REST 语义完整性）；边界
- 能说清「REST 状态码是错误分级协议（422 语义校验 vs 400 语法错误 vs 409 冲突）——客户端按码分支而非解析 body」属于加分
