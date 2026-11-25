---
title: [V3-377] Nuxt Content 模块适合什么场景？核心能力有哪些？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-377：Nuxt Content 模块适合什么场景？核心能力有哪些？
**答**：
- 场景：文档站、博客、运营可维护的静态内容——Markdown/MD/CSV/YAML 文件即内容源，不需要 CMS 后端。
- 能力：queryContent() 类型安全查询（路径/字段/正则）、MD 组件化（在 markdown 里用 Vue 组件）、代码高亮、frontmatter 元数据、目录树导航。
- 与 SEO：全静态预渲染 + sitemap/OG 自动生成，内容页天然适合 isr/prerender。
- 组件替换：`prose` 组件可覆盖（自定义 h2 样式、代码块复制按钮），样式可控。
- 权衡：内容更新走 git 提交，非技术运营不适合；需要 CMS 就换 API + isr。
