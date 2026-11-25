---
title: [MFW-583] 元框架的 A/B 测试：实验路由的产物策略
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-583：A/B 测试的产物策略

**答**:
- A/B 的三层实现：1) **middleware 分流**（cookie 写实验组 → rewrite 到变体路由（/p vs /p-b）——URL 层变体：独立路由独立缓存 RBL-888 分流的 Next 版）；2) **组件级变体**（server 侧读 cookie → 条件渲染变体组件——同 URL 两变体：缓存键含变体（cookie 进缓存键 = 路由动态化 RBL-510 的权衡——PPR 后洞级变体）；3) **client 变体**（SDK 分流——client 条件渲染：无 SSR 个性化但缓存友好）。
- 变体的缓存策略：URL 变体（/p-b 独立 URL）→ CDN 缓存独立（缓存友好但 URL 非规范——canonical 处理）；cookie 变体 → 缓存键含变体（CDN 需按 cookie 分桶缓存——Vary: cookie 或放弃 CDN）；「变体实现的缓存代价」是 A/B 架构的核心权衡。
- 实验的生命周期：实验结束 → 败者代码清理（RBL-798 清偿清单的元框架版：变体路由/组件删除 + 分流逻辑摘除）。
- 追问钩子：为什么「middleware + URL 变体」在缓存与 SEO 上最优？——URL 变体 = 变体有独立 URL → CDN 缓存独立键（变体页面可静态缓存）；cookie/组件变体 = 缓存键污染（CDN 缓存按 URL——同 URL 两内容 = 缓存串变体）；SEO：URL 变体的 canonical 指向控制组（避免重复内容）——「实验变体的可寻址性」决定缓存与 SEO 的健康度（RBL-548 locale URL 同理）。

```javascript
// middleware 分流（URL 变体）
export function middleware(req) {
  const exp = getExperiment('checkout-v2', req);         // cookie 分桶（稳定）
  if (exp === 'b' && req.nextUrl.pathname === '/checkout')
    return NextResponse.rewrite(new URL('/checkout-b', req.url));   // 变体路由
}
// app/checkout/page.tsx（control）与 app/checkout-b/page.tsx（treatment）
// 两条独立路由：独立缓存/独立画像（RBL-561）
// canonical：变体页 → 指向 control（SEO 去重）
// app/checkout-b/page.tsx
export const metadata = { alternates: { canonical: '/checkout' } };
// 组件级变体（server 读 cookie）
export default async function Page() {
  const variant = (await cookies()).get('exp')?.value ?? 'a';
  return variant === 'b' ? <NewCheckout /> : <OldCheckout />;
  // 代价：cookies() → 动态化路由（缓存失效——PPR 后可洞级）
}
// 实验清偿清单
const CLEANUP = ['checkout-b 路由删除', 'middleware 分流摘除', '实验 SDK 配置删除'];
```
