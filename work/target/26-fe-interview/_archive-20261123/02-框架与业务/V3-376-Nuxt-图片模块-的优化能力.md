---
title: [V3-376] Nuxt Image 模块能做哪些优化？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-376：Nuxt Image 模块能做哪些优化？
**答**：
- `<NuxtImg>`：按 provider（本 ipx / 阿里云 OSS / Cloudflare）生成带尺寸、质量、格式的 URL，自动 webp/avif 协商。
- `<NuxtPicture>`：产出 `<picture>` 多源 + srcset，按 DPR/视口下发最合适尺寸，避免大图小显示。
- 占位与懒加载：内置 placeholder（模糊小图/主色）与 loading=lazy 组合，LCP 图片排除懒加载并 preload。
- 工程约束：组件层统一走 NuxtImg，禁止裸 img 引用原图；图片尺寸在 CMS 上报时校验。
- 观测：LCP 元素耗时、图片字节数占比纳入性能看板。
```html
<NuxtPicture src="/goods/1.jpg" sizes="sm:100vw md:50vw lg:33vw" quality="80" format="avif,webp" />
```
