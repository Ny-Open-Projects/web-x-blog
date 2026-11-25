---
title: [MFW-747] RSC 的纯 HTML 模式
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-747：RSC 的纯 HTML 模式

**答**:
- RSC 的纯 HTML 模式：1) **无 JS 渲染**（RSC 的 HTML 完全可交互——form 原生提交 RBL-512、链接原生导航——零 JS 的页面也能完成核心功能）；2) **渐进增强**：JS 加载 → 水合 → 交互增强；JS 未加载 → 原生 HTML（form/link/锚点——每个交互都有无 JS 回退）；3) **纯 HTML 的测试**（JS 禁用的 Playwright 测试——核心功能验证（RBL-549 的 JS 禁用矩阵）。
- RSC 纯 HTML 的边界：1) **需要 JS 的交互**（拖拽/实时更新/复杂状态——需要 client 组件——纯 HTML 无法覆盖）；2) **无 JS 的降级形态**：表单提交（整页刷新——结果页）、搜索（URL 参数——SSR 结果页）、导航（原生 <a>——硬导航）；「无 JS 的体验降级」= 可用但体验差（整页刷新 vs 软导航——功能等价但速度差）。
- 追问钩子：为什么「纯 HTML 模式」是 RSC 相比 SPA 的最大架构优势？——SPA = 100% 依赖 JS（无 JS = 白屏——核心功能全部不可用）；RSC = server 渲染 HTML（form/link 原生——无 JS 也能完成任务）；「渐进增强的架构保障」：RSC 的 server 优先设计让 HTML 天然完整（不是事后补的 SSR——架构级的渐进增强）；JS 禁用测试 = 可用性的底线验证（RBL-724 分层产物的核心层验证）。

```tsx
// 纯 HTML 可用的 RSC 页面
export default async function ProductsPage({ searchParams }) {
  const products = await searchProducts(searchParams.q);
  return (
    <>
      <form action="/products" method="GET">              {/* 原生搜索：无 JS 可用 */}
        <input name="q" defaultValue={searchParams.q} />
        <button>Search</button>
      </form>
      <ul>
        {products.map(p => (
          <li key={p.id}>
            <a href={`/p/${p.id}`}>{p.name}</a>           {/* 原生链接：无 JS 导航 */}
            <form action={addToCartAction}>               {/* server action：无 JS 提交 */}
              <input type="hidden" name="id" value={p.id} />
              <button>Add to Cart</button>
            </form>
          </li>
        ))}
      </ul>
    </>
  );
}
// Playwright JS 禁用测试（RBL-549）
test('works without JS', async ({ browser }) => {
  const ctx = await browser.newContext({ javaScriptEnabled: false });
  const page = await ctx.newPage();
  await page.goto('/products');
  await page.fill('[name="q"]', 'laptop');
  await page.click('button:has-text("Search")');          // 原生提交
  await page.waitForURL('/products?q=laptop');            // URL 驱动
  await page.waitForSelector('text=laptop');              // SSR 结果
});
```
