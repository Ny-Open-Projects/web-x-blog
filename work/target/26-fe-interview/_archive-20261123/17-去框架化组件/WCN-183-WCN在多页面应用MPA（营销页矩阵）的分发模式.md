---
title: [WCN-183] WCN 在多页面应用（营销页矩阵）的分发模式：上百个落地页怎么共享组件？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-183：WCN 在多页面应用（营销页矩阵）的分发模式：上百个落地页怎么共享组件？

**答**：
- 场景：营销落地页数量多、模板化、更新频繁、多由非前端角色产出——WC + DSD 是最优解（服务端渲染完整、无框架锁定、按需 define）。
- 分发模式一（全局 importmap）：站点级 importmap + 少量 modulepreload；落地页只写 HTML 标签，组件自动加载。
- 模式二（模板构建时内联）：静态站点生成器（Astro）把 DSD 直接内联进页面 HTML，JS 只在交互位出现——性能最优（WCN-015）。
- 模式三（边缘注入）：无头 CMS 内容 + CDN 边缘函数（Cloudflare Workers）注入公共 head（importmap + token CSS），落地页源文件零前端配置。
- 版本策略：营销页矩阵大促前锁版本（importmap 固定 URL），避免发布窗口抖动；紧急修复走加载器熔断回滚。
- 量化：LCP 由 DSD 保证（HTML 即渲染）；JS 字节预算 = 交互组件之和（通常 <30KB）。

```html
<!-- 落地页模板（CMS 输出，Astro 构建内联 DSD） -->
<link rel="stylesheet" href="/tokens/brand-a.css">
<acme-hero>
  <template shadowrootmode="open">
    <style>/* 构建时从组件库注入 */</style>
    <slot name="title"></slot><slot name="cta"></slot>
  </template>
  <h1 slot="title">618 大促</h1>
  <acme-button slot="cta" tone="primary">立即抢购</acme-button>
</acme-hero>
```
