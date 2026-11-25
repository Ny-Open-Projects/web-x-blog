---
title: [MFW-543] 预取协调：Link 预取策略与 Router 的预算管理
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-543：Link 预取策略与 Router 预取预算

**答**:
- Link 预取的默认策略：视口内自动 prefetch（IntersectionObserver——RBL-769）+ hover 触发（未视口）；prefetch={null} 跟随全局配置（生产默认开 dev 关）。
- 预取内容的分层（App Router）：静态路由 → prefetch 完整 RSC payload；动态路由 → 只 prefetch「到 loading.js 的边界」（不含数据——骨架预取：导航即显骨架 + 流式数据）——「预取深度 = 静态性」：越静态预取越完整。
- 预取预算（RBL-769 的框架内建版）：视口内 Link 数量爆炸（长列表 500 Link）→ 预取风暴——框架内部并发限制 + 队列；「长列表的预取税」与 Bandwidth 竞争（RBL-895 命中率校准）。
- prefetch={false} 的语义：hover 时才拉（视口不自动）——交互意图明确才花流量。
- 追问钩子：为什么动态路由的预取「只到 loading 边界」？——动态 payload 含每用户数据（预取 = 为不存在的用户拉数据——浪费 + 隐私）；「骨架预取」= 导航瞬时反馈（loading.js 骨架秒显）+ 数据流式——预取的「内容分层」由数据性质决定：静态内容可完整预取、个性化内容只预取结构——预取预算的资源分配（RBL-765）框架化了。

```javascript
// Link 预取策略矩阵
<Link href="/about" prefetch={true} />                   // 静态：完整 payload
<Link href="/product/1" />                               // 动态：prefetch 到 loading 边界
<Link href="/search" prefetch={false} />                 // hover 才拉
// app/router 配置：prefetch 全局开关 + 并发预算
// 长列表的预取税控制
function ProductRow({ id }) {
  return <Link href={`/p/${id}`} prefetch={null}>        // 跟随全局（视口内自动）
    <Image src={thumb} />                                 // 500 行 = 500 预取请求
  </Link>;                                               // 框架内部并发限制保护
}
// 验收测试：导航即骨架（预取了 loading 边界）
test('instant skeleton', async ({ page }) => {
  await page.goto('/shop');
  const t0 = Date.now();
  await page.click('text=商品A');
  await page.waitForSelector('[data-loading="product"]', { timeout: 100 });
  // loading 边界预取命中：骨架 < 100ms
});
```
