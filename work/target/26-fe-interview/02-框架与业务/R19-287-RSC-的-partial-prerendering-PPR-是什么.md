---
title: [R19-287] Partial Prerendering（PPR）是什么？静态壳与动态洞怎么组合？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-287：Partial Prerendering（PPR）是什么？
**答**：
- PPR：构建期预渲染「静态外壳」（布局、导航、静态内容），动态部分（个性化数据）留 Suspense 洞在请求时流式填充。
- 收益：静态部分 CDN 即发（TTFB 极低），动态部分不阻塞整页——静态与动态不再二选一。
- 实现：Suspense 边界即动态洞边界；框架把边界外的内容 prerender、边界内请求时渲染。
- 适用：商品页（静态详情 + 动态库存/个性化推荐）、营销页（静态 + 动态表单）。
- 现状：Next 实验特性（experimental_ppr），依赖 PPR 兼容的缓存层与运行时。
