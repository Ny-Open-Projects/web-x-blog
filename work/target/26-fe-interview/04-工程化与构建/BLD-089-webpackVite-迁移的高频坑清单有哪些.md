---
title: [BLD-089] webpack→Vite 迁移的高频坑清单有哪些？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-089：webpack→Vite 迁移的高频坑清单有哪些？
**答**：
- CJS 动态 require：require('./locales/' + lang) 在 ESM 世界没有等价物——改 import.meta.glob（编译期展开）。
- 全局变量：process.env.XXX、global 在浏览器不存在——define 显式替换或改 import.meta.env。
- 环境变量前缀：REACT_APP_/VUE_APP_ 必须改名 VITE_ 才暴露到客户端。
- HTML 模板差异：ejs 语法、htmlWebpackPlugin 变量、Public Path（Vite 用 base）与 CDN 前缀逻辑要重写。
- 其他：require 上下文的 worker（new Worker(new URL()) 写法）、postcss 配置文件命名（.postcssrc → postcss.config.js 同名但加载时机不同）、CommonJS 依赖 504（optimizeDeps.include）、sass 的 @import 相对路径语义。

```javascript
// 坑清单逐条修复示例
// 坑一：CJS 动态 require -> import.meta.glob
// 旧：const modules = require.context('./locales', false, /\.json$/);
// 新：
const modules = import.meta.glob('./locales/*.json', { eager: true });
export const messages = Object.fromEntries(
  Object.entries(modules).map(([path, mod]) => [
    path.match(/locales\/(.+)\.json$/)[1], mod.default,
  ]),
);

// 坑二：global 变量
// vite.config.js 里 define: { global: 'globalThis' } 或源码替换

// 坑三：worker 写法
// 旧：new Worker(require.resolve('./worker.js'))
// 新：new Worker(new URL('./worker.js', import.meta.url), { type: 'module' })

// 坑四：VITE_ 前缀批量重命名
// bash 代码块：
// grep -rl "REACT_APP_" src | xargs sed -i '' 's/REACT_APP_/VITE_/g'
```
