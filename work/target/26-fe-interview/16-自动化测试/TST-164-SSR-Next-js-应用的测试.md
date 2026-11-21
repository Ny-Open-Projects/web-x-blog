---
title: [TST-164] SSR / Next.js 应用的测试有什么不同？策略怎么定？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-164：SSR / Next.js 应用的测试有什么不同？策略怎么定？
**答**：
- 多出来的测试维度：① 服务端渲染结果正确（SEO 关键）；② hydration 一致性（服务端 HTML 与客户端首次渲染必须一致，不一致白屏/告警）；③ `getServerSideProps`/Server Actions 的数据层逻辑；④ 依赖 window 的代码在服务端路径不炸。
- 分层策略：页面组件拆「服务端数据函数」与「纯展示组件」——数据函数用 node 环境单测（mock fetch/db，测缓存策略、错误分支）；展示组件用 RTL 正常测；整页 SSR + hydration 用 E2E 管（真实 Next server 起来，断言 SSR 返回的 HTML 含关键内容 + 交互正常）。
- hydration 一致性测试：Playwright 里先禁 JS（SSR-only）抓 HTML 片段，再启用 JS 后抓 DOM，对比关键节点——这是能自动化的「水合漂移」检查；日常更实际的做法是把 React hydration error 当 CI 阻断（console error 检测）。
- 环境隔离要点：单测里 `typeof window === 'undefined'` 分支要显式覆盖；MSW 在 node 环境拦服务端 fetch（`setupServer` 天然支持）；Next 的 `next build && next start` 做真产物验证，别用 dev server 跑 E2E。
- 追问钩子：流式渲染（App Router RSC + Suspense）怎么测？——断言「骨架先出现、最终内容到位」两段式，别断言一次到位。

```javascript
// E2E：SSR 输出 + hydration 双重验证
test('商品页 SSR 有关键内容且 hydration 后可交互', async ({ page, browser }) => {
  // 1) 禁 JS：验证服务端直出（SEO 视角）
  const nojs = await browser.newContext({ javaScriptEnabled: false });
  const html = await (await nojs.newPage()).goto('/goods/1')
    .then((r) => r.text());
  expect(html).toContain('商品标题 SEO 关键词');
  await nojs.close();

  // 2) 启用 JS：hydration 后可交互
  await page.goto('/goods/1');
  await page.getByRole('button', { name: '加入购物车' }).click();
  await expect(page.getByText('已加入')).toBeVisible();
});
```
