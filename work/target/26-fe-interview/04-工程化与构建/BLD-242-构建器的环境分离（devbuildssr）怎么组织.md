---
title: [BLD-242] 构建器的环境分离（dev/build/ssr 三形态）怎么组织？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-242：dev/build/ssr 三形态怎么组织？
**答**：
- 三形态差异：dev（unbundled ESM + HMR——速度优先）、build（bundled + 全量优化——产物优先）、ssr（Node 目标——模块语义/CSS 提取/无 DOM）——一份配置按形态分支。
- ssr 构建特殊性：external node_modules（Node 直接 require——与前端 bundle 的双构建）、条件导出 node 条件、CSS 处理（提取供 HTML 注入而非加载）。
- 双构建一致性：client 与 server 构建的模块解析条件不同（browser/node）——同一依赖两端选中不同入口是「SSR hydration mismatch」的常见根因。
- 配置组织：环境分支显式（defineConfig(({ command, mode, isSsr }) => ...)）——分支逻辑集中可测，不散落插件里。
- 追问钩子：为什么「同一依赖双端选不同入口」会造成 hydration mismatch——如某个包 browser 条件导出返回 DOM 依赖版本、node 条件返回纯逻辑版本；SSR 渲染用 node 版本（结构 A），客户端 hydrate 用 browser 版本（结构 B）——DOM 树不匹配；解法是双端强制同入口（SSR external 时 alias 对齐或包本身提供 isomorphic 入口）。

```javascript
export default defineConfig(({ command, isSsr }) => ({
  define: { __DEV__: command === 'serve' },
  ssr: { external: isSsr ? ['react'] : [] },          // SSR external node_modules
  resolve: { conditionNames: isSsr ? ['node', 'import'] : ['browser', 'import'] },
}));
// 双端同入口对齐（防 hydration mismatch）
resolve: { alias: { pkg: path.resolve('node_modules/pkg/isomorphic.js') } }
```
