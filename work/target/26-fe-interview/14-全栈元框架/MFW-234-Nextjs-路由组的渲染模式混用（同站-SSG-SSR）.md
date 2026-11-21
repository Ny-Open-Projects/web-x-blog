---
title: [MFW-234] 同一站点混用渲染模式（SSG/ISR/SSR 的路由级决策）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## MFW-234：同站渲染模式混用决策

**答**:
- 路由级分派：营销页 SSG（revalidate:false 纯静态）、列表/详情 ISR（60s 或按需 tag）、搜索/个人中心 SSR（force-dynamic）、API 段 Route Handler 按 need
- 混用的一致性联动：layout 不确定模式时以「最动态的子页」为准（父 layout 读 cookie 则全子树退出静态——布局层要守住纯净）
- export const dynamic/revalidate 的作用域：段级覆盖父级——用路由组 (marketing)/(app) 分组管理不同策略
- 审计方法：next build 输出表（○ 静态/● SSR/ISR 标记）逐行核对预期——「以为静态其实动态」是性能事故常见根因

```javascript
// app/(marketing)/page.tsx      → SSG（无动态 API）
// app/(shop)/[slug]/page.tsx    → ISR
export const revalidate = 60
// app/(app)/settings/page.tsx   → SSR
export const dynamic = 'force-dynamic'
// build 输出核对：○/●/ISR 标记与设计一致？
```
