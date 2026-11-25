---
title: [MFW-226] Next.js Middleware 的执行模型与限制清单
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-226：Middleware 执行模型与限制

**答**:
- 模型：Edge Runtime 每请求执行（路由匹配前）——轻量 V8 isolate，无 Node API；matcher 配置缩小触发面（省冷启动与费用）
- 能做：改写/重定向请求头、A/B 分流（cookie sticky）、鉴权前置校验、geo 路由——「请求级路由决策」都归它
- 不能做/限制：无文件系统/大内存、执行时长毫秒级（50ms 预算意识）、不能访问 DB（边缘无连接——用轻量 KV/JWT 本地校验）、Subrequest 数有限
- 设计原则：Middleware 只做「快且必须前置」的决策（<10ms）；慢逻辑（DB 查询鉴权）下沉到 RSC/Route Handler——Middleware 塞重是性能事故高发区

```javascript
export const config = { matcher: ['/app/:path*', '/api/secret'] }   // 缩面
export function middleware(req) {
  const token = req.cookies.get('session')?.value
  if (!verifyJwtLocal(token)) return redirect('/login')   // JWT 本地校验（不查 DB）
}
```
