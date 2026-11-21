---
title: [MFW-262] generateMetadata 与页面数据的缓存协同
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 笔试题
---

## MFW-262：generateMetadata 缓存协同

**答**:
- 双取问题：页面与 metadata 各自 fetch 同一资源（两次请求）——React 对同 URL+同选项的 fetch 自动去重（同渲染 pass 内）——但选项不同（不同 tag）就取两次
- 统一姿势：数据函数单例化（queryOptions 工厂——同 key 同选项），页面与 metadata 都调它——自动去重 + tag 一致（失效同步）
- SEO 数据新鲜度：metadata 常被 CDN 长缓存（爬虫视角）——页面改版但 title/og 旧——metadata 的 fetch 单独设短 revalidate 或与页面同 tag（一起失效）
- 动态 OG 图：ImageResponse 生成成本高——缓存产物（params hash key）+ CDN 长 cache（不变内容不重算）

```javascript
// 单例数据源
const productQuery = (id) => ({
  queryKey: ['product', id],
  queryFn: () => fetch(`/api/p/${id}`, { next: { tags: [`p:${id}`] } }).then(r=>r.json()),
})
export async function generateMetadata({ params }) {
  const d = await getProduct(params.id)          // 与页面同源去重
  return { title: d.title, openGraph: { images: [ogUrl(params.id)] } }   // og 图：params hash 缓存
}
```
