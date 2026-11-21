---
title: [BAS-061] SEO 三件套指什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-061：SEO 三件套指什么？
**答**：
- title：权重最高的关键词位置，每页唯一，推荐"页面名 - 站点名"结构。
- meta description：搜索结果里的摘要文案，不直接决定排名但影响点击率。
- canonical：声明规范 URL，把带参数、http/https 等多个 URL 变体的权重收敛到一个地址，避免重复页面分散权重。

```html
<title>前端面试题库 - 某站</title>
<meta name="description" content="一题一考点的前端基础速答题库，覆盖 HTML、CSS、JS、网络与工程化。" />
<link rel="canonical" href="https://example.com/basics" />
```

## 八、CSS 补充·布局与交互
