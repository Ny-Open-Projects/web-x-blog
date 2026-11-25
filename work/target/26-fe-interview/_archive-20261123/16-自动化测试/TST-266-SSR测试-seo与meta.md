---
title: [TST-266] SSR 的 SEO 相关断言（meta/结构化数据/可爬性）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-266：SSR 的 SEO 相关断言（meta/结构化数据/可爬性）？
**答**：
- 关键 meta 断言：title/description/og 标签按页面数据生成（模板渲染正确）。
- 结构化数据：JSON-LD 输出 schema 校验（商品/面包屑 schema.org 合法）。
- 可爬性：首屏 HTML 含核心内容（不依赖 JS 执行）、hreflang/canonical 正确。
- 回归防护：每次改 SSR 模板跑 SEO 快照断言（关键标签快照对比）。

```javascript
test('商品页 SEO', async ({ request }) => {
  const html = await (await request.get('/goods/1')).text();
  expect(html).toContain('<meta property="og:title" content="...商品名..."');
  const ld = extractJSONLD(html);
  expect(ld['@type']).toBe('Product');
});
r
```
