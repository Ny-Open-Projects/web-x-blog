---
title: [BLD-267] Node API 依赖（process/browser 字段）的兼容处理怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-267：Node API 兼容怎么做？
**答**：
- 依赖里的 Node API：包内部用 process.env/path/crypto——浏览器构建报错或打包 Node polyfill（体积暴涨）。
- 处理层次：① 打包器自动 polyfill（webpack 4 默认注入——体积黑洞，webpack 5 移除）；② 显式 polyfill（node-libs-browser 按需）；③ 假 polyfill（Define process.env.XXX 为字面量 / browser 字段别名到空模块）；④ 换浏览器兼容包。
- browser 字段利用：包自带浏览器实现（pkg.browser 映射）——resolver 优先选（SCN-BLD-202）。
- 追问钩子：为什么 webpack 5 移除 Node polyfill 自动注入是对的——自动注入对每个依赖默默塞入 crypto/path 的浏览器 polyfill（数 MB），用户无感知无选择权；移除后强制开发者显式声明——体积黑盒变成显式决策，虽然迁移痛（报错变多）但产物可控。

```javascript
// 显式处理
resolve: {
  fallback: { crypto: false, path: require.resolve('path-browserify') },   // 显式声明
  alias: { process: 'process/browser', buffer: 'buffer' },
}
// Define 假 polyfill
define: { 'process.env.NODE_ENV': '"production"', 'process.env.APP_ENV': '"web"' }
```
