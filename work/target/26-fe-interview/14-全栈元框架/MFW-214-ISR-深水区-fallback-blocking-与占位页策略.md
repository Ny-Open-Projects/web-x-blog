---
title: [MFW-214] ISR 深水区：fallback blocking 与占位页的取舍
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-214：fallback blocking 与占位页

**答**:
- dynamicParams/fallback 三态：blocking（首请求等渲染——SEO 完整但首访慢）、true（先占位页后填充——快但首内容可能空）、false（未知路径 404——白名单模式）
- 选择：SEO 关键页（商品详情被爬虫抓）用 blocking；内部页面/低频页用占位；强制白名单（内容审核后可见）用 false
- blocking 的变体：generateStaticParams 预渲染热门子集 + 剩余 blocking——预渲染与按需的平衡
- 深坑：blocking 页面的构建期数据获取失败会传染整个构建（generateStaticParams 阶段炸全 build）——params 数据源要容错（单页失败跳过该 params 不炸全局）

```javascript
export async function generateStaticParams() {
  try {
    const hot = await fetchTopProducts(100)         // 只预渲染热门 100
    return hot.map((p) => ({ slug: p.slug }))       // 失败返回 [] 不炸构建
  } catch { return [] }                             // 容错：params 源失败不传染
}
export const dynamicParams = true                  // 其余按需 blocking
```
