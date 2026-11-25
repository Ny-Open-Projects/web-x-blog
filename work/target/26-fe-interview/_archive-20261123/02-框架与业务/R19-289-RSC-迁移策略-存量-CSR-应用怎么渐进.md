---
title: [R19-289] 存量 CSR 应用怎么渐进迁移到 RSC？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-289：存量 CSR 应用怎么渐进迁移到 RSC？
**答**：
- 第一步：路由骨架 RSC 化（布局/导航/静态内容服务端渲染），页面主体保持 'use client'——零功能风险拿 SEO/首屏收益。
- 第二步：数据获取迁移——组件内 useEffect 拉数改为 RSC 直接取数传 props（叶子组件保持 client）。
- 第三步：写操作迁移——fetch/mutation 换 Server Action + useActionState。
- 度量每步：bundle 减少量、TTI、SEO 收录、回归测试通过率。
- 障碍预案：依赖浏览器 API 的组件保持 client；全局状态库（Redux）先不动，按域逐步收敛到 server state。
