---
title: [RBL-030] 大型项目 Rspack dev 热更新慢怎么排查与优化？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-030：大型项目 Rspack dev 热更新慢怎么排查与优化？
**答**：
- 先分层计时：文件变更→（编译）→（产物产出）→（浏览器 apply）三段分别打点，确定慢在哪一段；Rspack 场景编译段通常很快，慢的常是 JS 插件钩子或浏览器 apply 链。
- 编译段优化：持久缓存开启、缩减 dev rule 范围（source map 用 cheap-module-source-map）、关掉 dev 下不需要的压缩/分析插件。
- 插件段优化：dev 下禁用生产插件（manifest 生成、CDN 上传、i18n 校验），用条件载入；钩子里避免同步大遍历。
- 失效面控制：动态 require 的大依赖目录、巨型 JSON 会扩大失活范围；拆包或改运行时加载。
- 浏览器段优化：模块级 accept 粒度太粗（在根组件 accept 整个子树）导致整页重渲染，按组件粒度 accept。
- 追问钩子：Rspack 的增量是"模块粒度重编译"，不是文件内容级细粒度增量（那是 Turbopack 的路线），极端高频小改动场景可对比 Turbopack。

```javascript
// dev 环境插件条件加载模板
const prodPlugins = require('./plugins.prod');
module.exports = (env) => ({
  plugins: env.mode === 'production' ? prodPlugins : [/* 仅最小集 */],
});
// 浏览器段：细粒度 HMR accept
// if (import.meta.webpackHot) import.meta.webpackHot.accept('./components/List', () => {...});
```
