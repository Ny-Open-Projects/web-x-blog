---
title: [MFW-215] TanStack Start 的 Server Functions 与 Next Server Actions 对比
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-215：TanStack Start Server Functions vs Next Actions

**答**:
- 共同目标：同文件写前后端（编译器拆分到 server/client 两个 bundle）——开发体验同源
- 差异一：显式性——Start 的 createServerFn 显式声明 server-only 边界（.validator/.handler 链式），Next 的 'use server' 是文件/函数级标记（隐式拆分，误标记风险靠 lint）
- 差异二：生态位——Start 深度集成 TanStack Query/Router（invalidation 与路由 loader 一体），Next Action 与 App Router 缓存体系（revalidateTag）绑定
- 差异三：RPC 形态——Start 生成类型安全 RPC 客户端（调用即类型检查），Next 是 opaque 引用序列化（参数受序列化限制相同）
- 选型：TanStack 全家桶用户 Start 更顺；App Router 深度用户（RSC 树/ISR）留在 Next

```javascript
// TanStack Start：显式链式声明
export const createUser = createServerFn({ method: 'POST' })
  .validator(z.object({ name: z.string() }))         // 显式入参校验
  .handler(async ({ data }) => db.user.create(data))
// 调用（类型安全 RPC）
const { data } = await useMutation({ fn: createUser })
```
