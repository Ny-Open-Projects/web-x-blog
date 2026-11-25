---
title: [WCN-329] 自定义元素的 SEO 保障（爬虫能看到内容吗）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-329：自定义元素的 SEO 保障（爬虫能看到内容吗）？
**答**：
- DSD 直出 → 内容在 HTML 源码里 → 爬虫可读（主流方案）。
- 客户端注册渲染（无 DSD）→ 爬虫看到空标签——SEO 敏感页面必须 DSD。
- 语义补强：关键内容（标题/价格）同时出现在 light DOM 或 meta/schema（双保险）。
- 验证：curl 源码快照断言核心字段 + Search Console 抓取监控。

```javascript
test('SEO 可读', async ({ request }) => {
  const html = await (await request.get('/goods/1')).text();
  expect(html).toContain('<template shadowrootmode="open">');  // DSD 直出
  expect(html).toMatch(/商品核心标题/);
});
r
```
