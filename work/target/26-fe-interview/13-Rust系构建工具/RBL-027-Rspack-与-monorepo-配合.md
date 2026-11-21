---
title: [RBL-027] Rspack 在 monorepo 中如何配置与提速？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-027：Rspack 在 monorepo 中如何配置与提速？
**答**：
- 依赖解析：pnpm workspace 的 symlink 链接要配合 resolve.symlinks 默认 true（真实路径构建模块图）；包内 subpath exports 依赖 RspackResolver 支持 package.json exports 字段。
- 缓存粒度：每个子应用独立持久缓存；公共包变更用依赖图自动失效对应子应用，避免全量失效。
- 排除面收敛：include/exclude 明确限定业务目录，避免 resolve 扫到全仓；alias 优先精确匹配。
- 构建编排：多子应用用 turbo/nx 的任务图并行 + 远程缓存；Rspack 的持久缓存目录记得加进工具的 output 缓存清单。
- 类型检查分离：tsc --noEmit / api-extractor 等类型工作单独并行任务，不阻塞打包主链路（构建工具不负责类型检查是共识）。
- 追问钩子：monorepo 场景下"模块图共享"目前没有跨进程方案，每个子应用仍是独立构建。

```javascript
// turbo.json：Rspack 持久缓存纳入任务缓存体系
// {
//   "tasks": {
//     "build": { "dependsOn": ["^build"], "outputs": ["dist/**", "node_modules/.cache/rspack/**"] },
//     "typecheck": { "dependsOn": ["^build"] }
//   }
// }
// 每个子应用 rspack.config.js 共享基础配置
const base = require('@corp/rspack-base/base.config');
module.exports = { ...base, entry: './src/index.ts' };
```
