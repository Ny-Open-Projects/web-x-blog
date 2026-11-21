---
title: [MFW-202] RSC 边界案例：流式渲染中 session 过期的竞态
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-202：流式渲染中 session 过期的竞态

**答**:
- 场景：Shell 已流式输出（headers 已发），后续 Suspense 段里 session 过期——不能再 302 重定向（headers 已发送），会出现「页面渲染一半跳不回登录」
- 正确姿势：流式段内过期 → 返回客户端可处理的错误信号（RSC 抛出结构化错误 → 客户端 error boundary 或 useActionState 接管跳转）；或 Middleware 层前置校验（流式开始前拦截）
- 前置校验的最佳位置：Middleware（cookie 校验毫秒级）——比渲染段内发现过期体验好得多
- 设计原则：不可逆操作（重定向/清 cookie）必须在响应开始前决策；响应开始后只能做「客户端可感知的软信号」

```javascript
// middleware.ts：流式前拦截
export function middleware(req) {
  if (!req.cookies.get('session') && isProtected(req.nextUrl.pathname))
    return NextResponse.redirect('/login')
}
// 渲染段内（兜底）：软信号
async function PrivateData() {
  const session = await getSession()
  if (!session) throw new AuthExpiredError()      // 客户端 error boundary 接管跳转
  return <Data />
}
```
