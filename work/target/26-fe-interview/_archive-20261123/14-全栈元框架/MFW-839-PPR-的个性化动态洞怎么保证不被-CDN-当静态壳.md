---
title: [MFW-839] PPR 的个性化动态洞怎么保证不被 CDN 当静态壳缓存
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-839：PPR 的个性化动态洞怎么保证不被 CDN 当静态壳缓存

**答**：
- 结论：洞内容必须标记 private / 带 Vary(cookie, authorization)，且不能进 Full Route Cache；静态壳缓存只含占位、不含洞数据。
- 落地：洞用独立 fetch（cache: no-store）获取，响应头 Cache-Control: private, no-store；壳与洞在 RSC payload 中分块传输。
- 追问钩子：洞数据误入共享缓存会怎样？——越权泄露，A 用户的订单信息出现在 B 用户的壳里。

```javascript
// 壳：可共享缓存（public）
async function Shell() {
  return <Suspense fallback={<Skeleton/>}><Hole/></Suspense>;
}
// 洞：个性化数据，绝不共享
async function Hole() {
  const res = await fetch('/api/me/orders', { cache: 'no-store' });
  return <Orders data={await res.json()} />;
}
// Route Handler 兜底：明确私有 + Vary
export async function GET() {
  return NextResponse.json(await getOrders(), {
    headers: { 'Cache-Control': 'private, no-store', Vary: 'Cookie, Authorization' }
  });
}
```
