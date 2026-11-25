---
title: [MFW-227] Server Function 的序列化边界（能传什么不能传什么）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-227：Server Function 序列化边界

**答**:
- 可传：JSON 兼容值 + React Server Components 专属扩展（Date/Map/Set/Promise（流式）/BigInt——RSC 序列化协议比 JSON 宽）
- 不可传：函数（闭包）、class 实例（原型链丢失变普通对象）、Symbol、循环引用
- 安全边界：客户端传来的任何参数都是不可信输入——Action 必须带 schema 校验（zod）+ 鉴权检查在 handler 内（「客户端 import 了 server 函数」不等于「有权限调用」——高发误区）
- 闭包捕获陷阱：'use server' 函数体内引用外部变量必须是可序列化值（编译器会转成参数）——捕获复杂对象会构建期报错（好消息：报错早）

```javascript
// 安全边界模板
const update = createServerFn({ method: 'POST' })
  .validator(z.object({ id: z.string().uuid(), qty: z.number().int().min(1) }))
  .handler(async ({ data }) => {
    const user = await requireUser()            // 权限在 handler 内校验
    if (!canWrite(user, data.id)) throw new Error('403')
    return db.order.update(data)
  })
```
