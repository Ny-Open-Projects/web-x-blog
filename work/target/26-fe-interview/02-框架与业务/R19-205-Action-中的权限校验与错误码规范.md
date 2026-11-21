---
title: [R19-205] Server Action 中的权限校验与错误返回规范怎么设计？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-205：Server Action 中的权限校验与错误返回规范怎么设计？
**答**：
- 每个 action 入口先做鉴权（session 校验），不信任客户端传来的 userId——从 session 取。
- 错误返回统一结构：`{ ok: false, code, fieldErrors }` 或 throw createError；用 useActionState 的 state 承载，别靠异常穿透到用户。
- 幂等：写操作要求客户端带 requestId（FormData 隐藏字段），服务端按 id 去重，防双击/重试重复下单。
- 审计：action 内记录操作日志（who/what/when），出问题可追溯。
- 限速：高频 action（发评论）加服务端 rate limit，防脚本刷接口。
```javascript
'use server'
export async function createOrder(prev, formData) {
  const user = await auth()
  if (!user) return { ok: false, code: 'UNAUTHORIZED' }
  const requestId = formData.get('requestId')
  if (await isDuplicate(requestId)) return { ok: false, code: 'DUPLICATE' }
  // ...
}
```
