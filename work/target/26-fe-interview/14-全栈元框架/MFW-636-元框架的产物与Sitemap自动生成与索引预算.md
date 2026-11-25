---
title: [MFW-636] Sitemap 自动生成与索引预算
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-636：Sitemap 自动生成与索引预算

**答**:
- 大站 sitemap 的工程：1) **分片 sitemap**（50000 URL/片上限——sitemap index 索引片：sitemap.xml → sitemap-1.xml...）；2) **生成来源**（路由清单 × 数据（商品页 = 路由模板 × 商品 id——DB 驱动）；3) **索引预算**（搜索引擎抓取配额——sitemap 的优先级/lastmod 信号：lastmod 准确（RBL-595 增量构建的 meta 复用：变更时间戳）——「乱更新 lastmod = 爬虫信任下降」）。
- sitemap 的一致性：声明的 URL 必须可渲染（RBL-839 死链——sitemap 声明 404 = 爬虫信任损失）；「sitemap 与路由对账」（RBL-535 reconcile）。
- 元框架的集成：Next 的 MetadataRoute（app/sitemap.ts → 生成函数）；「动态 sitemap」：route handler 动态生成（数据驱动——构建期 vs 请求时的选择：百万页请求时生成（DB 查询）+ 缓存；千页构建期生成）。
- 追问钩子：为什么「lastmod 的准确性」比「URL 全量覆盖」更影响抓取效率？——爬虫用 lastmod 决定「重新抓取优先级」：乱填 lastmod（每次构建都改）→ 爬虫信任下降（抓取配额重新评估——全站抓取变慢）；准确的 lastmod = 爬虫只抓变化页（抓取预算的高效利用）；「sitemap 是与爬虫的契约」：契约的可信度 = 抓取效率——信号的质量 > 信号的数量。

```typescript
// app/sitemap.ts
import { MetadataRoute } from 'next';
export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const products = await db.products.findMany({ select: { id: true, updatedAt: true } });
  return [
    ...staticRoutes.map(path => ({ url: BASE + path, changeFrequency: 'weekly' })),
    ...products.map(p => ({ url: `${BASE}/p/${p.id}`, lastModified: p.updatedAt,   // 准确 lastmod
      priority: p.popularity > 0.8 ? 1.0 : 0.5 })),    // 流量加权优先级
  ];
}
// 分片（>50000）
function splitSitemap(urls, { perFile = 45000 } = {}) {
  return urls.reduce((acc, u, i) => {
    (acc[Math.floor(i / perFile)] ??= []).push(u); return acc;
  }, []).map((chunk, i) => ({ file: `sitemap-${i + 1}.xml`, urls: chunk }));
}
```
