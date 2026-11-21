---
title: [V3-374] Nuxt 模块机制是什么？怎么写一个自研模块？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-374：Nuxt 模块机制是什么？怎么写一个自研模块？
**答**：
- 模块 = Nuxt 构建生命周期的插件：在 nuxt hook 上注册（builder:webpack/vite 配置、nitro 配置、模板生成 addTemplate）。
- 常用能力：addComponent（自动注册组件）、addPlugin（注入客户端插件）、addImports（auto-import）、addServerHandler（server route）、extendPages（生成路由）。
- 典型自研：埋点模块（addPlugin 注入 SDK + 环境配置）、内网网关代理（nitro devProxy 配置）、公司 SSO 登录（server middleware + 会话）。
- 传配置：模块接收 options，支持 nuxt.config 里 moduleOptions 校验（zod/schema 校验）。
- 发布规范：module 声明 meta（name/configKey/compatibility），跟随 Nuxt 版本兼容矩阵。
```javascript
export default defineNuxtModule({
  meta: { name: '@acme/analytics' },
  setup(options, nuxt) {
    nuxt.hook('vite:extendConfig', (cfg) => { /* 注入 */ })
    addPlugin(resolve('./runtime/plugin'))
  }
})
```
