---
title: [MFW-085] Nuxt Layers 和模块系统怎么支撑大型多团队项目？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-085：Nuxt Layers 和模块系统怎么支撑大型多团队项目？
**答**：
- Layers（extends 机制）：一个「基础层」仓库沉淀主题、公共组件、数据层规范，各业务仓库通过 `extends` 继承并按目录覆盖（同名文件就近覆盖），实现「配置、组件、页面」三级复用——类似 Next 生态用 monorepo + npm 包做，但 Nuxt 是框架原生支持。
- Modules（@nuxt/* 模块）：构建期钩子注入能力（装 UI 库、接入鉴权、生成 sitemap），统一入口 `modules: []`，避免每团队手搓插件配置。
- 组合姿势：公司层（design-system + auth + 规范）→ 域层（商品/订单各自 layer）→ 应用层（把若干 layer 组合成站点）。跨仓库用 git 依赖或私有 npm 包。
- 风险与对策：层间隐式覆盖导致「行为来自哪一层」难排查——用 `.nuxt` 生成物与 nuxt devtools 的 layer 面板定位；层越多构建越慢，控制层数在 3 级以内。

```ts
// base-layer/nuxt.config.ts —— 公司基础层
export default defineNuxtConfig({
  modules: ['@nuxtjs/i18n', '@nuxt/image'],
  css: ['~/assets/theme.css'],
  app: { head: { link: [{ rel: 'icon', href: '/favicon.ico' }] } },
});
```

```ts
// product-app/nuxt.config.ts —— 业务应用组合层
export default defineNuxtConfig({
  extends: [
    '../base-layer',      // 公司规范与主题
    '../domain-order',    // 订单域（含自己的 pages/components/server）
  ],
  // 就近覆盖：app/pages/index.vue 会覆盖 base-layer 同名页面
  routeRules: { '/': { swr: 600 } },
});
```
