---
title: [RBL-092] Turbopack 的生产构建（next build）进展与取舍？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-092：Turbopack 的生产构建（next build）进展与取舍？
**答**：
- 演进路径：先 dev（--turbo）稳定 → 生产构建以 next build --turbo（实验）逐步 GA；官方目标是 dev/prod 都跑 Turbopack，彻底替换 webpack。
- 生产特有要求：tree shaking 质量、minify、代码分割、产物确定性与长效缓存——这些在 Turbopack 内逐步补齐（基于 SWC 压缩）。
- 取舍：dev 的收益（惰性+增量）在 prod 的收益不同——prod 本来就是全量构建一次，主要收益是"更快"而非"按需"，提速幅度小于 dev。
- 缓存价值：prod 构建的持久缓存对 CI 复用价值大（配置不变时大部分任务命中）。
- 现状答题要点：面试答"dev 已 GA、build 在推进"级别的现状描述即可，避免报具体版本号过时。
- 追问钩子：生产构建慢的常见根因往往不是打包器而是 CI 环境（网络安装、类型检查串行），优化要先测量。

```javascript
// package.json
// "dev": "next dev --turbo",
// "build": "next build --turbo"   // 实验性，视版本而定
// dev/prod 收益来源不同：
// dev  : 惰性按需 + 函数级增量（架构级收益）
// prod : 全量单次，收益 = Rust 执行速度 + CI 缓存复用
```
