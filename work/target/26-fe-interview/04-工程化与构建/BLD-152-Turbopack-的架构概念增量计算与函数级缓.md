---
title: [BLD-152] Turbopack 的架构概念：增量计算与函数级缓存到底指什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-152：Turbopack 的架构概念：增量计算与函数级缓存到底指什么？
**答**：
- Turbopack 核心：**Turbo 引擎做细粒度增量计算**——把构建任务建模为许多纯函数节点（"任务"），每个任务的输入哈希决定是否重算；文件变化只重算**直接依赖该文件的任务**，而不是"整个模块"甚至"整个 chunk"（对比 webpack 的模块级缓存粒度更细）。
- 函数级缓存：编译一个模块被拆成 parse、分析、代码生成等多个子任务，各自缓存；后续构建直接复用未变子任务结果（内存态，dev 场景为主）。
- 架构选择：Rust 内核 + 图数据库式的模块图 + **不依赖 rollup/webpack 插件生态**（有自己的 plugin 体系，JS 侧适配有限）；dev 专注按需 + 持久化 dev cache，产物仍打包。
- 与 Vite 的路线差异：Vite dev 不打包、esbuild 预构建、prod 用 rollup（dev/prod 双引擎不一致）；Turbopack dev/prod 同引擎，一致性好——这是面试常考的对比点。

```text
# Turbopack 与 webpack/Vite 的增量粒度对比（面试口述图）
webpack：缓存粒度 = 模块（module build 结果）
  文件变 → 重 build 该模块 → seal 全量重跑（分包/压缩整个 bundle）

vite dev：不打包；文件变 → 只失效该模块的 transformResult（HMR 单模块级）
  vite prod：rollup 全量，无增量（除非配缓存外部工具）

turbopack：缓存粒度 = 函数/任务级（parse、分析、codegen 各自是任务节点）
  文件变 → 只重算依赖它的任务节点 → dev 二次启动与热更新近常数时间
  代价：引擎复杂度极高、插件生态独立
```

```javascript
// next.config.js：Turbopack 的使用与关键配置（Next 15+ 默认 dev turbopack）
/** @type {import('next').NextConfig} */
module.exports = {
  // dev: next dev --turbopack
  // build: next build --turbopack（逐步 GA）
  turbopack: {
    resolveAlias: {
      '@ui': './packages/ui/src',           // turbopack 侧 alias（与 webpack 配置分离）
    },
    rules: {
      '*.svg': { loaders: ['@svgr/webpack'], as: '*.js' },  // 兼容层：按文件模式挂 loader
    },
  },
};
// 迁移判断：用标准 Next 生态（swc/SVG/样式）→ 直接开；
// 大量自定义 webpack 插件（自定义 loader 逻辑、特殊 plugin）→ 先做兼容评估（见 BLD-153 方法论）
```
