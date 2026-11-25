---
title: [BLD-095] monorepo 中的构建有什么特殊问题？共享依赖预构建与缓存隔离怎么做？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-095：monorepo 中的构建有什么特殊问题？共享依赖预构建与缓存隔离怎么做？
**答**：
- 特殊问题：幽灵依赖（共享提升）、跨包构建顺序（拓扑）、每包一份 node_modules 造成的重复预构建、dev server 对 workspace 包的 watching、缓存目录冲突。
- 依赖处理：pnpm workspace + workspace: 协议声明内部依赖；Vite/webpack 要 alias 内部包到源码（或用 exports 字段），并把内部包纳入 include/预构建。
- 缓存隔离：按 package 维度分 cache（Vite 的 cacheDir 配 .vite/包名、webpack cache.name 按包名），避免互相失效；顶层共享预构建产物用 npm 包级缓存。
- 任务编排：turbo/nx 做拓扑排序 + 远端缓存（按输入 hash 命中），本地 CI 双端复用。

```yaml
# pnpm-workspace.yaml
packages:
  - 'apps/*'
  - 'packages/*'
```

```javascript
// packages/ui/vite.config.js：monorepo 内部包的构建与缓存隔离
import { defineConfig } from 'vite';

export default defineConfig({
  cacheDir: '../../node_modules/.vite/ui', // 按包隔离缓存目录 防多 dev server 串台
  build: {
    lib: { entry: 'src/index.ts', formats: ['es'], fileName: 'index' },
    rollupOptions: { external: ['react', 'react-dom'] }, // peer 外部化
  },
});

// vite.config.js（应用侧，text 代码块）：
// resolve.alias = { '@app/ui': path.resolve(__dirname, '../packages/ui/src') } // 直接指源码 dev 免构建
// optimizeDeps.include = ['@app/ui']                                            // 或按包名预构建
```

```json
// turbo.json：拓扑构建 + 远程缓存
{
  "tasks": {
    "build": { "dependsOn": ["^build"], "outputs": ["dist/**"], "cache": true },
    "dev": { "cache": false, "persistent": true }
  }
}
```
