---
title: [RBL-172] Turbopack 在 CI 流水线里的定位与限制
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-172：Turbopack 在 CI 流水线里的定位与限制

**答**：
- 定位：Turbopack 的优势场景是 Next.js dev（增量按需编译），CI/生产构建支持随 Next 版本逐步 GA（next build --turbo）；决策前先确认所用 Next 版本与 Tabel 行为对齐。
- CI 限制点：1) 持久化缓存目录（.next/cache）进 CI 缓存要确认官方支持路径与失效行为；2) 与一些 webpack 生态插件不兼容（RBL-087），CI 上可能有专门构建脚本分支；3) 内核版本与 Next 强绑定，无法像 Rspack 那样独立升级。
- 混合策略常见形态：dev 用 Turbopack（HMR 体验），CI 生产构建仍走 webpack/Rspack 或随版本切换——决策要基于"CI 构建耗时占比"而非工具热度。
- 配合任务层：Next 单应用构建的缓存交给 turbo outputs（.next/**）声明，命中直接恢复产物，连 build 都不用跑。
- 追问钩子：能主动区分"dev 快"与"CI 快"两个维度（RBL-093 对比过 Vite dev）体现判断力。

```json
// turbo.json —— Next 应用在 CI 的任务声明
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "env": ["NEXT_PUBLIC_*", "VERCEL_ENV"],
      "outputs": [".next/**", "!.next/cache", "dist/**"], // 排除 .next/cache：巨大且可重建
      "outputsAreReusable": true
    }
  }
}
// package.json："build": "next build --turbo"
```
