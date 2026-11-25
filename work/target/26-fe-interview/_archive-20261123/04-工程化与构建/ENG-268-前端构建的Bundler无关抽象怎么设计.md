---
title: [ENG-268] Bundler 无关抽象（构建工具可替换性）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-268：Bundler 无关抽象怎么设计？
**答**：
- 可替换性清单：构建入口/产物约定（dist 结构/manifest 格式）/环境变量约定/插件能力清单——抽象这些「契约」而不是抽象构建器 API 本身（不可能）。
- 契约层设计：preset 屏蔽工具差异，项目只见「契约」（如产物 manifest schema 统一），换 bundler 时契约不变、preset 内部换实现。
- 限制认知：构建器特有优化（vite 的 preload 注入）通过能力探测降级，不要无条件依赖。
- 迁移预案沉淀：契约文档 + 产物基线（SCN-ENG-244 手法），让「未来换 bundler」是工程任务而非考古。
- 追问钩子：为什么「抽象构建器 API」不可行而「抽象产物契约」可行——各 bundler 的插件 API/配置模型差异巨大（webpack tapable vs vite rollup hooks），强行统一只能做最小子集；产物（manifest/目录结构/环境变量）是稳定语义，抽象它才有效。

```typescript
// 产物契约（bundler 无关）
interface BuildManifest {
  entry: string; chunks: { name: string; file: string; preload?: boolean }[];
  env: Record<string, string>;
}
// preset 内部适配
const manifest = bundler === 'vite' ? viteToContract(meta) : webpackToContract(stats);
```
