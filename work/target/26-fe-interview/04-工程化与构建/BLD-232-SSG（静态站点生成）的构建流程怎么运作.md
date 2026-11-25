---
title: [BLD-232] SSG 的构建流程怎么运作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-232：SSG 构建流程怎么运作？
**答**：
- 流程：路由枚举（静态路由 + 动态路由 getStaticPaths）→ 每路由数据获取 → SSR 渲染 HTML → 写盘 → 资产与 HTML 关联（hydration chunk）。
- 构建时长治理：路由数大时并行渲染（worker 池）+ 增量 SSG（只重建变更路由——内容 hash 键控，ISG 增量静态再生成）。
- 数据获取的构建期约束：构建时接口必须稳定（构建期数据快照——内容变更需重建，ISR/按需再生成解决）。
- 与 SPA 的产物差异：HTML 含完整内容（SEO）+ hydration 脚本——hydration mismatch 是 SSG 常见错误。
- 追问钩子：为什么 SSG 的「数据快照」特性既是优势也是约束——优势：HTML 静态可全量 CDN 缓存（SCN-ENG-241）+ 安全（无服务端攻击面）；约束：内容更新必须重建（构建时长随内容量线性增长）——ISR/按需再生成（变更时单路由重建）是快照优势与实时性矛盾的工程解。

```javascript
// Next.js SSG + 增量
export async function generateStaticParams() {       // 路由枚举
  return posts.map(p => ({ slug: p.slug }));
}
export const revalidate = 3600;                      // ISR: 1h 后台再生成
// 构建时长治理
experimental: { workers: 4 }                         // 并行渲染
```
