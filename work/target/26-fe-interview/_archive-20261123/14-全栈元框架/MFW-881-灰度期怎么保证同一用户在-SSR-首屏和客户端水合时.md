---
title: [MFW-881] 灰度期怎么保证同一用户在 SSR 首屏和客户端水合时看到同一实验变体
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-881：灰度期怎么保证同一用户在 SSR 首屏和客户端水合时看到同一实验变体

**答**：
- 结论：分桶必须在服务端决定并通过 cookie 固化，SSR 与客户端读同一个 cookie 值；绝不能两端各自用随机数分桶，否则水合时变体不一致导致闪变甚至 hydration 错误。
- 落地：Middleware 或 RSC 首次分桶写入 cookie（如 exp= B），后续服务端渲染和客户端 hydration 都读该 cookie。
- 追问钩子：首次访问没有 cookie 怎么办？——服务端先分桶并随响应 Set-Cookie，客户端首次渲染沿用服务端结果。

```javascript
// Middleware：分桶并固化到 cookie
export function middleware(req) {
  let variant = req.cookies.get('exp')?.value;
  if (!variant) {
    variant = assign(req.cookies.get('uid') || req.ip, ['A', 'B']);
    const res = NextResponse.next();
    res.cookies.set('exp', variant, { maxAge: 86400 }); // 固化
    return res;
  }
  return NextResponse.next();
}
// 服务端与客户端都读 req.cookies exp，保证一致
function getVariant(req) { return req.cookies.get('exp')?.value || 'A'; }
```
